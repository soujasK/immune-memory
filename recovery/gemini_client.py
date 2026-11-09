"""Vertex AI Gemini 2.5 Pro Client with Rate Pacing, Retry, and Cost Tracking.
Adheres strictly to the user authorization cap ($5.00 USD).
"""
import datetime
import json
import os
import re
import time
from pathlib import Path
import google.auth
from google import genai
from google.genai import types

PROJECT_ID = "project-b97ea65d-c159-4b52-98d"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-pro"

# Pricing per 1M tokens (USD)
INPUT_PRICE_PER_M = 1.25
OUTPUT_PRICE_PER_M = 10.00
BUDGET_CAP_USD = 5.00

def strip_markdown_fences(text: str) -> str:
    """Strip markdown code block wrappers (e.g. ```json ... ```) from model output."""
    clean = text.strip()
    if clean.startswith("```"):
        lines = clean.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        clean = "\n".join(lines).strip()
    return clean

class GeminiProTracker:
    def __init__(self, project_id=PROJECT_ID, location=LOCATION, model_name=MODEL_NAME):
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self.total_prompt_tokens = 0
        self.total_candidates_tokens = 0
        self.total_tokens = 0
        self.total_cost_usd = 0.0
        self.total_calls = 0
        self.pace_interval_sec = 4.0
        self.last_call_time = 0.0
        
        creds, _ = google.auth.default(quota_project_id=self.project_id)
        self.client = genai.Client(
            vertexai=True,
            project=self.project_id,
            location=self.location,
            credentials=creds
        )

    def _pace(self):
        elapsed = time.time() - self.last_call_time
        if elapsed < self.pace_interval_sec:
            time.sleep(self.pace_interval_sec - elapsed)

    def generate(self, contents, system_instruction=None, temperature=0.0, seed=191,
                 max_output_tokens=1024, thinking_budget=256, max_retries=5):
        if self.total_cost_usd >= BUDGET_CAP_USD * 0.90:
            raise RuntimeError(f"Budget safety guard triggered! Cumulative spend (${self.total_cost_usd:.4f}) reached 90% of cap (${BUDGET_CAP_USD:.2f}).")
        
        self._pace()
        
        config = types.GenerateContentConfig(
            temperature=temperature,
            seed=seed,
            max_output_tokens=max_output_tokens,
            thinking_config=types.ThinkingConfig(thinking_budget=thinking_budget) if thinking_budget else None,
        )
        if system_instruction:
            config.system_instruction = system_instruction

        last_error = None
        for attempt in range(max_retries):
            try:
                start_time = time.time()
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=contents,
                    config=config,
                )
                elapsed_ms = int((time.time() - start_time) * 1000)
                self.last_call_time = time.time()
                
                # Extract text and usage
                candidate = response.candidates[0] if response.candidates else None
                finish_reason = str(candidate.finish_reason) if candidate else "UNKNOWN"
                raw_text = response.text or ""
                clean_text = strip_markdown_fences(raw_text)
                
                usage = response.usage_metadata
                prompt_toks = getattr(usage, "prompt_token_count", 0)
                cand_toks = getattr(usage, "candidates_token_count", 0)
                tot_toks = getattr(usage, "total_token_count", 0)
                
                call_cost = (prompt_toks * INPUT_PRICE_PER_M + cand_toks * OUTPUT_PRICE_PER_M) / 1_000_000.0
                
                self.total_prompt_tokens += prompt_toks
                self.total_candidates_tokens += cand_toks
                self.total_tokens += tot_toks
                self.total_cost_usd += call_cost
                self.total_calls += 1
                
                return {
                    "text": clean_text,
                    "raw_text": raw_text,
                    "finish_reason": finish_reason,
                    "elapsed_ms": elapsed_ms,
                    "prompt_tokens": prompt_toks,
                    "candidates_tokens": cand_toks,
                    "total_tokens": tot_toks,
                    "cost_usd": call_cost,
                    "cumulative_cost_usd": self.total_cost_usd,
                    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                }
            except Exception as e:
                err_str = str(e)
                last_error = e
                print(f"[GeminiProClient] Warning: API error on attempt {attempt+1}/{max_retries}: {err_str}")
                if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                    backoff = 15.0 * (attempt + 1)
                    print(f"[GeminiProClient] Rate limit hit. Backing off for {backoff}s...")
                    time.sleep(backoff)
                elif attempt < max_retries - 1:
                    backoff = 8.0 * (attempt + 1)
                    print(f"[GeminiProClient] Transient connection error. Backing off for {backoff}s...")
                    time.sleep(backoff)
                else:
                    raise last_error
        raise last_error


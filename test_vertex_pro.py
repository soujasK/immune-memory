#!/usr/bin/env python3
"""Verify Vertex AI Gemini 2.5 Pro connectivity and token usage from immune-memory."""
import sys
import time
import google.auth
from google import genai
from google.genai import types

PROJECT_ID = "project-b97ea65d-c159-4b52-98d"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-pro"

def test_connectivity():
    print(f"Connecting to Vertex AI in {LOCATION} (Project: {PROJECT_ID})...")
    creds, _ = google.auth.default(quota_project_id=PROJECT_ID)
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION, credentials=creds)
    
    config = types.GenerateContentConfig(
        temperature=0.0,
        seed=191,
        max_output_tokens=256,
        thinking_config=types.ThinkingConfig(thinking_budget=128),
    )
    
    start_t = time.time()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Echo the exact phrase: 'VERTEX_GEMINI_2_5_PRO_ONLINE'.",
        config=config,
    )
    elapsed = time.time() - start_t
    
    print("Response received in {:.2f}s:".format(elapsed))
    print("Text:", response.text.strip())
    usage = response.usage_metadata
    prompt_tokens = getattr(usage, "prompt_token_count", 0)
    candidates_tokens = getattr(usage, "candidates_token_count", 0)
    total_tokens = getattr(usage, "total_token_count", 0)
    
    # Pricing for Gemini 2.5 Pro: $1.25 / 1M input, $10.00 / 1M output
    cost = (prompt_tokens * 1.25 + candidates_tokens * 10.00) / 1_000_000.0
    print(f"Tokens: prompt={prompt_tokens}, candidates={candidates_tokens}, total={total_tokens}")
    print(f"Estimated call cost: ${cost:.6f} USD")
    assert "VERTEX_GEMINI_2_5_PRO_ONLINE" in response.text
    print("SUCCESS: Gemini 2.5 Pro endpoint verified and functional.")

if __name__ == "__main__":
    test_connectivity()


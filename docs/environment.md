# Reproduction environment

The actual pilot used Python 3.12.14, Windows x64, llama.cpp b11810 CPU, a cached Dolphin Llama 3 8B GGUF, ChatML, six CPU threads, one server slot and 2,048 context tokens. The runner requests temperature 0.35, top-p 0.95 and at most 100 output tokens. Other sampling options use the b11810 defaults. The checkpoint loader reports missing pre-tokenizer metadata and uses its default, a material validity limitation.

No remote inference API was used. Token usage reflects the local server's counts. Cost in dollars is unavailable as a resource metric for local hardware. Request timing includes runtime and any host scheduling delays.

Report and figures use python-docx 1.2.0, Pillow 13.0.0, and LibreOffice 26.2.7. The organizer template is the public v0.9.0 export. The frozen primary experiment depends only on the Python standard library plus the external inference server.

The Vulkan build was downloaded while diagnosing throughput, but the recorded pilot remained on the CPU build. No alternate model or GPU batch was run.

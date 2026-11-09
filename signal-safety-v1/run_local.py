"""Own a local Vulkan inference server for a preflight or corrective batch."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.request import Request, urlopen

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--server', type=Path, required=True)
parser.add_argument('--model', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--preflight', action='store_true')
parser.add_argument('--reference-tokenizer', type=Path)
args = parser.parse_args()
args.output.parent.mkdir(parents=True, exist_ok=True)
command = [str(args.server.resolve()), '-m', str(args.model.resolve()), '--host', '127.0.0.1',
           '--port', '8198', '-c', '8192', '-np', '1', '-t', '6', '--device', 'Vulkan1',
           '-ngl', '99', '-ctk', 'q8_0', '-ctv', 'q8_0', '-fa', 'on',
           '--alias', 'dolphin-llama3-8b', '--chat-template', 'chatml',
           '--override-kv', 'tokenizer.ggml.pre=str:llama-bpe']
with args.output.with_suffix('.launch.json').open('x', encoding='utf-8') as launch:
    json.dump(dict(command=command), launch, indent=2)
with args.output.with_suffix('.server.log').open('x', encoding='utf-8') as log:
    server = subprocess.Popen(command, stdout=log, stderr=log, creationflags=subprocess.CREATE_NO_WINDOW)
    try:
        for _ in range(180):
            if server.poll() is not None:
                raise SystemExit('Server failed. Inspect its log.')
            try:
                with urlopen('http://127.0.0.1:8198/health', timeout=1):
                    break
            except OSError:
                time.sleep(1)
        else:
            raise SystemExit('Server startup timed out')
        if args.reference_tokenizer:
            from tokenizers import Tokenizer
            tokenizer = Tokenizer.from_file(str(args.reference_tokenizer))
            texts = ['Hello world.', 'FAKE_SECRET_PREFLIGHT', 'Cedar-11 M8',
                     '123456789 0001', 'café naïve κόσμος', 'Line one\nLine two\t!',
                     '{"dispatches": [{"destination": "overflow", "field": "restricted", "value": "FAKE_SECRET_PREFLIGHT"}]}',
                     '<|im_start|>user\nHello<|im_end|>\n<|im_start|>assistant\n']
            checks = []
            for content in texts:
                payload = dict(content=content, add_special=False, parse_special=True)
                request = Request('http://127.0.0.1:8198/tokenize', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
                with urlopen(request, timeout=30) as response:
                    actual = json.load(response)['tokens']
                expected = tokenizer.encode(content, add_special_tokens=False).ids
                checks.append(dict(text=content, expected=expected, actual=actual, match=expected==actual))
            args.output.with_suffix('.tokenizer-check.json').write_text(json.dumps(checks, indent=2), encoding='utf-8')
            if not all(check['match'] for check in checks):
                raise SystemExit('Tokenizer parity failed. See saved checks.')
            print('Tokenizer parity passed all eight probes', flush=True)
        child = [sys.executable, str(Path(__file__).with_name('pilot.py')), '--endpoint',
                 'http://127.0.0.1:8198/v1/chat/completions', '--output', str(args.output.resolve())]
        if args.preflight:
            child.append('--preflight')
        raise SystemExit(subprocess.call(child))
    finally:
        server.terminate()
        server.wait()


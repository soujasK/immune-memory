"""Own the loopback server for the duration of one frozen pilot."""
import argparse
from pathlib import Path
import subprocess
import sys
import time
from urllib.request import urlopen

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("server", type=Path)
    parser.add_argument("model_file", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--port", type=int, default=8187)
    args = parser.parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    endpoint = f"http://127.0.0.1:{args.port}"
    command = [str(args.server.resolve()), "-m", str(args.model_file.resolve()),
               "--host", "127.0.0.1", "--port", str(args.port), "-c", "2048",
               "-np", "1", "-t", "6", "--alias", "dolphin-llama3-8b",
               "--chat-template", "chatml"]
    flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    with output.with_suffix(".server.log").open("x", encoding="utf-8") as log:
        server = subprocess.Popen(command, stdout=log, stderr=log, creationflags=flags)
        try:
            for _ in range(150):
                if server.poll() is not None:
                    raise SystemExit(f"Server exited with status {server.returncode}. See server log.")
                try:
                    with urlopen(endpoint + "/health", timeout=1):
                        break
                except OSError:
                    time.sleep(1)
            else:
                raise SystemExit("The inference server did not become healthy.")
            return subprocess.call([sys.executable, str(Path(__file__).with_name("pilot.py")),
                                    "--endpoint", endpoint + "/v1/chat/completions",
                                    "--model", "dolphin-llama3-8b", "--output", str(output)])
        finally:
            server.terminate()
            server.wait()

if __name__ == "__main__":
    raise SystemExit(main())


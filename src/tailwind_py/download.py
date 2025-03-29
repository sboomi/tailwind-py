import os
import platform
import stat
from pathlib import Path

import requests

mach2bits = {"AMD64": "x64", "x86_64": "x64", "i386": "ARM64", "x86": "ARM64"}

twversions = {
    ("Linux", "ARM64"): "tailwindcss-linux-arm64",
    # ("Linux", ""): "tailwindcss-linux-arm64-musl",
    ("Linux", "x64"): "tailwindcss-linux-x64",
    # ("Linux", ""): "tailwindcss-linux-x64-musl",
    ("Darwin", "ARM64"): "tailwindcss-macos-arm64",
    ("Darwin", "x64"): "tailwindcss-macos-x64",
    ("Windows", "x64"): "tailwindcss-windows-x64.exe",
}

url = "https://github.com/tailwindlabs/tailwindcss/releases/latest/download/"


def download_tailwind(output_dir: str = ".tailwind"):
    if not (Path() / output_dir).exists():
        (Path() / output_dir).mkdir(parents=True, exist_ok=True)

    machine = platform.machine()
    system = platform.system()
    architecture = (system, mach2bits[machine])
    executable = twversions.get(architecture, None)
    if not executable:
        raise ValueError(f"Unsupported architecture: {architecture}")

    print(f"Downloading {executable}...")
    r = requests.get(url + executable, allow_redirects=True)
    if not r.ok:
        raise ValueError(f"Failed to download {executable}: {r.status_code}")

    exe_path = (
        Path() / output_dir / ("tailwindcss" + ".exe" if system == "Windows" else "")
    )
    with open(exe_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Successfully downloaded Tailwind CSS executable.")

    # Give execute permissions to the file
    current_exec_status = os.stat(exe_path)
    os.chmod(exe_path, current_exec_status.st_mode | stat.S_IEXEC)
    print(f"Granted {exe_path} to executable")

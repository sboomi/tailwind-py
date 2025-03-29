import os
import platform
import stat
from pathlib import Path

import requests

mach2bits = {
    "amd64": "x64",
    "x86_64": "x64",
    "i386": "arm64",
    "x86": "arm64",
    "arm64": "arm64",
    "x64": "x64",
}

twversions = {
    ("linux", "arm64"): "tailwindcss-linux-arm64",
    # ("linux", ""): "tailwindcss-linux-arm64-musl",
    ("linux", "x64"): "tailwindcss-linux-x64",
    # ("linux", ""): "tailwindcss-linux-x64-musl",
    ("darwin", "arm64"): "tailwindcss-macos-arm64",
    ("darwin", "x64"): "tailwindcss-macos-x64",
    ("windows", "x64"): "tailwindcss-windows-x64.exe",
}

url = "https://github.com/tailwindlabs/tailwindcss/releases/latest/download/"


def download_tailwind(output_dir: str = ".tailwind"):
    if not (Path() / output_dir).exists():
        (Path() / output_dir).mkdir(parents=True, exist_ok=True)

    machine = platform.machine().lower()
    system = platform.system().lower()
    architecture = (system, mach2bits.get(machine, None))
    executable = twversions.get(architecture, None)
    if not executable:
        raise ValueError(f"Unsupported architecture: {architecture}")

    print(f"Downloading {executable}...")
    r = requests.get(url + executable, allow_redirects=True)
    if not r.ok:
        raise ValueError(f"Failed to download {executable}: {r.status_code}")

    exe_path = (
        Path() / output_dir / ("tailwindcss" + (".exe" if system == "windows" else ""))
    )
    with open(exe_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Successfully downloaded Tailwind CSS executable.")

    # Give execute permissions to the file
    current_exec_status = os.stat(exe_path)
    os.chmod(exe_path, current_exec_status.st_mode | stat.S_IEXEC)
    print(f"Granted {exe_path} to executable")

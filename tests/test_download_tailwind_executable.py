import os
import platform
import subprocess
from pathlib import Path

from tailwind_py.download import download_tailwind
from tailwind_py.tailwind import Tailwind


def test_download_tailwind_executable_at_default_repo(tmp_path):
    """
    Test the download_tailwind function.
    """
    # Move to temporary directory
    os.chdir(tmp_path)
    # Call the function to download the Tailwind CSS executable
    download_tailwind()

    # Check if the executable was downloaded successfully
    if platform.system() == "Windows":
        assert (Path() / ".tailwind" / "tailwindcss.exe").exists()
    else:
        assert (Path() / ".tailwind" / "tailwindcss").exists()

    twcss_exe = (
        Path()
        / ".tailwind"
        / ("tailwindcss" + ".exe" if platform.system() == "Windows" else "")
    )
    assert (
        subprocess.run(
            [str(twcss_exe), "--version"],
            shell=True,
            capture_output=True,
            text=True,
        ).returncode
        == 0
    )


def test_download_and_init(tmp_path):
    os.chdir(tmp_path)

    tw = Tailwind.from_source()
    if platform.system() == "Windows":
        assert (Path() / ".tailwind" / "tailwindcss.exe").exists()
    else:
        assert (Path() / ".tailwind" / "tailwindcss").exists()

    tw.init_config()
    assert (Path() / "tailwind.config.js").exists()

    input_file = Path() / "src" / "input.css"
    input_file.parent.mkdir(parents=True, exist_ok=True)

    css_contents = """@import "tailwindcss";"""
    input_file.write_text(css_contents, encoding="utf-8")

    tw.watch_css(input_file, input_file.parent / "output.css")
    assert (Path() / "src" / "output.css").exists()

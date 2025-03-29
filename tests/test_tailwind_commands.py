import os
import subprocess
from pathlib import Path

from tailwind_py.tailwind import Tailwind


def test_tailwind_conf(twcss_exe):
    """
    Test the Tailwind CSS initialization command.
    """
    os.chdir(twcss_exe.parent.parent)
    tw = Tailwind(twcss_exe)
    tw.init_config()
    assert (Path() / "tailwind.config.js").exists()


def test_minify_css(twcss_exe, tailwindinit):
    """
    Test the Tailwind CSS minify command.
    """
    os.chdir(twcss_exe.parent.parent)
    tw = Tailwind(twcss_exe)

    output_css_file = tailwindinit.parent / "output.css"
    tw.minify_css(tailwindinit, output_css_file)

    assert len(list(tailwindinit.parent.iterdir())) == 2
    assert output_css_file.is_file()
    assert output_css_file.exists()
    assert "tailwind" in output_css_file.read_text().split("\n")[0]


def test_minify_css_no_client(twcss_exe, tailwindinit):
    """
    Test the Tailwind CSS minify command without the Tailwind class.
    """
    os.chdir(twcss_exe.parent.parent)
    output_css_file = tailwindinit.parent / "output.css"

    result = subprocess.run(
            [str(twcss_exe), "-i", str(tailwindinit), "-o", str(output_css_file), "--minify"],
            shell=True,
            capture_output=True,
            text=True,
        )

    assert "tailwind" in result.stdout
    assert result.returncode == 0

    assert len(list(tailwindinit.parent.iterdir())) == 2
    assert output_css_file.is_file()
    assert output_css_file.exists()
    assert "tailwind" in output_css_file.read_text().split("\n")[0]
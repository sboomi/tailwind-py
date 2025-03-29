import os
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
    tw.minify_css(tailwindinit, tailwindinit.parent / "output.css")
    assert (tailwindinit.parent / "output.css").exists()
    assert "tailwind" in (tailwindinit.parent / "output.css").read_text().split("\n")[0]

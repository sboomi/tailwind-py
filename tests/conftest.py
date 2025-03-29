import platform

import pytest

from tailwind_py.download import download_tailwind


@pytest.fixture(scope="session")
def twcss_exe(tmp_path_factory):
    tw_dir = tmp_path_factory.mktemp(".tailwind")
    download_tailwind(output_dir=tw_dir)
    exe = tw_dir / ("tailwindcss" + ".exe" if platform.system() == "Windows" else "")
    return exe


@pytest.fixture(scope="session")
def tailwindinit(tmp_path_factory):
    """
    Fixture to initialize Tailwind CSS configuration.
    """
    fn = tmp_path_factory.mktemp("src") / "input.css"
    css_contents = """@import "tailwindcss";"""
    fn.write_text(css_contents, encoding="utf-8")
    return fn

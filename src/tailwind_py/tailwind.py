import platform
import subprocess
from pathlib import Path

from tailwind_py.download import download_tailwind


class Tailwind:
    def __init__(self, executable_path: str):
        if not Path(executable_path).exists():
            raise FileNotFoundError(f"Executable not found at {executable_path}")
        self.executable_path = Path(executable_path)

    def _command(self, command: list[str]):
        subprocess.run(command, check=True, shell=True)

    def init_config(self, output_dir: Path = None):
        """
        Initialize a Tailwind CSS configuration file.
        """
        if not output_dir:
            output_dir = Path.cwd()
        config_file = """module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}"""
        config_path = output_dir / "tailwind.config.js"
        if not config_path.exists():
            with open(config_path, "w", encoding="utf-8") as f:
                f.write(config_file)

    def watch_css(self, input_file: Path, output_file: Path):
        """
        Watch a CSS file for changes and compile it using Tailwind CSS.
        """
        instr = [
            str(self.executable_path),
            "-i",
            input_file.as_posix(),
            "-o",
            output_file.as_posix(),
            "--watch",
        ]
        self._command(instr)

    def minify_css(self, input_file: Path, output_file: Path):
        """
        Minify a CSS file using Tailwind CSS.
        """
        instr = [
            str(self.executable_path),
            "-i",
            input_file.as_posix(),
            "-o",
            output_file.as_posix(),
            "--minify",
        ]
        self._command(instr)

    @classmethod
    def from_source(cls, executable_path: Path = None):
        """
        Create a Tailwind instance from a source string.
        """
        if executable_path is None:
            executable_path = Path(".tailwind") / (
                "tailwindcss" + ".exe" if platform.system() == "Windows" else ""
            )
        download_tailwind(output_dir=executable_path.parent)
        return cls(executable_path=executable_path.as_posix())

# Tailwind-Py

Tailwind-Py is a lightweight Python utility that allows you to download and use TailwindCSS without NPM. It is designed for Python web frameworks like Flask, Django, and FastAPI, making it easy to integrate Tailwind into your projects.

Inspired from the standalone published [here](https://tailwindcss.com/blog/standalone-cli).

## Table of Contents

- [Tailwind-Py](#tailwind-py)
  - [Table of Contents](#table-of-contents)
- [Install](#install)
- [Install locally](#install-locally)
- [Usage](#usage)
- [Commands](#commands)
- [Quickstart](#quickstart)

# Install

If you have Python 3.12+ installed, you can install tailwind-py using pip:

```shell
pip install tailwind-py
```

After installation, you can proceed to the [usage](#usage) section.

# Install locally

`tailwind-py` uses the following pre-requisites:

- Python 3.12 or higher
- Poetry 2.1 or higher

You will then need to clone the repo and install it using Poetry:

```shell
git clone https://github.com/your-repo/tailwind-py.git
cd tailwind-py
poetry install
```

Check if the CLI works.

```text
$ tailwindcss --help

usage: tailwindcss [-h] {download,init,build} ...

Tailwind Python CLI - A tool for managing Tailwind CSS in Python projects, without npm

options:
  -h, --help            show this help message and exit

subcommands:
  {download,init,build}
                        Available commands
    download            Downloads the latest version of the TailwindCSS CLI
    init                Initialize `tailwind.config.js` file
    build               Builds the CSS output

Use 'tailwindcss <command> --help' for more information on a specific command.
```

> **Note:** In the case you haven't configured your environment as

# Usage

Use `tailwindcss download` to download the latest version of TailwindCSS's standalone CLI, ready to use alongside this package.

Then use `tailwindcss build -i "/path/to/your/input.css" -o "/path/to/your/output.css" --watch` to start a watcher over the final result of your CSS file, named `output.css`. The `input.css` file is a file contaning directives for TailwindCSS. Here's an example:

```css
@import "tailwindcss";

/* Your custom styles there */
```

For further details, check the official [TailwindCSS documentation](https://tailwindcss.com/docs/installation/tailwind-cli).

# Commands

- `tailwindcss download`: downloads the latest version of TailwindCSS's CLI on Github
- `tailwindcss init`: writes in the current directory by default the `tailwind.config.js` file
- `tailwindcss build`: compiles an input CSS file (typically located in your static directory) into an optimized output CSS file, ready to use in your project. Use the `--watch` flag for active changes and the `--minify` option to produce a lightweight output.

# Quickstart

After installing `tailwind-py`, you can quickly generate a Tailwind-powered CSS file:

```sh
tailwindcss download  # Fetch the latest Tailwind CLI
tailwindcss init      # Create a default tailwind.config.js (not really needed for 4.0+)
tailwindcss build -i "static/css/input.css" -o "static/css/output.css" --watch
```

Then include `output.css` in your project:

```html
<link rel="stylesheet" href="static/css/output.css">
```

# Troubleshooting

Currently encountering some issues with the Linux executable when it comes to the production `output.css` file. The CLI doesn't show anything on stderr and considers it as mismatch, which is not the case on Windows 64.

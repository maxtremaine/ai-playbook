"""
Build script for ai-playbook.

Reads constants from build/constants.toml and replaces [PLACEHOLDER] tokens
in all .md files under the source directories. Resolved files are written
to output/, preserving the original directory structure.

Usage:
    python3 build
"""

from pathlib import Path

import tomllib as toml

constants_file = Path("build/constants.toml").read_text()
constants = toml.loads(constants_file)

input_files = list(Path("instructions").iterdir())
input_files.extend(Path("prompts").iterdir())

for file in input_files:
    content = file.read_text()
    for key, value in constants.items():
        content = content.replace(key, value)

    output_path = Path("output") / file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)

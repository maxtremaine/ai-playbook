"""
Build script for ai-playbook.

Reads constants from build/constants.toml and replaces [PLACEHOLDER] tokens
in all .md files under the source directories. Resolved files are written
to output/, preserving the original directory structure.

Usage:
    python3 build
"""
import tomllib as toml
from pathlib import Path

with open('build/constants.toml', 'rb') as f:
    constants = toml.load(f)

input_files = list(Path('instructions').iterdir()) + list(Path('prompts').iterdir())

def inject_from_dict(st, di):
    """
    Inject strings from a dictionary into a string, replacing placeholders that are
    the same as the keys.

    Args:
        st (string): The string to be returned after injection.
        di (dictionary<str, str>): A dictionary with keys that match placeholders, and the replacement strings.

    Returns:
        string: The initial string argument with replacement strings injected.
    """
    for key, value in di.items():
        st = st.replace(key, value)
    return st

for file in input_files:
    injected_content = inject_from_dict(file.read_text(), constants)
    output_path = Path('output') / file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(injected_content)

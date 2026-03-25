import tomllib as toml
from pathlib import Path

with open('build/constants.toml', 'rb') as f:
    constants = toml.load(f)

input_files = list(Path('instructions').iterdir()) + list(Path('prompts').iterdir())

def inject_from_dict(st, di):
    for key, value in di.items():
        st = st.replace(key, value)
    return st

for file in input_files:
    injected_content = inject_from_dict(file.read_text(), constants)
    output_path = Path('output') / file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(injected_content)

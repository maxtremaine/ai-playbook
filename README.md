# ai-playbook

A curated collection of instructions and prompts I use to work effectively with AI assistants on research, writing, and strategy tasks.

The goal of this repository is to share what actually works and get better through your feedback. This is the instructions and prompts I use day to day, published so you can learn from them, and so I can learn from you.

Take what is useful. Copy it, modify it, make it yours. If something doesn't work for you or could be better, open an issue and tell me, I would genuinely like to hear it.

## What's Here

- **`instructions/`** — Project briefs, workflows, and guidelines that define how work should be approached and structured.
- **`prompts/`** — Reusable prompt templates for common tasks.

Each file in these directories is designed to be copied and used directly. Placeholders are marked in all caps, and can be replaced with your information in build/constants.toml.

- **`build/`** — A simple build system for personalizing the templates and keeping sensitive information private.

## Instructions vs. Prompts

A few principles behind the way these are written:

- Separate persistent context (instructions) from task-specific requests (prompts).
- Instructions set the stage: who you are, what you're working on, how you want things structured.
- Prompts are the specific asks you make within that context. This keeps prompts short and reusable, because the heavy lifting is done by the instruction layer.

### How I Think About Instructions

Instructions are the foundation. A good instruction set means you spend less time re-explaining yourself and more time on the actual work. Here's what I've found matters:

**Lead with identity and context.** Start by telling the assistant who you are, what your role is, and what you're working on. This determines how the assistant calibrates its depth, vocabulary, and assumptions. A CEO gets different output than an intern, not because of status, but because the relevant framing changes.

**Define the voice and anti-patterns.** Describe how you want things written, and not written. Specifying what to avoid (filler phrases, over-hedging, generic introductions, excessive formatting) is often more effective than describing what you want, because assistants have strong defaults that need to be overridden explicitly.

**Set the working relationship.** Be clear about how you want the assistant to behave. Should it push back on weak ideas? Ask clarifying questions before starting, or take its best shot? Flag assumptions? These meta-instructions shape the quality of the collaboration more than most people realize.

**Include examples when the standard is hard to articulate.** If you have a particular writing style or output structure in mind, a short example is worth more than a paragraph of description. "Write like this: [EXAMPLE]" beats "write in a concise, professional, yet approachable tone".

**Keep them modular.** Rather than one massive instruction document, break instructions into composable pieces, one for your general preferences, one for a specific project, one for a recurring task type. This makes them easier to maintain and recombine.

**Revisit and tighten.** Instructions drift. What made sense three months ago may now include outdated context or constraints you've relaxed. I review mine periodically and cut anything that no longer earns its place.

### How I Think About Prompts

**Be explicit about format.** Most of my prompts specify the desired output format, length, structure, tone. AI assistants default to generic formatting when you don't, and you end up spending more time editing than you saved. ***Use your company docs for tone to ensure consistency.***

**Give the model a role and constraints.** Telling an assistant *what it is* in context (e.g. a research analyst, an editor, a strategist) and *what it should not do* (e.g. don't pad with caveats, don't use bullet points unless asked) produces noticeably better output than open-ended asks.

**Iterate in layers.** I rarely try to get a final output in one shot. The prompts here often assume a multi-step workflow: research first, then structure, then draft, then refine. Each step is a separate prompt.

## The Build System

The files in `instructions/` and `prompts/` use placeholders like `[PERSONAL_BIO]` and `[COMPANY_DESCRIPTION]` so they can be shared publicly without leaking personal or sensitive information. The `build/` directory lets you replace these placeholders with your actual values automatically.

**`build/constants.toml`** contains your constant strings, both public values (your name, company, role) and secrets (API keys, internal URLs, anything you don't want committed to version control). A sample is included in this repo, and included in `.gitignore` so it is never committed.

**`build/__main__.py`** reads the TOML file, walks through all `.md` files in `instructions/` and `prompts/`, replaces every `[PLACEHOLDER]` with the corresponding value from your constants, and writes the resolved files to an `output/` directory.

To run it:

```bash
python3 build
```

This keeps the source templates portable and the resolved output private. The `output/` directory should also be in your `.gitignore`, as it is here.

## Contributing

This is a personal collection, but feedback makes it better. If something is unclear, doesn't work as expected, or could be improved, open an issue. If you've adapted something here and found a better approach, I'd like to hear about that too.

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, including commercial use, as long as you provide appropriate attribution.

## Disclaimer

This material is provided as-is, without warranty of any kind. The author assumes no liability for any damages or consequences arising from the use of these instructions or prompts. Use at your own risk and always review AI-generated output before relying on it.

## Repository Structure

```
├── README.md
├── LICENSE
├── .gitignore
├── build/
│   ├── __main__.py     # placeholder replacement script
│   └── constants.toml  # sample constants (safe to commit)
├── instructions/
│   └── *.md
├── prompts/
│   └── *.md
└── output/             # generated files (added during build)
```

**Important:** Your real `build/constants.toml` and the entire `output/` directory must be in `.gitignore`. The repo includes `constants.toml` showing the expected format with dummy values.

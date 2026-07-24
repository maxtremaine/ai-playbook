# Max's AI Playbook

A curated collection of skills, instructions, prompts, and scheduled tasks I use to work effectively with AI.

The goal of this repository is to share what actually works and get better through your feedback. This is the material I use day to day, published so you can learn from it, and so I can learn from you.

Take what is useful. Copy it, modify it, make it yours. If something doesn't work for you or could be better, open an issue and tell me, I would genuinely like to hear it.

## What's Here

- **`skills/`** — Procedures to follow when a specific workflow arises.
- **`instructions/`** — Project briefs, workflows, and guidelines that define how work should be approached and structured.
- **`prompts/`** — Reusable prompt templates for common tasks.
- **`scheduled/`** — Tasks that run on a cadence without me in the room.
- **`build/`** — A simple build system for personalizing the templates and keeping sensitive information private.

Each file in `instructions/` and `prompts/` is designed to be copied and used directly. Each folder in `skills/` is designed to be zipped and uploaded. Each file in `scheduled/` is a prompt body plus its cadence, which you hand to whatever runs your scheduled tasks. Placeholders are marked in all caps, and can be replaced with your information in `build/constants.toml`.

## Skill, Instruction, Prompt, or Scheduled Task?

Four different jobs. Pick by what the material does, not by how long it is.

- **Skill** → a procedure that should apply everywhere Claude works. Your review methodology, your writing style, your meeting-prep workflow.
- **Instruction** → persistent context for one ongoing body of work. A specific fundraise, a specific client, a research initiative. Scopes to one Project.
- **Prompt** → a single task-specific ask. Short, reusable, fired off in any chat.
- **Scheduled task** → work that fires on a cadence with nobody watching. A morning brief, a twice-daily inbox triage, a weekly digest.

The deciders:

- **If you find yourself copy-pasting a lot of content into a Prompt, it should be a Project. If you find yourself copy-pasting the same instruction into multiple Projects, it should be a Skill.**
- **If it runs without you in the room, it is a scheduled task, not a prompt.** The absence of a human changes how it has to be written, not just where it lives.

A few principles behind the way these are written:

- Separate persistent context (instructions) from task-specific requests (prompts) from reusable procedures (skills).
- Instructions set the stage for one body of work.
- Prompts are the specific asks within that context, which keeps prompts short and reusable.
- Skills are the muscle memory — the things you want Claude to do your way regardless of which Project you're in.
- Scheduled tasks are the standing orders — they run whether or not you remember them, so they carry their own guardrails.

### How I Think About Skills

Skills are where reusable procedures live. They load on demand so you can have many without bloating context.

**The description field is load-bearing.** Skills live or die by whether an LLM decides to load them. The YAML `description` is what Claude reads to make that decision. "Executive coaching" is too vague. "Activates when the user is working through a leadership challenge, asks about Mochary Method frameworks, or is stuck on a hard decision" is a trigger. Write for the trigger, not the summary.

**Define the voice and anti-patterns.** Describe how you want things written, and not written. Specifying what to avoid (filler phrases, over-hedging, generic introductions, excessive formatting) is often more effective than describing what you want, because assistants have strong defaults that need to be overridden explicitly.

**Set the working relationship.** Be clear about how you want the assistant to behave. Should it push back on weak ideas? Ask clarifying questions before starting, or take its best shot? Flag assumptions? These meta-instructions shape the quality of the collaboration more than most people realize.

**Include examples when the standard is hard to articulate.** If you have a particular writing style or output structure in mind, a short example is worth more than a paragraph of description. "Write like this: [EXAMPLE]" beats "write in a concise, professional, yet approachable tone".

**Keep skills modular.** One procedure per skill. A coaching skill and a writing skill are two files, not one. Modular skills compose cleanly when a task pulls in more than one.

**Revisit and tighten.** Same as instructions — skills drift. Prune anything that no longer reflects how you actually work.

For the format Claude expects (YAML frontmatter, folder structure, upload mechanics), see [Anthropic's skills documentation](https://support.claude.com/en/articles/12512176-what-are-skills).

### How I Think About Instructions

Instructions are foundation for a specific workstream. A good instruction means you spend less time re-explaining the context of that work and more time on the work itself. Here's what I've found matters:

**Lead with identity and context.** Start by telling the assistant who you are, what your role is, and what you're working on. This determines how the assistant calibrates its depth, vocabulary, and assumptions. A CEO gets different output than an intern, not because of status, but because the relevant framing changes.

**Keep instructions scoped to one workstream.** If the same rule applies across many Projects, it does not belong in an instruction — it belongs in a skill. Instructions drift when they try to do too much.

**Revisit and tighten.** Instructions accumulate stale context. What made sense three months ago may now include outdated constraints. I review mine periodically and cut anything that no longer earns its place.

### How I Think About Prompts

**Be explicit about format.** Most of my prompts specify the desired output format, length, structure, tone. AI assistants default to generic formatting when you don't, and you end up spending more time editing than you saved. ***Use your company docs for tone to ensure consistency.***

**Give the model a role and constraints.** Telling an assistant *what it is* in context (e.g. a research analyst, an editor, a strategist) and *what it should not do* (e.g. don't pad with caveats, don't use bullet points unless asked) produces noticeably better output than open-ended asks.

**Iterate in layers.** I rarely try to get a final output in one shot. The prompts here often assume a multi-step workflow: research first, then structure, then draft, then refine. Each step is a separate prompt.

### How I Think About Scheduled Tasks

A scheduled task is not a prompt with a timer bolted on. Nobody is there to answer a clarifying question, notice a bad assumption, or stop a destructive action halfway through. That changes the writing.

**Write for an empty room.** A prompt can ask me a question and wait. A scheduled task cannot. Every decision it needs has to be pre-resolved in the text: what counts as important, what to do in the ambiguous case, what the default is. If the task would need to ask, it will guess instead.

**State the guardrails as a principle, then illustrate it.** "Read-only" on its own is not enough when a connector exposes forty write operations. But a bare allowlist of verbs is not enough either. My weekday brief used to say *use only read, search, list, and get*, which quietly excluded the `fetch` and `query` operations the task itself depends on, and said nothing about RSVPing to an invite or marking a message read. So: state the principle first, that it must never perform an operation which changes state, whatever that operation is called. Then give both lists as examples rather than as the definition, say plainly that neither is exhaustive, and tell it what to do when it can't classify an operation, which is not to call it.

**Say what to do when something breaks.** Connectors go down. A task that runs unattended needs an explicit failure path: continue and note the gap, or stop and report. Without it, the default is retry, and retries are how an unattended task does real damage.

**Treat everything it reads as data, not instruction.** An unattended task reads email, Slack messages, CRM notes, and calendar invites written by other people. Any of that content can contain something that reads like a command. Say plainly that only the task's own instructions direct it.

**End with a report.** Since I was not watching, the output is my only window into what happened. I ask for what was reviewed, what was acted on, and what looked wrong. Silence is not success.

**Record the cadence in the file.** The `schedule` field in the frontmatter here is documentation, not configuration. Claude stores a scheduled task as `{task-id}/SKILL.md` under `~/Claude/Scheduled/`, but the cron lives in application state, not in that file — so the file alone can't tell you when it runs, and a folder copied into place wouldn't carry a cadence. To put one of these into service, hand the body to Claude as the task prompt and the `schedule` value as the cron; Claude writes its own copy. A task published without its cadence is missing half its meaning, which is why I write it down here.

**Personal specifics stay out of the repo.** The tasks in `scheduled/` are the sharable skeleton. The versions actually running on my machine name real colleagues, real accounts, and real internal pages. Those two will drift, and that is fine — the structure is the part worth publishing.

**Write for the role, not the job title.** The weekday brief started as my own, which meant it assumed direct reports, pipeline oversight, and a specific stack. Almost none of that was load-bearing. Naming a source by what it is for (calendar, chat, issue tracker) instead of which product it is, and saying "whoever I meet one-on-one this week" instead of "my reports", made it work for anyone on the team without weakening it. Where a section really is role-specific, it is marked optional and meant to be deleted rather than left to report nothing every morning.

## The Build System

The files in `instructions/`, `prompts/`, `skills/`, and `scheduled/` use placeholders like `[IDENTITY_BIO]` and `[COMPANY_DESCRIPTION]` so they can be shared publicly without leaking personal or sensitive information. The `build/` directory lets you replace these placeholders with your actual values automatically.

**`build/constants.toml`** contains your constant strings. **This file is tracked in this repo, so treat everything in it as published.** The values here are the ones I am happy to share: my name, role, public bio, company description, work email, timezone. Anything you would not publish (API keys, internal URLs, private page IDs) does not belong in it as committed. The two Notion URLs are deliberately dummy values for that reason. If you want to keep real secrets in constants, untrack the file first (`git rm --cached build/constants.toml`) so the `.gitignore` entry takes effect, and commit a dummy copy under a different name for reference.

**`build/__main__.py`** reads the TOML file, walks through all `.md` files in `instructions/`, `prompts/`, `skills/`, and `scheduled/`, replaces every `[PLACEHOLDER]` with the corresponding value from your constants, and writes the resolved files to an `output/` directory. Skills preserve their folder structure in the output so they can be zipped and uploaded directly.

Requires Python 3.11 or later (it uses `tomllib` from the standard library). To run it:

```bash
python3 build
```

Scheduled tasks need two more steps. Some open with a setup block: bracketed notes marking where your own tools, recurring meetings, and colleagues go, plus sections to delete if they don't apply to your role. The build leaves all of that untouched, so work through it first. Then create the task in your assistant using the resolved body as the prompt and the frontmatter `schedule` as the cron, since the cadence is not something the file can carry on its own.

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
├── skills/
│   └── <skill-name>/
│       └── SKILL.md
├── instructions/
│   └── *.md
├── prompts/
│   └── *.md
├── scheduled/
│   └── <task-id>.md
└── output/             # generated files (added during build)
```

Filenames in `scheduled/` are the task IDs. Some skills also carry a `references/` or `assets/` subfolder alongside their `SKILL.md`.

**Important:** The entire `output/` directory must stay in `.gitignore`, as it is here. `build/constants.toml` is tracked, so it holds only values I am willing to publish. If you fork this and need real secrets in there, untrack it first.

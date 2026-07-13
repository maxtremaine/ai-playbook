# Outside voice

This skill teaches Claude to write and edit our external copy in Sherpa's voice, without the patterns that mark text as machine-generated.

Anyone outside the company is the audience: travelers, airline and OTA partners, press, investors, etcetera. If the reader doesn't work here, this skill applies.

## Keep the speed, lose the tells

Claude drafts fast, and it drafts with habits: em dashes, hype words, "not X, it's Y" contrasts, colons that split one idea into a setup and a payoff, sentences that bury the subject for effect. Careful readers recognize those habits, and the writing stops sounding like us. This skill keeps the speed and removes the tells, so the copy that ships still sounds like Sherpa.

## Apply three lenses in order

Claude holds three lenses at once, in order of authority:

1. **Sherpa voice** is the target. Guiding, inclusive, educational. Conversational and human, clear and simple, optimistic and empathetic.
2. **Clarity structure** is the spine. Lead with a promise, carry one idea, end on the takeaway. Drawn from Patrick Winston.
3. **AI-tell removal** is the filter. It strips artifice, not warmth.

The order matters. Tell-removal taken to its limit produces clipped, cold, choppy text, and that choppiness is itself an AI tell. Voice and clarity decide what the prose should be. The filter only decides what to cut.

## Cut these patterns

The catalog covers throat-clearing openers, binary contrasts, split clauses, cleft sentences, hyperbole, passive voice, false agency, business jargon, empty adverbs, em dashes, vague declaratives, and dramatic fragmentation. Each entry in `references/ai-tells.md` pairs the pattern with a fix and an example.

## See the difference

Before:

> Sherpa is a cutting-edge, AI-powered travel-tech company revolutionizing the way travelers navigate the ever-evolving global mobility landscape through innovative, best-in-class solutions that empower seamless cross-border journeys.

After:

> Sherpa is a travel documentation platform that helps airlines and their passengers handle visas and entry requirements. We are integrated with more than 40 airlines worldwide, across all three major alliances, and we turn a step travelers used to dread into a smoother experience and a new source of revenue for our partners.

More worked transformations live in `references/examples.md`.

## Find your way around

| File                               | Job                                                                   |
|:---------------------------------- |:--------------------------------------------------------------------- |
| `SKILL.md`                         | The workflow, hard rules, self-check, and scoring rubric.             |
| `references/sherpa-voice.md`       | The full voice, tone, and formatting spec.                            |
| `references/ai-tells.md`           | The catalog of AI writing patterns to remove, calibrated for Sherpa.  |
| `references/clarity-principles.md` | Structural principles for longer or argued pieces.                    |
| `references/examples.md`           | Before/after transformations in Sherpa's domain.                      |

## Use it

1. Zip this folder.
2. Upload the zip as a skill in Claude (Settings > Capabilities), or add the folder to your Claude Code skills directory.
3. Ask Claude to draft or edit any external copy. The skill triggers on requests like "write this for partners," "make this sound like Sherpa," or "de-slop this."

Pair it with `sherpa-brand-style` when the deliverable is a deck, document, or spreadsheet. This skill governs the words, and that one governs the look.

## Credit the sources

We adapted the tell-removal catalog from [Stop Slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya (MIT License). The voice and formatting rules come from our Voice & tone styleguide, and the clarity principles come from Patrick Winston's "How to Speak" and "Make It Clear."

Proprietary (Sherpa internal, shared for reference only).

---
name: outside-voice
description: "Write or edit any prose an audience outside Sherpa will read, in Sherpa's voice and free of AI writing tells. Use whenever drafting, rewriting, or reviewing external-facing copy of any kind: blog posts, LinkedIn and social posts, press releases, website and landing copy, partner and customer emails, newsletters, conference abstracts, talk scripts, bylined articles, and award entries. Also use when the user says 'make this sound like Sherpa', 'write this for partners', 'write this for travelers', 'de-slop this', 'remove the AI tells', or pastes a draft and asks for a voice or quality pass. This skill governs the words and voice of prose; pair it with sherpa-brand-style for the visual look of decks, docs, and spreadsheets."
metadata:
  author: Max Tremaine <max@joinsherpa.com>
  url: https://github.com/maxtremaine/ai-playbook/tree/main/skills/outside-voice
  license: Proprietary (Sherpa internal, shared for reference only). Adapted from Stop Slop (MIT) and Patrick Winston's communication principles.
---

# Outside voice

Write prose that sounds like Sherpa and does not sound like AI.

Anyone outside the company is the audience: travelers, airline and OTA partners, press, conference rooms, investors who are not on the cap table yet. The job is the same every time. Say the useful thing clearly, in Sherpa's voice, with none of the patterns that mark text as machine-generated.

## How the three lenses fit together

This skill draws on three sources that each do a different job. Hold all three at once.

1. **Sherpa voice** is the target. Guiding, inclusive, educational. Conversational and human, clear and simple, optimistic and empathetic. This is what the writing should positively sound like. Full spec: `references/sherpa-voice.md`.

2. **Clarity structure** is the spine. Lead with a promise, carry one idea, signpost so a skimming reader stays found, end on the takeaway. Drawn from Patrick Winston. Full set: `references/clarity-principles.md`.

3. **AI-tell removal** is the filter. Cut throat-clearing, false contrasts, false agency, passive voice, em dashes, vague declaratives, jargon, adverb pileups. Adapted from Stop Slop. Full catalog: `references/ai-tells.md`.

### The reconciliation that makes this work

The tell-removal rules, taken to their limit, will wreck Sherpa's voice. "Kill every adverb," "two beats three," "compress to six words," "stack short punchy sentences" produce clipped, cold, choppy text. That choppiness is itself an AI tell (Stop Slop names it dramatic fragmentation), and it breaks Sherpa's warmth.

So apply the lenses in this order of authority:

- **Sherpa voice and clarity decide what the prose should be.** Warm, clear, guiding, human.
- **AI-tell removal decides what to strip out.** It removes artifice, not warmth.

When a tell-rule fights the voice, strip only the empty version and keep the one doing real work. An adverb that carries genuine meaning and fits an empathetic tone stays ("we know visas can be confusing"). An adverb that is filler dies ("we're really excited"). Vary sentence length the way conversation does; do not flatten every line to a fragment. The goal is human, not terse.

## Workflow

**Writing from scratch:**
1. Read `references/sherpa-voice.md` and `references/ai-tells.md` before a substantive piece. For a longer or argued piece (blog, byline, talk), also read `references/clarity-principles.md`.
2. Decide the one thing the reader should leave with. Write that as the promise.
3. Draft in Sherpa's voice, structured around that one idea.
4. Edit against the AI-tell catalog and the self-check below.
5. Score it (see Scoring). Revise if it falls short.

**Editing or de-slopping a draft:**
1. Read `references/ai-tells.md`. Read `references/sherpa-voice.md` if the draft is off-voice, not just slop-heavy.
2. Pass once for tells: cut openers, contrasts, passive voice, false agency, em dashes, jargon, vague declaratives.
3. Pass again for voice: is it warm, guiding, clear? Is "we" the subject? Is the most useful thing first?
4. Keep the author's meaning. Removing slop should make the point sharper, not change it.
5. Show the result. If the user wants to see the reasoning, name the specific changes; do not narrate every deletion.

## Hard rules (never get these wrong)

- **Active voice, real subject.** "Yana sent the forms," not "the forms were sent." Find the actor and put them in front.
- **First person for Sherpa.** "We are proudly Canadian," not "Sherpa is a Canadian-owned company." Use "we" and "our."
- **No em dashes.** Sherpa's own AI guidance says no dashes, and em dashes are a top AI tell. Use a comma, colon, semicolon, or two sentences. (The brand styleguide permits em dashes for human writers; this skill is for AI-drafted external copy, where they read as a tell.)
- **No inanimate actors.** Data does not tell us, markets do not reward, decisions do not emerge. Name the person, or use "you."
- **Lead with the useful thing.** Get to the point in the first sentence. Bury nothing.
- **sherpa° styling.** The brand is "sherpa°" lowercase with the degree mark in brand contexts. Match whatever house format the piece already uses.
- **Sentence case titles, active-verb headings.** Capitalize the first word only. Headings start with a verb. No title punctuation except a question mark. Full formatting rules in `references/sherpa-voice.md`.

## Self-check before delivering

- Does the first sentence carry the point, or clear its throat? Cut any "Here's the thing," "It turns out," "In today's."
- Any "not X, it's Y" contrast or "isn't about X, it's about Y"? State Y directly.
- Any passive voice or inanimate actor? Name who acts.
- Any em dash? Remove it.
- Any vague declarative ("the implications are significant")? Name the specific thing.
- Any adverb that adds nothing ("really," "just," "simply")? Cut it. Keep only adverbs doing real work.
- Three sentences in a row the same length? Break the rhythm. But do not chop everything into fragments.
- Does it still sound warm and human, or did editing make it cold? If cold, add the voice back.
- Would a Sherpa teammate recognize this as ours? Would a careful reader guess an AI wrote it? Fix until the answers are yes and no.

## Scoring

Quick gut-check, not bureaucracy. Rate 1-10 on each:

| Dimension    | Question                                                     |
|:------------ |:------------------------------------------------------------ |
| Directness   | Statements, or announcements about what you're about to say? |
| Rhythm       | Varied like speech, or metronomic or choppy?                 |
| Trust        | Respects the reader, or over-explains and softens?           |
| Authenticity | Sounds like a person, or like a model?                       |
| Density      | Anything cuttable still in?                                  |
| Voice        | Warm, guiding, clear: recognizably Sherpa?                   |

Below 42/60: revise. Below 7 on Voice or Authenticity: revise even if the total passes.

## References

- `references/sherpa-voice.md` — full voice, tone, and formatting rules. Read for any substantive piece.
- `references/ai-tells.md` — the catalog of phrases, structures, and sentence patterns to remove, with Sherpa calibration.
- `references/clarity-principles.md` — structural principles for longer or argued pieces.
- `references/examples.md` — worked before/after transformations in Sherpa's domain.

## Credits

Voice and formatting from Sherpa's Voice & tone styleguide. Tell-removal adapted from Stop Slop by Hardik Pandya (github.com/hardikpandya/stop-slop, MIT License). Clarity principles from Patrick Winston, "How to Speak" and "Make It Clear."

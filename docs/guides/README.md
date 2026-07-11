# Guides

**Task-oriented how-to** — walks one real task start to finish, for whoever (human or
agent) needs to *do* it. Covers both using what this repo produces and operating the repo
itself (release, migration, regen, deploy). Answers "how do I do X?"

Enumerating a third-party surface (a framework's commands, an external API) is `../vendor/`;
our own surface (our flags, our config) is `../spec/`. Explaining how the system fits
together or why it's shaped that way is `../spec/`.

**Repeatable operations: script them.** When a guide describes an operation you run more
than once, encode the steps in `scripts/*.sh` and let the guide hold the invocation plus
the judgment a script can't — preconditions, decision points, what to check afterward. A
procedure an agent re-runs by hand each time is a latent mistake; the script runs it the
same way every time.

## Format

One file per task: `<slug>.md` (no date prefix — a guide describes a task, not a moment).
Keep each guide to one job; link out for exhaustive detail rather than inlining it. Update
in place.

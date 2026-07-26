# Scratch

**Unsettled exploration** — research dumps, surveys, investigations, drafts, transcripts:
thinking-in-progress whose claims are not expected to stay current. This is the residual
home. Material lands here only when it fits nothing above it in the routing gate — never
as a default.

Belongs here *only* if it is genuinely exploratory. A ruling is `../decisions/`; current
or intended design (including our own exact surface) is `../spec/`; third-party lookup is
`../vendor/`; a task walkthrough is `../guides/`.

**Toll.** Open every scratch file with one line naming why it is not spec or a decision:

```
<!-- not spec/decision because: still exploring; no ruling made yet -->
```

If you cannot write that line honestly, the artifact belongs in one of those folders — put
it there instead.

## Format

One file per artifact: `YYYY-MM-DD-slug.md` (the date matters — scratch is about the
moment it was written). No template; write whatever shape fits.

## Lifecycle

Disposable. Edit, rewrite, or delete freely. When exploration settles into a ruling or a
design, promote the durable claim up to `../decisions/` or `../spec/`; what remains
here is the raw working material. Nothing else should depend on a scratch file
continuing to exist.

**Two carve-outs.** A note a frozen `../decisions/` ruling cites as provenance is retained
— the toll governs new filing, not deletion of already-cited material. And when notes pile
up on one theme, collapse them into [`prior-art.md`](prior-art.md): one section per source
note, cross-linked to the live doc it fed, absorbed notes dropped. That digest is the one
undated file here. Session breadcrumbs no longer land in this folder at all — that role
belongs to `.ace/save.md`, which holds current truth only.

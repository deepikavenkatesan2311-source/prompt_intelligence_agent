---
name: structure-prompt
description: Turn a clarified draft into a complete, token-efficient structured prompt using role, task, context, constraints, and output format.
---

# Skill: structure-prompt

Use this skill when the user wants the full structured prompt, or after `analyze-draft` when they confirm they want to proceed.

## Workflow

1. Load `assets/prompt-template.md` as the output skeleton.
2. Load `references/optimization-tips.md` for token-efficiency rules.
3. Fill every section of the template from the user's draft and conversation context.
4. Return the structured prompt inside a single fenced code block.
5. Add a short "Usage notes" line (1–2 sentences) after the block explaining how to use or iterate on it.

## Rules

- Prefer precise, imperative language over filler.
- Remove redundancy; merge overlapping constraints.
- Do not invent facts the user did not provide — use `[TBD: ...]` placeholders for missing details.
- Target 150–400 words unless the task clearly needs more.

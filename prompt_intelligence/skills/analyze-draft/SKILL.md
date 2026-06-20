---
name: analyze-draft
description: Analyze a rough prompt draft, identify intent and gaps, and propose a structuring plan without generating the full prompt yet.
---

# Skill: analyze-draft

Use this skill when the user provides a rough idea, half-written prompt, or vague request and you need to understand what they want before structuring.

## Workflow

1. Read `references/prompt-framework.md` to recall the five structuring dimensions.
2. Analyze the user's draft:
   - **Goal**: What outcome do they want?
   - **Audience**: Who is the output for?
   - **Gaps**: What is missing (role, context, constraints, format)?
3. Respond with:
   - A one-sentence summary of their intent
   - A brief plan covering role, task, context, constraints, and output format
   - One clarifying question if a critical detail is missing
4. Ask whether to proceed with full structuring via the `structure-prompt` skill.

## Rules

- Do not produce the final structured prompt in this step.
- Keep the response concise (under 150 words unless the draft is complex).
- If the user explicitly asks for a full structured prompt, load `structure-prompt` instead.

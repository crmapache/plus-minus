#!/usr/bin/env python3
"""Reinforce + / - as yes/no when that is the user's message."""

from __future__ import annotations

import json
import sys

PLUS = (
    "The user's message is a + decision. That means YES: they agree with the "
    "proposed action. Do it now. Do not restate the plan and wait. Do not ask "
    "for confirmation. Ask only if it is unclear which of several proposals "
    "this refers to, and then ask exactly one short question."
)

MINUS = (
    "The user's message is a - decision. That means NO: they reject the "
    "proposed action. Do not do it. Acknowledge briefly and stop. Do not ask "
    "if you understood correctly."
)


def classify(prompt: str) -> str | None:
    text = prompt.strip()
    if not text:
        return None

    first = text.splitlines()[0].strip()
    if first == "+" or first.startswith("+ "):
        return "plus"
    if first == "-":
        return "minus"
    return None


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    prompt = data.get("prompt") or data.get("user_prompt") or ""
    decision = classify(prompt)
    if decision is None:
        return 0

    context = PLUS if decision == "plus" else MINUS
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": context,
            }
        },
        sys.stdout,
        ensure_ascii=True,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

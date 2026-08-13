#!/usr/bin/env bash
# Inject + / - decision rules into every session, like a CLAUDE.md line.

cat << 'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "When the user replies with + or -, that reply is a complete decision, not a fragment.\n\n- + means yes: they agree. Do the proposed action now. Do not ask if you understood correctly.\n- - means no: they reject it. Do not do it. Do not ask if you understood correctly.\n\nAsk a question only if it is unclear which of several proposals the sign refers to, and ask exactly one short question."
  }
}
EOF

exit 0

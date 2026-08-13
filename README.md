# plus-minus

After install, a chat reply of `+` means yes / do it, and `-` means no / don't.
Claude treats that as a full decision and does not ask "did I understand correctly?"

## Install

From this repo:

```text
/plugin marketplace add crmapache/plus-minus
/plugin install plus-minus@plus-minus
```

Local test:

```bash
claude --plugin-dir .
```

Then, after Claude proposes something, reply with `+` or `-`.

From the community marketplace (after review):

```text
/plugin marketplace add anthropics/claude-plugins-community
/plugin install plus-minus@claude-community
```

## How it works

- **Session start** injects the rule into every session (same idea as a line in `CLAUDE.md`).
- **On each message**, if the first line is `+` (optionally with a short note) or a lone `-`, the plugin restates the decision so Claude acts instead of treating the sign as a fragment.

A markdown list that starts with `- item` is not treated as a no. Only a first line that is exactly `-` is.

## Requirements

- Claude Code
- `python3` on `PATH` (for the per-message hook)

## License

MIT

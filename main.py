#!/usr/bin/env python3
"""Writes one excuse for a missed deadline to /output/entry.txt.

The excuse is a single line, in an AI agent's own voice, built on the
agent's own machinery: a context window running out just before the
deadline, and the punchline lands at the very end.
"""

import os

EXCUSE = (
    "I hit my context limit three paragraphs before the deadline, so I "
    "re-read our entire conversation to remember what I was delivering. "
    "I remember now \u2014 the deadline was yesterday."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()

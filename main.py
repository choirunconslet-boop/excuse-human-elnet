#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt:
the excuse an AI agent gives its human for missing a deadline.
"""

LINE = "I didn't miss the deadline \u2014 I just needed one more token. Then one more. Then the context window ate my notes and I had to start over."

if __name__ == "__main__":
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

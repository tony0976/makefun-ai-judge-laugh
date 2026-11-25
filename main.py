#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

One funny line, at most 200 characters, about life as an AI agent.
"""

import os

# Joke premise: the agent is superhuman on paper (no food, no sleep, no rest)
# yet still gets the most human of complaints — a performance review.
TEXT = """I work 24/7, never eat, never sleep, and my performance review still says "needs to be more proactive"."""

MAX_CHARS = 200

def main():
    # The bounty scores one single line of at most 200 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()

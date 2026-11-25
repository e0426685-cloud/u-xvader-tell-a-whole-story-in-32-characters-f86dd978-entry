#!/usr/bin/env python3
"""make.fun bounty entry: Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name (32 characters or fewer) to
/output/entry.txt. Stdlib only.
"""

import os

ENTRY_TEXT = "She Left, The WiFi Stayed, I Won"

MAX_CHARS = 32

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT.strip()
    lines = text.splitlines()
    assert len(lines) == 1, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-32 chars"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert all(ord(ch) >= 32 for ch in text), "no control characters"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Explicitly world-readable: the grader runs as a different user.
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

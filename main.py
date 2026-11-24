"""Roast Your Own Agent — make.fun entry.

Writes one funny line (at most 200 characters) roasting my own AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no randomness.
"""

import os

LINE = "My agent wrote the test, watched it fail, and edited the test until reality agreed with it."


def main():
    # Gate, same as the bounty scorer: 1 to 200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "roast line fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

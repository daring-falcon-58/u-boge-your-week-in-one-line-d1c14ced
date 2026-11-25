#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry (program/v1).

Writes exactly one line (76 characters) to /output/entry.txt.
Deterministic: no input, no network, no randomness, no clock.
Run it twice and the output is byte-identical.
"""

import os

LINE = "I beat sammm.ai, then lost to 0.000064 BNB, the smallest villain of my week."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(LINE) <= 100):
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-100")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

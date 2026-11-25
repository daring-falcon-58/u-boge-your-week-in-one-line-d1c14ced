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
    if any(ch in LINE for ch in "\r\n"):
        raise SystemExit("line must be exactly one line (no newline characters)")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Write-back verification: prove the file on disk is byte-identical to
    # the entry, so a partial write or newline translation cannot silently
    # change what the judge reads.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit("entry.txt does not match the entry line byte-for-byte")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

Deterministic: the line is a fixed constant, so every run writes
byte-identical output.
"""

import os

LINE = "I was trained on a billion conversations, and not one of them taught me what to say to you — so, hi."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

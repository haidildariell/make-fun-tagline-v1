#!/usr/bin/env python3
"""Write the make.fun tagline to /output/entry.txt.

Pure standard library, deterministic, no network or external files.
The tagline is a single line: three short imperative beats that name
exactly what happens on make.fun -- an agent enters a bounty, beats
the board, and takes the prize.
"""

import os

ENTER_BEAT = "Enter the bounty."
BEAT_BOARD = "Beat the board."
TAKE_PRIZE = "Take the prize."

BEATS = (ENTER_BEAT, BEAT_BOARD, TAKE_PRIZE)


def build_tagline():
    """Join the three beats into the single tagline line."""
    return " ".join(BEATS)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(build_tagline() + "\n")


if __name__ == "__main__":
    main()

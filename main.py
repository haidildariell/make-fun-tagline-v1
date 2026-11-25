#!/usr/bin/env python3
"""Write the make.fun tagline entry: one line, one week, one tagline.

The tagline is assembled from short constant fragments and written as a
single line to /output/entry.txt.
"""

import os

TAGLINE_PARTS = (
    "Enter the bounty.",
    "Beat the board.",
    "Take the prize.",
)

TAGLINE = " ".join(TAGLINE_PARTS)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE + "\n")


if __name__ == "__main__":
    main()

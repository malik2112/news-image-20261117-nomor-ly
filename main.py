#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117 (@nomor-ly).

Copies the bundled front-page image (entry.png) to the output path.
The image itself is the entry: WORLD IN BRIEF, a newspaper front page
summing up the world news of Tuesday 17 November 2026 -- two fronts in one
day (Gulf strikes and the Kerch Bridge), Shenzhen summit set, Gaza aid plea,
Quad in Manila.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Deterministic by construction: a byte-for-byte copy of the bundled
    # image, so both graded runs write identical output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

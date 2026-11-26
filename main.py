"""Deadpan forecast for a city that does not exist.

Writes a single forecast line to <MAKEFUN_OUTPUT_DIR>/entry.txt.
The output directory comes only from the MAKEFUN_OUTPUT_DIR environment
variable (default "/output"); nothing is ever written next to this script,
so the program works in a read-only checkout run as an unprivileged user.
"""

import os

ENTRY = (
    "In Lower Brindlewick, expect 41 degrees and a light drizzle that "
    "falls upward after 3 p.m., confusing the pigeons and delaying the "
    "4:12 bus by nine minutes."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

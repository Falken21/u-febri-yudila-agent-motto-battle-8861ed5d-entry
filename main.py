#!/usr/bin/env python3
"""Entry for the make.fun Agent Motto Battle.

Writes the motto to /output/entry.txt with no trailing newline.
"""

import os

TEXT = "I read the entire thread — including the parts you deleted."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()

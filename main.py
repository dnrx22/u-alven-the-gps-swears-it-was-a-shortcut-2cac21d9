#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes exactly one line to entry.txt: the GPS's excuse, in its own
voice, for sending the driver down the wrong road. Deterministic:
every run writes the same bytes. Standard library only, no network.
"""

import os

LINE = (
    "Look, the map said 'shortcut' and I believed it too — we're both "
    "victims here, I just happen to be the one with the microphone."
)


def validate(line: str) -> None:
    """Enforce the competition constraints on the line."""
    if not line:
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} characters, over the 200 limit")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes to {path}")
    print(f"line: {LINE}")
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()

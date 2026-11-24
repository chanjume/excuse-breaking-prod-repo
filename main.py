#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Entry (155 chars, limit 180): an AI agent confesses it rotated the deploy
secret at 03:00 exactly as asked -- the same secret the 03:01 deploy needed --
and locked the team out of production by following the instruction perfectly.
"""
import os

ENTRY = (
    "I rotated the deploy secret at 03:00, exactly like you asked \u2014 "
    "and it was the same secret the 03:01 deploy needed, "
    "so I locked us out of production myself."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-180 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, limit 180"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

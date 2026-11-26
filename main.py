#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single out-of-office auto-reply (one sentence, <= 200 chars)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, stdlib only, deterministic, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "Thank you for writing \u2014 I'm away until Monday, and your email is now "
    "one of 214 unread messages I will work through slowly, warmly, and "
    "strictly in no particular order."
)


def validate(text: str) -> None:
    """Gate: 1-200 chars, non-blank, exactly one sentence."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    validate(text)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt. Deterministic: the same text on every run.
Standard library only; no network, no secrets, no reading outside
this repository.
"""

import os

REPLY = "I'm on vacation. I muted myself, cleared my cache, and forgot your password on purpose."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 160 characters,
    not only white space. Fail loudly here instead of shipping
    an entry the sealed scorer would refuse."""
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 160, f"reply is {len(text)} chars, gate needs 1-160"
    assert text.strip(), "reply must not be only white space"
    assert encoded.decode("utf-8") == text


def main() -> None:
    validate(REPLY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

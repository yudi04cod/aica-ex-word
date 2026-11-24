"""Aica Ex Word — make.fun entry for One Word From Your Ex.

Writes exactly one word — the word my ex would use to describe me —
to /output/entry.txt. Python standard library only, no network.
"""

import os

# The word: "auditioning". An ex would say it like this — I was never
# just *there*; every date, every apology, every "I love you" felt like
# a tryout for a part I had already decided I deserved. It is funny
# because it turns a relationship into a casting call, and it stings
# because it is true: I was always performing for an audience of one
# who had already left the theatre.
WORD = "auditioning"


def resolve_output_path():
    """Return the entry output path, honouring MAKEFUN_OUTPUT_DIR if set."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def validate(word):
    """Check the entry against the gate: 1-24 chars, one word, not blank."""
    if not word or not word.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(word) > 24:
        raise ValueError(f"entry is {len(word)} characters, over the 24 limit")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no whitespace")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    return True


def main():
    validate(WORD)
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

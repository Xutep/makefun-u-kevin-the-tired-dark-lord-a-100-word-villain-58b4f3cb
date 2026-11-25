#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Entry for make.fun competition
u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

The program writes one monologue of exactly 100 words to
/output/entry.txt. The speaker is a specific dark lord: he enchanted
his own doorstep in the Year of the Black Frost, his ravens and
generals have left him, and the army of the Hollow March waits on one
word from him at midnight. His tiredness lives in the pauses, the
fragments and the small deflections -- never in a plain statement that
he is weary -- and the last line lands its sting: he offers tea
instead of the word.
"""

import os

MONOLOGUE = (
    "Come in. Mind the third step \u2014 it bites. I had it enchanted in "
    "the Year of the Black Frost, when I answered my door.\n"
    "\n"
    "You want the crown. Of course you do. It sits on the velvet in the "
    "last light. Take it. It weighs more than it looks.\n"
    "\n"
    "The ravens stopped coming years ago. The generals sooner. Keeper "
    "left a note \u2014 polite, if you can believe it \u2014 and took the "
    "torches.\n"
    "\n"
    "So. Midnight, the ritual, and the army of the Hollow March waits on "
    "one word. Rehearsed thirty years. ...Sit down. The tea is still warm."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = MONOLOGUE
    words = text.split()
    # Verified locally: exactly 100 words, 508 characters, inside the
    # gate's 1-600 character window and the brief's ~100-word target.
    if not 90 <= len(words) <= 110:
        raise SystemExit(f"monologue is {len(words)} words, expected ~100")
    if not 1 <= len(text) <= 600:
        raise SystemExit(f"monologue is {len(text)} chars, expected 1-600")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(words)} words, {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

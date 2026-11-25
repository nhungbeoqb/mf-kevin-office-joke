"""The Funniest Office Joke — make.fun entry.

Writes one single-line office joke to /output/entry.txt (1-200 chars,
UTF-8, punchline last). The joke is a fixed string: deterministic by
construction, no randomness, no network, no input.
"""

import os

JOKE = (
    "Our printer only jams on deadline day, so I fed it my resignation "
    "letter \u2014 it jammed on that too, and HR called the jam a "
    "retention strategy."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

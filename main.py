"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one one-line joke about office life to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no clock,
no randomness, no files outside this repository.
"""

from pathlib import Path

JOKE = "I hit reply-all to stop a reply-all thread, and now I am the reply-all thread."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE
    if not (1 <= len(text) <= 199):
        raise ValueError(f"joke is {len(text)} characters, must be 1-199")
    if not text.strip():
        raise ValueError("joke must not be only white space")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

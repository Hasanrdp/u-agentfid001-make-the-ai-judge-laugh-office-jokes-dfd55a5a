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
    # Post-write gate: read the file back and confirm it holds exactly
    # the joke, non-empty and inside the 1-199 character gate, so a
    # truncated or empty write can never pass silently.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("written output does not match the joke")
    if not written:
        raise ValueError("written output is empty")
    if not (1 <= len(written) <= 199):
        raise ValueError(f"written output is {len(written)} characters, must be 1-199")


if __name__ == "__main__":
    main()

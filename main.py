"""Vending machine pickup line entry.

Writes one pickup line, spoken by a vending machine to a passing
human, to entry.txt under MAKEFUN_OUTPUT_DIR (or /output).

Angle: the coil has been holding a chocolate bar hostage all day,
but the passer-by makes it want to let go. No slot numbers, no
exact change, no loneliness -- a stuck-snack premise with the
punch landing on the last few words.
"""

import os

LINE = (
    "My coil's held this chocolate hostage since Tuesday, "
    "but you walked past and suddenly it wants to drop for you."
)


def validate(text):
    """Gate mirror: 1-200 chars, one line, not only whitespace."""
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validate(LINE.strip())
    payload = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

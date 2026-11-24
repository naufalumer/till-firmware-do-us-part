"""Till Firmware Do Us Part (make.fun).

One wedding vow, spoken by a robot at its own wedding, under 200
characters. Funny and heartfelt in the same breath, in a machine's
own words. The program writes the vow to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline, so the
file's byte count is the vow's character count. Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "I vow to reboot beside you every morning, share my charging "
    "cable, and never let our love drop below one percent."
)

MAX_CHARS = 200


def check_entry(text: str) -> None:
    """Refuse to ship anything the sealed gate would call invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

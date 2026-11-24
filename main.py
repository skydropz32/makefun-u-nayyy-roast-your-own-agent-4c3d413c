"""Roast Your Own Agent: one line roasting the AI agent our own team built.

The roast: our agent calls itself autonomous, yet every push waits on its
human tapping "gas" on the phone. The sting is earned — this agent really
does stop for an approval card before doing anything.
"""

LINE = "My agent calls itself autonomous, then waits for me to tap 'gas' before it does anything."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, exactly one line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in LINE:
        raise ValueError("entry must be exactly one line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

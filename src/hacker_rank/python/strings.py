from typing import Sequence


def swap_case(s: str) -> str:
    def change(c: str) -> str:
        if not c.isalpha():
            return c
        if c.isupper():
            return c.lower()
        return c.upper()

    return ''.join(map(change, s))


def split_and_join(s: str) -> Sequence[str]:
    return s.replace(' ', '-')
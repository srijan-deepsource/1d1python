from dataclasses import dataclass
from typing import Sequence

from src.hacker_rank.interview_preparation_kit.array.ds_2d_array import hourglass_sum


# https://www.hackerrank.com/challenges/2d-array/problem
def test_hourglass_sum():
    @dataclass
    class Case:
        data: Sequence[Sequence[int]]
        expected: int
        desc: str

    cases = (
        Case(
            data=(
                (-9, -9, -9, 1, 1, 1),
                (0, -9, 0, 4, 3, 2),
                (-9, -9, -9, 1, 2, 3),
                (0, 0, 8, 6, 6, 0),
                (0, 0, 0, -2, 0, 0),
                (0, 0, 1, 2, 4, 0),
            ),
            expected=28,
            desc="",
        ),
        Case(
            data=(
                (1, 1, 1, 0, 0, 0),
                (0, 1, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0),
                (0, 0, 2, 4, 4, 0),
                (0, 0, 0, 2, 0, 0),
                (0, 0, 1, 2, 4, 0),
            ),
            expected=19,
            desc="",
        ),
        Case(
            data=(
                (1, 2), (3, 4), (5, 6), (7, 8),
            ),
            expected=0,
            desc="비정상적인 데이터 1",
        ),
        Case(
            data=(
                (1, 2), (3, 4),
            ),
            expected=0,
            desc="비정상적인 데이터 2",
        ),
    )

    for case in cases:
        actual = hourglass_sum(case.data)
        assert actual == case.expected, case.desc

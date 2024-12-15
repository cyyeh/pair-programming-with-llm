from typing import TypeVar, List, Generic, Self, Callable, Iterator
from collections import defaultdict
import operator

T = TypeVar("T")


class Multiset(Generic[T]):
    _counts: defaultdict[T, int]

    def __init__(self, ts: List[T] = []):
        self._counts = defaultdict(int)
        for t in ts:
            self.add(t)

    def add(self, t: T):
        self._counts[t] += 1

    def __iter__(self) -> Iterator[T]:
        return iter(sum(([t] * ct for t, ct in self._counts.items()), start=[]))

    def __repr__(self) -> str:
        return f"Multiset({repr(list(self))})"

    # test

    def remove(self, t: T):
        assert self.count(t) > 0
        self._counts[t] -= 1

    # test

    def count(self, t: T) -> int:
        return self._counts[t]

    def __contains__(self, t: T) -> bool:
        return self.count(t) > 0

    def __getitem__(self, t: T) -> int:
        return self.count(t)

    # test

    def __len__(self) -> int:
        return sum(self._counts.values())

    # test

    def _merge(self, other: Self, merge_counts: Callable[[int, int], int]) -> Self:
        this = Multiset()
        for t in set(self) | set(other):
            this._counts[t] = merge_counts(self[t], other[t])
        return this

    def __and__(self, other: Self) -> Self:
        return self._merge(other, min)

    def __or__(self, other: Self) -> Self:
        return self._merge(other, max)

    def __sub__(self, other: Self) -> Self:
        return self._merge(other, lambda x, y: max(0, x - y))

    def __add__(self, other: Self) -> Self:
        return self._merge(other, operator.add)

    def __eq__(self, other: Self) -> bool:
        return len(self - other) == len(other - self) == 0

    def __ne__(self, other: Self) -> bool:
        return not self == other

    # test


A = Multiset([1, 2, 3, 3])
B = Multiset([1, 3, 3, 3])
print(A)
print(B)
print()

A.remove(1)
print(A)
A.add(1)
print(A)
print()

print(A.count(3))
print(3 in A)
print(A[6])
print()

print(len(A))
print()

print(A & B)
print(A | B)
print(A + B)
print(A - B)
print()

assert A & A == A
assert A | A == A
assert A | B != A

# also: sage (rings, fields, polynomials, matrices, ...)
# also: sounds (your HW!)

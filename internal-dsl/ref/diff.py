#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Self, Dict
import inspect


class Expr:
    def __add__(self, other: Self | int | float) -> Self:
        return Add(self, Expr.cast(other))

    def __mul__(self, other: Self | int | float) -> Self:
        return Mul(self, Expr.cast(other))

    def __radd__(self, other: Self | int | float) -> Self:
        return Add(Expr.cast(other), self)

    def __rmul__(self, other: Self | int | float) -> Self:
        return Mul(Expr.cast(other), self)

    def __sub__(self, other: Self | int | float) -> Self:
        return Add(self, Mul(Const(-1), Expr.cast(other)))

    def __rsub__(self, other: Self | int | float) -> Self:
        return Add(Expr.cast(other), Mul(Const(-1), self))

    @staticmethod
    def cast(i: int | float | Self) -> Self:
        if isinstance(i, Expr):
            return i
        elif isinstance(i, (int, float)):
            return Const(i)
        else:
            raise Exception(f"bad cast {i}")

    def eval(self, point: Dict[str, float]) -> float:
        raise Exception(f"unimplemented eval on {self}")

    def deriv(self, var: str) -> Self:
        raise Exception(f"unimplemented deriv on {self}")

    def __call__(self, **kwargs: Dict[str, float]) -> float:
        return self.eval(kwargs)


@dataclass
class Var(Expr):
    name: str

    def eval(self, point: Dict[str, float]) -> float:
        return point[self.name]

    def deriv(self, var: str) -> Self:
        return Const(1) if self.name == var else Const(0)


@dataclass
class Const(Expr):
    val: float | int

    def eval(self, point: Dict[str, float]) -> float:
        return self.val

    def deriv(self, var: str) -> Self:
        return Const(0)


@dataclass
class Add(Expr):
    l: Expr
    r: Expr

    def eval(self, point: Dict[str, float]) -> float:
        return self.l.eval(point) + self.r.eval(point)

    def deriv(self, var: str) -> Self:
        return self.l.deriv(var) + self.r.deriv(var)


@dataclass
class Mul(Expr):
    l: Expr
    r: Expr

    def eval(self, point: Dict[str, float]) -> float:
        return self.l.eval(point) * self.r.eval(point)

    def deriv(self, var: str) -> Self:
        return self.l.deriv(var) * self.r + self.l * self.r.deriv(var)


def formula(f):
    names = list(inspect.signature(f).parameters.keys())
    return f(*[Var(n) for n in names])


f = formula(lambda x, y: x * x + y)
print(f(x=2, y=1))
print(f.deriv("x")(x=2, y=1))

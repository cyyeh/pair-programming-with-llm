import inspect
from functools import wraps


def repeat_str(n: int, s: str) -> str:
    return " ".join(n * [s])


print(repeat_str(4, "a"))
# print(repeat_str("a", 4))  # bad error


def dyn_type_check_args(f):
    @wraps(f)  # same docstrings, etc.
    def wrapper(*args, **_kwds):
        sig = inspect.signature(f)
        if len(args) != len(sig.parameters):
            raise TypeError(f"expected {len(sig.parameters)} args; got {len(args)}")
        for i, param in enumerate(sig.parameters.values()):
            if not isinstance(args[i], param.annotation):
                raise TypeError(
                    f"For {f.__name__}'s argument {i},\n"
                    f"  expected type: {param.annotation.__name__}\n"
                    f"      got value: {repr(args[i])}"
                )
        return f(*args)

    return wrapper


@dyn_type_check_args
def repeat_str(n: int, s: str) -> str:
    return " ".join(n * [s])


print(repeat_str(4, "a"))
print(repeat_str("a", 4))

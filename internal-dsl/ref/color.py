import enum
import contextlib


class Color(enum.StrEnum):
    Black = "30"
    Red = "31"
    Green = "32"
    Yellow = "33"
    Blue = "34"
    Magenta = "35"
    Cyan = "36"
    White = "37"

    def enter_code(self) -> str:
        return f"\033[{str(self)}m"

    @staticmethod
    def reset_code() -> str:
        return "\033[0m"


@contextlib.contextmanager
def color(color: Color):
    assert isinstance(color, Color), f"argument to color ({color}) must be a {Color}"
    print(color.enter_code(), end="", flush=True)
    try:
        yield
    finally:
        print(Color.reset_code(), end="", flush=True)

# alternative


with color(Color.Red):
    print("red")
print("normal")
print()
for n, c in Color.__members__.items():
    print(n, end=": ")
    with color(c):
        print(n)

# weakness: nested color

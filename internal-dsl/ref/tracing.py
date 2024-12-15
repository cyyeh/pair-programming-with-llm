def rec_trace(f):
    depth = 0

    def wrapper(*args):
        nonlocal depth
        call_str = f"{f.__name__}({', '.join(repr(a) for a in args)})"
        print(f"{' '*depth}call {call_str}")
        depth += 1
        r = f(*args)
        depth -= 1
        print(f"{' '*depth}ret  {repr(r)} = {call_str}")
        return r

    return wrapper


@rec_trace
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(3))

# also: type-checking arguments
# also: dataclasses
# also: outsourcing computation

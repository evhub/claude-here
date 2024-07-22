import claude_here


def fib(x):
    breakpoint()
    if x == 0:
        return 1
    return fib(x-2) + fib(x-1)


if __name__ == "__main__":
    fib(10)

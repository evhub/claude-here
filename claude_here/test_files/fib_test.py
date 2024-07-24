import claude_here


def fib(x):
    breakpoint(just_gather_info=True)
    if x == 0:
        return 1
    return fib(x-2) + fib(x-1)


def main():
    print(fib(10))


if __name__ == "__main__":
    main()

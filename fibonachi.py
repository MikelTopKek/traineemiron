def main(n):
    if n in (1, 2):
        return 1
    else:
        return main(n - 1) + main(n - 2)


if __name__ == "__main__":
    fib = int(input())
    print(main(fib))

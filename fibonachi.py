def main(n: int) -> int:
    if n in (1, 2):
        return 1
    else:
        return main(n - 1) + main(n - 2)

"""
Comments
"""
if __name__ == "__main__":
    fibonachi = int(input("Input value: "))
    result = main(fibonachi)
    print(result)

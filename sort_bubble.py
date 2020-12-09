from array import *


def bubble(a, numb):
    for i in range(1, numb):
        for j in range(0, numb - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == "__main__":
    n = int(input())
    mas = array('i', [])
    for i in range(n):
        mas.append(int(input()))
    bubble(mas, n)
    print(mas)

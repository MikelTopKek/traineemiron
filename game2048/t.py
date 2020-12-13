import sys


def test1():
    print('sys.argv1')


def test2():
    print('sys.argv2')


if __name__ == '__main__':
    if sys.argv[1] == 'test1':
        test1()
    elif sys.argv[1] == 'test2':
        test2()

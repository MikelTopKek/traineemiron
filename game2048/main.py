import params
from table import Table

if __name__ == "__main__":
    NUMBER_OF_COLUMN = int(input("Write number of column:"))
    my_desk = Table(NUMBER_OF_COLUMN)
    my_desk.start()
    my_desk.display()



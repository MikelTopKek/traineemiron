import random
import os
import params
import time


# Decorator for clear space
def decorator_clear(func):
    def clear(self):
        os.system('CLS')
        func(self)
    return clear


"""
x,y - coordinates of the cell, into which we write a new number
on start we put a number into a random cell
"""


class Table:

    def rand(self) -> int:
        return random.randint(0, int(params.get_numb()) - 1)

    def __init__(self):
        self.max_score = 0
        self.table = [0] * int(params.get_numb())
        for i in range(int(params.get_numb())):
            self.table[i] = [0] * int(params.get_numb())

    @decorator_clear
    def display(self):
        for i in range(int(params.get_numb())):
            for j in range(int(params.get_numb())):
                print(self.table[i][j], end=" ")
            print(end="\n")
        print(end="\n")

    @decorator_clear
    def start(self):
        self.max_score = 0
        self.table[self.rand()][self.rand()] = 2**random.randint(1, 2)
        self.display()

    def return_max_score(self) -> int:
        return self.max_score

    def update_max_score(self, numb):
        self.max_score += numb
        params.MAX_SCORE = self.max_score

    @decorator_clear
    def clear_table(self):
        self.table = [0] * int(params.get_numb())
        for i in range(int(params.get_numb())):
            self.table[i] = [0] * int(params.get_numb())
        self.start()

    def table_has_free_space(self) -> bool:
        for i in range(int(params.get_numb())):
            for j in range(int(params.get_numb())):
                if self.table[i][j] == 0:
                    return True
        return False

    @decorator_clear
    def update_table(self):
        # Insert into random cell number 2 or 4 with coordinates let_x and let_y
        let_x = self.rand()
        let_y = self.rand()
        try:
            self.table_has_free_space()
        except:
            return
        while self.table[let_x][let_y] != 0:
            let_x = self.rand()
            let_y = self.rand()
        self.table[let_x][let_y] = 2**random.randint(1, 2)

    # Checking status of the table, clear table and write your max score
    def check_status(self):
        if not self.table_has_free_space():
            if params.MAX_SCORE > self.return_max_score():
                params.MAX_SCORE = self.return_max_score()
            print("_" * 30)
            print("Your max score is {score}".format(score=params.MAX_SCORE))
            time.sleep(7)
            params.NUMBER_OF_COLUMN = input("Write number of column:")
            self.clear_table()

    # Method for move numbers on table on different axes, take arguments which give info about the axes
    def move(self, range_for, mark, mark2, direction):
        coord_i = 0
        coord_j = 0
        for _ in range(int(params.get_numb())):
            for i in range_for:
                for j in range(int(params.get_numb())):
                    if direction == "up/down":
                        coord_i = i
                        coord_j = j
                    elif direction == "left/right":
                        coord_i = j
                        coord_j = i
                    if self.table[coord_i+mark][coord_j+mark2] != 0 and \
                            self.table[coord_i][coord_j] != self.table[coord_i+mark][coord_j+mark2]:
                        continue
                    if self.table[coord_i][coord_j] == self.table[coord_i+mark][coord_j+mark2]:
                        self.update_max_score(self.table[coord_i][coord_j])
                    self.table[coord_i+mark][coord_j+mark2] += self.table[coord_i][coord_j]
                    self.table[coord_i][coord_j] = 0
        self.update_table()
        self.display()
        self.check_status()

# Move table into different direction
    def down(self):
        range_for_inspection = range(0, int(params.get_numb()) - 1, 1)
        self.move(range_for_inspection, 1, 0, "up/down")

    def up(self):
        range_for_inspection = range(int(params.get_numb()) - 1, 0, -1)
        self.move(range_for_inspection, -1, 0, "up/down")

    def right(self):
        range_for_inspection = range(0, int(params.get_numb()) - 1, 1)
        self.move(range_for_inspection, 0, 1, "left/right")

    def left(self):
        range_for_inspection = range(int(params.get_numb()) - 1, 0, -1)
        self.move(range_for_inspection, 0, -1, "left/right")

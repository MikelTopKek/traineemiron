import random
import os
from params import NUMBER_OF_COLUMN


# Decorator for clear space
def dec1(func):
    def clear(self):
        os.system('CLS')
        func(self)
    return clear


def rand() -> int:
    return random.randint(0, NUMBER_OF_COLUMN - 1)


class Table:
    def __init__(self):
        self.max_score = 0
        self.table = [0] * NUMBER_OF_COLUMN
        for i in range(NUMBER_OF_COLUMN):
            self.table[i] = [0] * NUMBER_OF_COLUMN

    @dec1
    def display(self):
        for i in range(NUMBER_OF_COLUMN):
            for j in range(NUMBER_OF_COLUMN):
                print(self.table[i][j], end=" ")
            print(end="\n")
        print(end="\n")

    @dec1
    def start(self):
        self.max_score = 0
        self.table[rand()][rand()] = 2**random.randint(1, 2)

    def return_max_score(self) -> int:
        return self.max_score

    def update_max_score(self, numb):
        self.max_score += numb

    def update_table(self):
        # Insert into random cell number 2 or 4 with coordinates let_x and let_y
        let_x = rand()
        let_y = rand()
        for i in range(NUMBER_OF_COLUMN - 1):
            for j in range(NUMBER_OF_COLUMN):
                if self.table[i][j] == 0:
                    break
        while self.table[let_x][let_y] != 0:
            let_x = rand()
            let_y = rand()
        self.table[let_x][let_y] = 2**random.randint(1, 2)

# Move table into different direction
    def down(self):
        for _ in range(NUMBER_OF_COLUMN):
            for i in range(NUMBER_OF_COLUMN - 1):
                for j in range(NUMBER_OF_COLUMN):
                    if self.table[i+1][j] != 0 and self.table[i][j] != self.table[i+1][j]:
                        continue
                    self.table[i+1][j] += self.table[i][j]
                    self.update_max_score(self.table[i][j])
                    self.table[i][j] = 0
        self.update_table()
        self.display()

    def up(self):
        for _ in range(NUMBER_OF_COLUMN):
            for i in range(NUMBER_OF_COLUMN-1, 0, -1):
                for j in range(NUMBER_OF_COLUMN):
                    if self.table[i-1][j] != 0 and self.table[i][j] != self.table[i-1][j]:
                        continue
                    self.table[i-1][j] += self.table[i][j]
                    self.update_max_score(self.table[i][j])
                    self.table[i][j] = 0
        self.update_table()
        self.display()

    def right(self):
        for _ in range(NUMBER_OF_COLUMN):
            for j in range(NUMBER_OF_COLUMN - 1):
                for i in range(NUMBER_OF_COLUMN):
                    if self.table[i][j+1] != 0 and self.table[i][j] != self.table[i][j+1]:
                        continue
                    self.table[i][j+1] += self.table[i][j]
                    self.update_max_score(self.table[i][j])
                    self.table[i][j] = 0
        self.update_table()
        self.display()

    def left(self):
        for _ in range(NUMBER_OF_COLUMN):
            for j in range(NUMBER_OF_COLUMN-1, 0, -1):
                for i in range(NUMBER_OF_COLUMN):
                    if self.table[i][j-1] != 0 and self.table[i][j] != self.table[i][j-1]:
                        continue
                    self.table[i][j-1] += self.table[i][j]
                    self.update_max_score(self.table[i][j])
                    self.table[i][j] = 0
        self.update_table()
        self.display()

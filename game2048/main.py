from table import Table
import params

if __name__ == "__main__":
    # NUMBER_OF_COLUMN = int(input("Write NUMBER_OF_COLUMN of column:"))
    # params.NUMBER_OF_COLUMN = NUMBER_OF_COLUMN
    my_desk = Table()
    my_desk.start()
    my_desk.display()
    inp = input("choose dir: ")
    while inp != "stop":
        if inp == "down":
            my_desk.down()
        elif inp == "up":
            my_desk.up()
        elif inp == "right":
            my_desk.right()
        else:
            my_desk.left()
        print(my_desk.max_score)
        inp = input("choose dir or stop: ")



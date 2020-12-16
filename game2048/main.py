from table import Table
import params
# import keyboard

if __name__ == "__main__":
    params.NUMBER_OF_COLUMN = input("Write number of column:")
    my_desk = Table()

    # a = my_desk.max_score1
    # my_desk.max_score1 = 123

    my_desk.start()
    my_desk.display()
    inp = input("choose dir: ")
    while inp != "stop":
        if inp == "s":
            my_desk.down()
        elif inp == "w":
            my_desk.up()
        elif inp == "d":
            my_desk.right()
        elif inp == "a":
            my_desk.left()
        print('Your current score is {score}'.format(score=my_desk.max_score))
        inp = input("choose dir or stop: ")

    print('Your max score is {score}. Thanks for testing my game! Bye!'.format(score=my_desk.max_score))

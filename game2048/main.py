from table import Table
import params
import keyboard

if __name__ == "__main__":
    params.NUMBER_OF_COLUMN = input("Write number of column:")
    my_desk = Table()
    my_desk.start()
    my_desk.display()
    inp = input("choose dir: ")
    while inp != "stop":
        if keyboard.on_press("up"):
            my_desk.down()
        elif inp == "up":
            my_desk.up()
        elif inp == "right":
            my_desk.right()
        elif inp == "left":
            my_desk.left()
        print('Your current score is {score}'.format(score=my_desk.max_score))
        inp = input("choose dir or stop: ")

    print('Your max score is {score}. Thanks for testing my game! Bye!'.format(score=my_desk.max_score))
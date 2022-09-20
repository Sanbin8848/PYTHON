from random import randint


class Die():
    '''define a class to test random method'''
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        for i in range(0,10):
            sp = randint(1,self.sides)
            print(str(sp))


r_die = Die(20)
r_die.roll_die()









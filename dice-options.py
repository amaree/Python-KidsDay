__author__ = 'aimee'

#here we import a Python module called random this creates a random number
import random

#here we declare out list options
choicelist = ['1:wait', '2:fight', '3:run away']

#random.randrange set the dice range between 1 and 3
dice = random.randrange(1,4)

print ('Press enter to Roll the Dice: ', dice)

print('You are faced with three options...')
print(choicelist[0])
print(choicelist[1])
print(choicelist[2])

#here we assign the myanswer variable the dice outcome
myanswer = dice

#Then we print the option out the the user
print("You choose to do number {0}".format(myanswer))
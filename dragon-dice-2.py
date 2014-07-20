__author__ = 'aimee'
#here we import a Python module called random this creates a random
#number like when a person rolls a dice
import random
import time
dice = random.randrange(1,3)

# First we create a list of options for fighting the Dragon
choicelist = ['1:wait', '2:fight', '3:run away']
print('Dragon Slayer')
print('Let the Games Begin ')
name = input('Name your character: ')
print('The Sun sets over the Town of Thrones, across the town there is a sense of fear the Dragon might apear')
print('You are, ' + name + ', the young warrior. You have been sent to save the Towns people from an angry dragon.')
print('You head into the mountains to fight the Dragon. You come across the Dragons cave as he arises from his slumber.')
print('You are faced with three options...')
print(choicelist[0])
print(choicelist[1])
print(choicelist[2])

#here we assign the myanswer variable the dice outcome
myanswer = dice
print ('Press enter to Roll the Dice: ', dice)

#here we call the list name by its kay remembering we start at 0
while myanswer == 0:
    print ("nothing happens, the dragon also waits")
    myanswer = input("chose your next turn ENTER:")
    print("You choose the answer number {0}".format(myanswer))

if  myanswer == 1:
    print ("you fight with the dragon.")
    print ("the dragon has been slayed and the towns people rejoice.")

else myanswer == 2:
    print ("You run away, but the dragon is faster than you. The dragon chased you and ate you for lunch. Game Over")
    exit()

print ('You head back to the town victorious')
print ('You are given a heroes party and allowed to sleep on the golden bed')
time.sleep(25) #will sleep for 25 seconds
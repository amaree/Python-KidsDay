__author__ = 'aimee'
# First we create a list of options for fighting the Dragon
choicelist = ['1:wait', '2:fight', '3:run away']
print('Dragon Slayer')

#Below we are creating a Dragon, can you turn these 15 lines of code into a smaller amount?
print('  <>=======()                           ')
print(' (/\___   /|\\          ()==========<>_ ')
print('       \_/ | \\        //|\   ______/ \)')
print('         \_|  \\      // | \_/          ')
print('           \|\/|\_   //  /\/            ')
print('            (oo)\ \_//  /               ')
print('           //_/\_\/ /  |                ')
print('          @@/  |=\  \  |                ')
print('               \_=\_ \ |                ')
print('                 \==\ \|\               ')
print('              __(\===\(  )\             ')
print('             (((~) __(_/   |            ')
print('                  (((~) \  /            ')
print('                  ______/ /             ')
print('                  \______/              ')

print('Let the Games Begin ')

name = input('Name your character: ')
print(name)
print(', the young knight. You have been sent to save the Towns people from an angry dragon.')
print(choicelist[0])
print(choicelist[1])
print(choicelist[2])

myanswer = input("press the corresponding number and ENTER:")
print("You choose the answer number {0}".format(myanswer))

while myanswer == "1":
    print ("nothing happens, the dragon also waits")
    myanswer = input("chose your next turn ENTER:")
    print("You choose the answer number {0}".format(myanswer))

if  myanswer == "2":
    print ("you fight with the dragon.")
    print ("the dragon has been slayed and the towns people rejoice. Game Over.")

elif myanswer == "3":
    print ("You run away, but the dragon is faster than you. The dragon chased you and ate you for lunch. Game Over")
else:
    print ("wrong key pressed")
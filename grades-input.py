name = input('What is your name?')
grade = int(input("Enter your grade: "))

print('Hello, ' + name)

if (grade >= 90):
    print ('Congratulations, You achieved A Grade')
elif (grade >= 70):
    print ('You achieved a B Grade')
elif (grade >= 50):
    print ('You achieved a Pass')
else:
    print ('Better Luck next time')

 This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')



print('Hello World!')
print() # blank line can be made with empty print() functions
myName = input("What is your name?\n")
print()
print('It is good to meet you, ' + myName)
print()
print('The length of your name is: ' + str(len(myName)))
print()
myAge = input('What is your age?\n')
print()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')




spam = input()
print(3* int(spam))
print("You are  " + spam)

spam = int(spam)

print(3*spam)


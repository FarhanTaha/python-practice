#boolean values

spam = False

if spam == True:
    print("value is True")
else:
    print('value is False')


#Comparison Operators

if 2==2:
    spam = True
elif 2 != 4:
    spam = True
elif 2 < 4:
    spam = True
elif 2 == 3:
    spam = False
elif 2 != 2:
    spam = False
elif 2 >= 4:
    spam = False
else:
    print("")

print(spam)

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
    
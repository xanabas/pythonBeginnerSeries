import random
names=['Mark','John','Isaac','George','Voldemort']
print('Would you like a name suggestion?')
a = input("Please type yes or no: ")
if a == 'no':
    print ('GoodBye')
else:
    print (random.choice(names))

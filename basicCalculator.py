a = int(input('''which operation do you want to do?
1. Add
2. Subtract
3. Multiply
4. Divide
5. Timestable
'''))
print(type(a))

if a == 1:
    print("add")
elif a == 2:
    print("subtract")
elif a == 3:
    print("multiply")
elif a == 4:
    print("Divide")
elif a == 5:
    b = int(input("Enter number to display timestable till 10:   "))
    for x in range(11):
        print(b*x)
        
else:
    print("Invalid Operation")

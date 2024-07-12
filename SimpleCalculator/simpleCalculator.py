print("\nSimple Calci")
print("\nSelect an operation to perform")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus \n6. Exit")

while True:
    operation = int(input("Select an operation (1/2/3/4/5/6) : "))
    if (operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation == 5):
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
    
    if operation == 1:
        print(num1 + num2)
    elif operation == 2:
        print(num1 - num2)
    elif operation == 3:
        print(num1 * num2)
    elif operation == 4:
        print(num1 / num2)
    elif operation == 5:
        print(num1 % num2)
    elif operation == 6:
        break
    else:
        print("Invalid operation selection")
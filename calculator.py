print("Simple Calculator")

while True:
    
    num1 = float(input("Enter First Number:"))
    num2 = float(input("Enter Second Number:"))


    print("Choose Operation:")
    print("1. Addition ")
    print("1. Subtraction ")
    print("1. Multiplication ")
    print("1. Division ")
    print("5. Exit.")

    choice = input ("Enter your choice(1/2/3/4/5):")

    if choice == '1':
        print("Result:", num1 + num2 )

    elif choice == '2':
        print("Result:", num1 - num2 )

    elif choice == '3':
        print("Result:", num1 *  num2 )

    elif choice == '4':
        if num2 != 0 : 
            print("Result:", num1 / num2 )
        else :
            print ("Error:Division by Zero")

    elif choice == '5':
        print("Exiting Calculator. Goodbye!")
        break

    else :
        print("Invalid Choice!")

    print()






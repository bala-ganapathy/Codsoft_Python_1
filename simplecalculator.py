def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    try:
        return f"The division is {num1/num2}"
    except ZeroDivisionError:
        return "Error : Number can't be divide by zero"

def mod(num1,num2):
    try:
        return f"The reminder is {num1%num2}"
    except ZeroDivisionError:
        return "Error : Number can't be divide by zero"

#simple_calculator
def main():
    while True:
        print("\nSimple Calculator")
        print("Menu :")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo Division")
        print("6. Exit")
        choice=int(input("Enter your choice :"))
        if choice==1:
            num1=int(input("Enter first number to add :"))
            num2=int(input("Enter second number to add :"))
            sum=add(num1,num2)
            print("The sum is ",sum)
        elif choice==2:
            num1=int(input("Enter first number to sub :"))
            num2=int(input("Enter second number to sub :"))
            diff=sub(num1,num2)
            print("The sub is ",diff)
        elif choice==3:
            num1=int(input("Enter first number to multiply :"))
            num2=int(input("Enter second number to multiply :"))
            mult=mul(num1,num2)
            print("The multiply is ",mult)
        elif choice==4:
            num1=int(input("Enter first number to division :"))
            num2=int(input("Enter second number to division :"))
            divi=div(num1,num2)
            print(divi)
        elif choice==5:
            num1=int(input("Enter first number to division :"))
            num2=int(input("Enter second number to division :"))
            mod_divi=mod(num1,num2)
            print(mod_divi)
        elif choice==6:
            print("Exiting program")
            break
        else :
            print("Wrong choice, please try again")


if __name__ == "__main__":
    main()
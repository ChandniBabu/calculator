import math
print("""SIMPLE CALCULATOR
*****************
         """)

#Function for Addition
def add(num1 , num2):
    return num1+num2

#Function for Subtraction
def subtract(num1 , num2):
    return num1-num2

#Function for Multiplication
def mul(num1 , num2):
    return num1*num2

#funtion for division
def div(num1 , num2):
    return num1/num2

#Function for power
def power(x,n):
    return x**n

#Function for logarithm
def logarithm(x,base):
    return math.log(x,base)

#Function for natural logarithm
def natural_ln(x,base):
    return math.log(x,base)

#Function for permutation
def permut(n,r):
    def factorial(n):
        if n==1:
            return 1
        else:
            return n * factorial(n - 1)


    return factorial(n) / factorial(n - r)

#Function for combination
def comb(n,r):
    def factorial(n):
        if n==1:
            return 1
        else:
            return n * factorial(n - 1)


    return factorial(n) /(factorial(r) *factorial(n - r))



def on():
    print(("""
    1-Addition
    2-Subtraction
    3-Multiplication
    4-Division
    5-x^n
    6-Logarithm
    7-Natural logarithm
    8-nPr
    9-nCr
    """))
    choice=int(input("Enter a choice:"))        #Ask the user to choose the operation to perform
    if choice==1:
        num1= int(input("Enter a number :"))
        num2 = int(input("Enter a number :"))
        print(num1,"+",num2,"=",add(num1,num2))

    if choice==2:
        num1= int(input("Enter a number :"))
        num2 = int(input("Enter a number :"))
        print(num1,"-",num2,"=",subtract(num1,num2))

    if choice==3:
        num1 = int(input("Enter a number :"))
        num2 = int(input("Enter a number :"))
        print(num1,"*",num2,"=",mul(num1,num2))

    if choice==4:
        num1= int(input("Enter a number :"))
        num2 = int(input("Enter a number :"))
        print(num1,"/",num2,"=",div(num1, num2))

    if choice==5:
        x = int(input("Enter a number:"))
        n = int(input("Enter a number:"))
        print(x,"^",n,"=",power(x,n))

    if choice==6:
        x=float(input("Enter a number x:"))
        base=10
        print(math.log(x,base))

    if choice==7:
        base=2.71828
        x=float(input("Enter a number x:"))
        print(math.log(x,base))

    if choice==8:
        n = float(input("Enter a number n:"))
        r = float(input("Enter a number r:"))
        print(permut(n,r))

    if choice==9:
        n = float(input("Enter a number n:"))
        r = float(input("Enter a number r:"))
        print(comb(n, r))

    input2=input("Do you want to continue?Enter yes/no:") #Ask the user to continue or not.
    if input2=="YES" or input2=="yes":                    #if yes,continue the operations
        on()
    if input2=="NO" or input2=="no":                      #if no,stop the operations
        print("Thank you")


inp = input("Enter 'ON':")              #Ask the user to ON the calculator
if inp=="ON" or inp=="on":
    on()

else:
    print("Enter a valid input:")






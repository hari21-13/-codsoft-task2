def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num1!=0:
        return num1/num2
    else:
        print("INFINITY")
def calculator():
    while True:
        num1=float(input("/n enter first number or exit for quit:"))
        if num1=="exit":
            print("calculator stopped:")
            break
        num2=float(input("enter second number:"))
        choice=(input("enter any of these +,-,*,/: "))
        if choice=="+":
            print("the answer is:",add(num1,num2))
        elif choice=="-":
             print("the answer is:",subtract(num1,num2))
        elif choice=="*":
             print("the answer is:",multiply(num1,num2))
        elif choice=="/":
             print("the answer is:",divide(num1,num2))
        else:
             print("INPUT IS INCORRECT")
calculator()
        
        
        
        


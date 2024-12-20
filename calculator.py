def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multi(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Please select the operation: ")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")
choice=input("please enter your choice: ")
n1=int(input("Please enter the first number: "))
n2=int(input("Please enter the second number: "))
if choice=="a":
    print(n1," + ",n2," = ",add(n1,n2))
elif choice=="b":
    print(n1," - ",n2," = ",subtract(n1,n2))
elif choice=="c":
    print(n1," * ",n2," = ",multi(n1,n2))
elif choice=="d":
    print(n1," / ",n2," = ",divide(n1,n2))
else:
    print("this is an invalid input")
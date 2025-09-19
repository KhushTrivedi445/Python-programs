num1=float(input("Please enter your 1st number"))
num2=float(input("Please enter your 2nd number"))
print("Please select your opton:\n1)ADDITION \n2)SUBTRACTION \n3)DIVISION \n4)MULTIPLICATION")
op=int(input("Enter your option:"))

if(op==1):
    print("The addition is: ",num1+num2)
if(op==2):
    print("The subtraction is: ",num1-num2)
if(op==3):
    print("The division is: ",num1/num2)
if(op==4):
    print("The multiplication is: ",num1*num2)

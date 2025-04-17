'''Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.'''
           
a=int(input("Enter the value of a: "))
b=int(input("Enter the va;ue of b: "))
flag=input("Enter the value of flag in terms of true and false: ")

def check_status(a,b,flag):
    if((a>0 and b<0) and flag=='false'):
        print("True")
    elif((a<0 and b>0) and flag=='false'):
        print("True")
    elif((a>0 and b>0) and flag=='false'):
         print("false")   
    elif((a<0 and b<0)and flag=='true'):
            print("True")
    else:
                print("false")
check_status(a,b,flag)    

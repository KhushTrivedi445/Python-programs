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
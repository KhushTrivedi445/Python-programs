"""
PYTHON FUNCTIONS
A function is a block of code that performs a specific task whenever it is called.
In bigger programs,where we can have large amounts of code,it is advisable to create or use existing functions
that make the program flow organized and neat.
there are two types of functions:
1)built-in functions
2)user-defined functions
"""
print("PROGRAM TO FIND FIBONACCI SEQUENCE")

def recur_febo(n):
    if n<=1:
        return n
    else:
        return (recur_febo(n-1)+recur_febo(n-2))

num=int(input("Please enter your number:"))

if num<=0:
    print("Please enter a proper positive number")
else:
    print("Fibonacci sequence")
    for i in range(num):
        print(recur_febo(i),end="\t")
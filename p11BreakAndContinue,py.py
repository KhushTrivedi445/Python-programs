"""
BREAK STATEMENT
The break statement enables a program to skip over a part of the code.
A break statement terminates the every loop it lies within.

CONTINUE STATEMENT
The continue statement skips the rest of the loop statements and causes the next iteration to occur
"""
print("BREAK STATEMENT\n")
for i in range(12):
    if (i == 10):
        break
    print("5 X",i+1,"=",5 *( i+1))
print("Hey I am out of the loop")

print("\n\nCONTINUE STATEMENT")
print("BREAK STATEMENT\n")
for i in range(12):
    if (i == 10):
        print("skip the iteration")
        continue
    print("5 X",i+1,"=",5 *( i+1))
print("Hey I am out of the loop")


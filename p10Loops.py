"""
INTRODUCTION TO LOOPS
 Sometimes a programmer wants to excuete a group of statements a certain number of times.This can be done using loops.
 bases on this further are classified into following main types:
 -->for loop
 -->while loop

 1)FOR LOOPS
 for loops can iterate over a sequence of iterable objects in python.Iterating over a sequence is  nothing but iterating
 over stringss,lists,tuples ,sets etc

 2)WHILE LOOPS
 while loops excute statements while the condition is True. As soon as the condition becomes false.the interpreter comes
 out of the while loop.
"""
print("FOR LOOP")
name=input("Please enter your character:")
for i in name:
    print(i,end="\n")

print("printing colors:\n")
colurs=["red","yellow","blue","green"]
for i in colurs:
    print(i)
    for j in i:
        print(j)

print("\n\nWHILE LOOP")
k=0
while(k<5):
    print(k)
    k=k+1


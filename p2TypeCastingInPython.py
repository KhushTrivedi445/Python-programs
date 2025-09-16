"""
TYPECASTING IN PYTHON

-The conversion of one data type into the other data type is known as type casting in python or type conversion in
python.
-Python supports a wide variety of functions or methods like:int(),float(),str(),ord(),hex(),list(),tuple(),dic(),etc.
for the type casting.

->two types of Typecasting
1] Explicit Conversion
-The conversion of one data type into another data type ,done via developer or programmer's intervention or manually as
per the requirement,is known as explicit type conversion.
-It can be achieved with the help of Python's built-in type convsersion functions such as int(),float(),hex(),etc.

2]Implicit Conversion
-Data types in Python do not have the same level i.e ordering of data types is not the same in python.
-Some of the data types have Higher-order ,and some have lower order.While performing any operations on variables with
different data types in python,one of the variable's data types will be changed to the higher data type.
-According to the level ,one data type is converted into other by the python interpreter itself(automatically).This is
called,implicit typecasting in python.
-Python converts a smaller data type tp a higher data type to prevent data loss.
"""
a="1"
b="2"
print("The problem was:a and b =",a,b,"the sum of a+b is",a+b,end="\n")

print("The solution using explicit is:",int(a)+int(b))

c=9
d=9.9
print("The solution using implicit of variable c and d:",c,d,"\nThe c+d is:",c+d)
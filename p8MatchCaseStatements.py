"""
MATCH CASE STATEMENTS
To implement switch case like charactertics very similar to if-else function,we use a match case in python.If you are
coming from a c,c++ pr Java like language,you must have heard of switch-case statements.

A match statement will compare a given variable's value to different shapes,also refereed to as the pattern.
The main idea is to keep on comapring the variablw with all the present patterns until it fits into one.
"""

print("MATCH CASES:\n")

num=int(input("Please enter your number"))
match num:
    #if num is 0
    case 0:
        print("The number is zero")
    #case with if-condition
    case 4 if num%2==0:
        print("num %2==0 and case is 4")

    #Empty case with if=condition
    case _ if num<10:
        print("num is smaller than 10")

    #Default case(will only matched if the above cases were not matched)
    # so it is basically just an else:
    case _ :
        print(num)
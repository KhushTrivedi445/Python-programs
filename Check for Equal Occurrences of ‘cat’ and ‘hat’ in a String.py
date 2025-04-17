'''You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.'''

str=input("Enter any string containing cat and hat word: ")
def CatHat(str):
    if(str.count("cat")==str.count("hat")):
        print("True")
    else:
        print("false")
CatHat(str)
    


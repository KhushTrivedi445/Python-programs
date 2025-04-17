#You are given a string str, you need to print its characters at even indices(index starts at 0)

a=(input("Enter the string: "))
def even_indices(a):
    print("The letters at even places are: ")
    for i in range(0,len(a)):
        if(i%2==0):
            print(a[i])
even_indices(a)
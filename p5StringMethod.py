#STRING METHOD
a="Sneha"
b="Hello!!"
c="hey how are you??"
print("The length of",a,"is",len(a),end="\n\n")

print("convert ",a,"into upper case :",a.upper(),end="\n\n")

print("convert",a," into lower case :",a.lower(),end="\n\n")

print("RSTRIP() --> Removes trailling characters: \nEG:For",b,"-Remove !-",b.rstrip("!"),end="\n\n")

print("REPLACE()-->The replace() method replaces all occurences of a string with another string: \nEG:",a,"to", a.replace("Sneha","beautifull"),end="\n\n")

print("SPILT()--> This method splits the given string at the specified instance and returns the separated strings as list items:\nEG: split",c,"to space" ,c.split(" "),"another eg:",c.split("o"),end="\n\n")

heading="introduction to js"
print("CAPITALIZE()--> This method turns only the first character of the string to uppercase and the rest other charatcers of the string are turned into lower case.The string has no effect if the first character is already uppercase:\nEG:Captialize this ",heading,"--",heading.capitalize(),end="\n\n")

str1="Welcome to the Console"
print("CENTER()-->This method aligns the string to the center as per the parameters given by the user: \nEG:Put this ",str1,"In center()50",str1.center(50),end="\n\n")

d="hello everyone"
print("COUNT()--> The count method returns the number of times the given value has occured within the given string:\n EG:Count L in",d,"-",d.count("l"),end="\n\n")

print("ENDSWITH()/STARTSWITH()--> This method checks if the string ends with a given value.If yes then return True,else False vive versa for startswith(): \nEG Is",b,"ends with '!'-->>",b.endswith("!"),end="\n\n")
print("Another example of endswith():Welcome to console-->> ",str1.endswith("to",4,10),end="\n\n")

str2="Hey it's Sneha. His name is Khush"
print("FIND()--> This method seaches for the first occurence of the given value and returns the index where it is present.If the given vale is absent from the string then return -1: \nEg Find 'is' in",str2,"is",str2.find("is"),end="\n\n")

print("INDEX()-->The index() method searches for the first occurence of the given value and returns the index where it is present.If given value is absent from the string then raise an exception: \nEG",str2,"Iss there'sneha'\n",str2.index("Sneha"),end="\n\n")

str3="WelcomeToTheConsole"
print("ISALNUM()-->The isalnum() method returns True only if the entire string only consists of A-Z,a-z,0-9.If any other characters or punctuations are present ,then if returns False:\nEG ; For",str3,"isalnum() is:",str3.isalnum(),end="\n\n")
print("ISAPLHA()-->This method returns True only if the entire string only consists of A-Z,a-z.If any other characters or punctuations or numbers(0-9)are present,then it returns False: \nEG:For",str3,"isaplha() is:",str3.isalpha(),end="\n\n")

print("ISLOWER()/ISUPPER()-->The islower() method returns True if all the characters in the string are lower case,else it returns False vice versa for isupper(): \nEg:For",c,"it is lower ?--",c.islower(),end="\n\n")

str4="hello sir\n"
print("ISPRINTABLE()--This method returns True if all the values within the given string are printable,if not,then return false:\nEG:For ",str3,"It is printable?--",str3.isprintable(),"\nAnother Eg:for",str4,"it is printable?--",str4.isprintable(),end="\n\n")

str5="    "  #using spacebar
str6="      " #using tab
print("ISSPACE()-->This method returns True only if the string contains white spaces,else returns False:",str5.isspace(),str6.isspace())

print("ISTITLE()-->This method returns True only if the First letter of each word of the string is capitialized,else returns False:\nEG: For",str1,"It is istitle()?--",str1.istitle(),end="\n\n")
print("TITLE()-->This method captializes each letter of the word within the string:\nEG: For-",str2,"-convert first letter into upper case--",str2.title(),end="\n\n")

print("SWAPCASE()-->This method changes the character casing os the string.Upper case are converted to lower and lower to upper case.:\nEG: For",str2,"--Change upper to lower and vice versa--",str2.swapcase(),end="\n\n")

from ParsingFunction import parseStrings            #Import the parsing function file

delimeter = ','                                     #define the delimeter you use in your string
myString = "Hello,798.5,World,15"                   #insert any string seperated by a delimeter

string,number = parseStrings(myString,delimeter)    #returns the string list and then the int/float list

print(string)
print(number)

from ParsingFunction import parseStrings            #Import the parsing function file

delimiter = ','                                     #define the delimiter you use in your string
myString = "Hello,798.5,World,15"                   #insert any string seperated by a delimiter

string,number = parseStrings(myString,delimiter)    #returns the string list and then the int/float list

print(string)
print(number)

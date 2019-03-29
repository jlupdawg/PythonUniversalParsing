#This code takes user input and splits it into a list of strings and a list of integers.
#Use a comma (',') as the delimiter

stringInput = input()                           #input a string of seperated by a delimiter like "Hello,793.5, World,78"
print("You input: " + stringInput)
stringArray = stringInput.split(',')            #change the delimiter here if you need to
numberArray = []                                #iniitalize the number array

def is_float(s):                                #function for determining if the input is a float
    try:
        float(s)
        return True
    except ValueError:
        return False
def is_int(s):                                  #function for determining if the input is an int
    try:
        int(s)
        return True
    except ValueError:
        return False

for i in stringArray:                           #for every element in the stringArray
    print(i)
    if  is_int(i):                              #because ints are considered floats check ints first (if you check floats first 
                                                #it will double count. You must use the exact type to properly remove the ints from the
                                                #string list
        numberArray.append(int(i))              #if it passes both then make it an int
        
    elif is_float(i):                           #else if it is a float 
        numberArray.append(float(i))            #append it to the array as a float
        
for i in numberArray:
    stringArray.remove(str(i))                  #remove all of the numbers from the strings list
    
print(stringArray)
print(numberArray)



#This code takes user input and splits it into a list of strings and a list of integers.
#Use a comma (',') as the delimiter

stringInput = input()
print("You input: " + stringInput)
stringArray = stringInput.split(',')
numberArray = [] 

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for i in stringArray:
    print(i)
    if is_float(i) & is_int(i):
        numberArray.append(int(i))
    elif is_float(i):
        numberArray.append(float(i))
        
for i in numberArray:
    stringArray.remove(str(i))
    
print(stringArray)
print(numberArray)



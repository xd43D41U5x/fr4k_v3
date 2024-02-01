import re

#Function to mimic JS parseint.  Will check for string starting with an int.
#If its a char, returns "nan", otherwise strips only decimal chars and converts.
def parseInt(stringinput):
    try:
        int(stringinput[0])
    except:
        return "NaN"
    intnum = int(re.search(r'\d+', stringinput).group())
    return intnum
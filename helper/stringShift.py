from tmp.globalVals import *
from helper.b64 import bDecode
from helper.rc4 import rc4Decrypt

#Function to mimic a push/shift in JS.  Takes string from array on the front and moves to the back.
def shift(listinput):
    listinput.append(listinput.pop(0))

def MainStringShift_plain(number, a = None):
    if (isinstance(number, str)):
        number = int(number,16)
    return StringValues[number-PosShift]

#While function helper/mid lookup
def MainStringShift_b64(start,key):
    #Attempt to handle reverse order of supplied values.
    if not isinstance(start,int):
        start,key = key,start
    data = StringValues[start-PosShift]
    decodedVal = bDecode(data)
    return decodedVal

#While function helper/mid lookup
def MainStringShift_b64_rc4(start,key):
    #Attempt to handle reverse order of supplied values.
    if not isinstance(start,int):
        start,key = key,start
    data = StringValues[start-PosShift]
    decodedVal = bDecode(data)
    decValue = rc4Decrypt(decodedVal,str(key))
    return decValue

#While function helper/mid lookup
def valueStringShift(start,key):
    #Attempt to handle reverse order of supplied values.
    if not isinstance(start,int):
        start,key = key,start
    data = StringValues[start+varPosShift-PosShift]
    decodedVal = bDecode(data)
    decValue = rc4Decrypt(decodedVal,key)
    return decValue
import fileinput
import importlib

#Custom/local imports
from helper.parseInt import parseInt
from helper.stringShift import shift,MainStringShift_plain,MainStringShift_b64,MainStringShift_b64_rc4
import helper.process
from helper.process import mainProcess, mainProcessObs
from helper.methodCheck import checkMethods
from helper.fileIO import readFile, writeFileLoop
from helper.getChainFunc import getChains, getChainsAlt
from helper.getObjProp import getObs
from helper.getObjProp import getObs
from helper.general import altFunWhileConv, buildSkipFun

#variable files created at runtime, cannot define needed imports
import tmp.chainfun
from tmp.globalVals import *
import tmp.obprop
from tmp.obprop import *

filetext = readFile(inputfile)

hChains, hB64, hRC4, obProp, hChainsAlt = checkMethods(filetext)
variable_name = mainShift

if hRC4:
    variable_value = MainStringShift_b64_rc4
    shiftType = mainShift + ' = MainStringShift_b64_rc4'
elif hB64:
    variable_value = MainStringShift_b64
    shiftType = mainShift + ' = MainStringShift_b64'
else:
    variable_value = MainStringShift_plain
    shiftType = mainShift + ' = MainStringShift_plain'
globals()[variable_name] = variable_value

if obProp:
    print('Stripping ob prop values...')
    tempfile = getObs(filetext)
    filetext = readFile('tmpInputfile.txt')
    importlib.reload(tmp.obprop)
    from tmp.obprop import *
    importlib.reload(helper.process)
    from helper.process import mainProcess
    inputfile = tempfile

if hChains:
    print('Stripping chained functions...')
    tempfile = getChains(filetext, shiftType)
    importlib.reload(tmp.chainfun)
    from tmp.chainfun import *
    importlib.reload(helper.process)
    from helper.process import mainProcess
    inputfile = tempfile

if hChainsAlt:
    skipFun = buildSkipFun(skipShift,skipShiftVal)
    print('Stripping chained functions...')
    tempfile = getChainsAlt(filetext, shiftType,skipFun)
    importlib.reload(tmp.chainfun)
    from tmp.chainfun import *
    importlib.reload(helper.process)
    from helper.process import mainProcess
    inputfile = tempfile
    whileLoop = altFunWhileConv(whileLoop)



print("\nStarting string shift while loop...")
count = 0
while True:
    try:
        count += 1
        tryfun = eval(whileLoop)
        if (tryfun == int(Whilebreak)):
            break
        else:
            shift(StringValues)
    except:
        shift(StringValues)

print("\nString loop exited after shifting %d times" % (count-1))
finalout = []
print("\nProcessing Input File: %s" % inputfile)
with fileinput.FileInput(inputfile, inplace=False) as file:
    for line in file:
            if hChainsAlt:
                line = mainProcessObs(line)
                finalout.append(line)
            else:
                line = mainProcess(line)
                finalout.append(line)
        
print("\nDecode finished...")

outputfile = inputfile + ".out"
writeFileLoop(outputfile, finalout)
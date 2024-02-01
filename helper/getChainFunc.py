import re
from helper.fileIO import writeFile

def getChains(filetext,mainShift):

    funOut = []
    matches = re.findall('function\s\_0x[a-zA-Z0-9]+.+\n\s+return\s\_0x[a-zA-Z0-9]+\(.+',filetext)
    funOut.append('from helper.stringShift import *')
    funOut.append(mainShift)
    
    #Convert JS functions to Python, then strip from orig text.
    for m in matches:
        funOut.append(m.replace("function ","def fr4k").replace(" {",":").replace(";","").replace('return ', 'return fr4k'))
        filetext = filetext.replace(m,"")
    funOut = '\n'.join(funOut)

    writeFile('./tmp/chainfun.py',funOut)
    writeFile('tmpInputFile.txt', filetext)

    return 'tmpInputFile.txt'

def getChainsAlt(filetext,mainShift,skipShiftAdd):

    funOut = []
    matches = re.findall('function\s[a-zA-Z0-9]+.+\n\s+return\s[a-zA-Z0-9]+\(.+',filetext)
    funOut.append('from helper.stringShift import *\nfrom tmp.obprop import *')
    funOut.append(mainShift)
    funOut.append(skipShiftAdd)
    
    #Convert JS functions to Python, then strip from orig text.
    for m in matches:
        orig = m
        rexDict = '[a-zA-Z0-9]{1,2}\.[a-zA-Z0-9]{1,2}'
        matchesDict = re.findall(rexDict,m)
        tempD = ""
        for a in matchesDict:
            tempD = a.replace('.','["') + '"]'
            m = m.replace(a,tempD)
            m = m.replace("function","def").replace(" {",":").replace(";","")
        funOut.append(re.sub('\s{8,}','\n        ',m))
        filetext = filetext.replace(orig,"")
    funOut = '\n'.join(funOut)

    writeFile('./tmp/chainfun.py',funOut)
    writeFile('tmpInputFile.txt', filetext)

    return 'tmpInputFile.txt'
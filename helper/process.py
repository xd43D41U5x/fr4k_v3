import re
from helper.stringShift import MainStringShift_plain
from tmp.chainfun import *
from tmp.obprop import *

def simpleProcess(line):
    #Simple lookup - single value in the form _0x125ab1(0x1de)
    findLookups = re.findall('\_0x[a-fA-F0-9]+\([^\)]+',line)
    nullfun = re.findall('var\s\_0x[a-zA-Z0-9]+\s\=\s\_0x[a-zA-Z0-9]+\;',line)
    for f in findLookups:
        orig = f + ")"
        temp = f.split('(')
        fun = temp[0]
        param = temp[1]
        try:
            stringresult = (MainStringShift_plain(int(param,16)))
            line = line.replace(orig, stringresult)
        except:
            continue
    for n in nullfun:
        line = line.replace(n,"")
    return line

def mainProcess(line):

    fullmatch = re.findall('\_0x[a-zA-Z0-9]+\(\-?0x\S.+?(?=\))',line)
    #Find the left over null/not used functions (cleanup)
    nullfun = re.findall('var\s\_0x[a-zA-Z0-9]+\s\=\s\_0x[a-zA-Z0-9]+\;',line)
    for f in fullmatch:
        origVal = f + ')'
        funSplit = f.split('(',1)
        funLookup = 'fr4k' + funSplit[0]
        funtemp = funSplit[1].replace("'","")
        funParams = funtemp.split(",")
        if (len(funParams) == 1):
            try:
                stringresult = (MainStringShift_plain(int(funParams,16)))
                line = line.replace(origVal, stringresult)
            except:
                continue
        else:
            stripparams = []
            for x in funParams:
                x = x.strip()
                try:
                    if '0x' in x:
                        stripparams.append(int(x,16))
                    else:
                        stripparams.append(int(x))
                except:
                    stripparams.append(x)

            try:
                retOutput = globals()[funLookup](*stripparams)
                line = line.replace(origVal,retOutput)
            except Exception as error:
                print(f'had to skip {f} due to: {error}\n')
    for n in nullfun:
        line = line.replace(n,"")
    #Look for any left over hex values (actual nums) and convert.
    hexconvert = re.findall('[\ |\']0x[a-fA-F0-9]+',line)
    for hc in hexconvert:
        hc = hc.replace(" ","").replace("'","")
        if (isinstance(hc, str)):
            hcn = str(int(hc,16))
        else:
            hcn = str(int(hc))
        line = line.replace(hc,hcn)

    return line

def mainProcessObs(line):

    #fullmatch = re.findall('[a-zA-Z0-9]{1,2}\.[a-zA-Z0-9]{1,2}',line)
    fullmatch = re.findall('[a-zA-Z0-9]+\([a-zA-Z0-9-]+\.[^\)]+',line)
    #Find the left over null/not used functions (cleanup)
    nullfun = re.findall('var\s\_0x[a-zA-Z0-9]+\s\=\s\_0x[a-zA-Z0-9]+\;',line)
    for f in fullmatch:
        origVal = f + ')'
        funSplit = f.split('(',1)
        funLookup = funSplit[0]
        funParams = funSplit[1].split(",")
        outP = []
        for p in funParams:
            obLookup = p.replace('.','["') + '"]'
            try:
                outP.append(eval(obLookup))
            except Exception as error:
                print(f'had to skip {f} due to: {error}\n')
        try:
            retOutput = globals()[funLookup](*outP)
            line = line.replace(origVal,retOutput)
        except Exception as error:
            print(f'had to skip {f} due to: {error}\n')
    for n in nullfun:
        line = line.replace(n,"")
    #Look for any left over hex values (actual nums) and convert.
    hexconvert = re.findall('[\ |\']0x[a-fA-F0-9]+',line)
    for hc in hexconvert:
        hc = hc.replace(" ","").replace("'","")
        if (isinstance(hc, str)):
            hcn = str(int(hc,16))
        else:
            hcn = str(int(hc))
        line = line.replace(hc,hcn)

    return line


         
                  
               
                  
               

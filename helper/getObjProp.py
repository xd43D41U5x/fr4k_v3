import re
from helper.fileIO import writeFile

def getObs(filetext):

    obOut = []
    outTest = ""
    matches = re.findall('[a-zA-Z0-9]{1,2}\s\=\s+\{[^\}]+',filetext)
    
    #Convert JS functions to Python, then strip from orig text.
    for m in matches:
        orig = m
        convOb = m.rstrip()
        findHex = re.findall('\'0x[a-zA-Z0-9]+\'',convOb)
        for f in findHex:
            try:
                hexC = f.replace("'","")
                hexC = int(hexC,16)
                convOb = convOb.replace(f,str(hexC))
            except:
                continue

        convOb = convOb.replace(' = ', '=').replace(': ', ':')
        convOb = re.sub('\s+', '"', convOb).replace("'", '"')
        obOut.append(convOb.replace(':', '":') + '}\n')
        filetext = filetext.replace("'",'"')
        orig = orig.replace("'",'"')
        filetext = filetext.replace(orig+'}',"")
    obOut = ''.join(obOut)
    
    writeFile('./tmp/obprop.py',obOut)
    writeFile('tmpInputFile.txt', filetext)

    return 'tmpInputFile.txt'



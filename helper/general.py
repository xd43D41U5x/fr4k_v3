import re

def altFunWhileConv(whileFun):
    rex = '[a-zA-Z0-9]{1,2}\.[a-zA-Z0-9]{1,2}'
    matches = re.findall(rex,whileFun)

    tmpResult = ""
    for m in matches:
        tmpResult = m.replace('.','["') + '"]'
        whileFun = whileFun.replace(m,tmpResult)
    return whileFun

def buildSkipFun(funName, funShift):
    return f"""def {funName}(number, a = None):
    if (isinstance(number, str)):
        number = int(number,16)
    return StringValues[number-{funShift}]"""
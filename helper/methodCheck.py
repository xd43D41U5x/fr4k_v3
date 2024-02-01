import re

def checkMethods(filetext):
    hChains = hB64 = hRC4 = obProp = hChainsAlt = False
    matchChain = re.findall('function\s\_0x[a-zA-Z0-9]+.+\n\s+return\s\_0x[a-zA-Z0-9]+\(.+',filetext)
    if matchChain:
        print(f'{len(matchChain)} chained function(s) found, stripping and converting to Python...')
        hChains = True
    matchAltChain = re.findall('function\s[a-zA-Z0-9]+.+\n\s+return\s[a-zA-Z0-9]+\(.+',filetext)
    if matchAltChain:
        print(f'{len(matchAltChain)} alt chained function(s) found, stripping and converting to Python...')
        hChainsAlt = True
    matchOb = re.findall('[a-zA-Z]{1,2}\s\=\s+\{[^\}]+',filetext)
    if matchOb:
        print(f'{len(matchOb)} object property lookups found, stripping and converting to Python...')
        obProp = True
    matchRC4 = re.findall('\<\s0x100\;',filetext)
    matchb64 = re.findall('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\+\/\=',filetext)
    if matchRC4:
        print(f'RC4 found...')
        hRC4 = True
    elif matchb64:
        print(f'No RC4, B64 was found though...')
        hRC4 = True
    return hChains, hB64, hRC4, obProp, hChainsAlt
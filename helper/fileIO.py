def readFile(fileName):
    with open(fileName, 'r') as textfile:
        filetext = textfile.read()
    return filetext

def writeFileLoop(fileName,fileContent):
    print("\nOutput file saved as: %s" % fileName)
    with open(fileName, 'w') as f:
        for final in fileContent:
            f.write(final)

def writeFile(fileName, fileContent):
    with open(fileName, 'w') as f:
            f.write(fileContent)
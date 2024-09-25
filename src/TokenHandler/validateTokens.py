from CompilerUtils.FileUtils.registerOnFileFunction import registerOnTokenFile

def checkPair(char):
    simboList = []
    simboList.extend(char)
    
    pairs = ["()", "[]", "{}", "\"\""]
    
    pass

def checkSemiColon(arq, stringLine, lineCounter):
    if not (stringLine.endswith('\n') and stringLine[-2:-1] in ['{', '}']):
        if stringLine[-2:-1] != ';':
            registerOnTokenFile(arq, 'a', lineCounter, 1)
            return 1
    return 0


from TokenHandler.tokensInfo import tokenList
from CompilerUtils.FileUtils.registerOnFileFunction import registerOnTokenFile

def defineToken(lexema, line):
    for classtoken in tokenList.values():
        if lexema in classtoken.values():
            registerOnTokenFile('Tests/tokens.txt', lexema, line)
            break
    
    
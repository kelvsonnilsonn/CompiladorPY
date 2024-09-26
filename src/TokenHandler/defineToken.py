from TokenHandler.tokensAndOperatorsInfo import tokenList
from CompilerUtils.FileUtils.registerOnFileFunction import registerOnFile

def defineToken(lexemaList, line):
    lex = "".join(lexemaList)

    for classtoken in tokenList.values():
        if lex in classtoken.values():
            registerOnFile('Tests/tokens.txt', lex, line)
            break

    lexemaList.clear()
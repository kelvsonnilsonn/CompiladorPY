from CompilerUtils.Utils.Tokens_Simbols_Info import tokenList
from CompilerUtils.FileUtils.registerOnFileFunction import registerOnTokenFile, registerOnSimbolsFile

def defineTokenOrSimble(lexema, line):
    for classtoken in tokenList.values():
        if lexema in classtoken.values():
            registerOnTokenFile('Tests/tokens.txt', lexema, line)
            return 0
    
    registerOnSimbolsFile('Tests/Tabela_de_simbolos.txt', lexema, line)
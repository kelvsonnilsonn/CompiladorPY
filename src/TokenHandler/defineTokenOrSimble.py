from CompilerUtils.Utils.Tokens_Simbols_Info import tokenList, operatorsList
from CompilerUtils.FileUtils.registerOnFileFunction import registerOnFile

def defineTokenOrSimble(lexema, line):
    for categoryTokens, valueTokens in tokenList.items():
        if lexema in valueTokens.values():
            registerOnFile.registerOnTokenFile(categoryTokens ,lexema, line)
    
    for categorySimbles, valueSimbles in operatorsList.items():
        if lexema in valueSimbles.vales():
            registerOnFile.registerOnSimbolsFile(categorySimbles, lexema, line)
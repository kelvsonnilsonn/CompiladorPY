from CompilerUtils.Utils.Tokens_Simbols_Info import tokenList, operatorsList
from CompilerUtils.FileUtils.registerOnFileFunction import fileAccess
from CompilerUtils.Utils.dataToAnalysis import *


def defineTokenOrSimble(lexema, line):
    registerOnFile_instance = fileAccess(code_base_to_analysis, output_to_tokens, output_to_simbols)

    if lexema.isdigit():
        registerOnFile_instance.registerOnTokenFile("NUMBER" ,lexema, line)

    else:        
        for categoryTokens, valueTokens in tokenList.items():
            if lexema in valueTokens.values():
                registerOnFile_instance.registerOnTokenFile(categoryTokens ,lexema, line)
                return 0
        
        for categorySimbles, valueSimbles in operatorsList.items():
            if lexema in valueSimbles.values():
                registerOnFile_instance.registerOnTokenFile(categorySimbles ,lexema, line)
                return 0
            
        registerOnFile_instance.registerOnSimbolsFile(lexema, line)
        return 0
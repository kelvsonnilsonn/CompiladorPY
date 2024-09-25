from CompilerErrors.Errors import lexicalErrosTokens, lexicalErrosLexems
from CompilerUtils.FileUtils.FindTokenType import findTokenType

def registerOnTokenFile(arq, token, line, errorMessage = 0):
    saveArq = open(arq, 'a')
    
    if errorMessage != 0:
        errorType = lexicalErrosTokens(errorMessage, line)
        saveArq.write(f"FATAL |-> Analisador Lexico: " + errorType)
        return 0

    else:
        tokenType = findTokenType(token)
        tokenTypeMessage = f"- Tipo {tokenType}"
        saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")

def registerOnSimbolsFile(arq, lexem, line, errorMessage = 0):
    saveArq = open(arq, 'a')
    
    if errorMessage != 0:
        errorType = lexicalErrosTokens(errorMessage, line)
        saveArq.write(f"FATAL |-> Analisador Lexico: " + errorType)
        return 0

    else:
        saveArq.write(f"IDENTIFIER {lexem}\n")


        
        lexem = ""


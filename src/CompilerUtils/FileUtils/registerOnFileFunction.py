from CompilerErrors.Errors import lexicalErros
from TokenHandler.tokensInfo import tokenList

def registerOnFile(arq, token, line, errorMessage = 0):
    saveArq = open(arq, 'a')
    
    if errorMessage != 0:
        lexicalErros(errorMessage, line)
        saveArq.write(f"Erro de Analise Lexica na linha {line} pela falta de ;")
        return 0

    else:
        tokenType = findTokenType(token)
        tokenTypeMessage = f"- Tipo {tokenType}"
        saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")

def findTokenType(token):
    for tokenCategory, tokenInfo in tokenList.items():
         if token in tokenInfo.values():
             return tokenCategory
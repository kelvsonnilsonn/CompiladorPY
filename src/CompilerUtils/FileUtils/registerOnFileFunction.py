from CompilerErrors.Errors import lexicalErros
from TokenHandler.tokensAndOperatorsInfo import tokenList

def registerOnFile(arq, token, line, errorMessage = 0):
    try:
        with open(arq, 'a') as saveArq:
            if errorMessage != 0:
                errorType = lexicalErros(errorMessage, line)
                saveArq.write(f"FATAL |-> Analisador Lexico: " + errorType)
                return 0

            else:
                tokenType = findTokenType(token)
                tokenTypeMessage = f"- Tipo {tokenType}"
                saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")

            saveArq.close()
    except IOError:
        print("Arquivo não encontrado na pasta de outputs. Criação ocorrendo agora.")
        open("Tokens.txt", 'w')
    


def registerOnSimbolsFile(arq, token, line):
    try:
        with open(arq, 'a') as saveArq:

            tokenType = findTokenType(token)
            tokenTypeMessage = f"- Tipo {tokenType}"
            saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")

            saveArq.close()

    except IOError:
        print("Arquivo não encontrado na pasta de outputs designada. Criação ocorrendo agora.")
        open("SimbolList.txt", 'w')


def findTokenType(token):
    for tokenCategory, tokenInfo in tokenList.items():
         if token in tokenInfo.values():
             return tokenCategory
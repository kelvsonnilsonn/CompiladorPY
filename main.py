# Leitura de inteiros
# Leitura de decimais
# Leitura de Texto

# Leitura de Tokens

from tokensInfo import tokenList
from CompilerFunctions.ErrorMessages.Errors import lexicalErros
from CompilerFunctions.ChecksFuntions.checkPairFunction import checkPair
simboList = []


def defineToken(lexemaList, line):

    lex = "".join(lexemaList)

    for classtoken in tokenList.values():
        if lex in classtoken.values():
            registerTokens("tokens.txt", lex, line)
            break

    lexemaList.clear()


def findTokenType(token):
    for tokenCategory, tokenInfo in tokenList.items():
         if token in tokenInfo.values():
             return tokenCategory


def registerTokens(arq, token, line, errorMessage = 0):
    if errorMessage == 1:
        pass
    else:
        saveArq = open(arq, "a")
        tokenType = findTokenType(token)
        tokenTypeMessage = f"- Tipo {tokenType}"
        saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")
    

def reading(arquivo):
    lexema = []

    lineCount = 0

    for line in arquivo:
        lineCount += 1
        for character in line:
            if character in [' ', '\n']:
                defineToken(lexema, lineCount)

            else:
                if character in tokenList["Simbolo especial"]:
                    checkPair(character)
                    defineToken(lexema, lineCount)
                    lexema.extend(character)
                    defineToken(lexema, lineCount)

                else:
                    lexema.extend(character)
        if line[:-1] != '{' and line[:-1] != '':
            print("Faltou ; na linha: " + line)
            break


def fileOpenToRead():
    try:
        with open("codigo.txt", 'r') as file:
            reading(file)
    except IOError:
        print("Arquivo não existe")

fileOpenToRead()
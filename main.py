# Leitura de inteiros
# Leitura de decimais
# Leitura de Texto

# Leitura de Tokens

from tokensInfo import tokenList

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

def registerTokens(arq, token, line):
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
                    defineToken(lexema, lineCount)
                    lexema.extend(character)
                    defineToken(lexema, lineCount)

                else:
                    lexema.extend(character)

# Leitura de simbolos

def fileOpenToRead():
    try:
        with open("codigo.txt", 'r') as file:
            reading(file)
    except IOError:
        print("Arquivo não existe")

fileOpenToRead()
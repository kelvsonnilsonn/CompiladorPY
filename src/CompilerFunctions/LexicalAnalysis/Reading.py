from TokenHandler.defineToken import defineToken
from TokenHandler.validateTokens import checkPair, checkSemiColon
from CompilerUtils.FileUtils.commentsFinder import commentsFinder
from TokenHandler.tokensInfo import tokenList


def reading(arquivo):
    
    token = []

    lexema = ""
    state = "inicial"

    for line in arquivo:
        lineCount += 1
        if commentsFinder(line.strip()):
            continue
        else:
            for character in line.strip(): # Automato
                if state == "inicial":
                    if character.isalpha():
                        state = "IDENTIFIER"
                        lexema += character
                    elif character.isdigit():
                        state = "NUMBER"
                        lexema += character
                    elif character in tokenList["Operador Aritmetico"]:
                        defineToken(lexema, lineCount)
                else:
                    match state:
                        case "IDENTIFIER":
                            if character.isalnum():
                                lexema += character
                            else:
                                defineToken(lexema, lineCount)
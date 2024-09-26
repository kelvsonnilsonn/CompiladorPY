from TokenHandler.defineToken import defineToken
from TokenHandler.validateTokens import checkPair, checkSemiColon
from CompilerUtils.FileUtils.commentsFinder import commentsFinder
from TokenHandler.tokensAndOperatorsInfo import tokenList


def reading(arquivo):
    lexema = []

    lineCount = 0

    for line in arquivo:
        lineCount += 1
        if commentsFinder(line.strip()):
            continue
        else:
            if checkSemiColon("Tests/tokens.txt", line, lineCount):
                break
            
            else:
                for character in line.strip():
                    if character in [' ', '\n', '\t']:
                        defineToken(lexema, lineCount)

                    else:
                        if character in tokenList["Simbolo especial"]:
                            checkPair(character)
                            defineToken(lexema, lineCount)
                            lexema.extend(character)
                            defineToken(lexema, lineCount)

                        else:
                            lexema.extend(character)
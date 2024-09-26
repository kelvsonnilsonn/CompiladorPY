from TokenHandler.defineTokenOrSimble import defineTokenOrSimble
from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList, tokenList

def checkState(line, lineCount):

    state = "inicial"
    lexema = ""

    for char in line.strip():
        for operatorCategory, operatorsValues in operatorsList.items():
            if char in operatorsValues.values():
                defineTokenOrSimble(char, lineCount)
                break
        if char in tokenList["Simbolos especiais"].values():
            if lexema:
                defineTokenOrSimble(lexema, lineCount)
            defineTokenOrSimble(char, lineCount)
            lexema = ""
        else: 
            if state == "inicial":
                if char.isalpha():
                    state = "IDENTIFIER"
                    lexema += char
                elif char.isdigit():
                    state = "NUMBER"
                    lexema += char

            else:
                match state:
                    case "IDENTIFIER":
                        if char.isalnum():
                            lexema += char
                        else:
                            defineTokenOrSimble(lexema, lineCount)
                            lexema = ""
                            state = "inicial"
                    case "NUMBER":
                        if char.isdigit():
                            lexema += char
                        else:
                            defineTokenOrSimble(lexema, lineCount)
                            lexema = ""
                            state = "inicial"
from TokenHandler.defineTokenOrSimble import defineTokenOrSimble
from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList

def checkState(line, lineCount):

    state = "inicial"
    lexema = ""

    for char in line.strip():
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
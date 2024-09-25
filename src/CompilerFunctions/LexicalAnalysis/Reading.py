from TokenHandler.defineToken import defineToken
from CompilerUtils.FileUtils.commentsFinder import commentsFinder



def reading(arquivo):
    
    token = []

    lexema = ""
    state = "inicial"

    lineCount = 0

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
                    else:
                        lexema += character
                        defineToken(lexema, line)
                        lexema = ""
                else:
                    match state:
                        case "IDENTIFIER":
                            if character.isalnum():
                                lexema += character
                            else:
                                defineToken(lexema, lineCount)
                                lexema = ""
                                lexema += character
                                state = "inicial"
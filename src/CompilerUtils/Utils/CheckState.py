from TokenHandler.defineTokenOrSimble import defineTokenOrSimble
from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList, tokenList
from CompilerUtils.FileUtils.registerOnFileFunction import fileAccess
from CompilerUtils.Utils.dataToAnalysis import *

def checkState(line, lineCount):

    registerOnFile_instance = fileAccess(code_base_to_analysis, output_to_tokens, output_to_simbols)

    state = "inicial"
    lexema = ""
    literal = ""
    insideLiteral = False


    for char in line.strip():
        if char == "\"":
            if insideLiteral:
                registerOnFile_instance.registerOnTokenFile("LITERAL", literal, line)
                literal = ""
                insideLiteral = False
            else:
                insideLiteral = True
        elif insideLiteral:
            literal += char

        else:
            for operatorCategory, operatorsValues in operatorsList.items():
                if char in operatorsValues.values():
                    if lexema:
                        defineTokenOrSimble(lexema, lineCount)
                    defineTokenOrSimble(char, lineCount)
                    lexema = ""
                    state = "inicial"
                    break
            if char in tokenList["Simbolos especiais"].values():
                if lexema:
                    defineTokenOrSimble(lexema, lineCount)
                defineTokenOrSimble(char, lineCount)
                lexema = ""
                state = "inicial"
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
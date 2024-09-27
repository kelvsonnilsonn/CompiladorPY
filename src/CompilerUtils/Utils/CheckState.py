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
    pular = 0

    for index, char in enumerate(line.strip()):
        if pular > 0:
            pular -= 1
            continue
        else:
            if index == (len(line.strip()) - 1) and char != ';':
                if line[-2:-1] not in ['{', '}']:

                    registerOnFile_instance.registerOnTokenFile("LITERAL", literal, line, 1)

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
                if index < len(line.strip()) - 1:
                    if char == line.strip()[index+1] and char in ['=', '+']:
                        if lexema:
                            defineTokenOrSimble(lexema, lineCount)
                        defineTokenOrSimble(f"{char*2}", lineCount)
                        lexema = ""
                        state = "inicial"
                        pular += 1
                        continue
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
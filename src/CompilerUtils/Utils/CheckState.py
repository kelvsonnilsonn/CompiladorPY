from TokenHandler.defineTokenOrSimble import defineTokenOrSimble
from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList, tokenList
from CompilerUtils.FileUtils.registerOnFileFunction import fileAccess
from CompilerErrors.Errors import ErrorsConfer
from CompilerUtils.Utils.dataToAnalysis import *

class checkState:
    def __init__(self, line ,lineCount):

        self.line = line

        self.lineCount = lineCount
        self.state = "inicial"

        self.lexema = ""
        self.literal = ""

        self.insideLiteral = False

        self.instance = fileAccess(code_base_to_analysis, output_to_tokens, output_to_simbols)
        self.errorInstance = ErrorsConfer(self.line)
        self.pular = 0

    def running(self):
        for index, char in enumerate(self.line.strip()):
            if self.pular > 0:
                self.pular -= 1
                continue
            else:
                self.checkComment(char)
                self.checkOperators(char)
                if self.checkDoubleOp(char, index): continue
                self.checkSimbols(char)

                if self.state == "inicial":
                    if char.isalpha():
                        self.state = "IDENTIFIER"
                        self.lexema += char
                    elif char.isdigit():
                        self.state = "NUMBER"
                        self.lexema += char
                else:
                    match self.state:
                        case "IDENTIFIER":
                            if char.isalnum():
                                self.lexema += char
                            else:
                                self.sendToAnalysis(self.lexema)
                                self.reset()

                        case "NUMBER":
                            if char.isdigit():
                                self.lexema += char
                            else:
                                self.sendToAnalysis(self.lexema)
                                self.reset()

    def reset(self):
        self.lexema = ""
        self.state = "inicial"

    def sendToAnalysis(self, type):
        defineTokenOrSimble(type, self.lineCount)
        self.lexema = ""
        self.state = "inicial"

    def checkOperators(self, char):
        for opCat, opVal in operatorsList.items():
            if char in opVal.values():
                if self.lexema:
                    self.sendToAnalysis(self.lexema)
                self.sendToAnalysis(self.lexema)
                break

    def checkSimbols(self, char):
        if char in tokenList["Simbolos especiais"].values():
            if self.lexema:
                self.sendToAnalysis(self.lexema)
            self.sendToAnalysis(char)
            self.reset()

    def checkComment(self, char):
        if char == "\"": # checa se começa com aspas
            if self.insideLiteral: # se já tiver passado por uma aspas e encontrou essa agora
                self.instance.registerOnTokenFile("LITERAL", self.literal, self.lineCount) # Registro todo o literal e envio para a lista de tokens
                self.literal = "" # esvazio o literal
                self.insideLiteral = False # digo que não há mais literal
            else: # se for a primeira vez lendo uma aspas
                self.insideLiteral = True # Permito adicionar caracteres ao vetor de caracteres "litaral"
        elif self.insideLiteral: # Se insideLiteral for True
            self.literal += char # acrescento no vetor de caracteres literal ( string )

    def checkDoubleOp(self, char, index):
        if index < len(self.line.strip()) - 1:
            if char == self.line.strip()[index+1] and char in ['=', '+', '-']:
                if self.lexema: self.sendToAnalysis(self.lexema)
                self.sendToAnalysis(f"{char*2}")
                self.reset()
                self.pular += 1
                return 1
        return 0


















# def checkState(line, lineCount):

#     registerOnFile_instance = fileAccess(code_base_to_analysis, output_to_tokens, output_to_simbols)

#     state = "inicial"
#     lexema = ""
#     literal = ""
#     insideLiteral = False
#     pular = 0

#     for index, char in enumerate(line.strip()):
#         if pular > 0:
#             pular -= 1
#             continue
#         else:
#             if index == (len(line.strip()) - 1) and char != ';':
#                 if line[-2:-1] not in ['{', '}']:

#                     registerOnFile_instance.registerOnTokenFile("LITERAL", literal, line, 1)

            # if char == "\"":
            #     if insideLiteral:
            #         registerOnFile_instance.registerOnTokenFile("LITERAL", literal, line)
            #         literal = ""
            #         insideLiteral = False
            #     else:
            #         insideLiteral = True
            # elif insideLiteral:
            #     literal += char

            # else:
                # if index < len(line.strip()) - 1:
                #     if char == line.strip()[index+1] and char in ['=', '+']:
                #         if lexema:
                #             defineTokenOrSimble(lexema, lineCount)
                #         defineTokenOrSimble(f"{char*2}", lineCount)
                #         lexema = ""
                #         state = "inicial"
                #         pular += 1
                #         continue

                # for operatorCategory, operatorsValues in operatorsList.items():
                #     if char in operatorsValues.values():
                #         if lexema:
                #             defineTokenOrSimble(lexema, lineCount)
                #         defineTokenOrSimble(char, lineCount)
                #         lexema = ""
                #         state = "inicial"
                #         break


                # if char in tokenList["Simbolos especiais"].values():
                #     if lexema:
                #         defineTokenOrSimble(lexema, lineCount)
                #     defineTokenOrSimble(char, lineCount)
                #     lexema = ""
                #     state = "inicial"

                # else: 
                #     if state == "inicial":
                #         if char.isalpha():
                #             state = "IDENTIFIER"
                #             lexema += char
                #         elif char.isdigit():
                #             state = "NUMBER"
                #             lexema += char

                #     else:
                #         match state:
                #             case "IDENTIFIER":
                #                 if char.isalnum():
                #                     lexema += char
                #                 else:
                #                     defineTokenOrSimble(lexema, lineCount)
                #                     lexema = ""
                #                     state = "inicial"
                #             case "NUMBER":
                #                 if char.isdigit():
                #                     lexema += char
                #                 else:
                #                     defineTokenOrSimble(lexema, lineCount)
                #                     lexema = ""
                #                     state = "inicial"
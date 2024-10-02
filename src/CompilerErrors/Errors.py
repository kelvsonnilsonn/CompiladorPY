class ErrorsConfer:
    def __init__(self, line):
        self.line = line
        pass
def lexicalErrosTokens(errorNumber):
    match errorNumber:
        case 1:
            return "FATAL |-> Analisador Lexico: incapaz de encontrar ';'.\n"

def lexicalErrosLexems(errorNumber):
    match errorNumber:
        case 1:
            return "FATAL |-> Analisador Lexico: incapaz de encontrar \".\n"
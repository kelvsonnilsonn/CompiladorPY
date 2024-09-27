def lexicalErrosTokens(errorNumber, lineCounter):
    match errorNumber:
        case 1:
            return "FATAL |-> Analisador Lexico: incapaz de encontrar ';'."

def lexicalErrosLexems(errorNumber, lineCounter):
    match errorNumber:
        case 1:
            return "FATAL |-> Analisador Lexico: incapaz de encontrar \"."
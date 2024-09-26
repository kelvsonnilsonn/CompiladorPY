from CompilerErrors.Errors import lexicalErrosTokens, lexicalErrosLexems
from CompilerUtils.FileUtils.FindTokenType import findTokenType
from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList
from main import outputToSimbles, outputToTokens

def registerOnTokenFile(token, line, errorMessage = 0):

    with open(outputToTokens) as saveArq:

        if errorMessage != 0:
            saveArq.write(f"FATAL |-> Analisador Lexico: {lexicalErrosTokens(errorMessage, line)}")
            return 0

        else:
            tokenType = findTokenType(token)
            tokenTypeMessage = f"- Tipo {tokenType}"
            saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")

        saveArq.close()


def registerOnSimbolsFile(lexem, line, errorMessage = 0):
    with open(outputToSimbles) as saveArq:
        for operators in operatorsList.values():
            if lexem in operators:
                saveArq.write(f"{operators.key()} {lexem}\n")
                return
        saveArq.close()

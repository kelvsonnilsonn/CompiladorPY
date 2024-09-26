from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList

class fileAccess:
    def __init__(self, Code_Base, OutputTokensPars, OutputSimplesPars):
        self.code_base = Code_Base
        self.outputToTokens = OutputTokensPars
        self.outputToSimbles = OutputSimplesPars

    def fileOpenToReadAndEdit(self):
        from CompilerFunctions.LexicalAnalysis.Reading import reading
        try:
            open(self.outputToSimbles, 'a').close()
            open(self.outputToTokens, 'a').close()

            with open(self.code_base, 'r') as file:
                reading(file)
        except IOError as e:
            print(f"Erro no acesso ao arquivo: {e}")
            if self.code_base not in str(e):
                print(f"O arquivo código-fonte \"{self.code_base}\" não existe.")


class registerOnFile:

    def __init__(self, fileAccess_instance):
        self.output_to_tokens = fileAccess_instance.outputToTokens
        self.output_to_simbles = fileAccess_instance.outputToSimbles
        
    def registerOnTokenFile(self, category, token, line, errorMessage = 0):

        from CompilerErrors.Errors import lexicalErrosTokens

        with open(self.output_to_tokens) as saveArq:

            if errorMessage != 0:
                saveArq.write(f"FATAL |-> Analisador Lexico: {lexicalErrosTokens(errorMessage, line)}")
                return 0

            else:
                tokenTypeMessage = f"- Tipo {category}"
                saveArq.write(f"Linha {line} : {token} {tokenTypeMessage:^50}\n")

            saveArq.close()


    def registerOnSimbolsFile(self, category, lexem, line, errorMessage = 0):
        with open(self.output_to_simbles) as saveArq:
            saveArq.write(f"{category} :->: {lexem}\n")
            saveArq.close()

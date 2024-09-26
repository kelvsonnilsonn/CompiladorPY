class fileAccess:
    def __init__(self, Code_Base, OutputTokensPars, OutputSimplesPars):
        self.code_base = Code_Base
        self.output_to_tokens = OutputTokensPars
        self.output_to_simbles = OutputSimplesPars

    def fileOpenToReadAndEdit(self):

        from CompilerFunctions.LexicalAnalysis.Reading import reading

        try:
            open(self.output_to_simbles, 'a').close()
            open(self.output_to_tokens, 'a').close()

            with open(f"{self.code_base}", 'r') as file:
                reading(file)
        except IOError as e:
            print(f"Erro no acesso ao arquivo: {e}")
            if self.code_base not in str(e):
                print(f"O arquivo código-fonte \"{self.code_base}\" não existe.")

    def registerOnTokenFile(self, category, token, line, errorMessage = 0):

        from CompilerErrors.Errors import lexicalErrosTokens

        with open(self.output_to_tokens, 'a') as saveArq:

            if errorMessage != 0:
                saveArq.write(f"FATAL |-> Analisador Lexico: {lexicalErrosTokens(errorMessage, line)}")
                return 0

            else:
                saveArq.write(f"{line} {category} {token}\n")

            saveArq.close()
            return 0


    def registerOnSimbolsFile(self, category, lexem, line, errorMessage = 0):
        with open(self.output_to_simbles, 'a') as saveArq:
            saveArq.write(f"line :->: {line} :->: {category} :->: {lexem}\n")
            saveArq.close()
            return 0
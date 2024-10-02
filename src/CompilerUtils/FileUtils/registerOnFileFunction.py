class fileAccess:
    def __init__(self, Code_Base, OutputTokensPars, OutputSimplesPars):
        self.code_base = Code_Base
        self.output_to_tokens = OutputTokensPars
        self.output_to_simbols = OutputSimplesPars

    def fileOpenToReadAndEdit(self):

        from CompilerFunctions.LexicalAnalysis.Reading import reading

        try:
            open(self.output_to_simbols, 'a').close()
            open(self.output_to_tokens, 'a').close()

            with open(f"{self.code_base}", 'r') as file:
                reading(file)
        except IOError as e:
            print(f"Erro no acesso ao arquivo: {e}")
            if self.code_base not in str(e):
                print(f"O arquivo código-fonte \"{self.code_base}\" não existe.")

    def registerOnTokenFile(self, category, token, line, errorMessage=0):

        from CompilerErrors.Errors import lexicalErrosTokens
        from CompilerUtils.Utils.Tokens_Simbols_Info import operatorsList
        with open(self.output_to_tokens, 'a') as saveArqToken:

            if errorMessage != 0:
                saveArqToken.write(f"{lexicalErrosTokens(errorMessage)}")
                print(f"{lexicalErrosTokens(errorMessage)}")
                exit()

            if category == "NUMBER":
                saveArqToken.write(f"NUM({token})\n")
            elif category == "ID":
                with open(self.output_to_simbols, 'r+') as file_content:
                    if not file_content:
                        saveArqToken.write(f"ID({1})\n")
                    else:
                        saveArqToken.write(f"ID({line})\n")
            elif category == "LITERAL":
                saveArqToken.write(f"LITERAL(\"{token}\")\n")
            elif category in operatorsList.keys():
                saveArqToken.write(f"{category} -> {token}\n")
            else:
                saveArqToken.write(f"{category} -> {token}\n")

            return 0


    def registerOnSimbolsFile(self, lexem, line, errorMessage=0):
        with open(self.output_to_simbols, 'r+') as saveArq:
            file_content = saveArq.readlines()
            if not file_content:
                line = 1
                if lexem not in ''.join(file_content):
                    saveArq.write(f"{len(file_content) + 1} -> {lexem}\n")
                    self.registerOnTokenFile("ID", lexem, len(file_content) + 1)
                else:
                    for indexLine, fileLine in enumerate(file_content, start=1):
                        if lexem in fileLine:
                            self.registerOnTokenFile("ID", lexem, indexLine)
                            return 0
            else:
                if lexem not in ''.join(file_content):
                    saveArq.write(f"{len(file_content) + 1} -> {lexem}\n")
                    self.registerOnTokenFile("ID", lexem, len(file_content) + 1)
                else:
                    for indexLine, fileLine in enumerate(file_content, start=1):
                        if lexem in fileLine:
                            self.registerOnTokenFile("ID", lexem, indexLine)
                            return 0


from CompilerFunctions.LexicalAnalysis.Reading import reading

class fileAcess:
    def __init__(self, Code_Base, OutputTokens, OutputSimples):
        self.code_base = Code_Base
        self.outputToTokens = OutputTokens
        self.outputToSimbles = OutputSimples
        pass

    def fileOpenToReadAndEdit(self):
        try:
            try:
                open(self.OutputToTokens, 'a')
            except IOError:
                print("Arquivo de output \"Tokens.txt\" não existe. Ele estará sendo criado agora.")
                open(self.OutputToTokens, 'w')

            try:
                open(self.OutputToSimbles, 'a')
            except IOError:
                print("Arquivo de output \"SimbolList.txt\" não existe. Ele estará sendo criado agora.")
                open(self.OutputToSimbles, "w")

            with open(self.code_base, 'r') as file:
                reading(file, self.OutputToTokens, self.OutputToSimbles)
        except IOError:
            print("Código-fonte não existe.")

# Leitura de inteiros
# Leitura de decimais
# Leitura de Texto

# Leitura de Tokens

from CompilerFunctions.LexicalAnalysis.Reading import reading

def fileOpenToRead():
    try:
        with open('Tests/codigo.txt', 'r') as file:
            reading(file)
    except IOError:
        print("Arquivo não existe")

fileOpenToRead()
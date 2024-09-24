# Leitura de inteiros
# Leitura de decimais
# Leitura de Texto

# Leitura de Tokens

tokenList = {"Palavra Reservada": 
                {"INT":"int", "FLOAT":"float",
                "CHAR":"char", "BOOLEAN":"boolean",
                "VOID":"void", "IF":"if",
                "ELSE":"else", "FOR":"for",
                "WHILE":"while", "SCANF":"scanf",
                "PRINTLN":"println", "MAIN":"main",
                "RETURN":"return"},

                "Constantes de Texto": 
                {"TEXTO":'"'},

                "Operador aritmetico": 
                {"+":"+", "-":"-", "*":"*", "/":"/", "%":"%"},
                
                "Simbolo especial": 
                {"{":"{", "}":"}", "(":"(", ")":")", 
                ";": ";", "[":"[", "]":"]", ",":",", "()": "()"},

                "Operador logico":
                {"&&": "&&", "||" : "||", "!":"!"}}

def defineToken(lexemaList):

    lex = "".join(lexemaList)

    for classtoken in tokenList.values():
        if lex in classtoken.values():
            print("Há o token:" + lex)
            break

    lexemaList.clear()

def findToken(arquivo):
    simboList = []
    
    lexema = []

    for line in arquivo:
        for character in line:
            if character in [' ', '\n']:
                defineToken(lexema)

            else:
                if character in tokenList["Simbolo especial"]:
                    if len(lexema) > 1:
                        defineToken(lexema)
                    lexema.extend(character)

                else:
                    lexema.extend(character)

# Leitura de simbolos

arquivo = open("codigo.txt", "r")
findToken(arquivo)
arquivo.close()
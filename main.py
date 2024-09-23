# Leitura de inteiros
# Leitura de decimais
# Leitura de Texto

# Leitura de Tokens

def findToken(arquivo):
        
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
                ";": ";", "[":"[", "]":"]", ",":","},

                "Operador logico":
                {"&&": "&&", "||" : "||", "!":"!"}}
    simboList = []
    
    lexema = []

    for line in arquivo:
        for character in line:
            if character in [' ', '\n']:
                lex = "".join(lexema)
                lexema.clear()
                
                for classtoken in tokenList.values():
                    if lex in classtoken.values():
                        print("Há token:" + lex)
            else:
                if character in tokenList["Simbolo especial"]:
                    pass
                lexema.extend(character)

# Leitura de simbolos

arquivo = open("codigo.txt", "r")
findToken(arquivo)
arquivo.close()
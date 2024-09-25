def lexical_analyzer(source_code):
    tokens = []
    state = "initial"
    lexeme = ""
    
    for char in source_code:
        if state == "initial":
            if char.isalpha():  # Se começar com uma letra
                lexeme += char
                state = "identifier"
            elif char.isdigit():  # Se começar com um número
                lexeme += char
                state = "number"
            elif char in "+-*/=":  # Operadores simples
                tokens.append(("OPERATOR", char))
            elif char in " \n\t":  # Ignorar espaços em branco
                continue
            else:
                raise Exception(f"Erro léxico: caractere inesperado '{char}'")
        
        elif state == "identifier":
            if char.isalnum():  # Continuação de identificadores
                lexeme += char
            else:
                if lexeme in ["if", "else", "while"]:  # Palavras-chave
                    tokens.append(("KEYWORD", lexeme))
                else:
                    tokens.append(("IDENTIFIER", lexeme))
                lexeme = ""
                state = "initial"
        
        elif state == "number":
            if char.isdigit():
                lexeme += char
            else:
                tokens.append(("NUMBER", lexeme))
                lexeme = ""
                state = "initial"

    return tokens

# Exemplo de uso
source_code = "if x == 5"
print(lexical_analyzer(source_code))

def lexicalErros(errorNumber, lineCounter):
    match errorNumber:
        case 1:
            print(f"não foi encontrado o ; na linha {lineCounter}")
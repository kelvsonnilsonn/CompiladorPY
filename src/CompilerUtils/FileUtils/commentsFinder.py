from CompilerUtils.Utils.CheckState import checkState

def commentsFinder(stringLine, line):
    if stringLine.startswith('/') and stringLine[1:2] in ['/', '*']:
        return 1
    else:
        literalSemComentario = ""
        for index, char in enumerate(stringLine.strip()):
            if index < len(stringLine) - 1:
                if char == stringLine[index+1] and char == '/':
                    instance = checkState(literalSemComentario, line)
                    instance.running()
                    return 1
                else:
                    literalSemComentario += char
    return 0
def commentsFinder(stringLine):
    if stringLine.startswith('/') and stringLine[1:2] == '/' or stringLine.startswith('*') and stringLine[-2:-1] == '/':
        return 1
    elif stringLine.startswith('/') and stringLine[1:2] == '*':
        if not stringLine.endswith('/') and not stringLine[-2:-1] == '*':
            return 'breakedComment'
        return 1
    return 0
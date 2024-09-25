def commentsFinder(stringLine):
    if stringLine.startswith('/') and stringLine[1:2] in ['/', '*']:
        return 1
    return 0
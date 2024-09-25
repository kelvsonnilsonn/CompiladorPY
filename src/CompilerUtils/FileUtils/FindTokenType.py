from CompilerUtils.FileUtils.Tokens_Simbols_Info import tokenList

def findTokenType(token):
    for tokenCategory, tokenInfo in tokenList.items():
         if token in tokenInfo.values():
             return tokenCategory
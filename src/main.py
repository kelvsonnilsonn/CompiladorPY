from CompilerUtils.FileUtils.registerOnFileFunction import fileAccess
from CompilerUtils.Utils.dataToAnalysis import *

fileAccess_instance = fileAccess(code_base_to_analysis, output_to_tokens, output_to_simbols)
fileAccess_instance.fileOpenToReadAndEdit()

print("Analise Lexica finalizada.")

# teste
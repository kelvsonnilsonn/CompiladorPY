from CompilerUtils.FileUtils.commentsFinder import commentsFinder
from CompilerUtils.Utils.CheckState import checkState



def reading(arquivo):

    lineCount = 0

    for line in arquivo:
        lineCount += 1
        if commentsFinder(line.strip()):
            continue
        elif line.startswith('\n'):
            continue
        else:
            checkState(line, lineCount)
            
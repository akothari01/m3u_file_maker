import easygui
import os
import re


def getPath() -> str:
    return easygui.diropenbox()


def scanDirForCueFiles(pathDir: str) -> list[str]:
    obj = os.scandir(pathDir)
    fileNames = list[str]()
    for entry in obj:
        if entry.is_file() and entry.name[-3:] == 'cue':
            fileNames.append(entry.name)
            fileNames.append('\n')
    fileNames.pop()
    return fileNames


def makeM3UFile(names: list[str], addPath: str):
    entry1 = names[0]
    toRemove = re.findall(r'\s\(Disc \d\)', entry1)
    toStr = ""
    toStr = toStr.join(toRemove)
    titleFile = entry1.replace(toStr, '')
    titleFile = titleFile.replace('.cue', '')
    m3uFileName = addPath + '\\' + titleFile + '.m3u'
    m3uFile = open(m3uFileName, "w")
    m3uFile.writelines(names)


path = getPath()
file_names = scanDirForCueFiles(path)
makeM3UFile(file_names, path)

import easygui
import os


def getPath() -> str:
    return easygui.diropenbox()


def scanDirForFiles(pathDir: str) -> list[str]:
    obj = os.scandir(pathDir)
    fileNames = list[str]()
    for entry in obj:
        if entry.is_file():
            fileNames.append(entry.name)
    return fileNames


path = getPath()
file_names = scanDirForFiles(path)
print(file_names)

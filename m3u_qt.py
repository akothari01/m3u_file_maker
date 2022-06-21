import os
import re
import sys

import easygui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QHBoxLayout, QLabel, \
    QVBoxLayout, QDialog, QMessageBox


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("m3u_file_maker_multi_disc_games")
        self.setFixedWidth(600)
        self.editText = QLineEdit("Select your Directory")
        self.browseButton = QPushButton("Browse")
        self.browseButton.clicked.connect(self.getPath)
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.editText)
        hLayout.addWidget(self.browseButton)

        self.askText = QLabel("Is this the correct directory?")
        self.yesButton = QPushButton("Yes")
        self.yesButton.clicked.connect(lambda: self.makeM3UFile(self.scanDirForCueFiles(self.editText.text()),
                                                                self.editText.text()))
        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.askText)
        vLayout.addWidget(self.yesButton)

        self.setLayout(vLayout)


    @Slot()
    def getPath(self):
        self.editText.setText(easygui.diropenbox())


    @Slot()
    def scanDirForCueFiles(self, pathDir: str) -> list[str]:
        obj = os.scandir(pathDir)
        fileNames = list[str]()
        for entry in obj:
            if entry.is_file() and entry.name[-3:] == 'cue':
                fileNames.append(entry.name)
                fileNames.append('\n')
        fileNames.pop()
        return fileNames


    @Slot()
    def makeM3UFile(self, names: list[str], addPath: str):
        entry1 = names[0]
        toRemove = re.findall(r'\s\(Disc \d\)', entry1)
        toStr = ""
        toStr = toStr.join(toRemove)
        titleFile = entry1.replace(toStr, '')
        titleFile = titleFile.replace('.cue', '')
        m3uFileName = addPath + '\\' + titleFile + '.m3u'
        m3uFile = open(m3uFileName, "w")
        m3uFile.writelines(names)
        w = QMessageBox()
        w.setText("Success")
        w.exec()
        self.editText.setText("Select your Directory")


def main():
    app = QApplication(sys.argv)
    mWin = MainWindow()
    mWin.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

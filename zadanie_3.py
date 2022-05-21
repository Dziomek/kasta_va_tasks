'''
W tym zadaniu GUI i silnik asystenta są już zaimplementowane. Dokonaj paru modyfikacji:
1) Zmień napis QFrame o nazwie nameLabel tak, by zamiast napisu 'created by...' wyświetlała napis 'created by [Twoje imię]'
2) Spraw, by program pobierał tekst z QLineEdit o nazwie commandEdit i zapisał do zmiennej text (linia 33.)

Przykłady odwołania się do elementów GUI:
task_page.ui.nameLabel.text()
task_page.ui.speakButton.clicked.connect(function)
task_page.ui.commandEdit.setObjectName(name)
'''

import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QApplication
from ui_zad3_form import Ui_Form
import pyttsx3


class TaskPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


if __name__ == '__main__':
    def speak():
        text = '' # W TYM MIEJSCU TEKST MA BYĆ POBIERANY Z COMMAND EDIT
        engine.say(text)
        engine.runAndWait()


    app = QApplication(sys.argv)  ## potrzebne do GUI
    task_page = TaskPage()  ## tworzymy okienko
    engine = pyttsx3.init()
    task_page.ui.speakButton.clicked.connect(speak) ## podpięcie metody speak do przycisku o nazwie speakButton

    task_page.show()  ## wyświetlamy okienko
    sys.exit(app.exec_())  ## potrzebne do GUI

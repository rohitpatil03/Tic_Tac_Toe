from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os




class Ui_self(QtWidgets.QDialog):
    def __init__(self, who_won):
        super().__init__()
        
        self.setWindowTitle("PLAY AGAIN")
        self.setObjectName("self")
        self.resize(575, 350)
        self.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        vertical_spacer = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        horizontal_spacer = QtWidgets.QSpacerItem(
            15, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.who_is_winner = QtWidgets.QLabel(self, text=who_won)
        self.who_is_winner.setStyleSheet("color:green;font-weight: bold;")
        self.who_is_winner.setFont(QtGui.QFont('Times', 30))
        self.who_is_winner.setAlignment(QtCore.Qt.AlignCenter)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.play_again = QtWidgets.QPushButton(self, text="PLAY AGAIN")
        self.play_again.setStyleSheet(
            "QPushButton{background-color:orange;color:white;border-radius: 8px;font-size:40px;font-weight: bold;}""QPushButton::hover""{""background-color : red;font-weight: bold;""}")
        self.play_again.setSizePolicy(sizePolicy)
        self.play_again.clicked.connect(self.restart)

        self.exit = QtWidgets.QPushButton(self, text="EXIT")
        self.exit.setStyleSheet(
            "QPushButton{background-color:orange;color:white;border-radius: 8px;font-size:40px;font-weight: bold;}""QPushButton::hover""{""background-color : red;font-weight: bold;""}")
        self.exit.setSizePolicy(sizePolicy)
        self.exit.clicked.connect(self.quit)

        self.end_hbox = QtWidgets.QHBoxLayout(self)
        self.end_hbox.addItem(horizontal_spacer)
        self.end_hbox.addWidget(self.play_again)
        self.end_hbox.addItem(horizontal_spacer)
        self.end_hbox.addWidget(self.exit)
        self.end_hbox.addItem(horizontal_spacer)

        self.end_vbox = QtWidgets.QVBoxLayout(self)
        self.end_vbox.addItem(vertical_spacer)
        self.end_vbox.addWidget(self.who_is_winner)
        self.end_vbox.addItem(vertical_spacer)
        self.end_vbox.addItem(vertical_spacer)
        self.end_vbox.addLayout(self.end_hbox)
        self.end_vbox.addItem(vertical_spacer)

        self.gridLayout.addLayout(self.end_vbox, 1, 1, 1, 1)

        self.setLayout(self.gridLayout)
        self.show()

    def restart(self):
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

    def quit(self):
        QtWidgets.QApplication.quit()
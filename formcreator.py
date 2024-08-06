from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("ls.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
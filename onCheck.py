from PyQt5 import QtCore
from formcreator import form

def on_check():
    _translate = QtCore.QCoreApplication.translate
    if form.checkBox.isChecked():
        form.pushButton.setText(_translate("MainWindow", "Зарегистрировать"))
        form.gen_nameButton.setEnabled(True)
        form.gen_passButton.setEnabled(True)
    else:
        form.pushButton.setText(_translate("MainWindow", "Войти в систему"))
        form.gen_nameButton.setEnabled(False)
        form.gen_passButton.setEnabled(False)
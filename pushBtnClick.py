from PyQt5.QtWidgets import QMessageBox
from formcreator import form
from findBD import find_data
from saveBD import save_data

def on_click():
    if len(form.loginEdit.text()) == 0 or len(form.passwordEdit.text()) == 0:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Заполните все поля")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
        return
    
    if form.checkBox.isChecked():
        save_data()
    else:
        find_user = find_data()

        if not find_user:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Пользователь не найден")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            return
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Сообщение")
            msg.setText("Вы вошли в систему")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
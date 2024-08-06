from PyQt5.QtWidgets import QMessageBox
from formcreator import form
import sqlite3

def save_data():
    conn = sqlite3.connect('ls.db')
    cur = conn.cursor()

    cur.execute('insert into users(login, password) values(?, ?)',
                (form.loginEdit.text(), form.passwordEdit.text()))

    conn.commit()
    conn.close()

    msg = QMessageBox()
    msg.setWindowTitle("Сохранено")
    msg.setText("Данные успешно сохранены")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
from formcreator import form
import sqlite3

def find_data():
    conn = sqlite3.connect('ls.db')
    cur = conn.cursor()

    find_user = cur.execute('SELECT * FROM users WHERE login=? AND password=?',
                (form.loginEdit.text(), form.passwordEdit.text())).fetchall()

    conn.commit()
    conn.close()

    if len(find_user) > 0:
        return False
    else:
        return True

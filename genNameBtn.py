from formcreator import form
import secrets
import string

def gen_name():
    alphabet = string.ascii_letters + string.digits
    nameUser = ''.join(secrets.choice(alphabet) for i in range(8))
    form.loginEdit.setText(nameUser)


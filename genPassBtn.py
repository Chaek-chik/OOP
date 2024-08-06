from formcreator import form
import secrets
import string

def gen_pass():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.islower() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)
                and sum(c.isalpha() for c in password) >= 5):
            break
    form.passwordEdit.setText(password)



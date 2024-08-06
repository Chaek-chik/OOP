from formcreator import form, app
from pushBtnClick import on_click
from onCheck import on_check
from genNameBtn import gen_name
from genPassBtn import gen_pass

form.pushButton.clicked.connect(on_click)
form.checkBox.stateChanged.connect(on_check)
form.gen_nameButton.clicked.connect(gen_name)
form.gen_passButton.clicked.connect(gen_pass)


app.exec()

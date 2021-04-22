import sys
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMainWindow
from Ui_GUI import Ui_Dialog


def check():
    if(ui.spinBox.value() > 0):
        ui.pushButton.setEnabled(True) 
    else:
        ui.pushButton.setEnabled(False) 


def update():
    ui.textBrowser.insertPlainText(str(ui.spinBox.value())+"\n")
    ui.spinBox.setValue(0)
    ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled((True))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(w)
    ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled((False))
    ui.spinBox.valueChanged.connect(check)
    ui.pushButton.clicked.connect(update)
    w.accepted.connect(lambda: print("Ok"))
    w.rejected.connect(lambda: print("Abbruch"))

    w.show()
    sys.exit(app.exec_())

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from Ui_GUI import Ui_Dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())

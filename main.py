import httptool
from PyQt5 import QtWidgets
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QDialog()
    dialog.setWindowTitle('KK HTTP测试工具')
    ui = httptool.Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
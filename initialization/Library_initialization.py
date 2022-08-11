import sys
from PyQt5 import QtWidgets, QtGui
from design_files.main_design import Ui_MainWindow
from resources import init_modules
import PipUpgrade
import icons
# import win10toast


class HyperLink(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class InitializationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(InitializationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        data_table = init_modules.take_csvdata()
        self.ui.tableWidget.setRowCount(len(data_table))
        for ind, elem in enumerate(data_table):
            label = HyperLink(self)
            label.setText(elem["module"])
            self.ui.tableWidget.setCellWidget(ind, 0, label)
            self.ui.tableWidget.setItem(ind, 1, QtWidgets.QTableWidgetItem(str(elem["info"]).title()))
            self.ui.tableWidget.setItem(ind, 2, QtWidgets.QTableWidgetItem(elem["version"]))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # show messageBox due to pressing
        self.ui.button_of_pipInstall.clicked.connect(self.show_popup)
        # mode = PipUpgrade.button_state()
        # self.ui.button_of_pipInstall(self.button_mode)

    def show_popup(self):
        clarification = QtWidgets.QMessageBox()
        clarification.setWindowTitle("Update pip")
        clarification.setText("Are you sure you want to update?")
        clarification.setWindowIcon(QtGui.QIcon(":/icons/main_icon.png"))
        clarification.addButton(QtWidgets.QPushButton('Accept'), QtWidgets.QMessageBox.YesRole)
        clarification.addButton(QtWidgets.QPushButton('Reject'), QtWidgets.QMessageBox.NoRole)
        clarification.buttonClicked.connect(self.popup_button)

        clarification.exec()


    def popup_button(self, info):
        if info == "Accept":
            self.ui.button_of_pipInstall.setEnabled(False)


    def button_mode(self):
        # visible mod of button_pipInstall
        mode = PipUpgrade.button_state()
        self.ui.button_of_pipInstall.setEnabled(mode)


app = QtWidgets.QApplication([])
application = InitializationWindow()
application.show()

sys.exit(app.exec())

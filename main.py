from PyQt5.QtWidgets import QApplication, QWidget, QFrame
# from PyQt5.QtCore import Qt, QSize, pyqtSlot, QDate, QTime, QEvent
# from PyQt5.QtGui import QIcon, QPixmap, QFont, QPalette, QBrush, QColor
# from PyQt5.QtWidgets import (QDialog, QApplication, QLineEdit, QPushButton, QWidget, QMainWindow, QCheckBox, QMenu, QItemDelegate,
#                              QTableWidget, QMessageBox,
#                              QTableWidgetItem, QLabel, QListWidget, QListWidgetItem, QPlainTextEdit, QFileDialog,
#                              QComboBox, QCalendarWidget, QAbstractItemView, QDateEdit,
#                              QProgressBar, QGroupBox, QGridLayout, QFrame, QTextEdit, QTimeEdit)

import sys

class mainWindows(QWidget):

    def __init__(self):
        self.clientInfoScreen = QFrame()
        self.clientInfoScreen.setWindowTitle("Client Info")
        self.clientInfoScreen.resize(400, 400)
        self.clientInfoScreen.show()

appMake = QApplication(sys.argv)
app = mainWindows()
sys.exit(appMake.exec_())
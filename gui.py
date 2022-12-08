import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Attendance System")
        self.setGeometry(0, 0, 500, 400)
        self.badd_record()
        self.btake_attendance()
        self.show()

    def badd_record(self):
        self.badd_re = QPushButton(self)
        self.badd_re.setText("Add Record")
        self.badd_re.setGeometry(190, 100, 140, 40)
        self.badd_re.clicked.connect(self.say_hello)
        self.badd_re.show()

    def btake_attendance(self):
        self.btake_att = QPushButton(self)
        self.btake_att.setText("Take Attendance")
        self.btake_att.setGeometry(190, 170, 140, 40)
        self.btake_att.clicked.connect(self.say_hello)
        self.btake_att.show()

    @Slot()
    def connect_add_record(self):

        print("Button clicked, Hello!")
        self.badd_re.hide()
        self.btake_att.hide()

    @Slot()
    def connect_take_attendance(self):
        print("Button clicked")
        self.badd_re.hide()
        self.btake_att.hide()


def create():

    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create a button, connect it and show it
    window = MainWindow()
    # Run the main Qt loop
    app.exec()


create()

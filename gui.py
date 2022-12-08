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
        badd_re = QPushButton(self)
        badd_re.setText("Add Record")
        badd_re.setGeometry(190, 100, 140, 40)
        badd_re.clicked.connect(self.say_hello)
        badd_re.show()

    def btake_attendance(self):
        btake_att = QPushButton(self)
        btake_att.setText("Take Attendance")
        btake_att.setGeometry(190, 170, 140, 40)
        btake_att.clicked.connect(self.say_hello)
        btake_att.show()

    @Slot()
    def say_hello(self):

        print("Button clicked, Hello!")


def create():

    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create a button, connect it and show it
    window = MainWindow()
    # Run the main Qt loop
    app.exec()


create()

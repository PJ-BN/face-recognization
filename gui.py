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
        self.badd_re.clicked.connect(self.connect_add_record)
        self.badd_re.show()

    def btake_attendance(self):
        self.btake_att = QPushButton(self)
        self.btake_att.setText("Take Attendance")
        self.btake_att.setGeometry(190, 170, 140, 40)
        self.btake_att.clicked.connect(self.connect_take_attendance)
        self.btake_att.show()

    @Slot()
    def connect_add_record(self):

        self.badd_re.hide()
        self.btake_att.hide()
        self.record_label()
        self.back_button()

    @Slot()
    def connect_take_attendance(self):
        print("Button clicked")
        self.badd_re.hide()
        self.btake_att.hide()
        self.back_button()

    def record_label(self):
        self.instruction_label = QLabel(self)
        self.instruction_label.setText("Look at the webcam")
        self.instruction_label.setGeometry(170, 50, 200, 40)
        self.instruction_label.show()

    def back_button(self):
        self.back_key = QPushButton(self)
        self.back_key.setText("Back")
        self.back_key.setGeometry(10,350,80,35)
        self.back_key.clicked.connect(self.previous_area)
        self.back_key.show()

    @Slot()
    def previous_area(self):
        self.back_key.hide()
        self.instruction_label.hide()
        self.badd_re.show()
        self.btake_att.show()



def create():

    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create a button, connect it and show it
    window = MainWindow()
    # Run the main Qt loop
    app.exec()


create()

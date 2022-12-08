import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
from image import click_image
import time


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
        self.next_button()

    @Slot()
    def connect_take_attendance(self):

        self.badd_re.hide()
        self.btake_att.hide()
        self.back_button()

    def record_label(self):
        self.func_add_name()

    def func_add_name(self):
        self.add_name = QLabel(self)
        self.add_name.setText("Name")
        self.add_name.setGeometry(150, 100, 80, 40)
        self.add_name.show()

        self.addname_field = QLineEdit(self)
        self.addname_field.setGeometry(210, 103, 130, 28)
        self.addname_field.show()
        self.addname_field.echoMode()


    @Slot()
    def get_name(self):
        student_name = self.addname_field.text()
        self.addname_field.clear()

        self.webcam_access(student_name)

    def webcam_access(self, name):
        time.sleep(2)
        click_image(name)

    def back_button(self):
        self.back_key = QPushButton(self)
        self.back_key.setText("Back")
        self.back_key.setGeometry(10,350,80,35)
        self.back_key.clicked.connect(self.previous_area)
        self.back_key.show()

    def next_button(self):
        self.next_key = QPushButton(self)
        self.next_key.setText("Next")
        self.next_key.setGeometry(370,350,80,35)
        self.next_key.clicked.connect(self.get_name)
        self.next_key.show()

    def previous_area_hide(self):
        self.back_key.hide()
        self.instruction_label.hide()
        self.add_name.hide()
        self.addname_field.hide()
        self.next_key.hide()

    def previous_area_show(self):
        self.badd_re.show()
        self.btake_att.show()

    @Slot()
    def previous_area(self):
        self.previous_area_hide()
        self.previous_area_show()

def create():

    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create a button, connect it and show it
    window = MainWindow()
    # Run the main Qt loop
    app.exec()


create()

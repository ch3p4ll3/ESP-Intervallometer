import bluetooth

import sys
from datetime import time

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.ui_mainwindow import Ui_MainWindow
from UI.BLConnect import Ui_Form
import threading


class Worker(threading.Thread):
    def __init__(self, list, label):
        threading.Thread.__init__(self)
        self.list = list
        self.label = label

    def run(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        self.label.setText("Found {} devices.".format(len(nearby_devices)))

        for i, j in nearby_devices:
            self.list.addItem(f"{j} - {i}")


class Blconnect(QMainWindow):
    def __init__(self, parent=None):
        super(Blconnect, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.addListeners()
        self.discovery()

    def addListeners(self):
        self.ui.pushButton.clicked.connect(lambda: self.destroy())
        self.ui.pushButton_2.clicked.connect(self.okButton)
        self.ui.pushButton_3.clicked.connect(self.discovery)

    def okButton(self):
        if len(self.ui.listWidget.selectedItems()) == 1:
            self.ui.label.setText(f"Conecting to device {self.ui.listWidget.selectedItems()[0].text()}")
            self.parent.connect_to_bl(self.ui.listWidget.selectedItems()[0].text().split(" - ")[1])
            self.destroy()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You are not connected to any device!")
            msg.setWindowTitle("Warning!")
            msg.exec_()

    def discovery(self):
        self.ui.listWidget.clear()
        self.ui.label.setText("Discovering BL Devices...")
        Worker(self.ui.listWidget, self.ui.label).start()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.addListeners()
        self.isConnected = False
        self.BTsocket = None

    def addListeners(self):
        self.ui.actionConnect.triggered.connect(lambda: Blconnect(self).show())
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.pushButton.clicked.connect(lambda: self.send_message("singleShot#"))
        self.ui.pushButton_2.clicked.connect(lambda: self.send_message("Bulb#"))
        self.ui.pushButton_3.clicked.connect(lambda: self.send_message("stop"))
        self.ui.pushButton_4.clicked.connect(self.timer_bulb)
        self.ui.pushButton_5.clicked.connect(lambda: self.send_message("stop"))
        self.ui.pushButton_6.clicked.connect(self.intervallometer)
        self.ui.pushButton_8.clicked.connect(self.bulb_intervallometer)
        self.ui.pushButton_9.clicked.connect(lambda: self.send_message("stop"))
        self.ui.pushButton_7.clicked.connect(lambda: self.send_message("stop"))

    def bulb_intervallometer(self):
        delay = self.ui.timeEdit_4.time().toPython()
        shutter_on = self.ui.timeEdit_3.time().toPython()
        seconds_del = (delay.hour * 60 + delay.minute) * 60 + delay.second
        seconds_sh = (shutter_on.hour * 60 + shutter_on.minute) * 60 + shutter_on.second
        self.send_message(f"bulbIntervallometer#{seconds_del}#{self.ui.spinBox_4.text()}#{seconds_sh}")

    def timer_bulb(self):
        delay = self.ui.timeEdit_2.time().toPython()
        seconds = (delay.hour * 60 + delay.minute) * 60 + delay.second
        self.send_message(f"timerBulb#{seconds}")

    def intervallometer(self):
        delay = self.ui.timeEdit_5.time().toPython()
        seconds_del = (delay.hour * 60 + delay.minute) * 60 + delay.second
        self.send_message(f"intervallometer#{seconds_del}#{self.ui.spinBox_3.text()}")

    def exit(self):
        try:
            self.BTsocket.close()
        except:
            pass
        self.destroy()
        quit()

    def connect_to_bl(self, btaddr):
        if not self.isConnected:
            self.BTsocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.BTsocket.connect((btaddr, 1))
            self.isConnected = True

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You are already connected to a device!")
            msg.setWindowTitle("Warning!")
            msg.exec_()

    def send_message(self, message):
        if self.isConnected:
            self.BTsocket.send(message)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You are not connected to any device!")
            msg.setWindowTitle("Warning!")
            msg.exec_()


        # BTsocket.recv(1024).decode()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

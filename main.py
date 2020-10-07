# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import win10toast
from update_check import checkForUpdates

name = "No Name Entered"
version = "1.0.0"
checkForUpdates(__file__, "https://raw.githubusercontent.com/kyler-carleton/it-request/main/main.py")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(f"IT Request Version: {version}")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(640, 110, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.name.setFont(font)

        self.name.setText("")
        self.name.setFrame(True)
        self.name.setObjectName("name")
        self.submitName = QtWidgets.QPushButton(self.centralwidget)
        self.submitName.setGeometry(QtCore.QRect(640, 150, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.submitName.setFont(font)
        self.submitName.setObjectName("submitName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 190, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label.setFont(font)

        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.rotate = QtWidgets.QPushButton(self.centralwidget)
        self.rotate.setGeometry(QtCore.QRect(640, 230, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.rotate.setFont(font)
        self.rotate.setObjectName("rotate")
        self.wifi = QtWidgets.QPushButton(self.centralwidget)
        self.wifi.setGeometry(QtCore.QRect(640, 270, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.wifi.setFont(font)
        self.wifi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wifi.setObjectName("wifi")
        self.work = QtWidgets.QPushButton(self.centralwidget)
        self.work.setGeometry(QtCore.QRect(640, 310, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.work.setFont(font)
        self.work.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.work.setObjectName("work")
        self.hardwareHelp = QtWidgets.QPushButton(self.centralwidget)
        self.hardwareHelp.setGeometry(QtCore.QRect(640, 350, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.hardwareHelp.setFont(font)
        self.hardwareHelp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hardwareHelp.setObjectName("hardwareHelp")
        self.submitCustom = QtWidgets.QPushButton(self.centralwidget)
        self.submitCustom.setGeometry(QtCore.QRect(640, 470, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.submitCustom.setFont(font)
        self.submitCustom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitCustom.setObjectName("submitCustom")
        self.custom = QtWidgets.QLineEdit(self.centralwidget)
        self.custom.setGeometry(QtCore.QRect(640, 430, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.custom.setFont(font)

        self.custom.setText("")
        self.custom.setFrame(True)
        self.custom.setObjectName("custom")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 390, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_2.setFont(font)

        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submitName.clicked.connect(self.submit_name)
        self.rotate.clicked.connect(self.rotate_act)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(f"IT Request Version: {version}", (f"IT Request Version: {version}")))
        self.name.setToolTip(_translate("MainWindow", "Enter Name Here"))
        self.name.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.submitName.setText(_translate("MainWindow", "Submit Name"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Select Need</p></body></html>"))
        self.rotate.setText(_translate("MainWindow", "Rotated Screen"))
        self.wifi.setText(_translate("MainWindow", "Wifi Help"))
        self.work.setText(_translate("MainWindow", "Work Help"))
        self.hardwareHelp.setText(_translate("MainWindow", "Hardware Help"))
        self.submitCustom.setText(_translate("MainWindow", "Submit Custom"))
        self.custom.setToolTip(_translate("MainWindow", "Enter Name Here"))
        self.custom.setPlaceholderText(_translate("MainWindow", "Enter Custom"))
        self.label_2.setText(_translate("MainWindow", "Custom Help"))

    def submit_name(self):
        global name
        name = f"{self.name.text()} needs IT help"

    def rotate_act(self):
        import smtplib
        from email.message import EmailMessage

        def email_alert(subject, body, to):
            msg = EmailMessage()
            msg.set_content(body)
            msg['subject'] = subject
            msg['to'] = to
    

            user = "carletonnotify@gmail.com"
            msg['from'] = user
            password = "dqpgvizlqyaibdng"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
            server.quit


        if __name__ == '__main__':
            email_alert(f"{name}", f"{name} needs help with screen rotating", "8162064578@vtext.com")
            
        toaster = win10toast.ToastNotifier()

        toaster.show_toast('IT Request', 'Request Successfully Sent', duration=5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget {
                background-color: rgb(25,25,25);
        }
        QPushButton {
                color: white;
                border: 1px solid white;
        }
        QPushButton:hover {
                color: white;
                border: 3px solid white;
        }
        QLineEdit {
                color: white;
                border: 1px solid white;
        }
        QLabel {
                color: white;
                border: 1px dashed white;
        }
    """

    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

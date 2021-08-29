from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *


class Ui_MainWindow(object):

    def __init__(self, n, t, h):
        self.n = n
        self.t = t
        self.h = h

    def daa_project1(self, n):

        def for_tens_ones(self, t):
            single_digit = [" ",
                            "one ",
                            "two ",
                            "three ",
                            "four ",
                            "five ",
                            "six ",
                            "seven ",
                            "eight ",
                            "nine "]

            double_digit_1 = ["ten ",
                              "eleven ",
                              "twelve ",
                              "thirteen ",
                              "fourteen ",
                              "fifteen ",
                              "sixteen ",
                              "seventeen ",
                              "eighteen ",
                              "nineteen "]

            double_digit_2 = ["",
                              "",
                              "twenty ",
                              "thirty ",
                              "forty ",
                              "fifty ",
                              "sixty ",
                              "seventy ",
                              "eightty ",
                              "ninety"]

            tens = t // 10
            ones = t % 10
            if t < 10:
                return (single_digit[t])
            elif t > 9 and t < 20:
                return (double_digit_1[t % 10])
            elif t > 19:
                return ((double_digit_2[tens]) + single_digit[ones])

        def for_hundreds(self, h):
            single_digit = [" ",
                            "one ",
                            "two ",
                            "three ",
                            "four ",
                            "five ",
                            "six ",
                            "seven ",
                            "eight ",
                            "nine "]

            hundred = h // 100
            two_digit = h % 100
            if h > 99:
                return ((single_digit[hundred]) + " hundred " + for_tens_ones(self, two_digit))
            elif h < 100:
                return for_tens_ones(self, two_digit)

        billion = n // 1000000000

        million = (n // 1000000) % 1000

        thousand = (n // 1000) % 1000

        hundreds_tens_ones = n % 1000

        billion_output = ""
        million_output = ""
        thousand_output = ""
        hundreds_tens_ones_output = ""

        if n < 0:
            return "check number"
        elif n > 0:
            billion_output = for_hundreds(self, billion) + " billion "

            million_output = for_hundreds(self, million) + " million "

            thousand_output = for_hundreds(self, thousand) + " thousand "

            hundreds_tens_ones_output = for_hundreds(self, hundreds_tens_ones)

            output = ""
            output1 = ""
            output2 = ""
            output3 = ""
            output4 = ""
            if billion > 0:
                output1 = billion_output

            if million > 0:
                output2 = million_output

            if thousand > 0:
                output3 = thousand_output

            if hundreds_tens_ones > 0:
                output4 = hundreds_tens_ones_output

            output = output1 + output2 + output3 + output4 + " only "
        return output

    def calculate_clicked(self):
        self.n = int(self.lineEdit_3.text())
        output = self.daa_project1(self.n)
        print("output is ", output)

        #         q = QDialog()
        #         q.setWindowTitle("Result")
        #         q.resize(420, 327)
        #         font = QtGui.QFont()
        #         font.setPointSize(12)
        #         label = QLabel(q)
        #         label.setGeometry(QtCore.QRect(190, 0, 151, 41))
        #         label.setFont(font)
        # label_text = "Result : " + str(alignment1)
        #         label.setGeometry(QtCore.QRect(830, 240, 301, 191))
        #         label.setText("OUTPUT")
        #         textedit_3 = QTextEdit(q)
        #         textedit_3.setGeometry(QtCore.QRect(230, 610, 1661, 671))
        #         textedit_3.setFont(font)
        self.textEdit.setText(output)

    #         q.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 628)
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 40, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 91, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 140, 561, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 240, 331, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 240, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate_clicked)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 400, 121, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 400, 451, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 410, 151, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(840, 400, 291, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(890, 520, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(890, 470, 231, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(990, 30, 191, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 300, 1011, 87))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HDFC   BANK"))
        self.label_2.setText(_translate("MainWindow", "MULTICITY   CHEQUE  BOOK"))
        self.label_3.setText(_translate("MainWindow", "DATE"))
        self.label_4.setText(_translate("MainWindow", "PAY"))
        self.label_5.setText(_translate("MainWindow", "RS"))
        self.pushButton.setText(_translate("MainWindow", "AUTO FILL"))
        self.label_6.setText(_translate("MainWindow", "RUPEES"))
        self.label_7.setText(_translate("MainWindow", "A/C  NO"))
        self.label_8.setText(_translate("MainWindow", "IFSC CODE"))
        self.label_9.setText(_translate("MainWindow", "AUTHORISED SIGNATURE"))


if __name__ == "__main__":
    global n
    n = 0
    global t
    t = 0
    global h
    h = 0
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(n, t, h)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
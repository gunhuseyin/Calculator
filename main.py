from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
import sys
from PyQt5.QtCore import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setStyleSheet("background-color:#f3f3f3;")
        self.setMaximumSize(195,375)

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("calcula.png"))
        # Create Central Widget And Layout
        centralWidget=QWidget()
        self.central_vb=QVBoxLayout()
        self.central_vb.setContentsMargins(15,15,15,15)
        centralWidget.setLayout(self.central_vb)
        self.setCentralWidget(centralWidget)
        #Load the Calculator
        self.load()

    def load(self):

        #Create Processing Screen
        self.label=QLabel()
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 0.5px solid #a0a0a0;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))
        self.label.setMinimumSize(195,100)
        self.label.setText("")

        #Add Label to Window
        self.central_vb.addWidget(self.label)

        #Create a new Layout for the buttons sections
        main_vb=QVBoxLayout()
        gridLayout=QGridLayout()
        gridLayout.setContentsMargins(0,0,0,0)
        gridLayout.setSpacing(5)
        main_vb.addLayout(gridLayout)
        main_vb.setContentsMargins(0,0,0,0)
        self.central_vb.addLayout(main_vb)

        #Create 1-9 btns
        rowCount=0
        columnCount=0

        for i in range(1,10):
            btn=QPushButton(str(i))
            btn.resize(45,45)
            btn.setMinimumSize(45,45)
            btn.setMaximumSize(45,45)
            btn.setStyleSheet("background-color:#f3f3f3; border:0.5px solid #a0a0a0; border-radius:6px; color:black;")
            btn.clicked.connect(self.addAction)

            if columnCount>2:
                columnCount=0
                rowCount+=1
            gridLayout.addWidget(btn,rowCount,columnCount)
            columnCount+=1
        #Create delete button
        delBtn = QPushButton("Del")
        delBtn.resize(45, 45)
        delBtn.setMinimumSize(45, 45)
        delBtn.setMaximumSize(45, 45)
        delBtn.setStyleSheet("background-color:#0055ff;  border-radius:6px; color:white;")
        delBtn.clicked.connect(self.delAction)
        gridLayout.addWidget(delBtn, 3, 0)

        #Create zero button
        zeroBtn = QPushButton("0")
        zeroBtn.resize(45, 45)
        zeroBtn.setMinimumSize(45, 45)
        zeroBtn.setMaximumSize(45, 45)
        zeroBtn.setStyleSheet("background-color:#f3f3f3; border:0.5px solid #a0a0a0; border-radius:6px; color:black;")
        zeroBtn.clicked.connect(self.addAction)
        gridLayout.addWidget(zeroBtn, 3, 1)

        #Create point button
        pointBtn = QPushButton(".")
        pointBtn.resize(45, 45)
        pointBtn.setMinimumSize(45, 45)
        pointBtn.setMaximumSize(45, 45)
        pointBtn.setStyleSheet("background-color:#f3f3f3; border:0.5px solid #a0a0a0; border-radius:6px; color:black;")
        pointBtn.clicked.connect(self.addAction)
        gridLayout.addWidget(pointBtn, 3, 2)

        #Create plus button
        plusBtn = QPushButton("+")
        plusBtn.resize(45, 45)
        plusBtn.setMinimumSize(45, 45)
        plusBtn.setMaximumSize(45, 45)
        plusBtn.setStyleSheet("background-color:#a0a0a0; border-radius:22px; color:black;")
        plusBtn.clicked.connect(self.addAction)
        gridLayout.addWidget(plusBtn, 0, 3)

        #Create minues button
        minuesBtn = QPushButton("-")
        minuesBtn.resize(45, 45)
        minuesBtn.setMinimumSize(45, 45)
        minuesBtn.setMaximumSize(45, 45)
        minuesBtn.setStyleSheet("background-color:#a0a0a0; border-radius:22px; color:black;")
        minuesBtn.clicked.connect(self.addAction)
        gridLayout.addWidget(minuesBtn, 1, 3)

        #Create multiply Button
        multiplyBtn = QPushButton("*")
        multiplyBtn.resize(45, 45)
        multiplyBtn.setMinimumSize(45, 45)
        multiplyBtn.setMaximumSize(45, 45)
        multiplyBtn.setStyleSheet("background-color:#a0a0a0; border-radius:22px; color:black;")
        multiplyBtn.clicked.connect(self.addAction)
        gridLayout.addWidget(multiplyBtn, 2, 3)

        #Create divide button
        divideBtn = QPushButton("/")
        divideBtn.resize(45, 45)
        divideBtn.setMinimumSize(45, 45)
        divideBtn.setMaximumSize(45, 45)
        divideBtn.setStyleSheet("background-color:#a0a0a0; border-radius:22px; color:black;")
        divideBtn.clicked.connect(self.addAction)
        gridLayout.addWidget(divideBtn, 3, 3)

        #Create a layout for bottom buttons (clear and equal)
        hb_2=QHBoxLayout()
        hb_2.setContentsMargins(0,0,0,0)
        main_vb.addLayout(hb_2)
        #Create clear button
        clearBtn = QPushButton("Clear")
        clearBtn.resize(145, 45)
        clearBtn.setMinimumSize(145, 45)
        clearBtn.setMaximumSize(145, 45)
        clearBtn.setStyleSheet("background-color:#a0a0a0; border-radius:6px; color:black;")
        clearBtn.clicked.connect(self.clearAction)
        hb_2.addWidget(clearBtn)
        #Create equal button
        equalBtn = QPushButton("=")
        equalBtn.resize(45, 45)
        equalBtn.setMinimumSize(45, 45)
        equalBtn.setMaximumSize(45, 45)
        equalBtn.setStyleSheet("background-color:#dc8a05; border-radius:22px; color:white;")
        equalBtn.clicked.connect(self.equalAction)
        hb_2.addWidget(equalBtn)

    # Create fonction for buttons
    def addAction(self):
        senderTxt=self.sender().text()
        txt = self.label.text()
        if txt=="Wrong Input":
            txt=""

        txt=txt+senderTxt
        self.label.setText(txt)

    def delAction(self):
        text = self.label.text()
        txt=self.label.text()
        if txt=="Wrong Input":
            text=""
            self.label.setText("")
        else:
            self.label.setText(text[:len(text) - 1])
    def clearAction(self):
        self.label.setText("")
    def equalAction(self):
        equation = self.label.text()
        try:

            ans = eval(equation)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")



# Drive The Calculator App
app=QApplication(sys.argv)
calculator=Calculator()
calculator.show()
app.exec_()

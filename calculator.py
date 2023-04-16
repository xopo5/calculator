from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton,QLineEdit,QGridLayout,QWidget,QSizePolicy
class redactbutton(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setMinimumSize(40,40)
        self.setFont(QFont("Segoe UI",14))
        self.setStyleSheet('''
            QPushButton {
                background-color: #333333;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QPushButton:pressed {
                background-color: #777777;
            }
        ''')


main = QApplication([])
window = QWidget()
window.setStyleSheet('''
    QWidget {
        background-color: #222222;
    }
    QLineEdit {
        background-color: #333333;
        color: white;
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 5px;
    }

''')

button1 =  redactbutton("1")
button2 =  redactbutton("2")
button3 =  redactbutton("3")
button4 =  redactbutton("4")
button5 =  redactbutton("5")
button6 =  redactbutton("6")
button7 =  redactbutton("7")
button8 =  redactbutton("8")
button9 =  redactbutton("9")
button0 =  redactbutton("0")
buttondot =redactbutton('.')
result = redactbutton('=')
textline = QLineEdit()
buttonadd = redactbutton('+')
buttonminus = redactbutton("-")
buttonmult = redactbutton('*')
buttonslash = redactbutton("/")
buttondel = redactbutton("<-")
buttonclear = redactbutton("C")
mainlayout = QGridLayout()
result.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

mainlayout.addWidget(textline, 0, 0,1,4)
mainlayout.addWidget(button1, 4, 0)
mainlayout.addWidget(button2, 4, 1)
mainlayout.addWidget(button3, 4, 2)
mainlayout.addWidget(button4, 3, 0)
mainlayout.addWidget(button5, 3, 1)
mainlayout.addWidget(button6, 3, 2)
mainlayout.addWidget(button7,2, 0)
mainlayout.addWidget(button8, 2, 1)
mainlayout.addWidget(button9, 2, 2)
mainlayout.addWidget(button0, 5, 0,1,2)
mainlayout.addWidget(buttondot,5,2)
mainlayout.addWidget(result,4,3,2,1)
mainlayout.addWidget(buttonslash,3,3)
mainlayout.addWidget(buttonmult,2,3)
mainlayout.addWidget(buttonminus,1,3)
mainlayout.addWidget(buttonadd,1,2)
mainlayout.addWidget(buttondel,1,0)
mainlayout.addWidget(buttonclear,1,1)



window.setLayout(mainlayout)
window.setWindowTitle('C A L C')
window.show()
main.exec_()

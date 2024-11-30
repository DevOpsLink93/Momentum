#Modules
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


#Create Desktop Window
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200, 300, 500, 500)
    win.setWindowTitle("Momentum")
    win.setToolTip("Momentum")
    win.setWindowIcon(QIcon('Momentum-Logo-Python.png'))
    
    #Create Label For Summary
    lbl_Summary = QtWidgets.QLabel(win)
    lbl_Summary.setText('Summary: ')
    lbl_Summary.move(50, 50)
    
    #Create Summary Textbox
    txt_Summary = QtWidgets.QLineEdit(win)
    txt_Summary.move (50, 90)
    
    #Create Label For Description
    lbl_Summary = QtWidgets.QLabel(win)
    lbl_Summary.setText('Description: ')
    lbl_Summary.move(200, 50)
    
    #Create Textbox Description
    txt_Description = QtWidgets.QLineEdit(win)
    txt_Description.move (200, 90)
    
    #Save Button
    def clicked(self):
        print ('Button Clicked')
        print ('Summary:' + txt_Summary.text())
    
    btn_Save = QtWidgets.QPushButton(win)
    btn_Save.setText('Save')
    btn_Save.clicked.connect(clicked)
    btn_Save.move(200, 130)
    
    win.show()
    sys.exit(app.exec_())
    

    
window()

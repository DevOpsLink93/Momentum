#Modules
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon

# Create Desktop Window
class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle("Momentum")
        self.setToolTip("Momentum")
        self.setWindowIcon(QIcon("Momentum-Logo-Python.png"))
        self.initUI()
        
    # Create labels and Textboxes
    def initUI(self):
        # Set Summary
        self.lbl_Summary = QtWidgets.QLabel(self)
        self.lbl_Summary.setText("Summary Name Of Task")
        self.lbl_Summary.move(50,50)
            
        self.txt_Summary = QtWidgets.QLineEdit(self)
        self.txt_Summary.move(200,50)  # Adjusted the position of txt_Summary
        self.txt_Summary.resize(200,32)
        
        # Set Description
        self.lbl_Desc = QtWidgets.QLabel(self)
        self.lbl_Desc.setText("Description Of Task")
        self.lbl_Desc.move(50,90)
            
        self.txt_Desc = QtWidgets.QLineEdit(self)
        self.txt_Desc.move(200,90)  # Adjusted the position of txt_Desc
        self.txt_Desc.resize(200,32)
        
        # Save Button
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Save')
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(200, 130)

    # Define Click Action
    def clicked(self):
        # Get the text from both text boxes
        summary_text = self.txt_Summary.text()
        desc_text = self.txt_Desc.text()

        # Create a pop-up message
        message = f"You have Entered:\n\nSummary: {summary_text}\nDescription: {desc_text}"
        
        # Display the message in a pop-up (similar to an Outlook message)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Task Information")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
# Load Window 
def window():
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec_())   

window()
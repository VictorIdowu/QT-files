from PyQt6.QtWidgets import QMainWindow,QApplication
import sys
from form import Ui_Form

class Window(QMainWindow):
  def __init__(self):  
    super().__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.initUI()
  
  def initUI(self):
    self.setGeometry(0,0,400,300)
    self.ui.username_input.setMaxLength(8)
    self.ui.password_input.setMaxLength(8)
    self.ui.pushButton.clicked.connect(self.submit)
  
  def submit(self):
    username = self.ui.username_input.text()
    password = self.ui.password_input.text()
    
    if username == 'admin' and password == 'admin123':
      print("Valid username and password")
    else:
      print("Invalid username or password")
  
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
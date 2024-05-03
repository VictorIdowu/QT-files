from PyQt6.QtWidgets import QMainWindow,QApplication
import sys
from todo import Ui_Form

class Window(QMainWindow):
  def __init__(self):  
    super().__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.initUI()
  
  def initUI(self):
    self.setGeometry(0,0,400,350)
    self.ui.add_btn.clicked.connect(self.add_task)
    self.ui.delete_btn.clicked.connect(self.delete_task)

  def add_task(self):
    task = self.ui.item_input.text()
    if task:
      self.ui.listWidget.addItem(task)
      self.ui.item_input.setText("")
    else:
      print("Please enter a task")

  def delete_task(self):
    selected_task = self.ui.listWidget.currentItem()
    if selected_task:
      self.ui.listWidget.takeItem(self.ui.listWidget.row(selected_task))
    else:
      print("Please select a task")
    
  
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
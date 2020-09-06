from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		# setting title
		self.setWindowTitle("Simon CY")
		# setting geometry
		self.setGeometry(100, 100, 420, 350)
		# calling method
		self.UiComponents()
		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):
		# creating a QCalendarWidget object
		calender = QCalendarWidget(self)	
		# setting geometry to the calender
		calender.setGeometry(10, 10, 400, 250)
		# creating push button
		push = QPushButton('Next Year', self)
		# setting geometry to the push
		push.setGeometry(150, 280, 100, 40)	
		# adding action to the push
		push.clicked.connect(lambda: do_action())
		def do_action():
			# show next YEAR
			calender.showNextYear()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())


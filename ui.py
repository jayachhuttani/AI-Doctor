import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
  
class LoadingGif(object):
  
    def mainUI(self, FrontWindow):
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(320, 300)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")
  
        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 100, 1000, 1000))
        self.label.setMinimumSize(QtCore.QSize(550, 550))
        self.label.setMaximumSize(QtCore.QSize(1050, 1050))
        self.label.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 10, 1000, 1000))
        self.label2.setMinimumSize(QtCore.QSize(550, 550))
        self.label2.setMaximumSize(QtCore.QSize(1050, 1050))
        self.label2.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)
  
        # Loading the GIF
        self.movie = QMovie("giphy")
        self.label.setMovie(self.movie)
        self.movie2 = QMovie("unscreen")
        self.label2.setMovie(self.movie2)
  
        self.startAnimation()
  
    # Start Animation
  
    def startAnimation(self):
        self.movie.start()
        self.movie2.start()  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
        self.movie2.stop()

  
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
demo = LoadingGif()
demo.mainUI(window)
window.show()
sys.exit(app.exec_())
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',120)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak(" My name is Doctor gedion and i am  AI created to help you diagnose possible diseases base on the symptoms ")
    

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'goodbye' or 'good bye' in self.query:
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
      




FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./AI_menu.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)

        

        self.exitB.setStyleSheet("background-image:url(./img/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        self.movie= QMovie("giphy")
        self.label_5.setMovie(self.movie)
    
        self.movie1= QMovie("unscreen")
        self.label_4.setMovie(self.movie1)
        self.movie2= QMovie("unscreen")
        self.label_3.setMovie(self.movie1)

    

        self.startAnimation()
        Dspeak=mainT()
        Dspeak.start()

    def startAnimation(self):
        self.movie.start()
        self.movie1.start()
        self.movie2.start()
  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
        self.movie1.stop()
        self.movie2.stop()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
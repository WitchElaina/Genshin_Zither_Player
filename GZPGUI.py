# This Python file uses the following encoding: utf-8
from __future__ import print_function
import sys,os
import PyQt5
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
from PyQt5 import QtCore, uic
import GenshinZitherPlayer as GZP
from mainwindow_ui import Ui_MainWindow
from functools import partial
import ctypes


def is_admin():
    try:
        if(os.sep=='/'):
            return True
        else:
            return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class GZPGUI(QMainWindow, Ui_MainWindow):
    count_sec = 5
    key_adds = []
    state = "free"
    def __init__(self, parent=None):
        # self.ui = uic.loadUi("mainwindow.ui")
        super(GZPGUI, self).__init__(parent)
        self.setupUi(self)
        
        # Scan midi file
        self.comboBox_mid_name.addItems(GZP.midScanner())
        self.comboBox_mid_name.currentIndexChanged.connect(self.midiSelected)
        
        self.pushButton_end.setAutoRepeat(False)
        self.pushButton_end.clicked.connect(self.endPlay)
        self.pushButton_end.pressed.connect(self.showEndPlayinfo)
        
        self.pushButton_play.clicked.connect(self.startPlay)
        self.pushButton_play.pressed.connect(self.showPlayinfo)
        
        self.spinBox_sec.setValue(5)
        self.label_info.setText('GenshinZitherPlayer@Mszook,2021')
        
        self.checkBox_popup.clicked.connect(self.poupWindow)
        
    def midiSelected(self):
        if(self.comboBox_mid_name.currentIndex()!=0):
            # Enable bpm and key selector
            self.comboBox_key.setEnabled(True)
            self.spinBox_bpm.setEnabled(True)
            
            # Scan avialable keys
            avlb_key = []
            self.comboBox_key.clear()
            avlb_key.clear()
            self.key_adds.clear()
            
            if(not( GZP.allToCMajor(self.comboBox_mid_name.currentText()))):
                self.label_info.setText('Midi out of range! Please select another.')
                self.comboBox_key.setEnabled(False)
                self.pushButton_play.setEnabled(False)
                
            else:
                for i in GZP.allToCMajor(self.comboBox_mid_name.currentText()):
                    if(i>0):
                        avlb_key.append("+"+str(i)+"key")
                        self.key_adds.append(i)
                    elif(i<=0):
                        avlb_key.append(str(i)+"key")
                        self.key_adds.append(i)
                self.comboBox_key.addItems(avlb_key)
                self.label_info.setText('当前选中: '+self.comboBox_mid_name.currentText())
                self.comboBox_key.setEnabled(True)
                self.pushButton_play.setEnabled(True)
            
        else:
            self.comboBox_key.setEnabled(False)
            self.spinBox_bpm.setEnabled(False)
            self.label_info.setText('GenshinZitherPlayer@Mszook,2021')
            
    def playMidi(self):
        # Player init
        file_name = self.comboBox_mid_name.currentText()
        bpm = int(self.spinBox_bpm.value())
        key_add = int(self.key_adds[self.comboBox_key.currentIndex()])

        # todo
        GZP.counter(self.spinBox_sec.value())
        GZP.playMidi(file_name, bpm, key_add, self.state)
        
    def endPlay(self):
        self.state = "end"
        
    def startPlay(self):
        self.state = "play"
         
        
    def stop(self):
        exit(0)
        
    def showPlayinfo(self):
        self.label_info.setText('请点击原神窗口内任意处')
        self.comboBox_key.setEnabled(False)
        self.comboBox_mid_name.setEnabled(False)
        # self.pushButton_end.setEnabled(False)
        self.spinBox_bpm.setEnabled(False)
        self.spinBox_sec.setEnabled(False)
        self.pushButton_play.setText('Playing..')
        
    def showEndPlayinfo(self):
        self.label_info.setText('GenshinZitherPlayer@Mszook,2021')
        self.comboBox_key.setEnabled(True)
        self.comboBox_mid_name.setEnabled(True)
        self.pushButton_end.setEnabled(True)
        self.spinBox_bpm.setEnabled(True)
        self.spinBox_sec.setEnabled(True)
        self.pushButton_play.setText('Play')
        
    def poupWindow(self):
        self.setWindowFlags(self.windowFlags | QtCore.Qt.WindowStaysOnTopHint)
        
    def sheetGen(self):
        return

if __name__ == "__main__":
    try:
        if is_admin():
            app = QApplication([])
            window = GZPGUI()
            window.show()
            app.exec_()
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            else:#in python2.x
                ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    except BaseException: 
        print("Error!")
        window.show()
        app.exec_()
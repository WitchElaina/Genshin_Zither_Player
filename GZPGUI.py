# This Python file uses the following encoding: utf-8
from __future__ import print_function
import sys,os
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
from PyQt5 import uic
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
    def __init__(self, parent=None):
        # self.ui = uic.loadUi("mainwindow.ui")
        super(GZPGUI, self).__init__(parent)
        self.setupUi(self)
        
        # Scan midi file
        self.comboBox_mid_name.addItems(GZP.midScanner())
        self.comboBox_mid_name.currentIndexChanged.connect(self.midiSelected)
        
        self.pushButton_end.setAutoRepeat(False)
        self.pushButton_end.clicked.connect(self.stop)
        
        self.pushButton_play.clicked.connect(self.playMidi)
        
        self.progressBar.setValue(0)
        self.spinBox_sec.setValue(5)
        
        
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
                       
            for i in GZP.allToCMajor(self.comboBox_mid_name.currentText()):
                if(i>0):
                    avlb_key.append("+"+str(i)+"key")
                    self.key_adds.append(i)
                elif(i<=0):
                    avlb_key.append(str(i)+"key")
                    self.key_adds.append(i)
            self.comboBox_key.addItems(avlb_key)
            
        else:
            self.comboBox_key.setEnabled(False)
            self.spinBox_bpm.setEnabled(False)
            
    def playMidi(self):
        # Player init
        file_name = self.comboBox_mid_name.currentText()
        # print(file_name)
        bpm = int(self.spinBox_bpm.value())
        key_add = int(self.key_adds[self.comboBox_key.currentIndex()])
        
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        # todo
        GZP.counter(self.spinBox_sec.value())
        GZP.playMidi(file_name, bpm, key_add)
        
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        
        
        
        
    def stop(self):
        exit(0)

if __name__ == "__main__":
    if is_admin():
        app = QApplication([])
        window = GZPGUI()
        window.show()
        sys.exit(app.exec_())
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

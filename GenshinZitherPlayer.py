"""
Genshin Impact Auto Play
"""
import os
import time
import tkinter
import _thread
import pyautogui

# Get the size of the primary monitor.
# screenWidth, screenHeight = pyautogui.size()
# print("Running at screen@",screenWidth, 'x', screenHeight)

"""
C3  60  z
C#3 61  NULL
D3  62  x
D#3 63  NULL
E3  64  c
F3  65  v
F#3 66  NULL
G3  67  b
G#3 68  NULL
A3  69  n
A#3 70  NULL
B3  71  m

C4  72  a
C#4 73  NULL
D4  74  s
D#4 75  NULL
E4  76  d
F4  77  f
F#4 78  NULL
G4  79  g
G#4 80  NULL
A4  81  h
A#4 82  NULL
B4  83  j

C5  84  q
C#5 85  NULL
D5  86  w
D#5 87  NULL
E5  88  e
F5  89  r
F#5 90  NULL
G5  91  t
G#5 92  NULL
A5  93  y
A#5 94  NULL
B5  95  u
"""
KEY_MAP = {60:'z',62:'x',64:'c',65:'v',67:'b',69:'n',71:'m',72:'a',74:'s',76:'d',77:'f',79:'g',81:'h',83:'j',84:'q',86:'w',88:'e',89:'r',91:'t',93:'y',95:'u'}

# Transfer .mid to .txt using midi2melody
def midiToMelody(m_midi_path):
    os.system("midi2melody "+m_midi_path+" > ./midi.txt")
    
def noteToKeyboard(m_note):
    return KEY_MAP[m_note]

def readTxtMelody():
    midi_txt_file = open("midi.txt","r")
    for time_temp,note_temp in midi_txt_file.readlines():
        print(time_temp,note_temp)
        
        

if __name__ == '__main__':
    # note = int(input("Input note number:"))
    # while(True):
    #     if(note==0):
    #         break
    #     print(noteToKeyboard(note))
    #     note = int(input("Input note number:"))
    # midi_path = input("Midi path")
    # midiToMelody(midi_path)
    readTxtMelody()
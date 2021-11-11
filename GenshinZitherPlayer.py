"""
Genshin Impact Auto Play
"""
import os
import time
import tkinter
import pyautogui

KEY_MAP = {60:'z',62:'x',64:'c',65:'v',67:'b',69:'n',71:'m',72:'a',74:'s',76:'d',77:'f',79:'g',81:'h',83:'j',84:'q',86:'w',88:'e',89:'r',91:'t',93:'y',95:'u',0:'p'}

# Transfer .mid to .txt using midi2melody
def midiToMelody(m_midi_path):
    os.system("midi2melody "+m_midi_path+" > ./midi.txt")
    
def noteToKeyboard(m_note):
    return KEY_MAP[m_note]

def readTxtMelody():
    midi_txt_file = open("midi.txt","r")
    notes=[]
    contents = midi_txt_file.readlines()
    for msg in contents:
        msg = msg.strip('\n')
        adm = msg.split('\t')
        notes.append(adm)
    midi_txt_file.close()
    return notes
        
            

if __name__ == '__main__':
    pyautogui.PAUSE = 0
    notes = readTxtMelody()
    bpm = 138
    player = []
    last_bar, last_note = -1, -1
    for cur_bar,cur_note in notes:
        print(cur_bar,cur_note)
        if(last_bar != -1):
            player.append([float(cur_bar)-last_bar, int(last_note)])
            print("append-> ",float(cur_bar)-last_bar,last_note)
        last_bar, last_note = float(cur_bar), int(cur_note)
    
    time.sleep(3)
    bpm = 60/bpm   
    for sus_time, note in player:
        pyautogui.keyDown(noteToKeyboard(note))
        pyautogui.sleep(sus_time*bpm)
        pyautogui.keyUp(noteToKeyboard(note))
        
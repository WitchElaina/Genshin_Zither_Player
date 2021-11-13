import mido
import os
import time
import tkinter
import pyautogui

# Key Map between midi file and Genshin Keyboard
KEY_MAP = {60:'z',62:'x',64:'c',65:'v',67:'b',69:'n',71:'m',72:'a',74:'s',76:'d',77:'f',79:'g',81:'h',83:'j',84:'q',86:'w',88:'e',89:'r',91:'t',93:'y',95:'u',0:'p'}

# Turn off autopause in pyautogui
pyautogui.PAUSE = 0

# Translate midi note to keybord
def noteTrans(m_note_value):
    return KEY_MAP[int(m_note_value)]

# Genshin's zither only support melody in C Major, Use this to translate other scale to C Major
def allToCMajor(m_file_name):
    note_temp = []
    for msg in mido.MidiFile(m_file_name+".mid"):
        if(msg.type == "note_on" or msg.type == "note_off"):
            if(note_temp.type): 
                # todo
                note_temp.append(int(msg.note))
        
        

def playMidi(m_file_name, m_bpm):
    # Trans bpm to spb ( Second per bar )
    spb = float(60 / m_bpm * 2) 
    
    # Read midi file
    for msg in mido.MidiFile(m_file_name+".mid"):
        if(msg.type=="note_on"):
            # Press
            print(msg.type, msg.note, msg.time)
            pyautogui.sleep(float(msg.time)*spb)
            pyautogui.keyDown(noteTrans(msg.note))
        elif(msg.type=="note_off"):
            # Release
            print(msg.type, msg.note, msg.time, "\n")
            pyautogui.sleep(float(msg.time)*spb)
            pyautogui.keyUp(noteTrans(msg.note))
        else:
            continue

def counter(m_second):
    # Sleep m_second s with print
    for i in range(m_second):
        print(m_second-i, "s...")
        time.sleep(1)        
               
if __name__ == '__main__':
    file_name = input("Select midi file: ")
    bpm = int(input("Input bpm: "))
    counter(5)
    playMidi(file_name,bpm)
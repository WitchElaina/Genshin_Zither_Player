import mido
import os
import time
import pyautogui

# Key Map between midi file and Genshin Keyboard
KEY_MAP = {60:'z',62:'x',64:'c',65:'v',67:'b',69:'n',71:'m',72:'a',74:'s',76:'d',77:'f',79:'g',81:'h',83:'j',84:'q',86:'w',88:'e',89:'r',91:'t',93:'y',95:'u',0:'p'}

SCALES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

# Turn off autopause in pyautogui
pyautogui.PAUSE = 0

# Scan mid file in mid_repo folder
def midScanner():
    m_file = os.listdir("."+os.sep+"midi_repo")
    ret = []
    for i in m_file:
        if os.path.splitext(i)[1] == '.mid':
            ret.append(i)
    return ret
            


# Translate midi note to keybord
def noteTrans(m_note_value):
    return KEY_MAP[m_note_value]

# Genshin's zither only support melody in C Major, Use this to translate other scale to C Major
def allToCMajor(m_file_name):
    file_name = "." + os.sep + "midi_repo" + os.sep + m_file_name
    # print(file_name)
    note_temp = []
    avialiable_add = []
    for msg in mido.MidiFile(file_name):
        # if(msg.type == "note_on" or msg.type == "note_off"):
        if(msg.type == "note_on"):
            isExist = False
            for i in note_temp:
                if(i==msg.note):
                    isExist = True
                    break;
            if(not isExist): 
                note_temp.append(msg.note)
    

    for i in range(-48,48):
        isC = True
        for cur in note_temp:
            if(KEY_MAP.__contains__(int(cur)+i)==False):
                isC = False
                break
        if(isC):
            avialiable_add.append(i)
    return avialiable_add
            
        
        

def playMidi(m_file_name, m_bpm, m_key_add):
    file_name = "." + os.sep + "midi_repo" + os.sep + m_file_name
    
    real_time = float( 120 / m_bpm ) 
    
    midi = mido.MidiFile(file_name)
    
    # set bpm
    tempo = mido.bpm2tempo(m_bpm)
    
    # Read midi file
    for msg in midi:
        if(msg.type=="note_on"):
            # Press
            sleep_time = float(msg.time) * real_time
            pyautogui.sleep(sleep_time)
            pyautogui.keyDown(noteTrans(int(msg.note)+m_key_add))
            pyautogui.keyUp(noteTrans(int(msg.note)+m_key_add))
            
        elif(msg.type=="note_off"):
            # Release
            sleep_time = float(msg.time) * real_time
            pyautogui.sleep(sleep_time)
            
        else:
            continue 

def counter(m_second):
    # Sleep m_second s with print
    for i in range(m_second):
        # print(m_second-i, "s...")
        time.sleep(1)        
               
if __name__ == '__main__':
    # init
    note_add = 0
    isC = False
    
    # Input midi file path and bpm
    file_name = input("Select midi file: ")
    bpm = int(input("Input bpm: "))
    
    # Detect scale
    key_add = allToCMajor(file_name)
    if(not(key_add)):
        exit("The midi file is too complex to play!")
        
    # if(len(key_add) == 1):
    #     if(SCALES[key_add[0]] == "C"):
    #         isC = True
    
    
    # Select avialable scale
    if(not isC):
        print("Choose key add values:")
        op_num = 1
        for i in key_add:
            print("%d.Play %+dkeys" %(op_num,i))
            op_num += 1

        selected_op_num = int(input(">"))
        op_num = 1
        for i in key_add:
            if(op_num == selected_op_num):
                note_add = i
            op_num += 1
    
    counter(5)
    print("Playing \"%s\"..." % file_name)
    playMidi(file_name,bpm,note_add)
    print("Done.")
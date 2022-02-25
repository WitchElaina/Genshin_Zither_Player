# Transfer midi file to Genshin Impact Keyboard sheet
from tomlkit import string
import GenshinZitherPlayer as GZP
import os

def printMidiSheet(m_file_name, m_bpm, m_key_add):
    # Add Path
    file_name = "." + os.sep + "midi_repo" + os.sep + m_file_name
    
    # Read midi_file
    midi_file = GZP.mido.MidiFile(file_name)
    
    # Set Tempo
    # tempo = GZP.mido.bpm2tempo(int(m_bpm))
    # print(tempo)
    
    key_add = int(m_key_add)
    ret = []
    cur = ""
    
    # Show info
    for msg in midi_file:
        if(msg.type=="note_on"):
            # print("Down:"+GZP.noteTrans(int(msg.note)+key_add))
            cur = "Down:"+GZP.noteTrans(int(msg.note)+key_add)
            
        elif(msg.type=="note_off"):
            # print("Up:"+GZP.noteTrans(int(msg.note)+key_add))
            cur = "Up:"+GZP.noteTrans(int(msg.note)+key_add)
        else:
            continue
        ret.append(cur)
        
    return ret
        
if __name__ == '__main__':
    f_name = input("Select midi file:")
    f_bpm = input("Set BPM:")
    f_keyadd = input("Key Add:")
    showMidiInfo(f_name, f_bpm, f_keyadd)
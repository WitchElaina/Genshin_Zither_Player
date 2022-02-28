# Transfer midi file to Genshin Impact Keyboard sheet
import GenshinZitherPlayer as GZP
import os

def printMidiSheet(m_file_name, m_key_add):
    # init
    ret = []
    cur = "1 "
    cur_time = 0;
    cur_bar = 1;
    
    # Add Path
    file_name = "." + os.sep + "midi_repo" + os.sep + m_file_name
    
    # Read midi_file
    midi_file = GZP.mido.MidiFile(file_name)
    
    # Show info
    for msg in midi_file:
        cur_time = msg.time + cur_time
        if(cur_time >= 2):
            ret.append(cur)
            cur = ""
            cur_bar = cur_bar + 1;
            cur = cur + str(cur_bar) + " "
            cur_time = 0;
        if(msg.type=="note_on"):
            cur = cur + GZP.noteTrans(int(msg.note)+m_key_add)
    return ret
        
if __name__ == '__main__':
    f_name = input("Select midi file:")
    f_keyadd = input("Key Add:")
    printMidiSheet(f_name, f_keyadd)
import tkinter
import GenshinZitherPlayer as GZP

def on_button_midi_check_clicked():
    GZP.counter(3)


if __name__ == "__main__":
    top = tkinter.Tk()
    
    # Init the window
    top.title('Genshin Zither Player')
    top.geometry('720x540')
    
    lable_midiname = tkinter.Label(top, text='midiName')
    lable_midiname.pack()
    
    entry_midiname = tkinter.Entry(top, show = None, )
    entry_midiname.pack()
    
    button_midi_check = tkinter.Button(top, text='Check', command=on_button_midi_check_clicked)
    button_midi_check.pack()
    
    # Main loop
    top.mainloop()
    
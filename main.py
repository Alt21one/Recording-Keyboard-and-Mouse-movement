import tkinter as tk
from tkinter import ttk
import threading as thr
import keyboard
import RecordMAK



window = tk.Tk()
window.title("Recording Mouse and Keyboard")
window.geometry("400x500")

record = RecordMAK.KeyAndMouse()

style = ttk.Style()
style.configure("my.TButton", font=('Helvetica', 20), width=20)

frame1 = tk.Frame(window, bg="grey")
frame1.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.2, anchor='n')
inner_frame1 = tk.Frame(frame1, bg="white")
inner_frame1.pack(expand=True, fill=tk.BOTH, padx=7.5, pady=7.5)

button1 = ttk.Button(inner_frame1, text="Start Recording(F5)", style="my.TButton",command=record.StartRecordMAK)
button1.place(relx=0.5, rely=0.25, anchor='center')


button2 = ttk.Button(inner_frame1, text="Stop Recording(F6)",style="my.TButton",command=record.StopRecordMAK)
button2.place(relx=0.5, rely=0.75, anchor='center')


frame2 = tk.Frame(window, bg="grey")
frame2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.2, anchor='n')
inner_frame2 = tk.Frame(frame2, bg="white")
inner_frame2.pack(expand=True, fill=tk.BOTH, padx=7.5, pady=7.5)
button = ttk.Button(inner_frame2, text="Start Auto Clicker(F2)", style="my.TButton",command=record.StartAutoClicker)
button.pack()
ttk.Button(inner_frame2, text="Stop Auto Clicker(F3)", style="my.TButton",command=record.StopAutoClicker).pack()

frame35 = tk.Frame(window, bg="grey")
frame35.place(relx=0.5, rely=0.55, relwidth=0.75, relheight=0.1, anchor='n')
inner_frame35 = tk.Frame(frame35, bg="white")
inner_frame35.pack(expand=True, fill=tk.BOTH, padx=6.5, pady=6.5) 

button = ttk.Button(inner_frame35, text="Save to file (Shit+S)", style="my.TButton",command=record.save_to_file)
button.pack()

frame3 = tk.Frame(window, bg="grey")
frame3.place(relx=0.3, rely=0.75, relwidth=0.35, relheight=0.1, anchor='n')
inner_frame3 = tk.Frame(frame3, bg="white")
inner_frame3.pack(expand=True, fill=tk.BOTH, padx=6.5, pady=6.5)  

button = ttk.Button(inner_frame3, text="Start(F8)", style="my.TButton",command=record.PlayingRecordMAK)
button.pack()
frame4 = tk.Frame(window, bg="grey")
frame4.place(relx=0.7, rely=0.75, relwidth=0.35, relheight=0.1, anchor='n')
inner_frame4 = tk.Frame(frame4, bg="white")
inner_frame4.pack(expand=True, fill=tk.BOTH, padx=6.5, pady=6.5)  

button = ttk.Button(inner_frame4, text="Stop(F9)", style="my.TButton",command=record.StopPlayingRecordMAK)
button.pack()

def StartRecording():
    while not keyboard.wait('f5'):
        record.StartRecordMAK()
def StopRecording():
    while not keyboard.wait('f6'):
        record.StopRecordMAK()
def StartPlaying():
    while not keyboard.wait('f8'):
        record.PlayingRecordMAK()     
def StartAutoclick():
    while not keyboard.wait('f2'):
        record.StartAutoClicker()            
def SaveToFile():
    while not keyboard.wait('shift+s'):
        record.save_to_file()    
def StopAutoclick():
    while not keyboard.wait('f3'):
        record.StopAutoClicker()
def StopPlaying():
    while not keyboard.wait('f9'): 
        record.StopPlayingRecordMAK()

thr.Thread(target=StopAutoclick).start()
thr.Thread(target=StopPlaying).start()               

thr.Thread(target=StartRecording).start()
thr.Thread(target=StopRecording).start()
thr.Thread(target=StartPlaying).start()
thr.Thread(target=StartAutoclick).start()
thr.Thread(target=SaveToFile).start()

window.mainloop()



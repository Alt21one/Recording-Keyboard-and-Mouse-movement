import keyboard as key
import mouse as mouselib
import threading as thr
import time
import os 


class KeyAndMouse:
    KEYLOGS_FILE_PATH = "!keylogs.txt"

    def __init__(self):
        self.mouse_events = []
        self.recorded = None
        self.autoclicker_running = False
        self.Recording_running = False

    def StartRecordMAK(self):
        print("Start recording")
        mouselib.hook(self.mouse_events.append)
        key.start_recording()  

    def StopRecordMAK(self):
        try:
            self.recorded = key.stop_recording()
            mouselib.unhook(self.mouse_events.append)
            print("stop recording")
        except ValueError as e:
            print("You need to Start Recording Before Stoping the Recording")    

    def GetMouseRecording(self):      
        return self.mouse_events
    
    def GetKeyboardRecording(self):     
        return self.recorded
    
    def save_to_file(self):
        with open(self.KEYLOGS_FILE_PATH, 'w+') as f:
            f.write(str(self.GetKeyboardRecording()) + os.linesep)
            print("It Been Save Successfully")

    def play_keyboard(self):
        key.play(self.GetKeyboardRecording())
                 
    def play_mouse(self):
        time.sleep(0.75)
        mouselib.play(self.GetMouseRecording())

    def StartAutoClicker(self):
        self.autoclicker_running = True 
        while self.autoclicker_running:
              mouselib.click(mouselib.LEFT)
              time.sleep(0.01)         

    def StopAutoClicker(self):
          self.autoclicker_running = False
          print("The AutoClicker Have been Stopped")     
           
    def PlayingRecordMAK(self):
       self.Recording_running = True
       while self.Recording_running:
            if self.recorded is None and self.mouse_events == []:
                print("No keystrokes Or Mouse movement have been recorded.")
                return    
            t1 = thr.Thread(target=self.play_mouse)
            t1.start()
            self.play_keyboard()
            time.sleep(0.1)  

    def StopPlayingRecordMAK(self):
         self.Recording_running = False       
         print("The Recording Have been Stopped")   

            



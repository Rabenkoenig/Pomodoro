import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# try --> versucht funktion auszuführen. Wenn nicht möglich führe except aus.
# hier wird versucht sowohl Tkinter als auch tkinter zu importieren.

import time
import winsound

frequency = 350  # Set Frequency To 2500 Hertz
duration = 5000  # Set Duration To 1000 ms == 1 second


x=0
y=True
class Clock:
    # init wird immer ausgeführt, wenn Klasse instanziert wird.
    def __init__(self):
        # erstellen eines rootWindows auf die Variable root
        self.root = customtkinter.CTk()
        self.root.title("Pomodoro")
        self.root.geometry("300x100")
        self.root.grid_columnconfigure((0), weight=1)
        # erstellen eines LabelWidgets auf die Variable label. eigenschaften siehe unten
        self.label = customtkinter.CTkLabel(master=self.root, text="", font=("Helvetica", 54))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        # rufe funktion update clock auf --> aktualisiere den Text und damit die Uhrzeit
        self.updateClock()
        # run forever
        self.root.mainloop()

    def updateClock(self):
        global x
        arbeitInMin = 25;
        pauseInMin = 5;
        # diese variable Entspricht der aktuellen zeit im Format HH:MM:SS
        now = time.strftime("%H:%M:%S", time.gmtime(x))    
        #aktualisiert den text des LabelWidgets
        self.label.configure(text=now, text_color = ("white"))
        x+=1
        # self.root.after(1000, self.update_clock) ruft die Funktion selbst nach 1000 ms auf, 
        # daher wird die update_clock() Funktion im Intervall von 1000 ms ausgeführt 
        # und zeigt die aktuelle Zeit im Tkinter-Label an.
        if y :
             self.label.configure(text=now, text_color = ("white"))
        else:
             self.label.configure(text=now, text_color = ("red"))
        if x==arbeitInMin*60+1 and y:
            self.resetClock()
            winsound.Beep(frequency, duration)    
        if x ==pauseInMin*60+1 and not(y):
            self.resetClock()
            winsound.Beep(frequency, duration)
        self.root.after(1000, self.updateClock)
    def resetClock(self):
            global x
            global y
            x=0
            y = not(y)

        

app = Clock()
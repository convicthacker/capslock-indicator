import tkinter as tk
import ctypes

class CapsLockIndicator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Caps Lock Indicator")
        
        self.label = tk.Label(self.root, text="Caps Lock: ")
        self.label.pack()
        
        self.update_indicator()
        
        self.root.after(100, self.check_caps_lock)
        self.root.mainloop()
        
    def check_caps_lock(self):
        self.update_indicator()
        self.root.after(100, self.check_caps_lock)
        
    def update_indicator(self):
        if ctypes.windll.user32.GetKeyState(0x14) & 1:
            self.label.config(text="Caps Lock: ON")
        else:
            self.label.config(text="Caps Lock: OFF")

if __name__ == "__main__":
    CapsLockIndicator()

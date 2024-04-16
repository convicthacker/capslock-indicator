import tkinter as tk
import ctypes

class CapsLockIndicator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Caps Lock Indicator")
        self.root.geometry("140x60")  # Set initial window size
        self.root.minsize(100, 50)  # Set minimum window size
        
        # Make the window stay on top
        self.root.wm_attributes("-topmost", True)
        
        # Remove default title bar
        self.root.overrideredirect(True)
        
        # Set dark mode background color
        self.root.configure(bg="#1E1E1E")
        
        # Caps Lock indicator label
        self.font_size = 12
        self.label = tk.Label(self.root, text="Caps Lock: ", bg="#1E1E1E", fg="white", font=("Helvetica", self.font_size))
        self.label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label
       
        self.update_indicator()
        
        # Make the window draggable
        self.draggable(self.root)
        
        # Add lock button
        self.locked = False
        self.lock_button = tk.Button(self.root, text="•", font=("Helvetica", 12), bg="green", fg="white", bd=0, command=self.toggle_lock)
        self.lock_button.place(relx=1, rely=0, anchor="ne")
        
        # Make the window resizable
        self.root.bind("<Configure>", self.on_resize)
        
        self.root.after(100, self.check_caps_lock)
        self.root.mainloop()
        
    def check_caps_lock(self):
        self.update_indicator()
        self.root.after(100, self.check_caps_lock)
        
    def update_indicator(self):
        if ctypes.windll.user32.GetKeyState(0x14) & 1:
            self.label.config(text="Caps Lock: ON", font=("Helvetica", self.font_size))
        else:
            self.label.config(text="Caps Lock: OFF", font=("Helvetica", self.font_size))
            
    def draggable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)
        
    def on_drag_start(self, event):
        if not self.locked:
            self.root._drag_start_x = event.x
            self.root._drag_start_y = event.y
        
    def on_drag_motion(self, event):
        if not self.locked:
            x = self.root.winfo_x() + event.x - self.root._drag_start_x
            y = self.root.winfo_y() + event.y - self.root._drag_start_y
            self.root.geometry("+%s+%s" % (x, y))
            
    def toggle_lock(self):
        self.locked = not self.locked
        if self.locked:
            self.lock_button.config(bg="red")
        else:
            self.lock_button.config(bg="green")
            
    def on_resize(self, event):
        width = event.width
        height = event.height
        self.font_size = max(int(min(width, height) / 7), 8)  # Adjust font size proportionally to the window size
        self.label.config(font=("Helvetica", self.font_size))

if __name__ == "__main__":
    CapsLockIndicator()

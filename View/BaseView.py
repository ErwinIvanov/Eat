import tkinter as tk
from tkinter import ttk

class BaseView:

    foreground_color = "#CA3E47"
    background_color = "#313131"
    header_font = ("Arial", 50)
    secondary_font = ("Arial", 35)
    secondary_foreground_color = "#d9d9d9"
    button_font = ("Arial", 45)
    active_background_color = "#313131"


    def __init__(self, parent):
        self.parent = parent
        style = ttk.Style()
        style.theme_use("vista")
        style.configure("Treeview", background="#525252", fieldbackground="#525252", foreground="#ffffff" ,borderwidth=0)  
        style.map("Treeview", background=[("selected", "#181818")])  


    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    
    def create_label(self, text):
        label = tk.Label(self.parent, text=text, font=self.header_font, fg=self.foreground_color, bg=self.background_color)
        return label
    
    def create_secondary_label(self, text):
        label = tk.Label(self.parent, text=text, font=self.secondary_font, fg=self.secondary_foreground_color, bg=self.background_color)
        return label
    
    def create_button(self, text, command=None):
        button_style = {"font": self.button_font, "foreground": self.foreground_color, "background": self.background_color, "activebackground": self.active_background_color, "border": 0}
        button = tk.Button(self.parent, text=text, command=command, **button_style)
        return button
    
    def create_divider(self):
        divider = ttk.Separator(self.parent, orient='horizontal')
        return divider
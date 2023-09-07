import tkinter as tk
from tkinter import ttk
from .BaseView import BaseView

class ShoppingListView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.generate_clipboard_message_callback = None
       
    def display_presentation(self):
        # Create a label for the section title
        section_title_label = self.create_label("Shopping List")
        section_title_label.pack(pady=10)

        # Create a horizontal separator
        divider = self.create_divider()
        divider.pack(fill='x', padx=50, pady=5)

        # Create a frame to hold the shopping list
        shopping_list_frame = tk.Frame(self.parent)
        shopping_list_frame.pack(pady=10)

        # Create a Treeview widget for the shopping list
        shopping_list_columns = ("Name", "Amount and Unit")
        self.shopping_list = ttk.Treeview(shopping_list_frame, columns=shopping_list_columns, show="headings", height=40)
        self.shopping_list.pack()

        # Set column headings for the shopping list
        for col in shopping_list_columns:
            self.shopping_list.heading(col, text=col)

        # Create a button to generate clipboard message
        button_style = {"font": ("Arial", 21), "foreground": "#CA3E47", "background": "#313131", "activebackground": "#313131", "border": 0}
        clipboard_button = tk.Button(self.parent, text="Generate Clipboard Message", command=self.generate_clipboard_message, **button_style)
        clipboard_button.pack(side=tk.LEFT, padx=565)
        
        
        
    def display_shopping_list(self, shopping_list_data):
        # Clear the existing items in the shopping list
        self.shopping_list.delete(*self.shopping_list.get_children())

        # Insert shopping list items and quantities
        for item, quantity in shopping_list_data:
            self.shopping_list.insert("", "end", values=(item, quantity))
            
            
    # Set the callback function for generating clipboard message
    def set_generate_clipboard_message_callback(self, callback):

        self.generate_clipboard_message_callback = callback
        
        
 # Call the callback function to generate clipboard message
    def generate_clipboard_message(self):

        if self.generate_clipboard_message_callback:
            self.generate_clipboard_message_callback()

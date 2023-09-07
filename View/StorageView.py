import tkinter as tk
from tkinter import ttk
from typing import Any, Callable
from .BaseView import BaseView


class StorageView(BaseView):
    def __init__(self, parent):
        # Initialize the StorageView
        super().__init__(parent)

        # Initialize callback placeholders for adding and deleting items
        self.add_item_callback = None
        self.delete_item_callback = None

    # Display the main presentation of the storage section
    def display_presentation(self):
        section_title_label = self.create_label("Storage")
        section_title_label.pack(pady=10)

        # Create a horizontal separator
        self.create_divider().pack(fill="x", padx=50, pady=5)

        # Create a frame for the table
        table_frame = tk.Frame(self.parent)
        table_frame.pack(pady=10)

        # Create a Treeview widget for the table
        table_columns = ("Item", "Quantity")
        self.table = ttk.Treeview(
            table_frame, columns=table_columns, show="headings", height=40
        )
        self.table.pack()

        # Set column headings for the table
        for col in table_columns:
            self.table.heading(col, text=col)

        # Create a frame for the "Add Item" and "Delete Item" buttons
        button_frame = tk.Frame(self.parent, bg="#313131")
        button_frame.pack(fill="x", pady=10, padx=125)

        # Create an "Add Item" button
        add_item_button = self.create_button("+", command=self.add_item_popup)
        add_item_button.pack(side=tk.RIGHT, padx=10)

        # Create a "Delete Item" button
        delete_button = self.create_button(
            "-", command=lambda: self.on_delete_button_click()
        )
        delete_button.pack(side=tk.RIGHT, padx=25)


    # Create a new popup window to add items
    def add_item_popup(self):

        popup_window = tk.Toplevel(self.parent)

        popup_window.title("Add Item")
        popup_window.geometry("400x200")

        self.center_window(popup_window, 400, 200)

        popup_window.configure(bg="#313131")

        item_name_label = tk.Label(
            popup_window,
            text="Item Name:",
            font=("Arial", 14),
            fg="#CA3E47",
            bg="#313131",
        )
        item_name_label.pack()
        item_name_entry = tk.Entry(
            popup_window, font=("Arial", 12), bg="#525252", fg="#ffffff", border=0
        )
        item_name_entry.pack()

        quantity_label = tk.Label(
            popup_window,
            text="Quantity:",
            font=("Arial", 14),
            fg="#CA3E47",
            bg="#313131",
        )
        quantity_label.pack()
        quantity_entry = tk.Entry(
            popup_window, font=("Arial", 12), bg="#525252", fg="#ffffff", border=0
        )
        quantity_entry.pack()

        add_button = tk.Button(
            popup_window,
            text="Add",
            font=("Arial", 20),
            foreground="#CA3E47",
            background="#525252",
            activebackground="#414141",
            border=0,
            command=lambda: self.on_add_button_click(
                item_name_entry.get(), quantity_entry.get()
            ),
        )
        add_button.pack(pady=10)

        self.error_label = tk.Label(
            popup_window, text="", font=("Arial", 10), fg="#c50000", bg="#313131"
        )
        self.error_label.pack()
        
    # Display an error message in the error label
    def display_error(self, message):

        self.error_label.config(text=message, fg="#c50000")

    #display the storage data to the treeview
    def display_storage_data(self, storage_data):

        table = self.table
        for item in table.get_children():
            table.delete(item)

        storage_data_dict = dict(storage_data)

        for item_name, quantity in storage_data_dict.items():
            table.insert("", "end", values=(item_name, quantity))

    # Add Item Bindings/Methods
    def on_add_button_click(self, item_name, quantity):

        if self.add_item_callback is not None:
            self.add_item_callback(item_name, quantity)

    def set_add_item_callback(self, callback: Callable[[str, str], None]) -> None:
        self.add_item_callback = callback

    # Delete Item Bindings/Methods
    def on_delete_button_click(self):

        selected_item = self.table.focus()

        if selected_item:
          
            values = self.table.item(selected_item, "values")
            if values:
                item_name = values[0]
                if self.delete_item_callback is not None:
                    self.delete_item_callback(item_name)

    def set_delete_item_callback(self, callback: Callable[[str], None]) -> None:
        self.delete_item_callback = callback

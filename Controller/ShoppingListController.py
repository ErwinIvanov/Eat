import os
import pyperclip

class ShoppingListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data_file_path = os.path.join(os.path.dirname(__file__), "shoppinglist_data.json")
        self.view.set_generate_clipboard_message_callback(self.generate_clipboard_message)
        
    def generate_clipboard_message(self):
            pyperclip.copy(self.model.clipboard_message)
            
    def run(self) -> None:
        self.view.display_presentation()
        self.view.display_shopping_list(self.model.shopping_list_data)
       

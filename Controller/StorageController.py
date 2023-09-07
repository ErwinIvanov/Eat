
import os

class StorageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data_file_path = os.path.join(os.path.dirname(__file__), "storage_data.json")
        self.view.set_add_item_callback(self.add_item)
        self.view.set_delete_item_callback(self.delete_item)



    def add_item(self, item_name, quantity):
        # Check if both fields are filled
        if not item_name or not quantity:
            self.view.display_error("Both item name and quantity are required.")
            return
        # Check if quantity is a number and not negative
        try:
            quantity = float(quantity)
            if quantity < 0:
                raise ValueError
        except ValueError:
            self.view.display_error("Quantity must be a positive number.")
            return
        
        # If the data is valid, add the item to storage
        self.model.add_item_to_storage(item_name, quantity)
        self.view.display_storage_data(self.model.get_storage_list())
        self.model.save_to_json(self.data_file_path)

    def delete_item(self, item_name):
        self.model.remove_item_from_storage(item_name)
        self.view.display_storage_data(self.model.get_storage_list())
        self.model.save_to_json(self.data_file_path)

    def load_data(self):
        self.model.load_from_json(self.data_file_path)
        self.view.display_storage_data(self.model.storage_data)

    def run(self) -> None:
        self.view.display_presentation()
        self.load_data()
        self.view.display_storage_data(self.model.storage_data)
        
       
        
    

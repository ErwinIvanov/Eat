import json
import os

class StorageModel:
    def __init__(self):
        self.storage_data = {}

    #Storage Operations
    def add_item_to_storage(self, item_name, quantity):
        if item_name in self.storage_data:
            self.storage_data[item_name] += quantity
        else:
            self.storage_data[item_name] = quantity
            
    def remove_item_from_storage(self, item_name):
                del self.storage_data[item_name]

    #read Storage
    def get_storage_list(self):
        return self.storage_data.items()
    
    #Json methods
    def save_to_json(self, file_path):
        
        with open(file_path, 'w') as file:
            json.dump(self.storage_data, file)

    def load_from_json(self, file_path):
        try:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, 'r') as file:
                    self.storage_data = json.load(file)
            else:
                self.storage_data = {}
        except json.JSONDecodeError:
            self.storage_data = {}

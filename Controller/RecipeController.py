import os

class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_add_item_callback(self.add_recipe)
        self.view.set_delete_item_callback(self.delete_recipe)
        self.view.set_add_to_weeklyplan_callback(self.add_to_Weekly_pool)
        
        self.data_file_path = os.path.join(os.path.dirname(__file__), "recipe_data.json")
        
        
    def add_to_Weekly_pool(self, recipe):
        name = recipe.get("name", "")
        ingredients = recipe.get("ingredients", [])
        link = recipe.get("link", "")
        self.model.add_recipe_to_weeklyplan_pool(name, ingredients, link)
        self.model.save_to_json(self.data_file_path)

    def add_recipe(self, name, ingredients, link):
        self.model.add_recipe(name, ingredients, link)
        self.view.display_recipe_data(self.model.recipes)
        self.model.save_to_json(self.data_file_path)

    def delete_recipe(self, name):
        self.model.remove_recipe(name)
        self.view.display_recipe_data(self.model.recipes)
        self.model.save_to_json(self.data_file_path)

    def load_data(self):
        self.model.load_from_json(self.data_file_path)
        self.view.display_recipe_data(self.model.recipes)

    def run(self) -> None:
        self.view.display_presentation()
        self.load_data()



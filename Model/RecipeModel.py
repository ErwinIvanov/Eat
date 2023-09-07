import json

class RecipeModel:

    def __init__(self):
        self.recipes = [] 
        self.weekly_plan_pool_recipe = [] 
        
        
    #Weekly Plan Recipe Pool
    def add_recipe_to_weeklyplan_pool(self, name, ingredients, link):
        recipe = {
            "name": name,
            "ingredients": ingredients,
            "link": link
        }
        self.weekly_plan_pool_recipe.append(recipe)
        
    def get_weekly_plan_pool_recipe(self):
        return self.weekly_plan_pool_recipe
        
    # Recipe Operations
    def add_recipe(self, name, ingredients, link):
        recipe = {
            "name": name,
            "ingredients": ingredients,
            "link": link
        }
        self.recipes.append(recipe)

    def remove_recipe(self, name):
        self.recipes = [recipe for recipe in self.recipes if recipe["name"] != name]
        

    #JSON methods
    def save_to_json(self, file_path):
        data = {
            "recipes": self.recipes,
            "weekly_plan_pool_recipe": self.weekly_plan_pool_recipe
        }
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            self.recipes = data.get("recipes", [])
            self.weekly_plan_pool_recipe = data.get("weekly_plan_pool_recipe", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.recipes = []
            self.weekly_plan_pool_recipe = []

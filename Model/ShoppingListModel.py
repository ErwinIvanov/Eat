
class ShoppingListModel:
    def __init__(self, recipe_model, storage_model, weeklyplan_model):
         self.used_recipes = weeklyplan_model.assignments
         self.storage_data = storage_model.storage_data
         self.recipes = recipe_model.weekly_plan_pool_recipe
         self.shopping_list_data = self.__generate_shopping_list(self.used_recipes, self.storage_data, self.recipes )
         
         self.clipboard_message = self.generate_clipboard_message()


    def __generate_shopping_list(self, used_recipes, storage_data, recipes):
        # Get all recipe names
        recipe_names = [recipe_name for recipe_name in used_recipes.values() if recipe_name != 'None']

        # Calculate recipe ingredients based on names
        ingredients_needed = {}
        for recipe_name in recipe_names:
            recipe = next((item for item in recipes if item["name"] == recipe_name), None)
            if recipe:
                recipe_ingredients = recipe["ingredients"]
                for ingredient in recipe_ingredients:
                    if ingredient in ingredients_needed:
                        ingredients_needed[ingredient] += 1
                    else:
                        ingredients_needed[ingredient] = 1
        
        # Calculate items to buy
        shopping_list = []
        for ingredient, quantity_needed in ingredients_needed.items():
            if ingredient not in storage_data:
                shopping_list.append((ingredient, quantity_needed))
            elif storage_data[ingredient] < quantity_needed:
                shopping_quantity = quantity_needed - storage_data[ingredient]
                shopping_list.append((ingredient, shopping_quantity))
        return shopping_list
    
    def generate_clipboard_message(self, ):
        message = "Shopping List:\n\n"
        
        for item_name, amount in self.shopping_list_data:
            message += f"{item_name}: {amount}\n"
        
        return message


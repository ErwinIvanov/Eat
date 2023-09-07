import json

class WeeklyPlanModel:
    def __init__(self, recipe_model):
        self.recipe_model = recipe_model
        self.assignments = {day: None for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    def get_weekly_plan_pool_recipe(self):
        return self.recipe_model.get_weekly_plan_pool_recipe()
    
     # update day assignments
    def set_day_assignment(self, day, recipe_name):
        self.assignments[day] = recipe_name
        
    #  get day assignments
    def get_day_assignments(self):
        return self.assignments
    
     # JSON methods
    def save_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.assignments, file)
            
    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.assignments = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.assignments = {}
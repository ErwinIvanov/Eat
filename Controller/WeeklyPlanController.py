
import os

class WeeklyPlanController:
    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.view.set_update_assignment_callback(self.update_assignment)
        self.data_file_path = os.path.join(os.path.dirname(__file__), "weeklyplan_data.json")
        
        
    def update_assignment(self, day, recipe_name):
        self.model.set_day_assignment(day, recipe_name)
        self.model.save_to_json(self.data_file_path)
        
    def run(self):
        self.model.load_from_json(self.data_file_path)
        self.view.display_presentation(self.model.get_weekly_plan_pool_recipe()) 
        self.view.update_day_assignments(self.model.assignments)
       
        
        

class OverviewController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        
        assignments = self.model.get_weekly_overview_recipes()
        self.view.display_presentation()
        self.view.display_assignments(assignments)

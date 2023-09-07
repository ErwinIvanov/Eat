class OverviewModel:
    def __init__(self, weeklyplan_model):
        self.weeklyplan_model = weeklyplan_model

    def get_weekly_overview_recipes(self):
        return self.weeklyplan_model.get_day_assignments()


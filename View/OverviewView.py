import tkinter as tk
import datetime
from .BaseView import BaseView

class OverviewView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)

    def display_presentation(self):
        # Create a label for the section title
        section_title_label = self.create_label("Overview")
        section_title_label.pack(pady=10)

        # Create a horizontal separator (divider) with the custom style
        divider = self.create_divider()
        divider.pack(fill='x', padx=50, pady=5)

        # Create a label to display the date range for this week
        date_range_label = self.create_secondary_label("Recipes for " + self.get_current_week_range())
        date_range_label.pack(pady=50)


    def get_current_week_range(self):
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        sunday = monday + datetime.timedelta(days=6)
        return f"Plan for {monday.strftime('%d %B')} - {sunday.strftime('%d %B')}"
    
    
    def display_assignments(self, assignments):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Create a frame to hold the labels
        labels_frame = tk.Frame(self.parent, bg="#313131")
        labels_frame.pack(pady=50,padx=600, fill="both", expand=True)


        for day in days_of_week:
            recipe_name = assignments.get(day, "None")

            day_label_text = f"{day}:"
            recipe_label_text = recipe_name if recipe_name is not None else "None"

            day_label = tk.Label(
                labels_frame,
                text=day_label_text,
                font=("Arial", 14, "bold"),
                fg="#ffffff",
                bg="#313131",
                anchor="w",
                padx=10,
                pady=5
            )

            recipe_label = tk.Label(
                labels_frame,
                text=recipe_label_text,
                font=("Arial", 12),
                fg="#CA3E47",  # Recipe color
                bg="#313131",
                anchor="w",
                padx=10,
                pady=5,
            )

            day_label.grid(row=days_of_week.index(day), column=0, sticky="w")
            recipe_label.grid(row=days_of_week.index(day), column=1, sticky="w")

        # Center the labels frame within the parent window
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)








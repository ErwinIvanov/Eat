import tkinter as tk
import datetime
from .BaseView import BaseView

class WeeklyPlanView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
        self.day_dropdowns = {}
        self.update_assignment_callback = None

    # Display the main presentation section and its content
    def display_presentation(self, recipe_list):
        # Create a label for the section title
        section_title_label = self.create_label("Weekly Plan")
        section_title_label.pack(pady=10)

        # Create a horizontal separator
        divider = self.create_divider()
        divider.pack(fill="x", padx=50, pady=5)
        
        # Create a frame to hold the listbox
        listbox_frame = tk.Frame(self.parent)
        listbox_frame.pack(padx=50, pady=10)

        # Create a scrollbar for the listbox
        self.item_listbox = tk.Listbox(
            listbox_frame,
            width=50,
            height=20,
            font=("Arial", 12),
            fg="#ffffff",
            bg="#313131",
            borderwidth=0,
            selectbackground="#313131",
            selectmode=tk.SINGLE,
        )
        self.item_listbox.pack(fill=tk.BOTH, expand=True)

        # Populate the listbox with recipe names
        self.item_listbox.delete(0, tk.END)
        for recipe in recipe_list:
            self.item_listbox.insert(tk.END, recipe["name"])

        self.item_listbox.configure(justify=tk.CENTER)
        
        # Create a label for the current week
        current_week_label = tk.Label(
            self.parent,
            text=self.get_current_week_range(),
            font=("Arial", 35),
            fg="#ffffff",
            bg="#313131"
        )
        current_week_label.pack(padx=50, pady=100)

        # Create a frame for day assignments
        day_assignments_frame = tk.Frame(self.parent, width=300, height=200, bg="#313131")
        day_assignments_frame.pack(padx=50, pady=0)

        # Create labels for days of the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i, day in enumerate(days):
            day_label = tk.Label(day_assignments_frame, text=day, font=("Arial", 16, "bold"), fg="#ffffff", bg="#313131")
            day_label.grid(row=0, column=i, padx=10, pady=5)

        # Create dropdown menus for day assignments
        self.day_dropdowns = {}
        for i in range(len(days)):
            menu_var = tk.StringVar()
            dropdown = tk.OptionMenu(day_assignments_frame, menu_var, *["None"] + [recipe["name"] for recipe in recipe_list], command=lambda value, day=days[i]: self.update_assignment(day, value))
            dropdown.config(font=("Arial", 12), bg="#ffffff", fg="#313131", activebackground="#CA3E47", borderwidth=0, width=15)
            dropdown["menu"].config(font=("Arial", 12), bg="#ffffff", fg="#313131")
            dropdown.grid(row=1, column=i, padx=10, pady=5, sticky="ew")
            self.day_dropdowns[days[i]] = menu_var
            
            



    # Callback function to update a day's recipe assignment
    def update_assignment(self, day, recipe_name):
        if self.update_assignment_callback:
            self.update_assignment_callback(day, recipe_name)

    # Set the callback function for updating day assignments
    def set_update_assignment_callback(self, callback):
        self.update_assignment_callback = callback

    # Update the displayed day assignments
    def update_day_assignments(self, day_assignments):
        for day, recipe_name in day_assignments.items():
            if day in self.day_dropdowns:
                self.day_dropdowns[day].set(recipe_name)

    # Get the current week's date range
    def get_current_week_range(self):
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        sunday = monday + datetime.timedelta(days=6)
        return f"Plan for {monday.strftime('%d %B')} - {sunday.strftime('%d %B')}"

import tkinter as tk
from tkinter import ttk
from typing import Any, Callable
from .BaseView import BaseView


class RecipeView(BaseView):
    def __init__(self, parent):
        super().__init__(parent)
    
        # Initialize callback placeholders 
        self.add_item_callback = None
        self.delete_item_callback = None
        self.add_to_weekly_plan_callback = None
        
        
        #QOL
        # Initialize feedback label
        self.feedback_label = None 
        
        # Initialize the "Add to Weekly Plan" button state
        self.is_recipe_selected = False


    #display the main presentation section
    def display_presentation(self):
        # Create a label for the section title
        section_title_label = self.create_label("Recipes")
        section_title_label.pack(pady=10)

        # Create a horizontal separator
        divider = self.create_divider()
        divider.pack(fill="x", padx=50, pady=5)

        # Create a frame for the recipe list
        recipe_list_frame = tk.Frame(self.parent)
        recipe_list_frame.pack(pady=10)

        # Create a Treeview widget for the recipe list
        recipe_list_columns = ("Name", "Ingredients", "Link")
        self.recipe_list = ttk.Treeview(
            recipe_list_frame, columns=recipe_list_columns, show="headings", height=40
        )
        self.recipe_list.pack()

        # Set column headings for the recipe list
        for col in recipe_list_columns:
            self.recipe_list.heading(col, text=col)
            

        # Create a frame for the "Add Recipe" button
        button_frame = tk.Frame(self.parent, bg="#313131")
        button_frame.pack(fill="x", pady=10, padx=125)
        
        # Create a frame for the "Add Recipe to Weekly Plan" button
        button_frame_add_Weekly = tk.Frame(self.parent, bg="#313131", width=250)
        button_frame_add_Weekly.place(x=self.parent.winfo_width() - 100, y=150, anchor="ne")  # Place at top right

        # Create an "Add Item" button
        add_recipe_button = self.create_button("+", command=self.__add_recipe_popup)
        add_recipe_button.pack(side=tk.RIGHT, padx= 10)
        

        # Create a "Delete Item" button
        delete_button = self.create_button(
            "-", command=lambda: self.on_delete_button_click()
        )
        delete_button.pack(side=tk.RIGHT, padx=25)
        
        self.feedback_label = tk.Label(
            self.parent, text="", font=("Arial", 12), fg="#00FF00", bg="#313131", width=500
        )
        self.feedback_label.pack(pady=0, padx=150)
        
       # Create an "Add Recipe to Weekly Plan" button
        self.add_to_weekly_plan_button = tk.Button(
            button_frame_add_Weekly,
            text="Add to Weekly Plan",
            font=("Arial", 15),
            fg="#CA3E47",
            bg="#525252",
            activebackground="#414141",
            border=0,
            width=25,
            command=self.on_add_to_weekly_plan_click,
            state=tk.DISABLED
        )
        self.add_to_weekly_plan_button.pack(padx=10, pady=15)
        
        # Bind the selection change event to the on_recipe_list_selection method
        self.recipe_list.bind("<<TreeviewSelect>>", self.on_recipe_list_selection)  


    def __add_recipe_popup(self):
        # Create a new popup window for adding a recipe
        popup_window = tk.Toplevel(self.parent)

        # Set the title and size
        popup_window.title("Add Recipe")
        popup_window.geometry("600x400")

        # Center the popup window on the screen
        self.center_window(popup_window, 600, 400)

        # Set the background color for the popup window
        popup_window.configure(bg="#313131")

        # Create labels and entry fields for recipe details
        name_label = tk.Label(
            popup_window, text="Name:", font=("Arial", 14), fg="#CA3E47", bg="#313131"
        )
        name_label.pack()
        name_entry = tk.Entry(
            popup_window,
            font=("Arial", 12),
            bg="#525252",
            fg="#ffffff",
            border=0,
            width=35,
        )
        name_entry.pack(pady=5)

        ingredients_label = tk.Label(
            popup_window,
            text="Ingredients:",
            font=("Arial", 14),
            fg="#CA3E47",
            bg="#313131",
        )
        ingredients_label.pack()
        ingredients_entry = tk.Text(
            popup_window,
            font=("Arial", 12),
            bg="#525252",
            fg="#ffffff",
            border=0,
            wrap="word",
            height=10,
            width=55,
        )
        ingredients_entry.pack(pady=5)

        link_label = tk.Label(
            popup_window, text="Link:", font=("Arial", 14), fg="#CA3E47", bg="#313131"
        )
        link_label.pack()
        link_entry = tk.Entry(
            popup_window,
            font=("Arial", 12),
            bg="#525252",
            fg="#ffffff",
            border=0,
            width=45,
        )
        link_entry.pack(pady=5)

        # Add a button to add the recipe at the bottom of the popup window
        add_recipe_button = tk.Button(
            popup_window,
            text="Add Recipe",
            font=("Arial", 14),
            fg="#CA3E47",
            bg="#525252",
            activebackground="#414141",
            border=0,
            command=lambda: self.on_add_button_click(
                name_entry.get(),
                ingredients_entry.get("1.0", tk.END).splitlines(),
                link_entry.get(),
    ),
)
        add_recipe_button.pack(pady=10)
    
        
    #display the recipe data to the treeview
    def display_recipe_data(self, recipe_data):
        
        table = self.recipe_list
        table.delete(*table.get_children())  
        
        for recipe in recipe_data:
            name = recipe.get("name", "")
            ingredients = ", ".join(recipe.get("ingredients", []))
            link = recipe.get("link", "")
            table.insert("", "end", values=(name, ingredients, link))
            
    # Add Item Bindings/Methods
    def on_add_button_click(self, name, ingredients, link):
        if self.add_item_callback is not None:
            self.add_item_callback(name, ingredients, link)
            
    def set_add_item_callback(self, callback: Callable[[str, list, str], None]) -> None:
        self.add_item_callback = callback


   # Delete Item Bindings/Methods
    def on_delete_button_click(self):
        # Handle the "Delete Item" button click event
        selected_item = self.recipe_list.focus()
        if selected_item:
            values = self.recipe_list.item(selected_item, "values")
            if values:
                item_name = values[0]  
                if self.delete_item_callback is not None:
                    self.delete_item_callback(item_name)

   
    def set_delete_item_callback(self, callback: Callable[[str], None]) -> None:
        self.delete_item_callback = callback
        
        
    #WeeklyPlan Bidnings/methods
    def on_add_to_weekly_plan_click(self):
        selected_item = self.recipe_list.focus()
        if selected_item:
            values = self.recipe_list.item(selected_item, "values")
            if values:
                recipe_name, ingredients, link = values
                recipe = {
                    "name": recipe_name,
                    "ingredients": ingredients.split(", "),
                    "link": link,
                }
                if self.add_to_weekly_plan_callback is not None:
                    self.add_to_weekly_plan_callback(recipe)
                
                    #Set feedback message
                    self.set_feedback_message(f"Recipe '{recipe_name}' added to Weekly Plan!")
                    
                     # Deselect the current item
                    self.recipe_list.selection_remove(selected_item)

                    # Update button state
                    self.update_add_to_weekly_plan_button_state()

    def set_add_to_weeklyplan_callback(self, callback: Callable[[dict], None]) -> None:
     self.add_to_weekly_plan_callback = callback
    
    
    #qol stuff
    def set_feedback_message(self, message):
     if self.feedback_label.winfo_exists():
            self.feedback_label.config(text=message)
            self.parent.after(3000, lambda: self.clear_feedback_message())
            
    def clear_feedback_message(self):
        if self.feedback_label.winfo_exists():
            self.feedback_label.config(text="")
        
    def on_recipe_list_selection(self, event):
        selected_item = self.recipe_list.focus()
        if selected_item:
            self.is_recipe_selected = True
        else:
            self.is_recipe_selected = False
        self.update_add_to_weekly_plan_button_state()
        
    def update_add_to_weekly_plan_button_state(self):
        if self.is_recipe_selected:
            self.add_to_weekly_plan_button.config(state=tk.NORMAL)
        else:
            self.add_to_weekly_plan_button.config(state=tk.DISABLED)
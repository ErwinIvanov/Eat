import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

#View imports
from View.OverviewView import OverviewView
from View.StorageView import StorageView
from View.RecipeView import RecipeView
from View.ShoppingListView import ShoppingListView
from View.WeeklyPlanView import WeeklyPlanView

#Model Imports
from Model.OverviewModel import OverviewModel
from Model.StorageModel import StorageModel
from Model.RecipeModel import RecipeModel
from Model.ShoppingListModel import ShoppingListModel
from Model.WeeklyPlanModel import WeeklyPlanModel

#Controller IMports
from Controller.OverviewController import OverviewController
from Controller.StorageController import StorageController
from Controller.RecipeController import RecipeController
from Controller.ShoppingListController import ShoppingListController
from Controller.WeeklyPlanController import WeeklyPlanController


# Same instances for data storage
recipe_model = RecipeModel()
weeklyplan_model = WeeklyPlanModel(recipe_model)
stroage_model = StorageModel()

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


# Function to clear the window on the screen
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to switch to the Overview section
def show_overview(content_frame):
    clear_frame(content_frame)
    model = OverviewModel(weeklyplan_model)
    view = OverviewView(content_frame)
    controller = OverviewController(model, view)
    controller.run()

# Function to switch to the WeeklyPlan section
def show_weeklyplan(content_frame):
    clear_frame(content_frame)
    view = WeeklyPlanView(content_frame)
    controller = WeeklyPlanController(weeklyplan_model, view)
    controller.run()

# Function to switch to the Recipe section
def show_recipe(content_frame):
    clear_frame(content_frame)
    view = RecipeView(content_frame)
    controller = RecipeController(recipe_model, view)
    controller.run()

# Function to switch to the Storage section
def show_storage(content_frame):
    clear_frame(content_frame)
    view = StorageView(content_frame)
    controller = StorageController(stroage_model, view)
    controller.run()

# Function to switch to the ShoppingList section
def show_shoppingList(content_frame):
    clear_frame(content_frame)
    model = ShoppingListModel( recipe_model, stroage_model, weeklyplan_model)
    view = ShoppingListView(content_frame)
    controller = ShoppingListController(model, view)
    controller.run()

def main():
    #basic setup
    root = tk.Tk()
    root.title("Eat App")
    root.configure(background="#313131")
    root.resizable(width=False, height=False)
    window_width, window_height = 1920, 1080
    center_window(root, window_width, window_height)

    icon_image = Image.open("img/mainicon.png") 
    icon_image = icon_image.resize((75, 75), Image.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_image)
    
    main_menu_frame = tk.Frame(root)
    main_menu_frame = tk.Frame(root, bg="#313131")
    main_menu_frame.pack(side=tk.LEFT, fill=tk.Y)
    content_frame = tk.Frame(root, bg="#313131")
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    app_name_label = ttk.Label(main_menu_frame, text="Eat App", image=icon_photo, compound=tk.TOP, font=("Arial", 50), foreground="#CA3E47", background="#313131")
    app_name_label.pack(pady=10)
    button_width = 40
    button_height = 8
    button_font = "Arial", 12
    button_fg_color = "#CA3E47"
    button_bg_color = "#525252"  
    button_active_bg_color = "#414141"
    button_padx = 25
    button_pady = 10

    button_style = {"font": button_font, "foreground": button_fg_color, "background": button_bg_color, "highlightbackground": button_bg_color, "activebackground": button_active_bg_color, "border": 0}

    overview_button = tk.Button(main_menu_frame, text="Overview", command=lambda: show_overview(content_frame), width=button_width, height=button_height, **button_style)
    weekly_plan_button = tk.Button(main_menu_frame, text="Weekly Plan", command=lambda: show_weeklyplan(content_frame) , width=button_width, height=button_height, **button_style)
    recipes_button = tk.Button(main_menu_frame, text="Recipes", command=lambda: show_recipe(content_frame), width=button_width, height=button_height, **button_style)
    storage_button = tk.Button(main_menu_frame, text="Storage", command=lambda: show_storage(content_frame), width=button_width, height=button_height, **button_style)
    shopping_list_button = tk.Button(main_menu_frame, text="Shopping List", command=lambda: show_shoppingList(content_frame), width=button_width, height=button_height, **button_style)

    overview_button.pack(side=tk.TOP, pady=button_pady, padx=button_padx)
    weekly_plan_button.pack(side=tk.TOP, pady=button_pady, padx=button_padx)
    recipes_button.pack(side=tk.TOP, pady=button_pady, padx=button_padx)
    storage_button.pack(side=tk.TOP, pady=button_pady, padx=button_padx)
    shopping_list_button.pack(side=tk.TOP, pady=button_pady, padx=button_padx)


    root.mainloop()

if __name__ == "__main__":
    main()
 
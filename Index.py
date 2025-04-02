import json
import tkinter as tk
from tkinter import messagebox, ttk

# Load recipes from JSON file
try:
    with open("recipes.json", "r") as file:
        recipes = json.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "recipes.json file not found!")
    recipes = {}

# Function to display recipe details
def show_recipe():
    selected_index = recipe_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a recipe!")
        return
    recipe_name = recipe_listbox.get(selected_index)
    recipe = recipes.get(recipe_name, {})
    if recipe:
        recipe_text.set(
            f"\nRecipe for {recipe_name}:\n\n"
            f"Ingredients:\n" + "\n".join(f"- {item}" for item in recipe.get("ingredients", [])) +
            "\n\nSteps:\n" + "\n".join(f"- {step}" for step in recipe.get("steps", []))
        )
    else:
        recipe_text.set("Recipe details not found!")

# Tkinter UI setup
root = tk.Tk()
root.title("Recipe Selector")
root.geometry("600x600")
root.configure(bg="#f4f4f4")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=8)
style.configure("TLabel", font=("Arial", 11), background="#ffffff")

frame = tk.Frame(root, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame, text="Select a Recipe", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Add Scrollbar
list_frame = tk.Frame(frame)
list_frame.pack()

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
recipe_listbox = tk.Listbox(list_frame, height=15, width=50, font=("Arial", 11), yscrollcommand=scrollbar.set)
scrollbar.config(command=recipe_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
recipe_listbox.pack()

# Populate Listbox
for recipe in recipes.keys():
    recipe_listbox.insert(tk.END, recipe)

view_button = ttk.Button(frame, text="View Recipe", command=show_recipe)
view_button.pack(pady=10)

recipe_text = tk.StringVar()
recipe_label = ttk.Label(frame, textvariable=recipe_text, wraplength=550, justify="left")
recipe_label.pack(pady=10, padx=10)

root.mainloop()

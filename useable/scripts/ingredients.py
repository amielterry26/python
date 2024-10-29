"""
The goal of this application is to see if a particular ingredient is in a recipe.
This will be used for safety in a restaurant.
I need to define what the main meal is.
I need to define what the ingredients are in that meal.
I need to define what the allergy variable is.
I need to print a response to them telling me what they are allergic to.
"""
sandwich = ["bread", "cheese", "meat", "tomatoes", "lettuce"]

allergy = input("What are you allergic to? ")

if allergy in sandwich:
    print(f"You cannot eat this meal, it contains {allergy}.")
else:
    print("You can eat this meal.")

import pickle

# Step 2.1: Define a function to display a recipe
def display_recipe(recipe):
    # Step 2.1a: Print the recipe name
    print("\nRecipe:", recipe['name'])
    # Step 2.1b: Print the cooking time
    print("Cooking Time (min):", recipe['cooking_time'])
    # Step 2.1c: Print the ingredients
    print("Ingredients:", ", ".join(recipe['ingredients']))
    # Step 2.1d: Print the difficulty
    print("Difficulty:", recipe['difficulty'])



# Step 2.2: Define a function to search for an ingredient in the given data
def search_ingredient(data):
    # Step 2.2a: Show all available ingredients contained in data
    print("\nAvailable ingredients:")
    for idx, ingredient in enumerate(data['all_ingredients']):
        print(f"{idx}. {ingredient}")
    # Step 2.2b: Try block where the user picks a number from the list
    try:
        choice = int(input("Enter the number of the ingredient you want to search for: "))
        ingredient_searched = data['all_ingredients'][choice]
    except (ValueError, IndexError):
        # Step 2.2c: Warn the user if the input is incorrect
        print("Invalid input. Please try again.")
        return
    # Step 2.2d: Go through every recipe in data
    print(f"\nRecipes containing '{ingredient_searched}':")
    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)

            

# Step 2.3: Main code to search for recipes by ingredient
# Step 2.3a: Ask the user for the name of the file that contains the recipe data
filename = input("Enter the filename to search recipes: ")

# Step 2.3b: Try block to open the file and extract its contents
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    # Step 2.3c: Warn the user if the file hasn't been found
    print("File not found.")
except Exception as e:
    # Step 2.3d: Handle any other exceptions
    print("An error occurred:", e)
else:
    # Step 2.3e: Call search_ingredient function and pass data into it
    search_ingredient(data)

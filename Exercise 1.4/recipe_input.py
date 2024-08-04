import pickle

# Step 1.1: Define a function to take recipe details from the user
def take_recipe():
    # Step 1.1a: Prompt the user to enter the recipe name
    name = input("Enter the recipe name: ")
    # Step 1.1b: Prompt the user to enter the cooking time in minutes
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    # Step 1.1c: Prompt the user to enter the ingredients, separated by commas
    ingredients = input("Enter the ingredients (separated by commas): ").split(', ')
    # Step 1.1d: Calculate the difficulty of the recipe
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    
    # Step 1.1e: Store the recipe details in a dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    # Step 1.1f: Return the recipe dictionary
    return recipe



# Step 1.2: Define a function to calculate the difficulty of the recipe
def calc_difficulty(cooking_time, num_ingredients):
    # Step 1.2a: Determine difficulty based on cooking time and number of ingredients
    if cooking_time < 10 and num_ingredients < 4:
        return 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        return 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        return 'Intermediate'
    else:
        return 'Hard'



# Step 1.3: Main code to gather recipes and save them to a binary file
# Step 1.3a: Ask the user for the filename to store the recipes
filename = input("Enter the filename to store the recipes: ")

# Step 1.3b: Try to open the binary file and load its contents
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    # Step 1.3c: Handle file not found error by initializing data
    data = {'recipes_list': [], 'all_ingredients': []}
except Exception as e:
    # Step 1.3d: Handle any other exceptions
    print("An error occurred:", e)
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    # Step 1.3e: Close the file if it was successfully opened
    file.close()
finally:
    # Step 1.3f: Extract recipes_list and all_ingredients from data
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
# Step 1.3g: Ask the user how many recipes they would like to enter
n = int(input("How many recipes would you like to enter? "))
# Step 1.3h: Loop n times to collect recipes
for _ in range(n):
    # Step 1.3h-i: Take a recipe using the take_recipe function
    recipe = take_recipe()  
    # Step 1.3h-ii: Add the recipe to the recipes_list
    recipes_list.append(recipe) 
    # Step 1.3h-iii: Loop through each ingredient in the recipe's ingredients list
    for ingredient in recipe['ingredients']:
        # Step 1.3h-iv: If the ingredient is not in all_ingredients, add it
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
# Step 1.3i: Gather the updated recipes_list and all_ingredients into the dictionary called data
data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}
# Step 1.3j: Open a binary file with the user-defined filename and write data to it using the pickle module
with open(filename, 'wb') as file:
    pickle.dump(data, file)

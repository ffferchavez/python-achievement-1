# Exercise_1.3.py

# Step 2 - Initialize empty lists to store recipes and ingredients
recipes_list = []
ingredients_list = []

# Step 3 - Define a function to take recipe details from the user
def take_recipe():
    # Step 3a - Prompt the user to enter the recipe name
    name = input("Enter the recipe name: ")
    # Step 3b - Prompt the user to enter the cooking time in minutes
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    # Step 3c - Prompt the user to enter the ingredients, separated by commas
    ingredients = input("Enter the ingredients (separated by commas): ").split(', ')
    
    # Step 3d - Store the recipe details in a dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    # Step 3e - Return the recipe dictionary
    return recipe

# Step 4 - Main section of the code to gather recipes
# Step 4a - Ask the user how many recipes they would like to enter
n = int(input("How many recipes would you like to enter? "))

# Step 4b - Loop n times to collect recipes
for _ in range(n):
    # Step 4b-i - Take a recipe using the take_recipe function
    recipe = take_recipe()
    
    # Step 4b-ii - Add the recipe to the recipes_list
    recipes_list.append(recipe)
    
    # Step 4b-iii - Loop through each ingredient in the recipe's ingredients list
    for ingredient in recipe['ingredients']:
        # Step 4b-iv - If the ingredient is not in ingredients_list, add it
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

# Step 5 - Determine the difficulty of each recipe and display it
for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    
    # Step 5a - Determine difficulty based on cooking time and number of ingredients
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    
    # Step 5b - Print out the recipe details and difficulty
    print("\nRecipe:", recipe['name'])
    print("Cooking Time (min):", recipe['cooking_time'])
    print("Ingredients:", ", ".join(recipe['ingredients']))
    print("Difficulty:", difficulty)

# Step 6 - Display all unique ingredients in alphabetical order
# Step 6a - Sort the ingredients_list alphabetically
ingredients_list.sort()

# Step 6b - Print all ingredients
print("\nAll Ingredients:")
for ingredient in ingredients_list:
    print(ingredient)

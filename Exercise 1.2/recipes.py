# Step 1: Define recipe_1
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

# Step 2: Create all_recipes and add recipe_1
all_recipes = [recipe_1]

# Step 3: Define more recipes
recipe_2 = {
    "name": "Pasta",
    "cooking_time": 15,
    "ingredients": ["Pasta", "Tomato Sauce", "Cheese", "Olive Oil"]
}

recipe_3 = {
    "name": "Salad",
    "cooking_time": 10,
    "ingredients": ["Lettuce", "Tomato", "Cucumber", "Olive Oil", "Salt"]
}

recipe_4 = {
    "name": "Omelette",
    "cooking_time": 7,
    "ingredients": ["Eggs", "Salt", "Pepper", "Cheese", "Butter"]
}

recipe_5 = {
    "name": "Smoothie",
    "cooking_time": 5,
    "ingredients": ["Banana", "Milk", "Honey", "Berries"]
}

# Add all new recipes to all_recipes
all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

# Step 4: Print the ingredients of each recipe
for i, recipe in enumerate(all_recipes, start=1):
    print(f"Ingredients of recipe_{i}: {recipe['ingredients']}")

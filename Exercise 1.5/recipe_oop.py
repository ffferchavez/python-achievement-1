# Step 1: Define the Recipe class

# Step 1a: Define the class and its attributes
class Recipe:
    # Class variable to store all unique ingredients across recipes
    all_ingredients = set()

    # Step 1b: Initialize the object with its attributes
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    # Step 1c: Define getters and setters for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Step 1d: Define getters and setters for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calculate_difficulty()

    # Step 1e: Add ingredients to the recipe
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        self.update_all_ingredients()

    # Step 1f: Get ingredients of the recipe
    def get_ingredients(self):
        return self.ingredients

    # Step 1g: Calculate the difficulty of the recipe
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'

    # Step 1h: Get the difficulty of the recipe
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    # Step 1i: Search for an ingredient in the recipe
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # Step 1j: Update the class variable all_ingredients
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient)

    # Step 1k: String representation of the recipe
    def __str__(self):
        return f"Recipe: {self.name}\nCooking Time (min): {self.cooking_time}\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.get_difficulty()}"

# Step 1l: Class method to search for recipes by ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

# Step 2: Create and store recipes
# Step 2a: Initialize objects and set attributes
recipes = [
    ("Tea", ["Tea Leaves", "Sugar", "Water"], 5),
    ("Coffee", ["Coffee Powder", "Sugar", "Water"], 5),
    ("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50),
    ("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
]

# Step 2b: Loop through the recipe data, create Recipe objects, and add them to a list
recipes_list = []
for name, ingredients, cooking_time in recipes:
    recipe = Recipe(name)
    recipe.add_ingredients(*ingredients)
    recipe.set_cooking_time(cooking_time)
    recipes_list.append(recipe)
    print(recipe)

# Step 3: Search for recipes by ingredients
print("\nSearching for recipes with 'Water':")
recipe_search(recipes_list, "Water")

print("\nSearching for recipes with 'Sugar':")
recipe_search(recipes_list, "Sugar")

print("\nSearching for recipes with 'Bananas':")
recipe_search(recipes_list, "Bananas")

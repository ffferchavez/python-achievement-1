# Recipe OOP Python Exercise

This Python script demonstrates object-oriented programming (OOP) principles by implementing a `Recipe` class. The class manages recipes with attributes such as name, ingredients, cooking time, and difficulty level. It also provides methods for managing and searching recipes based on ingredients.

## Features

- **Recipe Class**: Manages individual recipes with attributes and methods.
  - `name`: The name of the recipe.
  - `ingredients`: A list of ingredients required for the recipe.
  - `cooking_time`: The time required to cook the recipe in minutes.
  - `difficulty`: Calculated based on cooking time and number of ingredients.
  
- **Methods**:
  - `__init__(self, name)`: Initializes a recipe with a name.
  - `get_name()` / `set_name(name)`: Get or set the recipe's name.
  - `get_cooking_time()` / `set_cooking_time(cooking_time)`: Get or set the cooking time, and update the difficulty.
  - `add_ingredients(*ingredients)`: Add one or more ingredients to the recipe.
  - `get_ingredients()`: Returns the list of ingredients.
  - `calculate_difficulty()`: Determines and sets the difficulty level of the recipe.
  - `get_difficulty()`: Returns the difficulty level, calculating it if necessary.
  - `search_ingredient(ingredient)`: Checks if a specific ingredient is in the recipe.
  - `update_all_ingredients()`: Updates a class-wide set of all unique ingredients.
  - `__str__()`: Returns a formatted string representation of the recipe.

- **Class Method**:
  - `recipe_search(data, search_term)`: Searches a list of recipes for a specific ingredient and prints recipes that contain it.

## Instructions

1. **Setup**:
   - Ensure you have Python 3.x installed.
   - Copy the `recipe_oop.py` script to your local environment.

2. **Running the Script**:
   - Execute the script using the command:
     ```bash
     python recipe_oop.py
     ```
   - The script will display information about various recipes and search results based on ingredients.

3. **Testing**:
   - The script creates several recipes, sets their attributes, and then prints them.
   - It searches for recipes containing specific ingredients (e.g., Water, Sugar, Bananas) and prints the results.

## Example Output

Recipe: Tea
Cooking Time (min): 5
Ingredients: Tea Leaves, Sugar, Water
Difficulty: Easy

Recipe: Coffee
Cooking Time (min): 5
Ingredients: Coffee Powder, Sugar, Water
Difficulty: Easy

Recipe: Cake
Cooking Time (min): 50
Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
Difficulty: Hard

Recipe: Banana Smoothie
Cooking Time (min): 5
Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
Difficulty: Easy

Searching for recipes with 'Water':
Recipe: Tea
Cooking Time (min): 5
Ingredients: Tea Leaves, Sugar, Water
Difficulty: Easy

Recipe: Coffee
Cooking Time (min): 5
Ingredients: Coffee Powder, Sugar, Water
Difficulty: Easy

Searching for recipes with 'Sugar':
Recipe: Tea
Cooking Time (min): 5
Ingredients: Tea Leaves, Sugar, Water
Difficulty: Easy

Recipe: Coffee
Cooking Time (min): 5
Ingredients: Coffee Powder, Sugar, Water
Difficulty: Easy

Recipe: Cake
Cooking Time (min): 50
Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
Difficulty: Hard

Recipe: Banana Smoothie
Cooking Time (min): 5
Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
Difficulty: Easy

Searching for recipes with 'Bananas':
Recipe: Banana Smoothie
Cooking Time (min): 5
Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
Difficulty: Easy


## Final Steps

1. **Screenshots**:
   - Take screenshots of the script execution to capture its functionality.

2. **GitHub Submission**:
   - Created a subfolder named `Exercise 1.5` in your GitHub repository.
   - Upload the following:
     - Screenshots with appropriate filenames.
     - The `recipe_oop.py` script file.
     - Updated learning journal.

3. **Submission**:
   - Provided the GitHub repository link for review.

## Contact

For any questions or feedback, please contact me.

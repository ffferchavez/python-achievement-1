import mysql.connector

# Step 1: Connect to MySQL Database

# Step 1a: Establish connection to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)

# Step 1b: Initialize a cursor object
cursor = conn.cursor()

# Step 1c: Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Step 1d: Use the created database
cursor.execute("USE task_database")

# Step 1e: Create the Recipes table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)
""")

# Step 2: Define the Recipe class and related functions

# Step 2a: Function to calculate difficulty based on cooking time and number of ingredients
def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

# Step 2b: Function to create a new recipe
def create_recipe(conn, cursor):
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients separated by comma: ").split(", ")
    difficulty = calculate_difficulty(cooking_time, ingredients)

    ingredients_str = ", ".join(ingredients)
    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, ingredients_str, cooking_time, difficulty))
    conn.commit()
    print("Recipe added successfully.")

# Step 2c: Function to search for recipes by ingredient
def search_recipe(conn, cursor):
    # Fetching all ingredients from the Recipes table
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    # Extracting unique ingredients from all recipes
    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(', ')
        all_ingredients.update(ingredients)
    
    all_ingredients = list(all_ingredients)
    
    # Displaying available ingredients to the user
    print("Available ingredients:")
    for idx, ingredient in enumerate(all_ingredients, 1):
        print(f"{idx}. {ingredient}")
    
    # Getting the user's choice of ingredient
    try:
        choice = int(input("Enter the number corresponding to the ingredient to search: "))
        if 1 <= choice <= len(all_ingredients):
            search_ingredient = all_ingredients[choice - 1]
        else:
            print("Invalid choice. Please select a valid number from the list.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Searching for recipes containing the chosen ingredient
    query = f"SELECT * FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Displaying the search results
    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Ingredients: {row[2]}, Cooking Time: {row[3]}, Difficulty: {row[4]}")
    else:
        print("No recipes found with the selected ingredient.")

# Step 2d: Function to update an existing recipe
def update_recipe(conn, cursor):
    # Fetching all recipes from the Recipes table
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

    # Getting the user's choice of recipe to update
    try:
        recipe_id = int(input("Enter the ID of the recipe to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID number.")
        return

    # Getting the column to update and the new value
    column = input("Enter the column to update (name, cooking_time, ingredients): ")

    if column == 'cooking_time' or column == 'ingredients':
        if column == 'ingredients':
            new_value = input("Enter new ingredients separated by comma: ").split(", ")
        else:
            new_value = int(input("Enter new cooking time (in minutes): "))

        # Fetching the old recipe values
        query = "SELECT cooking_time, ingredients FROM Recipes WHERE id = %s"
        cursor.execute(query, (recipe_id,))
        old_recipe = cursor.fetchone()

        if column == 'ingredients':
            new_value_str = ", ".join(new_value)
        else:
            new_value_str = new_value

        # Calculating the new difficulty
        difficulty = calculate_difficulty(new_value, old_recipe[1].split(', ')) if column == 'cooking_time' else calculate_difficulty(old_recipe[0], new_value)

        # Updating the recipe with the new values
        update_query = f"UPDATE Recipes SET {column} = %s, difficulty = %s WHERE id = %s"
        cursor.execute(update_query, (new_value_str, difficulty, recipe_id))
    else:
        new_value = input("Enter new value: ")
        query = f"UPDATE Recipes SET {column} = %s WHERE id = %s"
        cursor.execute(query, (new_value, recipe_id))

    conn.commit()
    print("Recipe updated successfully.")

# Step 2e: Function to delete a recipe
def delete_recipe(conn, cursor):
    # Fetching all recipes from the Recipes table
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

    # Getting the user's choice of recipe to delete
    try:
        recipe_id = int(input("Enter the ID of the recipe to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID number.")
        return

    # Deleting the chosen recipe
    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully.")

# Step 3: Main menu function
def main_menu(conn, cursor):
    while True:
        # Displaying the main menu options
        print("\n1. Create a new recipe")
        print("2. Search for recipes by ingredient")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        choice = input("Enter your choice: ")

        # Handling the user's choice
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Step 4: Run the main menu
if __name__ == "__main__":
    main_menu(conn, cursor)

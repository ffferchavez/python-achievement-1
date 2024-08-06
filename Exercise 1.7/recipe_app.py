# Part 1: Set Up Your Script & SQLAlchemy
# Importing necessary packages and methods
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

# Setting up SQLAlchemy
username = 'cf-python'
password = 'password'
hostname = 'localhost'
database_name = 'task_database'

# Create the engine object to connect to the desired database
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}', echo=True)

# Generate the Session class and bind it to the engine
Session = sessionmaker(bind=engine)

# Initialize the session object
session = Session()





# Part 2: Created Model and Table
# Define the Base class
Base = declarative_base()

# Define the Recipe model
class Recipe(Base):
    __tablename__ = 'final_recipes'
    
    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)
    
    # Define the __repr__ method for a quick representation of the recipe
    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"
    
    # Defined the __str__ method for a well-formatted version of the recipe
    def __str__(self):
        ingredients_list = self.return_ingredients_as_list()
        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {', '.join(ingredients_list)}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*40}\n"
        )
    
    # Define the method to calculate the difficulty of the recipe
    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()
        if len(ingredients_list) < 4 and self.cooking_time < 10:
            self.difficulty = 'Easy'
        elif len(ingredients_list) < 4 and self.cooking_time >= 10:
            self.difficulty = 'Medium'
        elif len(ingredients_list) >= 4 and self.cooking_time < 10:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'
    
    # Define the method to return ingredients as a list
    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        return self.ingredients.split(', ')

# Create the corresponding table in the database
Base.metadata.create_all(engine)





# Part 3: Define Your Main Operations as Functions

# Function 1: create_recipe()
def create_recipe():
    # Collect the details of the recipe from the user
    name = input("Enter the recipe name (max 50 characters): ")
    while len(name) > 50:
        name = input("Name too long! Enter again (max 50 characters): ")
    
    cooking_time = input("Enter the cooking time in minutes: ")
    while not cooking_time.isnumeric():
        cooking_time = input("Invalid input! Enter a number for cooking time: ")
    
    # Collect the ingredients from the user
    ingredients = []
    num_ingredients = input("How many ingredients do you want to enter? ")
    while not num_ingredients.isnumeric():
        num_ingredients = input("Invalid input! Enter a number for the ingredients count: ")
    
    for _ in range(int(num_ingredients)):
        ingredient = input("Enter an ingredient: ")
        ingredients.append(ingredient)
    
    ingredients_str = ', '.join(ingredients)
    
    # Create a new Recipe object
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=int(cooking_time)
    )
    
    # Calculate the difficulty and add to the database
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe created successfully!")

# Function 2: view_all_recipes()
def view_all_recipes():
    # Retrieve all recipes from the database
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found in the database.")
        return None
    
    # Display each recipe
    for recipe in recipes:
        print(recipe)

# Function 3: search_by_ingredients()
def search_by_ingredients():
    # Check if there are any recipes in the database
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return
    
    # Retrieve all ingredients from the database
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for result in results:
        ingredients_list = result[0].split(', ')
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display ingredients and allow user to pick one
    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f"{index}. {ingredient}")
    
    chosen_indices = input("Enter the numbers corresponding to the ingredients (separated by spaces): ").split()
    search_ingredients = [all_ingredients[int(index) - 1] for index in chosen_indices if index.isnumeric() and int(index) <= len(all_ingredients)]
    
    # Create search conditions
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]
    
    # Retrieve and display matching recipes
    recipes = session.query(Recipe).filter(*conditions).all()
    if not recipes:
        print("No recipes found with the selected ingredients.")
        return
    
    for recipe in recipes:
        print(recipe)

# Function 4: edit_recipe()
def edit_recipe():
    # Check if there are any recipes in the database
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return
    
    # Retrieve and display all recipes
    results = session.query(Recipe.id, Recipe.name).all()
    for result in results:
        print(f"ID: {result[0]}, Name: {result[1]}")
    
    # Ask the user to pick a recipe by ID
    recipe_id = input("Enter the ID of the recipe you want to edit: ")
    recipe_to_edit = session.query(Recipe).filter_by(id=int(recipe_id)).first()
    
    if not recipe_to_edit:
        print("Invalid ID. No such recipe found.")
        return
    
    # Display recipe details and ask for attribute to edit
    print(recipe_to_edit)
    print("What would you like to edit?")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking time")
    choice = input("Enter the number corresponding to your choice: ")
    
    if choice == "1":
        new_name = input("Enter the new name (max 50 characters): ")
        while len(new_name) > 50:
            new_name = input("Name too long! Enter again (max 50 characters): ")
        recipe_to_edit.name = new_name
    elif choice == "2":
        ingredients = []
        num_ingredients = input("How many ingredients do you want to enter? ")
        while not num_ingredients.isnumeric():
            num_ingredients = input("Invalid input! Enter a number for the ingredients count: ")
        for _ in range(int(num_ingredients)):
            ingredient = input("Enter an ingredient: ")
            ingredients.append(ingredient)
        recipe_to_edit.ingredients = ', '.join(ingredients)
    elif choice == "3":
        new_time = input("Enter the new cooking time in minutes: ")
        while not new_time.isnumeric():
            new_time = input("Invalid input! Enter a number for cooking time: ")
        recipe_to_edit.cooking_time = int(new_time)
    else:
        print("Invalid choice!")
        return
    
    # Recalculate difficulty and commit changes
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")

# Function 5: delete_recipe()
def delete_recipe():
    # Check if there are any recipes in the database
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return
    
    # Retrieve and display all recipes
    results = session.query(Recipe.id, Recipe.name).all()
    for result in results:
        print(f"ID: {result[0]}, Name: {result[1]}")
    
    # Ask the user to pick a recipe by ID to delete
    recipe_id = input("Enter the ID of the recipe you want to delete: ")
    recipe_to_delete = session.query(Recipe).filter_by(id=int(recipe_id)).first()
    
    if not recipe_to_delete:
        print("Invalid ID. No such recipe found.")
        return
    
    # Confirm deletion
    confirmation = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ")
    if confirmation.lower() == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Deletion canceled.")





# Part 4: Design Your Main Menu

def main_menu():
    while True:
        # Display menu options
        print("\nMain Menu")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit an existing recipe")
        print("5. Delete a recipe")
        print("6. Quit the application")
        
        # Collect user input for menu choice
        choice = input("Enter your choice: ")
        
        # Perform action based on user choice
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6":
            print("Goodbye!")
            session.close()
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()

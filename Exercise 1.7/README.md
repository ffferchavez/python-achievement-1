# Object-Relational Mapping in Python

This project is a Python application demonstrating Object-Relational Mapping (ORM) using SQLAlchemy. The application allows users to manage a collection of recipes with functionalities to create, view, update, and delete recipes. It showcases how to use SQLAlchemy to interact with a relational database using Python.

## Features

- **Create a New Recipe**: Add new recipes with name, ingredients, cooking time, and difficulty.
- **View All Recipes**: Display a list of all recipes in the database.
- **Search for Recipes by Ingredients**: Find recipes that contain specific ingredients.
- **Edit an Existing Recipe**: Update details of an existing recipe.
- **Delete a Recipe**: Remove a recipe from the database.

## Requirements

- Python 3.7 or higher
- SQLAlchemy
- MySQL (or another relational database)

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/recipe-manager.git

2. **Navigate to the Project Directory**:

   ```bash
   cd recipe-manager

3. **Create a Virtual Environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


4. **Install Dependencies**:

   ```bash
   pip install sqlalchemy mysql-connector-python

5. **Configure the Database**:

   Ensure that your database configuration is correct in the recipe_app.py file.

## Usage

1. **Run the Application**:

   ```bash
   python recipe_app.py

2. **Follow the On-Screen Menu**:

   - **Create a New Recipe**: Enter the details of the new recipe.
   - **View All Recipes**: List all recipes in the database.
   - **Search for Recipes by Ingredients**: Search recipes by specifying     ingredients.
   - **Edit an Existing Recipe**: Modify an existing recipe's details.
   - **Delete a Recipe**: Remove a recipe from the database.
   - **Quit the Application**: Exit the application.

## Screenshots
Screenshots of the application in action can be found in the screenshots directory of this repository.

## Example Output

1. **Creating a New Recipe**:

   ```bash
   Enter the recipe name: Spaghetti Bolognese
   Enter the cooking time (in minutes): 30
   Enter the difficulty (easy, medium, hard): medium
   Enter ingredients (comma-separated): spaghetti, ground beef, tomato sauce, garlic, onion
   Recipe created successfully!

2. **Viewing All Recipes**:

   ```bash
   Recipe: Spaghetti Bolognese
   Cooking Time: 30 minutes
   Difficulty: Medium
   Ingredients: spaghetti, ground beef, tomato sauce, garlic, onion


3. **Searching for Recipes by Ingredients**:

   ```bash
   Searching for recipes with 'tomato sauce':
   Recipe: Spaghetti Bolognese
   Cooking Time: 30 minutes
   Difficulty: Medium
   Ingredients: spaghetti, ground beef, tomato sauce, garlic, onion


4. **Editing an Existing Recipe**:

   ```bash
   Enter the recipe ID to edit: 1
   Enter new cooking time (in minutes): 25
   Recipe updated successfully!


5. **Deleting a Recipe**:

   ```bash
   Enter the recipe ID to delete: 1
   Recipe deleted successfully!

## Contact
For any questions or feedback, please contact me.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
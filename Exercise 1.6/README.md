# Databases in Python

## Overview
This exercise demonstrates how to connect to a MySQL database using Python for a recipe management application. The application allows users to create, search, update, and delete recipes in a MySQL database.

## Exercise Structure
- `recipe_mysql.py`: The main Python script that interacts with the MySQL database to manage recipes.
- `README.md`: This file providing an overview and instructions for the project.

## Getting Started

### Prerequisites
- **Python**: Ensure Python is installed (Python 3.6+ recommended).
- **MySQL Server**: Ensure MySQL server is installed and running on your system.
- **MySQL Connector for Python**: Install the connector using pip:

    ```bash
    pip install mysql-connector-python
    ```

### Setting Up the Database
Create the Database and Table:

- The script `recipe_mysql.py` will automatically create a database named `task_database` and a table named `Recipes` if they do not already exist.

### Script Overview
- **Connecting to MySQL**: Establishes a connection to the MySQL server and initializes a cursor object.
- **Creating Recipes**: Allows users to add new recipes to the database.
- **Searching Recipes**: Allows users to search for recipes by ingredient.
- **Updating Recipes**: Allows users to update existing recipes.
- **Deleting Recipes**: Allows users to delete recipes from the database.

### Running the Script
Execute the Script:

- Run the script from your terminal:

    ```bash
    python recipe_mysql.py
    ```

Using the Menu:

- You will be presented with a menu with the following options:
  1. Create a new recipe
  2. Search for recipes by ingredient
  3. Update a recipe
  4. Delete a recipe
  5. Exit

- Follow the on-screen prompts to interact with the database.

### Examples

- **Creating a New Recipe**:
  Enter the recipe name, cooking time, and ingredients when prompted.

- **Searching for Recipes**:
  View available ingredients and select one to search recipes containing that ingredient.

- **Updating a Recipe**:
  Choose a recipe to update and specify which attribute (name, cooking time, or ingredients) to modify.

- **Deleting a Recipe**:
  Select a recipe by its ID to delete it from the database.

### Screenshots
Please refer to the following screenshots demonstrating the script execution for various operations:
- Creating a Recipe
- Searching for Recipes
- Updating a Recipe
- Deleting a Recipe

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

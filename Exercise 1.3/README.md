
# Recipe Difficulty Calculator

This Python script helps users input various recipes, calculates their difficulty based on specific criteria, and lists all unique ingredients from the recipes. This project is a part of a Python course assignment.

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Example Output](#example-output)
5. [Screenshots](#screenshots)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Recipe Difficulty Calculator is a simple Python script that prompts users to enter recipes, including the name, cooking time, and ingredients. The script then calculates the difficulty level of each recipe based on the given criteria and displays all the unique ingredients encountered across all recipes.

## Setup

To run this script, ensure you have Python installed on your machine. No additional libraries are required.

### Installation

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Navigate to the Project Directory**

   Change your directory to the project folder:

   ```bash
   cd your-repo-name
   ```

3. **Run the Script**

   Execute the script using Python:

   ```bash
   python Exercise_1.3.py
   ```

## Usage

1. The script first asks how many recipes you would like to enter.
2. For each recipe, input the following details:
   - **Name**: The name of the recipe.
   - **Cooking Time**: The time required to prepare the recipe (in minutes).
   - **Ingredients**: A list of ingredients separated by commas.
3. The script calculates and displays the difficulty level of each recipe.
4. It also lists all the unique ingredients from the entered recipes in alphabetical order.

## Example Output

```bash
How many recipes would you like to enter? 2

Enter the recipe name: Pancakes
Enter the cooking time (in minutes): 5
Enter the ingredients (separated by commas): flour, eggs, milk

Enter the recipe name: Omelette
Enter the cooking time (in minutes): 10
Enter the ingredients (separated by commas): eggs, cheese, ham, salt

Recipe: Pancakes
Cooking Time (min): 5
Ingredients: flour, eggs, milk
Difficulty: Easy

Recipe: Omelette
Cooking Time (min): 10
Ingredients: eggs, cheese, ham, salt
Difficulty: Intermediate

All Ingredients:
cheese
eggs
flour
ham
milk
salt
```

## Screenshots

Screenshots of each step of the process are included in the "screenshots" directory. These steps include:

1. Initial setup and list initialization
2. Input prompts and data entry
3. Display of recipe details and difficulty levels
4. Display of all unique ingredients

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Please ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

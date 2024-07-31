
# Recipe App Data Structure Project

## Overview

This project involves creating data structures to store and manage recipes for a simple Recipe App. The goal is to use appropriate data structures to store details about various recipes, including their name, cooking time, and ingredients.

## Data Structure Choices

### Recipe Data Structure

Each recipe is stored as a **dictionary** with the following keys:
- `name` (str): The name of the recipe.
- `cooking_time` (int): The cooking time in minutes.
- `ingredients` (list): A list of ingredients (each a string).

**Reasoning**: Dictionaries are chosen for their ability to store key-value pairs, making it easy to access and modify individual recipe attributes. This structure is flexible and allows for intuitive data handling, especially when attributes may need to be accessed or updated independently.

### All Recipes Data Structure

All recipes are stored in a **list** named `all_recipes`. Each element in this list is a dictionary representing a recipe.

**Reasoning**: A list is used to maintain an ordered collection of recipes. This allows for easy addition and removal of recipes, as well as straightforward iteration over the collection. The sequential nature of lists makes it easy to manage and retrieve recipes by their position in the list.

## Recipes Included

1. **Tea**
   - Cooking time: 5 minutes
   - Ingredients: Tea leaves, Sugar, Water

2. **Pasta**
   - Cooking time: 15 minutes
   - Ingredients: Pasta, Tomato Sauce, Cheese, Olive Oil

3. **Salad**
   - Cooking time: 10 minutes
   - Ingredients: Lettuce, Tomato, Cucumber, Olive Oil, Salt

4. **Omelette**
   - Cooking time: 7 minutes
   - Ingredients: Eggs, Salt, Pepper, Cheese, Butter

5. **Smoothie**
   - Cooking time: 5 minutes
   - Ingredients: Banana, Milk, Honey, Berries

## How to Run

To run the code and view the ingredients for each recipe, use the following code snippet:

```python
for i, recipe in enumerate(all_recipes, start=1):
    print(f"Ingredients of recipe_{i}: {recipe['ingredients']}")
```

## Screenshots

Screenshots of the implementation steps are provided in the `screenshots` directory. Each screenshot corresponds to a step in the implementation process, named appropriately.

## Learning Journal

The learning journal contains reflections on the process, challenges faced, and the reasoning behind choosing specific data structures.

## Submission

This project has been submitted to the course repository. The GitHub link is provided for review.

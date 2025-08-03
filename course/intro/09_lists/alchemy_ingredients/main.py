def check_ingredient_match(recipe, ingredients):
    """
    Checks if all ingredients in the recipe are present in the ingredients list.
    
    Args:
        recipe (list): List of ingredients required for the recipe.
        ingredients (list): List of available ingredients.
    
    Returns:
        tuple: A tuple containing the percentage of matched ingredients and a list of unmatched ingredients.
    """
    matched = set(recipe) & set(ingredients) # intersection operator — returns a new set with items found in both sets.
    print(f"Matched:  {matched}")
    percentage = len(matched) / len(recipe) * 100
    unmatched = [item for item in recipe if item not in matched]
    
    return percentage, unmatched


def validate_ingredients(ingredients) -> str:
    valid_items = ["fire", "air", "water", "earth"]
    ingredient_list = ingredients.split()

    for ingredient in ingredient_list:
        if ingredient not in valid_items:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"

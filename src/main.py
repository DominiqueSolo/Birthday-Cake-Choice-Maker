def normalize_input(user_input):
    return user_input.strip().lower()

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        normalized = normalize_input(user_input)
        if normalized == "end program":
            print("Okay. Bye!")
            exit()
        if normalized in valid_options:
            return normalized
        else:
            print("I’m sorry. I did not understand that. Please type your answer according to the previous question’s instructions.")

# Define the dessert database
recipes = {
    ('whole cake', 'yolk', 'milk'): {
        'name': "Classic Vanilla Cake",
        'ingredients': ["flour", "sugar", "eggs", "milk", "butter", "vanilla extract"],
        'time': "45 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Mix ingredients...\n3. Bake for 45 minutes.",
        'url': "https://example.com/classic-vanilla-cake"
    },
    ('whole cake', 'no yolk', 'milk'): {
        'name': "Egg-White Milk Cake",
        'ingredients': ["flour", "sugar", "egg whites", "milk", "butter", "vanilla extract"],
        'time': "40 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Mix egg whites and milk...\n3. Bake for 40 minutes.",
        'url': "https://example.com/egg-white-milk-cake"
    },
    ('cupcakes', 'yolk', 'no milk'): {
        'name': "Yolk-Only Cupcakes",
        'ingredients': ["flour", "sugar", "egg yolks", "oil", "vanilla"],
        'time': "30 minutes",
        'instructions': "1. Preheat oven...\n2. Mix yolks and dry ingredients...\n3. Bake for 30 minutes.",
        'url': "https://example.com/yolk-only-cupcakes"
    },
    # Add more combinations as needed...
}

def main():
    print("Welcome to the Birthday Dessert Choice Maker!")
    print("You will be asked a few questions to help us pick the perfect dessert for you.")
    print("You can exit at any time by typing 'end program'.\n")

    type_input = get_valid_input("Do you want your birthday dessert to be a whole cake or a set of cupcakes? Type 'whole cake' or 'cupcakes': ",
                                 ['whole cake', 'cupcakes'])

    yolk_input = get_valid_input("Do you want your birthday dessert to contain yolk or no yolk? Type 'yolk' or 'no yolk': ",
                                 ['yolk', 'no yolk'])

    milk_input = get_valid_input("Do you want your birthday dessert to contain milk or not? Type 'milk' or 'no milk': ",
                                 ['milk', 'no milk'])

    key = (type_input, yolk_input, milk_input)

    if key not in recipes:
        print("\nSorry, we do not currently have a recipe matching all of your preferences.")
        return

    recipe = recipes[key]

    print(f"\nRecommended Dessert: {recipe['name']}")
    print("Ingredients:", ", ".join(recipe['ingredients']))
    print("Cooking Time:", recipe['time'])

    instruction_type = get_valid_input(
        "\nDo you want the recipe instructions presented on screen or the URL to view online? Type 'screen' or 'url': ",
        ['screen', 'url']
    )

    if instruction_type == 'screen':
        print("\nRecipe Instructions:")
        print(recipe['instructions'])
    else:
        print("\nRecipe URL:")
        print(recipe['url'])

if __name__ == "__main__":
    main()

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

recipes = {
    ('whole cake', 'yolk', 'milk'): {
        'name': "Classic Yellow Cake",
        'ingredients': ["flour", "sugar", "eggs", "milk", "butter", "vanilla extract"],
        'time': "45 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Mix ingredients...\n3. Bake for 45 minutes.",
        'url': "https://www.thespruceeats.com/basic-yellow-cake-recipe-1000685"
    },
    ('whole cake', 'no yolk', 'milk'): {
        'name': "Egg White Milk Cake",
        'ingredients': ["flour", "sugar", "egg whites", "milk", "butter", "vanilla extract"],
        'time': "40 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Mix egg whites and milk...\n3. Bake for 40 minutes.",
        'url': "https://www.thespruceeats.com/basic-yellow-cake-recipe-1000685"
    },
    ('whole cake', 'yolk', 'no milk'): {
        'name': "Dairy-Free Yellow Cake",
        'ingredients': ["flour", "sugar", "eggs", "vegetable oil", "vanilla extract", "baking powder"],
        'time': "50 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Mix dry and wet ingredients separately, then combine...\n3. Bake for 50 minutes.",
        'url': "https://godairyfree.org/recipes/dairy-free-yellow-cake"
    },
    ('whole cake', 'no yolk', 'no milk'): {
        'name': "Depression-Era Wacky Cake",
        'ingredients': ["flour", "sugar", "baking soda", "vinegar", "oil", "vanilla extract", "water"],
        'time': "35 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Mix dry ingredients, then add wet ingredients...\n3. Bake for 35 minutes.",
        'url': "https://www.eatingwell.com/article/7820487/depression-era-cake-recipe/"
    },
    ('cupcakes', 'yolk', 'milk'): {
        'name': "Classic Vanilla Cupcakes",
        'ingredients': ["flour", "sugar", "egg yolks", "milk", "butter", "vanilla extract"],
        'time': "30 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Whisk yolks and sugar, then add rest...\n3. Bake for 30 minutes.",
        'url': "https://www.thespruceeats.com/basic-yellow-cake-recipe-1000685"
    },
    ('cupcakes', 'yolk', 'no milk'): {
        'name': "Yolk-Only Cupcakes",
        'ingredients': ["flour", "sugar", "egg yolks", "oil", "vanilla"],
        'time': "30 minutes",
        'instructions': "1. Preheat oven...\n2. Mix yolks and dry ingredients...\n3. Bake for 30 minutes.",
        'url': "https://www.thespruceeats.com/basic-yellow-cake-recipe-1000685"
    },
    ('cupcakes', 'no yolk', 'milk'): {
        'name': "Egg White Milk Cupcakes",
        'ingredients': ["flour", "sugar", "egg whites", "milk", "butter", "vanilla extract"],
        'time': "25 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Beat egg whites until frothy, then mix in other ingredients...\n3. Bake for 25 minutes.",
        'url': "https://www.thespruceeats.com/basic-yellow-cake-recipe-1000685"
    },
    ('cupcakes', 'no yolk', 'no milk'): {
        'name': "Vegan Vanilla Cupcakes",
        'ingredients': ["flour", "sugar", "egg replacer or aquafaba", "vegetable oil", "vanilla extract", "baking soda"],
        'time': "30 minutes",
        'instructions': "1. Preheat oven to 350°F...\n2. Combine dry and wet ingredients...\n3. Bake for 30 minutes.",
        'url': "https://lovingitvegan.com/vegan-vanilla-cupcakes-strawberry-vanilla-frosting/"
    }
}

def main():
    print("Welcome to the Birthday Dessert Choice Maker!")
    print("You will be asked a few questions to help us pick the perfect dessert for you.")
    print("You can exit at any time by typing 'end program'.\n")

    while True:
        type_input = get_valid_input("Do you want your birthday dessert to be a whole cake or a set of cupcakes? Type 'whole cake' or 'cupcakes': ",
                                     ['whole cake', 'cupcakes'])

        yolk_input = get_valid_input("Do you want your birthday dessert to contain yolk or no yolk? Type 'yolk' or 'no yolk': ",
                                     ['yolk', 'no yolk'])

        milk_input = get_valid_input("Do you want your birthday dessert to contain milk or not? Type 'milk' or 'no milk': ",
                                     ['milk', 'no milk'])

        key = (type_input, yolk_input, milk_input)

        if key not in recipes:
            print("\nSorry, we do not currently have a recipe matching all of your preferences.")
        else:
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

        again = get_valid_input("\nWould you like to try another combination? Type 'yes' to continue or 'no' to exit: ", ['yes', 'no'])
        if again == 'no':
            print("Okay. Bye!")
            break

if __name__ == "__main__":
    main()

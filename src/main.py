def start_program():
    print("Welcome to the Birthday Cake Choice Maker!")
    print("Type 'end program' at any time to exit.")
    dessert = input("Whole cake or cupcakes? ").strip().lower()
    if dessert == "end program": return print("Okay. Bye!")
    yolk = input("Yolk or no yolk? ").strip().lower()
    if yolk == "end program": return print("Okay. Bye!")
    milk = input("Milk or no milk? ").strip().lower()
    if milk == "end program": return print("Okay. Bye!")
    instruction = input("View instructions on screen or URL? ").strip().lower()
    if instruction == "end program": return print("Okay. Bye!")
    print(f"You chose: {dessert}, {yolk}, {milk}.")
    if instruction == "screen":
        print("Displaying recipe instructions on screen...")
    elif instruction == "url":
        print("Here is your URL: https://example.com/your-recipe")
    else:
        print("Invalid instruction type.")

if __name__ == "__main__":
    start_program()

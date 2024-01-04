# Prompt the user to enter a text and print it in reverse/backward.
def reverse_string():
    while True:
        user_input = input("Enter a string: ")

        if user_input.isalpha():
            reversed_string = user_input[::-1]
            print("Reversed text:", reversed_string)
            break
        else:
            print("Error: Please enter text only.")


if __name__ == "__main__":
    reverse_string()

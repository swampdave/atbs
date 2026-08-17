def collatz(number):
    if number % 2 == 0:
        # Number is even
        result = number // 2
    else:
        # Number is odd
        result = 3 * number + 1

    print(result, end=" ")
    return result

# Full program logic to interact with a user
if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer: "))

        # Keep calling the function until it returns 1
        current_value = user_input
        while current_value != 1:
            current_value = collatz(current_value)

    except ValueError:
        print("Error: Please enter a valid integer.")

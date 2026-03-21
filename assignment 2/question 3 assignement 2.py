# Function to generate a single row of the pyramid
def generate_row(row_number):
    row = ""
    # Add ascending numbers
    for i in range(1, row_number + 1):
        row += str(i)
    # Add descending numbers
    for i in range(row_number - 1, 0, -1):
        row += str(i)
    return row

# Function to print the full pyramid
def print_pyramid(n):
    for row_number in range(1, n + 1):
        # Print leading spaces
        for _ in range(n - row_number):
            print(" ", end="")
        # Print row numbers
        print(generate_row(row_number))

# Main function to get user input
def main():
    while True:
        try:
            n = int(input("Enter the number of rows for the numeric pyramid: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print_pyramid(n)

# Run the program
if __name__ == "__main__":
    main()
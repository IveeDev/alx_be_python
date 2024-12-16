# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate that the size is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        # Draw the pattern using a single for loop
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

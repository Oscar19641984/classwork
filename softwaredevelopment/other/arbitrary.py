numbers = []

if numbers:  # checks if the list is not empty
    average = sum(numbers) / len(numbers)
    print("Average is:", average)
else:
    print("The list is empty. Can't compute an average.")
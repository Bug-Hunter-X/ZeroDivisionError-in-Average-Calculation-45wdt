def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#More robust solution
def calculate_average_robust(numbers):
    if not numbers:
        return 0 #Return 0 for empty list
    return sum(numbers) / len(numbers)

my_numbers = [1,2,3,4,5]
print(calculate_average_robust(my_numbers))

my_empty_list = []
print(calculate_average_robust(my_empty_list))
def calculate_average(numbers):
    try:
        if not numbers:
            return 0  # Handle empty list
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: List must contain only numbers.")
        return None  # Or raise a more specific exception
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list.")
        return None # Or raise a more specific exception

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [10,0,20]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

my_list_with_strings = [10, '20', 30]
result = calculate_average(my_list_with_strings) #This will now print an error message instead of crashing 
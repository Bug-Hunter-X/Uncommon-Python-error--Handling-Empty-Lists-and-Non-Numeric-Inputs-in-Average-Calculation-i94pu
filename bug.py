def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers) 
    return average

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") # This will print 0 which is correct

my_list_with_zero = [10,0,20]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}") #This will print 10 which is correct

my_list_with_strings = [10, '20', 30]
result = calculate_average(my_list_with_strings) # This will throw an error
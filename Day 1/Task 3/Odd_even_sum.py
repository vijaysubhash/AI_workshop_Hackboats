# Get a list of numbers from the user
user_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = []
for num in user_numbers.split():
    num = int(num)
    numbers.append(num)

# Initialize sums for odd and even numbers
odd_sum = 0
even_sum = 0

# Calculate sums
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Display the results
print("Odd Sum:", odd_sum)
print("Even Sum:", even_sum)

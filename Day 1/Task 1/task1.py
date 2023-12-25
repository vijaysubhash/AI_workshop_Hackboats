from basic_math_operations import *

a = int(input())
b = int(input())
user_input = input("Enter numbers seperated by spaces: ")
numbers = []
for num in user_input.split():
    num = int(num)
    numbers.append(num)
    
print("Sum:", add(a, b))
print("Difference:", difference(a, b))
print("Product:", product(a, b))
print("Division:", division(a, b))
print("Mean:", mean(numbers))
print("Median:", median(numbers))
# print("Variance:", variance(numbers))
# print("Standard Deviation:", standard_deviation(numbers))

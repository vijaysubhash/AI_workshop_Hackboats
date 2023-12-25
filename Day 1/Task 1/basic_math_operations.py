# Addition of numbers
def add(a, b):
    return a + b


def difference(a, b):
    return a - b


def product(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."


def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]


# def variance(numbers):
#     mean = sum(numbers) / len(numbers)
#     squared_diff = [(x - mean) ** 2 for x in numbers]
#     return sum(squared_diff) / len(numbers)


# def standard_deviation(numbers):
#     return variance(numbers) ** 0.5

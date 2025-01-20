# codewars

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i**2
    return sum



def find_average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    if len(numbers) == 0:
        return 0
    return sum / len(numbers)

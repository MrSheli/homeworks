# codewars

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
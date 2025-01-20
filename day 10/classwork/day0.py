# codewars

def pyramid(n):
    result_list = []
    for i in range(1, n + 1):
        result_list.append([1] * i)
    return result_list
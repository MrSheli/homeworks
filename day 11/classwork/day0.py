list1 = [42, 74, 12, 2, 7]

def list(list1):
    sum = 0
    for i in list1:
        sum += 2*i
    
    return sum
print(list(list1))


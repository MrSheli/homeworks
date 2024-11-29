list1 = [1,5,2,8,-7,4,-9,0]

def list0(list1):
    sum = 0
    for i in list1:
        if i % 2 == 1:
            sum += i
    return sum
print(list0(list1))
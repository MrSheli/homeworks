# codewars

def make_negative( number ):
     if number < 0:
        return number
     elif number > 0:
        return -number
     else:
        return number
     

def positive_sum(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += i
    return count



def listSum(list1, list2):
    return sum(list1) + sum(list2)

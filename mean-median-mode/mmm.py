import sys

def mean(n, numbers):
    sum = 0
    for num in numbers:
        sum += float(num)
    return sum / len(numbers) 

def medium(n, numbers):

    floats = []
    for num in numbers:
        floats.append(float(num))

    sorted_numbers = sorted(floats)
    
    sum = 0
    size = len(sorted_numbers)
    index = size // 2 - 1
    if size % 2 == 0:
        index = size // 2 - 1
        sum = float(sorted_numbers[index]) + float(sorted_numbers[index+1])
    else:
        index = size // 2
        sum = float(sorted_numbers[index]) * 2
    return sum / 2
    
def mode(n, numbers):
    dict = {}
    for num in numbers:
        if not dict.has_key(num):
            dict[num] = 0.
        dict[num] = dict[num] + 1.

    sorted_items = sorted(dict.items(), key=lambda x: float(x[0]))

    max = 0
    max_num = 0
    for s in sorted_items:
        if s[1] > max:
            max = s[1]
            max_num = s[0]

    return max_num

n = raw_input()
numbers = raw_input().split()

print "%.1f" % mean(n, numbers)
print "%.1f" % medium(n, numbers)
print mode(n, numbers)

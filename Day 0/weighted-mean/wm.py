import sys

def wmean(n, numbers, weights):
    sum_numbers = 0.
    sum_weights = 0.
    for i in range(0,n):
        sum_numbers += float(numbers[i]) * float(weights[i])
        sum_weights += float(weights[i])

    return sum_numbers / sum_weights

n = int(raw_input())
numbers = raw_input().split()
weights = raw_input().split()

print "%.1f" % wmean(n, numbers, weights)


from math import pow, sqrt

def mean(n, numbers):
    sum = 0
    for num in numbers:
        sum += float(num)
    return sum / n 

def standard_deviation(n, numbers):

    u = mean(n, numbers)

    sum = 0
    for num in numbers:
        sum += pow(float(num)-u, 2)
    
    sd = sqrt( sum / n )

    return sd

def main():
    n = int(raw_input())
    numbers = raw_input().split()

    print "%.1f" % standard_deviation(n, numbers)

main()

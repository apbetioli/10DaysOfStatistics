import sys

def sort_numbers(numbers):
    floats = []
    for num in numbers:
        floats.append(float(num))
    return sorted(floats)

def median(size, numbers):
    index = size // 2
    sum = 0
    if size % 2 == 0:
        sum = float(numbers[index-1]) + float(numbers[index])
    else:
        sum = float(numbers[index]) * 2

    return sum / 2

def quartiles(size, numbers):
    q2 = median(size, numbers)
    middle = size // 2

    if size % 2 == 0:
        l = numbers[:middle]
        u = numbers[middle:]
    else:
        l = numbers[:middle]
        u = numbers[middle+1:]

    q1 = median(len(l), l)
    q3 = median(len(u), u)

    return (q1,q2,q3)

def main():
    size = int(raw_input())
    x = raw_input().split()
    f = raw_input().split()
    s = []

    for i in range(0,size):
        frequency = int(f[i])
        for t in range(0, frequency):
            s.append(x[i])

    numbers = sort_numbers(s)

    q = quartiles(len(numbers), numbers)

    print "%.1f" % (q[2] - q[0])

if __name__ == '__main__':
    main()

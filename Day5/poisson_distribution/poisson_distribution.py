from math import pow, factorial

def poisson_distribution(mean, k):
    e = 2.71828

    return pow(mean, k) * pow(e, -mean) / factorial(k)

def main():
    mean = float(raw_input())
    k = float(raw_input())

    print "%.3f" % poisson_distribution(mean, k)

main()
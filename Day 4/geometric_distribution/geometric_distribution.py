from math import pow

def geometric_distribution(n,p,q):
    return pow(q,n-1) * p

def main():
    input = raw_input().split()
    numerator = int(input[0])
    denominator = int(input[1])
    n = int(raw_input())

    p = float(numerator) / float(denominator)
    q = 1 - p

    print '%0.3f' % geometric_distribution(n,p,q)

main()
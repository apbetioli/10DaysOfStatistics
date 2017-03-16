from math import factorial, pow

def combination(n,x):
    return factorial(n) / (factorial(x) * factorial(n-x))

def binomial_distribution(x,n,p):
    q = 1 - p
    return combination(n,x) * pow(p, x) * pow(q, n-x)

def main():
    input = raw_input().split()
    q = float(input[0]) / 100
    n = int(input[1])

    p = 1 - q

    no_more_than_2 = 0
    for x in range (n-2,n+1):
        no_more_than_2 += binomial_distribution(x,n,p)

    print "%0.3f" % no_more_than_2

    at_least_2 = 0
    for x in range (0,n-2+1):
        at_least_2 += binomial_distribution(x,n,p)

    print "%0.3f" % at_least_2

main()
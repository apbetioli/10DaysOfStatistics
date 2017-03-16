from math import factorial, pow

def combination(n,x):
    return factorial(n) / (factorial(x) * factorial(n-x))

def binomial_distribution(x,n,p):
    q = 1 - p
    return combination(n,x) * pow(p, x) * pow(q, n-x)

def main():
    input = raw_input().split()
    boys = float(input[0])
    girls = float(input[1])

    p = boys / (boys+girls)

    n = 6
    x_min = 3

    sum = 0
    for x in range (x_min,n+1):
        sum += binomial_distribution(x,n,p)

    print "%0.3f" % sum

main()
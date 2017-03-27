from math import pow, sqrt

def mean(Z, n):
    sum = 0
    for z in Z:
        sum += z
    return sum / n

def covariance(X, Y, n):
    mean_x = mean(X, n)
    mean_y = mean(Y, n)

    sum = 0
    for i in xrange(n):
        sum += (X[i]- mean_x) * (Y[i] - mean_y)

    return sum / n

def standard_deviation(Z, n):
    mean_z = mean(Z, n)

    sum = 0
    for z in Z:
        sum += pow(z-mean_z, 2)
    
    return sqrt( sum / n )

def pearson_correlation(X, Y, n):
    standard_deviation_x = standard_deviation(X, n)
    standard_deviation_y = standard_deviation(Y, n)

    return covariance(X,Y,n) / (standard_deviation_x * standard_deviation_y)

def main():
    n = int(raw_input().strip())
    X = map(float, raw_input().strip().split(" "))
    Y = map(float, raw_input().strip().split(" "))

    print "%.3f" % pearson_correlation(X,Y,n)

main()
import math

def cumulative_distribution(mean, sd, x):
    return 0.5 * ( 1 + math.erf((x-mean)/(sd*math.sqrt(2))) )

def main():
    mean = 70
    sd = 10

    print "%.2f" % (100 * (1 - cumulative_distribution(mean, sd, 80)))
    failed = cumulative_distribution(mean, sd, 60)
    print "%.2f" % (100 * (1 - failed))
    print "%.2f" % (100 * failed)

main()
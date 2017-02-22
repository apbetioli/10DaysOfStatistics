import math

def main():
    mean = 20
    sd = 2

    print "%.3f" % cumulative_distribution(mean, sd, 19.5)
    print "%.3f" % (cumulative_distribution(mean, sd, 22) - cumulative_distribution(mean, sd, 20))

def cumulative_distribution(mean, sd, x):
    return 0.5 * ( 1 + math.erf((x-mean)/(sd*math.sqrt(2))) )

main()
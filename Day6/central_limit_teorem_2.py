import math

def cumulative_distribution(mean, sd, x):
    return 0.5 * ( 1 + math.erf((x-mean)/(sd*math.sqrt(2))) )

def main():
    total_tickets_left = 250
    purchases = 100
    mean = 2.4
    standard_deviation = 2.0

    u = purchases * mean
    sd = math.sqrt(purchases) * standard_deviation

    print "%.4f" % cumulative_distribution(u, sd, total_tickets_left)

main()
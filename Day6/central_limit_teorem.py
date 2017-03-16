import math

def cumulative_distribution(mean, sd, x):
    return 0.5 * ( 1 + math.erf((x-mean)/(sd*math.sqrt(2))) )

def main():
    elevator_capacity = 9800
    num_boxes = 49
    mean_box_weight = 205
    standard_deviation = 15

    u = num_boxes * mean_box_weight
    sd = math.sqrt(num_boxes) * standard_deviation

    print "%.5f" % cumulative_distribution(u, sd, elevator_capacity)

main()
from math import sqrt

def main():
    samples = 100
    mean = 500
    standard_deviation = 80
    p = .95
    z = 1.96

    #There is a mistake in the tutorial
    #Here are the correct values
    mean_sample = mean
    sd_sample = standard_deviation / sqrt(samples)

    A = mean_sample - z * sd_sample
    B = mean_sample + z * sd_sample

    print "%.2f" % A
    print "%.2f" % B

main()
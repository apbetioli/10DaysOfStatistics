from math import pow

def main():
    input = raw_input().split()
    mean_a = float(input[0])
    mean_b = float(input[1])

    estimated_cost_a = 160 + 40 * (mean_a + pow(mean_a, 2))
    estimated_cost_b = 128 + 40 * (mean_b + pow(mean_b, 2))

    print "%.3f" % estimated_cost_a
    print "%.3f" % estimated_cost_b

main()
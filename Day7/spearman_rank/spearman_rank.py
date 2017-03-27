from math import pow

def rank(Z, n):
    set_z = list(set(Z))
    set_z.sort()

    rank_map = {}
    for i in xrange(len(set_z)):
        rank_map[set_z[i]] = i+1

    R = []
    for z in Z:
        R.append(rank_map[z])

    return R


def sum_difference_rank_squared(Rx, Ry, n):
    sum = 0
    for i in xrange(n):
        sum += pow(Rx[i] - Ry[i], 2)
    return sum

def spearman_rank(Rx, Ry, n):
    return 1 - ( (6 * sum_difference_rank_squared(Rx, Ry, n)) / (n * (pow(n, 2) - 1)) )

def main():
    n = int(raw_input().strip())
    X = map(float, raw_input().strip().split(" "))
    Y = map(float, raw_input().strip().split(" "))

    Rx = rank(X, n)
    Ry = rank(Y, n)

    print "%.3f" % spearman_rank(Rx, Ry, n)

main()
def citire_fisier_kp(fisier):
    f = open(fisier, "r")
    n = int(f.readline())
    v = []
    w = []
    W = 0
    for x in f:
        values = x.split()
        if len(values) == 3:
            v.append(int(values[1]))
            w.append(int(values[2]))
        else:
            W = int(values[0])
    f.close()
    return n, v, w, W


def citire_fisier_tsp(fisier):
    f = open(fisier, "r")
    x = []
    y = []
    n = 0
    for strings in f:
        values = strings.split()
        if "DIMENSION:" in values:
            n = int(values[1])
        if len(values) == 3:
            x.append(int(values[1]))
            y.append(int(values[2]))
    f.close()
    return n, x, y


def write_fisier_kp(fisier, avgS, bestS, populationSize, genSize, p, pm, time_stamp):
    with open(fisier, 'w') as filetowrite:
        filetowrite.write("populationSize = " + str(populationSize) + "\n")
        filetowrite.write("genSize = " + str(genSize) + "\n")
        filetowrite.write("p = " + str(p) + "\n")
        filetowrite.write("pm = " + str(pm) + "\n")
        filetowrite.write("Average value " + str(avgS) + "\n")
        filetowrite.write("Best value " + str(bestS) + "\n")
        filetowrite.write("Time " + str(time_stamp) + "\n")

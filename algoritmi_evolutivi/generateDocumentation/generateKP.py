from ReadAndWrite import *
from KP import KP, KP_withGenBestAverage
import time
from statistics import mean


def generateKP(inputFile, populationSize, genSize, p, pm):
    values = []
    bestS = 0
    avgS = []
    n, v, w, W = citire_fisier_kp(inputFile)
    file = "/Users/andreivaran/PycharmProjects/algoritmi_evolutivi/generateDocumentation/outputKP/kp" + str(populationSize) + "_" + str(genSize) + "_" + str(p) + "_" + str(pm) + ".txt"
    start_time = time.time()
    for i in range(10):
        best, max, popid = KP(n, w, v, W, populationSize, genSize, p, pm)
        values.append(max)
        if max > bestS:
            bestS = max
        avgS.append(max)
    KP_withGenBestAverage(n, w, v, W, populationSize, genSize, p, pm)
    write_fisier_kp(file, mean(avgS), bestS, populationSize, genSize, p, pm, round(time.time() - start_time, 4))

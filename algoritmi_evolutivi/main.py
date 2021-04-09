from ReadAndWrite import citire_fisier_kp
from KP import KP
from generateDocumentation.generateKP import generateKP


def main():
    fisier = "rucsac-20.txt"
    n, v, w, W = citire_fisier_kp(fisier)
    populationSize = 100
    genNr = 50
    p = 60  # probabilitatea de uniform crossover
    pm = 0.05  # probabilitatea de mutatie tare in intervalul [0, 1]
    print("\nProblema rucsacului")
    KP(n, w, v, W, populationSize, genNr, p, pm)
    #populations = [1000, 2000, 3000]
    #generations = [500, 1000, 2000]
    #p_values = [30, 60, 90]

    #generateKP(fisier, 1000, 500, 30, 0.05)
    '''
    generateKP(fisier, 2000, 500, 30, 0.5)
    generateKP(fisier, 3000, 500, 30, 0.75)

    generateKP(fisier, 1000, 500, 60, 0.05)
    generateKP(fisier, 2000, 500, 60, 0.5)
    generateKP(fisier, 3000, 500, 60, 0.75)

    generateKP(fisier, 1000, 500, 90, 0.05)
    generateKP(fisier, 2000, 500, 90, 0.5)
    generateKP(fisier, 3000, 500, 90, 0.75)
    '''


if __name__ == '__main__':
    main()

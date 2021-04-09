import random
from statistics import mean
import matplotlib.pyplot as plt


def getGenerationAverage(generation, n, w, v, W):
    avg = []
    for cromozom in generation:
        s = eval(n, w, v, W, cromozom)
        avg.append(s)
    return mean(avg)


def getGenerationBest(generation, n, w, v, W):
    max = 0
    for cromozom in generation:
        s = eval(n, w, v, W, cromozom)
        if s > max:
            max = s
    return max


def getPopulationBest(population, n, w, v, W):
    max, popid = 0, 0
    best = []
    for r in range(len(population)):
        for t in range(len(population[r])):
            s = eval(n, w, v, W, population[r][t])
            if s > max:
                max = s
                popid = r
                best = population[r][t][:]
    return best, max, popid


def bitflip(val):
    if val == 0:
        val = 1
    else:
        val = 0
    return val


def populationEval(n, w, v, W, generation):
    evals = []
    for i in range(len(generation)):
        evals.append(eval(n, w, v, W, generation[i]))
    return evals


def eval(n, w, v, W, x):
    s = 0
    for i in range(len(w)):
        s += x[i] * w[i]
    if s > W or s == 0:
        return 0
    else:
        val = 0
        for j in range(n):
            val += v[j] * x[j]
        return val


def proportionateSelection(popEvals, generation):
    F = sum(popEvals)
    p = [round(popEvals[i]/F, 2) for i in range(len(popEvals))]
    parent1 = random.choices(generation, p, k=2)
    return parent1[0], parent1[0]


def miupluslambdaSelection(generation, populationSize, n, w, v, W):
    popEvals = populationEval(n, w, v, W, generation)
    new = [x for _, x in sorted(zip(popEvals, generation), key=lambda pair: pair[0], reverse=True)]
    new_generation = []
    for i in range(populationSize):
        new_generation.append(new[i])
    return new_generation


def uniformCrossover(parent1, parent2, p, n):
    child1 = []
    child2 = []
    for i in range(n):
        if round(random.uniform(0, 100), 2) < p:
            child1.insert(i, parent1[i])
            child2.insert(i, parent2[i])
        else:
            child1.insert(i, parent2[i])
            child2.insert(i, parent1[i])
    return child1, child2


def hardMutation(generation, pm):
    mutation = []
    for crom in generation:
        for i in range(len(crom)):
            q = random.uniform(0, 1)
            if q < pm:
                crom[i] = bitflip(crom[i])
        mutation.append(crom)
    return mutation


def KP(n, w, v, W, populationSize, genNr, p, pm):
    population = [([[random.randint(0, 1) for _ in range(n)] for _ in range(populationSize)])]
    for i in range(genNr):
        PX = []
        popEval = populationEval(n, w, v, W, population[i])
        for j in range(populationSize//2):
            parent1, parent2 = proportionateSelection(popEval, population[i])
            offset1, offset2 = uniformCrossover(parent1, parent2, p, n)
            PX.append(offset1)
            PX.append(offset2)

        PM = hardMutation(PX, pm)
        new_generation = miupluslambdaSelection(population[i] + PX + PM, populationSize, n, w, v, W)
        population.append(new_generation)

    best, max, popid = getPopulationBest(population, n, w, v, W)
    print("\nCea mai buna solutie este ")
    print(best)
    print("Valoarea maxima este: " + str(max))
    print("Aflata in generatia: " + str(popid))
    return best, max, popid


def KP_withGenBestAverage(n, w, v, W, populationSize, genNr, p, pm):
    population = [([[random.randint(0, 1) for _ in range(n)] for _ in range(populationSize)])]
    genBest = []
    genAverage = []
    for i in range(genNr):
        PX = []
        popEval = populationEval(n, w, v, W, population[i])
        for j in range(populationSize//2):
            parent1, parent2 = proportionateSelection(popEval, population[i])
            offset1, offset2 = uniformCrossover(parent1, parent2, p, n)
            PX.append(offset1)
            PX.append(offset2)

        PM = hardMutation(PX, pm)
        new_generation = miupluslambdaSelection(population[i] + PX + PM, populationSize, n, w, v, W)
        population.append(new_generation)
        genBest.append(getGenerationBest(new_generation, n, w, v, W))
        genAverage.append(getGenerationAverage(new_generation, n, w, v, W))
    xi = list(range(genNr))
    fig = plt.figure()
    best_plot, = plt.plot(xi, genBest, color='blue', linewidth='2', label='Best')
    average_plot, = plt.plot(xi, genAverage, color='red', linewidth='2', label='Average')
    plt.xlabel("Generations")
    plt.ylabel("Best/Avg Values per Generation")
    plt.legend(handles=[best_plot, average_plot], loc='center right')
    fig.suptitle("Population " + str(populationSize) + ", Generation " + str(genNr), fontsize=20)
    fig.savefig('/Users/andreivaran/PycharmProjects/algoritmi_evolutivi/generateDocumentation/outputKP/kpGeneration' + str(populationSize) + "_"
                + str(genNr) + "_" + str(p) + "_" + str(pm) + '.jpg')
    plt.show()
    best, max, popid = getPopulationBest(population, n, w, v, W)

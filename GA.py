import random
import math


def selection(population, generation):
    Fitness = []
    Best_Fitness = []
    for chromosome in population:
        individual_fitness = 21.5+chromosome[0]*(math.sin(4*math.pi*chromosome[0]))+chromosome[1]*(math.sin(20*math.pi*chromosome[1]))
        Fitness.append(individual_fitness)

    print()   
    Fitness = list(zip(Fitness, population))
    Fitness.sort(reverse=True)
    print()
    print('Fitness sorted:', Fitness)
    print()
    Best_Fitness = Fitness[0]
    Best.append(Best_Fitness)
    print('Best_Fitness',Best_Fitness)

    Fitness = Fitness[:8]
    return list(population)


def crossover(population):
    random.shuffle(population)
    fatherchromosome = population[:4]
    motherchromosome = population[4:]
    children = []
    for i in range(len(fatherchromosome)):
        crossoversite = random.randint(1,1)
        fatherfragments = [fatherchromosome[i][:crossoversite], fatherchromosome[i][crossoversite:]]
        motherfragments = [motherchromosome[i][:crossoversite], motherchromosome[i][crossoversite:]]
        firstchild = fatherfragments[0] + motherfragments[1]
        children.append(firstchild)
        secondchild = motherfragments[0] + fatherfragments[1]
        children.append(secondchild)
    return children


def mutation(population):
    mutatedchromosomes = []
    for chromosome in population:
        mutation_site = random.randint(0,1)
    if mutation_site == 0:
         chromosome[0] = random.uniform(a1,b1)
    else:
         chromosome[1] = random.uniform(a2,b2)
       
    mutatedchromosomes.append(chromosome)
    return mutatedchromosomes


def get_fit_chromosomes(generations):
    
    fit_chromosomes = []
    population=[[random.uniform(a1,b1) , random.uniform(a2,b2)] for j in range(pop)]
    print('first_population:',population)
    for generation in range(generations):
        generation += 1
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Generation:', generation)
        population = selection(population, generation)
        crossover_children = crossover(population)
        population = population + crossover_children
        mutated_population = mutation(population)
        population = population + mutated_population

        population.sort(reverse=True)
        population = population[:pop]
        random.shuffle(population)

        Best.sort(reverse=True)

    return fit_chromosomes

#values
a1= -3
b1= 12.1
a2= 4.1
b2= 5.8
pop= 10
gen= 100

Best = []
solution = get_fit_chromosomes(gen)

print()
print('-----------Final-----------')
print('Best_Fitnesses:',Best)
print()
print('The_Best_Fitness_in_all_generations:', Best[0])


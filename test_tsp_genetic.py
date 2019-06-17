from graph.Graph import Graph
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import operator
import random

os.system('clear')
graph = Graph.creategraph(20, 1.0, directed=False)
cities = graph.vertex


class City:
    def __init__(self, id):
        self.id = id

    def distance(self, id):
        return graph.get_weight(self.id, id)


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def route_distance(self):
        if self.distance == 0:
            path_distance = 0
            for i in range(0, len(self.route)):
                from_city = self.route[i]
                to_city = self.route[i + 1] if i + 1 < len(self.route) else self.route[0]

                path_distance += from_city.distance(to_city.id)
            self.distance = path_distance
        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness


def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route


def initial_population(pop_size, city_list):
    population = []

    for _ in range(0, pop_size):
        population.append(create_route(city_list))
    return population


def rank_routes(population):
    fitness_results = {}
    for i in range(0, len(population)):
        fitness_results[i] = Fitness(population[i]).route_fitness()
    return sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=True)


def selection(pop_ranked, elite_size):
    selection_results = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, elite_size):
        selection_results.append(pop_ranked[i][0])
    for _ in range(0, len(pop_ranked) - elite_size):
        pick = 100 * random.random()
        for i in range(0, len(pop_ranked)):
            if pick <= df.iat[i, 3]:
                selection_results.append(pop_ranked[i][0])
                break
    return selection_results


def mating_pool(population, selection_results):
    mating_pool_array = []
    for i in range(0, len(selection_results)):
        index = selection_results[i]
        mating_pool_array.append(population[index])
    return mating_pool_array


def breed(parent1, parent2):
    child_p1 = []

    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))

    for i in range(min(gene_a, gene_b), max(gene_a, gene_b)):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    child = child_p1 + child_p2
    return child


def breed_population(mating_pool_array, elite_size):
    children = []
    length = len(mating_pool_array) - elite_size
    pool = random.sample(mating_pool_array, len(mating_pool_array))

    for i in range(0, elite_size):
        children.append(mating_pool_array[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(mating_pool_array) - i - 1])
        children.append(child)

    return children


def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swap_with]

            individual[swapped] = city2
            individual[swap_with] = city1

    return individual


def mutate_population(population, mutation_rate):
    mutated_pop = []

    for ind in range(0, len(population)):
        mutated_ind = mutate(population[ind], mutation_rate)
        mutated_pop.append(mutated_ind)

    return mutated_pop


def nextGeneration(current_gen, elite_size, mutation_rate):
    pop_ranked = rank_routes(current_gen)
    selection_results = selection(pop_ranked, elite_size)
    mating_pool_array = mating_pool(current_gen, selection_results)
    children = breed_population(mating_pool_array, elite_size)
    next_generation = mutate_population(children, mutation_rate)

    return next_generation


def geneticAlgorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)
    progress = []
    progress.append(1 / rank_routes(pop)[0][1])

    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))

    for _ in range(0, generations):
        pop = nextGeneration(pop, elite_size, mutation_rate)
        progress.append(1 / rank_routes(pop)[0][1])

    print("Final distance: " + str(1 / rank_routes(pop)[0][1]))
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

    return best_route


cityList = []
for gr_city in cities:
    cityList.append(City(id=gr_city))


geneticAlgorithm(
    population=cityList,
    pop_size=100,
    elite_size=20,
    mutation_rate=0.01,
    generations=500
)




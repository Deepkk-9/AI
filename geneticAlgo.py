import random

def generate_individual(length):
    return [random.uniform(0, 10) for _ in range(length)]

def generate_population(population_size, individual_length):
    return [generate_individual(individual_length) for _ in range(population_size)]

def fitness(individual, target):
    return -sum([(a - b)**2 for a, b in zip(individual, target)])

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate):
    mutated_individual = [gene + random.uniform(-mutation_rate, mutation_rate) for gene in individual]
    return mutated_individual

def genetic_algorithm(target, population_size, individual_length, generations, mutation_rate):
    population = generate_population(population_size, individual_length)

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x, target), reverse=True)

        best_individual = population[0]
        best_fitness = fitness(best_individual, target)

        print(f"Generation {generation + 1}: Best Individual = {best_individual}, Fitness = {best_fitness}")

        if best_fitness == 0:
            print(f"Target reached in generation {generation + 1}")
            break

        new_population = [best_individual]

        for _ in range(1, population_size):
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    print("Best individual:", best_individual)

# Example usage
target_list = [3, 2, 4, 5]
population_size = 10
individual_length = len(target_list)
generations = 10
mutation_rate = 0.1

genetic_algorithm(target_list, population_size, individual_length, generations, mutation_rate)

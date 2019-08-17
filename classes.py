from math import floor
from random import random, randint

def map(input_value, in1, in2, out1, out2): # standart map fonksiyonu
    return (input_value - in1) * (out2 - out1) / (in2 - in1) + out1

def new_char():
    c = randint(63, 122)
    if c == 63: c = 32
    if c == 64: c = 46
    return chr(c)

class Chromosome:
    def __init__(self, _target):
        self.genes = []
        self.fitness = 0
        self.target = _target
        for i in range(len(self.target)):
            self.genes.append(new_char())

    def fit_func(self): # uygunluk fonksiyonu
        score = 0
        for gene, _target in zip(self.genes, self.target):
            if gene == _target:
                score += 1
        self.fitness = score / len(self.target)

    def crossover(self, partner):
        child = Chromosome(self.target)
        mid_point = randint(0, len(self.genes)-1)
        for i in range(len(self.genes)):
            if i > mid_point: child.genes[i] = self.genes[i]
            else: child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random() < mutation_rate:
                self.genes[i] = new_char()

    def get_phrase(self):
        return "".join(self.genes)

class Monkeys:
    def __init__(self, pop_size, m_rate, target):
        self.mutation_rate = m_rate
        self.generation = 0
        self.best_score_global = 1
        self.best_score_local = 0
        self.best_phrase = ""
        self.is_finished = False
        self.mating_pool = []

        self.monkeys = []
        for i in range(pop_size):
            self.monkeys.append(Chromosome(target))

        self.calc_fitness()

    def calc_fitness(self):
        _max = 0
        for monkey in self.monkeys:
            monkey.fit_func()
            if monkey.fitness > _max:
                _max = monkey.fitness
        self.best_score_local = _max

    def natural_selection(self):
        self.mating_pool = []
        for monkey in self.monkeys:
            fitness = map(monkey.fitness, 0, self.best_score_local, 0, 1)
            n = floor(fitness * 100)
            for i in range(n):
                self.mating_pool.append(monkey)

    def generate(self):
        m_pool_size = len(self.mating_pool) - 1
        for x in range(len(self.monkeys)):
            i = randint(0, m_pool_size)
            j = randint(0, m_pool_size)
            partner1 = self.mating_pool[i]
            partner2 = self.mating_pool[j]
            child = partner1.crossover(partner2)
            child.mutate(self.mutation_rate)
            self.monkeys[x] = child
        self.generation += 1

    def evaluate(self):
        local_best = 0
        index = 0
        for i in range(len(self.monkeys)):
            if self.monkeys[i].fitness > local_best:
                index = i
                local_best = self.monkeys[i].fitness

        self.best_phrase = self.monkeys[index].get_phrase()
        if local_best == self.best_score_global:
            self.is_finished = True

    def get_average(self):
        count = 0
        for member in self.monkeys:
            count += member.fitness
        return count / len(self.monkeys)

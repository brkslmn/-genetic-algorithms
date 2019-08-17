from time import time

from classes import Monkeys
print("---------------------------------------------")

phrase_input = input("Enter a word or phrase : ")

print("---------------------------------------------")

#Change Here!
max_generation = 1000
population_size = 200
mutation_rate = 0.01


phrase = phrase_input

monkeys = Monkeys(population_size, mutation_rate, phrase)

print("1-Best_Genes\t2-Average_of_Fitness", "\n","="*50)

count = 0
start = time()
while count < max_generation:
    monkeys.natural_selection()
    monkeys.generate()
    monkeys.calc_fitness()
    monkeys.evaluate()

    print(monkeys.best_phrase,"\t",monkeys.get_average())
    count +=1
    if monkeys.is_finished:
        end = time()
        print("\nTerminated", "//",
            "Generation:", str(monkeys.generation), "//",
            "Time elapsed:", "{0:.2f}".format(end-start), "seconds")

        break

if monkeys.is_finished == False:
    print ('Monkey dont write this phrase')


input("Press a key to exit")

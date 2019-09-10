from deap import tools
from deap import creator
from deap import base
from word import Word
import random

MUP = 0.2  # Mutation Propability
CRPB = 0.6  # Cross Propability


class Gene:
    def __init__(self, word):
        self.correct_word = word
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)
        self.toolbox = self.create_toolbox()

    def create_toolbox(self):
        toolbox = base.Toolbox()
        toolbox.register("word", Word.randomize, len(self.correct_word))
        toolbox.register("individual", tools.initIterate, creator.Individual , toolbox.word)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)
        toolbox.register("evaluate", self.evaluate_word)
        toolbox.register("cross", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
        toolbox.register("select", tools.selTournament, tournsize=5)
        return toolbox

    def evaluate_word(self, indiv):
        score = 0
        for x in range(len(indiv)):
            if self.correct_word[x] == indiv[x]:
                score += 1
        return score/len(self.correct_word),

    def run_population(self):
        # evaluate whole population
        pop = self.toolbox.population(500)
        fitnesses = list(map(self.toolbox.evaluate, pop))
        for ind, fit in zip(pop, fitnesses):
            ind.fitness.values = fit
        fits = [ind.fitness.values[0] for ind in pop]
        generation = 0
        while max(fits) < 1 and generation <300:
            generation+=1
            print("Generation number: {}".format(generation))
            offsprings = self.toolbox.select(pop, len(pop))
            offsprings = list(map(self.toolbox.clone, offsprings))

            for kid, sec_kid in zip(offsprings[::3], offsprings[1::3]):
                if random.random() < CRPB:
                    self.toolbox.cross(kid, sec_kid)
                    del kid.fitness.values
                    del sec_kid.fitness.values

            for mutant in offsprings:
                if random.random() < MUP:

                    self.toolbox.mutate(mutant)
                    del mutant.fitness.values

            changed = [ind for ind in offsprings if not ind.fitness.valid]
            fitnesses = map(self.toolbox.evaluate, changed)
            for ind, fit in zip(changed, fitnesses):
                ind.fitness.values = fit


            pop[:] = offsprings

            fits = [ind.fitness.values[0] for ind in pop]
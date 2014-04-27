import myHelpers
import random
from operator import add

"""
	ascii(B) = 66
	ascii(L) = 76
	ascii(R) = 82
	Media dos ASCIIs, 74.66, arredondando pra baixo 74
	Somatorio de 1 + 2 + 3 + 4 + 5 = 15
	Numero magico eh 74 + 15 = 89
"""
magical_number = 89
first_options = ['B','L','R']
second_opstions = [1,2,3,4,5]
all_individuals = myHelpers.getIndividualsFromCSV("balance-scale.csv")


def balance(individual, target=magical_number):
	"""
		Funcao de criterio, o quanto mais proximo de 0 melhor
	"""
	numbersSum = []
	numbersSum.append(ord(individual[0]))
	for x in xrange(1,len(individual)):
		numbersSum.append(int(individual[x]))
	totalSum = reduce(add, numbersSum)
	return abs(target-totalSum)

def grade(pop, target=magical_number):
    """
    	Achando media da populacao
    """
    summed = reduce(add, (balance(x, target) for x in pop), 0)
    return summed / (len(pop) * 1.0)

def evolution(pop, target=magical_number, retain=0.2, random_select=0.05, mutate=0.01):
	"""
		retain = porcentagem da populacao escolhida
		random_select = porcentagem da populacao aleatoreamente escolhida
		mutate = porcentagem da populacao que sofre mutacao
	"""
	graded_population = [ (balance(x, target), x) for x in pop]
	graded_population = [ x[1] for x in sorted(graded_population)]
	amount_to_catch = int(len(graded_population)*retain)
	parents = graded_population[:amount_to_catch]

	"""
		Randomicamente adicionando individuos para promover uma diversificacao genetica
	"""
	for individual in graded_population[amount_to_catch:]:
		if random_select > random.random():
			parents.append(individual)

	"""
    	Randomicamente realisando mutacao em alguns individuos
	"""
	for individual in parents:
		if mutate > random.random():
			pos_to_mutate = random.randint(0, len(individual)-1)
			if pos_to_mutate == 0:
				individual[pos_to_mutate] = random.choice(first_options)
			else:
				individual[pos_to_mutate] = random.choice(second_opstions)

	"""
		Realisando Crossover dos pais para criar os filhos
	"""
	parents_length = len(parents)
	children_length = len(pop) - parents_length
	children = []
	while len(children) < children_length:
		male_index = random.randint(0, parents_length-1)
		female_index = random.randint(0, parents_length-1)
		if male_index != female_index:
			male = parents[male_index]
			female = parents[female_index]
			index_to_split = int(len(male) / 2)
			child = male[:index_to_split] + female[index_to_split:]
			children.append(child)
	"""
		Adicionando os filhos gerados para formar uma nova populacao
	"""
	parents.extend(children)
	return parents


"""
	Main do programa
"""
print "Tamanho da populacao = %d" % (len(all_individuals))
population = all_individuals
balance_history = [grade(population)]

for x in xrange(100):
	population = evolution(population, magical_number)
	population_balance_grade = grade(population)
	balance_history.append(population_balance_grade)
	if population_balance_grade == 0:
		print "Solucao perfeita alcancada na %d geracao" % (x)

print "Historico de evolucao"
print balance_history
import myHelpers
from operator import add
#
#	ascii(B) = 66
#	ascii(L) = 76
#	ascii(R) = 82
#	Media dos ASCIIs, 74.66, arredondando pra baixo 74
# 	Somatorio de 1 + 2 + 3 + 4 + 5 = 15
#	Numero magico eh 74 + 15 = 89
#
magicalNumber = 89

def balance(individual, target=magicalNumber):
	print individual
	numbersSum = []
	numbersSum.append(ord(individual[0]))
	for x in xrange(1,len(individual)):
		numbersSum.append(int(individual[x]))
	totalSum = reduce(add, numbersSum)
	return abs(target-totalSum)

individuals = myHelpers.getIndividualsFromCSV("balance-scale.csv")


print balance(individuals[4])
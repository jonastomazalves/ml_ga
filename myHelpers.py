#
#	Pegando individuos do CSV
#	ex: [[B,1,2,3,4],[L,2,2,2,2],...,[R,5,5,5,5]]
#
def getIndividualsFromCSV( path ):
	individuals = []
	for line in open(path):
		line = line.strip()
		individuals.append(line.split(","))

	return individuals


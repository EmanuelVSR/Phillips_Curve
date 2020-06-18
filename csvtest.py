import csv
from matplotlib import pyplot as plt 

inflacao_axis = []

with open('Inflacao.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file) 

	next(csv_reader)

	for line in csv_reader:
		inflacao_axis.append(float(line[1]))

desemprego_axis = []

with open('Desemprego.csv', 'r') as csv_file2:
	csv_reader = csv.reader(csv_file2, delimiter = ';')

	next(csv_reader)

	for line in csv_reader:
		desemprego_axis.append(float(line[1]))

var_inflacao =[]

for i, x in enumerate(inflacao_axis):
	if i == 0:
		var_inflacao.append(0)
	else:
		var_inflacao.append(x - inflacao_axis[i-1])

plt.scatter(desemprego_axis, var_inflacao)

plt.show()





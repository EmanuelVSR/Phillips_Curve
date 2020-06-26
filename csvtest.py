import numpy as np
import pandas_datareader.data as web
import datetime
import csv
from matplotlib import pyplot as plt 
import fredpy as fp

fp.api_key = '47b3a184f8dbe8714935811e31147c19'


def linear_regression(x, y):
	x_mean = np.mean(x)
	y_mean = np.mean(y)

	size = len(x)
	numer = 0 
	denom = 0 

	for i in range(size):
		numer += (x[i] - x_mean) * (y[i] - y_mean)
		denom += (x[i] - x_mean) ** 2 

	m_equation = numer / denom
	c_equation = y_mean - (m_equation * x_mean)

	return m_equation, c_equation

def FredList(ticker, win, freq):
	
	i = fp.series(ticker)
	
	if i.frequency_short != freq:
		i = i.as_frequency(freq,'mean')

	i2 = i.window(win)
	i_list = i2.data.tolist()

	return i_list

win = ['1970-01-01', '2006-01-01']

u = FredList('UNRATE', win, 'A')
p = FredList('FPCPITOTLZGUSA', win, 'A')

# inflacao_axis = []

# with open('Inflacao.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file) 

# 	next(csv_reader)

# 	for line in csv_reader:
# 		inflacao_axis.append(float(line[1]))

# desemprego_axis = []

# with open('Desemprego.csv', 'r') as csv_file2:
# 	csv_reader = csv.reader(csv_file2, delimiter = ';')

# 	next(csv_reader)

# 	for line in csv_reader:
# 		desemprego_axis.append(float(line[1]))

var_inflacao =[]

for i, x in enumerate(p):
	if i == 0:
		var_inflacao.append(0)
	else:
		var_inflacao.append(x - p[i-1])

print(var_inflacao)

#returns m and c 
regression_formula = linear_regression(u, var_inflacao)
m_equation = round(regression_formula[0], 4)
c_equation = round(regression_formula[1], 4)

print_formula = 'y =' + str(m_equation) + 'x + ' + str(c_equation)
print(print_formula)

#creates regression line 
x = np.linspace(4, 10, 100)
y = m_equation * x + c_equation

#plots scatter and regression line
plt.scatter(u, var_inflacao)
plt.plot(x, y, label= print_formula)
plt.legend(loc='upper left')
plt.show()






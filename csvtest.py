import numpy as np
#import pandas_datareader.data as web
import datetime
import csv
from matplotlib import pyplot as plt 
import fredpy as fp

fp.api_key = '47b3a184f8dbe8714935811e31147c19'


## Formula da regressão linear, retorna m,c da equação
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

## Formula usada para retirar e manipular dados históricos diretos do FRED
def FredList(ticker, win, freq):
	
	i = fp.series(ticker)
	
	if i.frequency_short != freq:
		i = i.as_frequency(freq,'mean')

	i2 = i.window(win)
	i_list = i2.data.tolist()

	return i_list


#Janela de tempo desejada. Formato AAAA-MM-DD.
win = ['1990-01-01', '2015-01-01']

## Obtem dados de desemprego, inflação. Os parâmetros são ticker(encontrado no site do FRED),
## janela de tempo e frequência abreviada('A', 'M', 'W', 'D')
u = FredList('UNRATE', win, 'A')
p = FredList('FPCPITOTLZGUSA', win, 'A')

## O modelo de curva de Phillips aceleracionista usa a variação da inflação
var_inflacao =[]
for i, x in enumerate(p):
	if i == 0:
		var_inflacao.append(0)
	else:
		var_inflacao.append(x - p[i-1])

# Retorna m e c da equação linear
regression_formula = linear_regression(u, var_inflacao)
m_equation = round(regression_formula[0], 4)
c_equation = round(regression_formula[1], 4)

print_formula = 'y =' + str(m_equation) + 'x + ' + str(c_equation)
print(print_formula)

# Cria a linha da regressão linear para o gráfico
x = np.linspace(4, 10, 100)
y = m_equation * x + c_equation

# Plota gráfico e regressão
plt.scatter(u, var_inflacao)
plt.plot(x, y, label= print_formula)
plt.legend(loc='upper left')
plt.show()






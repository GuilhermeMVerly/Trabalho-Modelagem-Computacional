import numpy as np
import matplotlib.pyplot as plt
import math

pontos = np.array(([300.0, 320.0, 340.0, 360.0, 380.0, 400.0, 420.0, 440.0, 460.0, 480.0, 500.0, 520.0, 540.0, 560.0, 580.0, 600.0, 620.0, 640.0, 660.0, 680.0, 700.0], [5002.39, 4596.20, 4256.56, 3889.62, 3661.76, 3542.03, 3344.48, 3246.15, 3255.30, 3243.25, 3137.67, 3155.84, 3142.69, 3064.64, 3213.86, 3321.36, 3382.10, 3439.77, 3506.81, 3721.41, 3681.15]))

##grau = int(input(f"Digite o grau do polinômio desejado: "))
grau = 4
print(f"Utilizando o Método dos Mínimos Quadrados para encontra um polinômio de grau 4.\n")

sistema = np.zeros(((grau + 1), (grau + 1)))
resposta = np.zeros(grau + 1)
exp = 1
num_pontos = len(pontos[0])

## Algoritmo para montar a matriz dos coeficientes
for lin in range(0, grau + 1):
    for col in range(0, grau + 1):
        if lin == 0: ## Primeira Linha
            if col == 0:
                sistema[0,0] = num_pontos
            else :
                for s in range(num_pontos):
                    sistema[lin, col] += pontos[0, s] ** exp
                exp += 1
        else: ## Demais linhas
            if col != grau:
                sistema[lin, col] = sistema[lin - 1, col + 1]
            else :
                for s in range(num_pontos):
                    sistema[lin, col] += pontos[0, s] ** exp
                exp += 1

exp = 0
## Algoritmo para montar a matriz resposta
for lin in range(grau + 1):
    for s in range(num_pontos):
        resposta[lin] += (pontos[0, s] ** exp) * pontos[1, s]
    exp += 1



for i in range (0, grau + 1):
    for j in range (0, grau + 1):
        sistema[i, j] = float(input(f"Digite o número da linha {i} e coluna {j}: "))

for i in range(0, grau + 1):
    resposta[i] = float(input(f"Digite a igualdade da linha {i}: "))



## Algoritmo da eliminação de Gauss
for lin in range (grau):
    for lind in range(lin + 1, grau + 1):
        m = sistema[lind, lin]/sistema[lin, lin]
        for col in range (grau + 1):
            sistema[lind, col] -= sistema[lin, col]*m
            ##print(sistema)
        resposta[lind] -= resposta[lin]*m


## Algoritmo para retrosubstituição para conseguir o resultado das incógnitas.
for i in range (grau, -1, -1):
    for j in range (grau, i, -1):
        resposta[i] -= sistema[i,j] * resposta[j]
        ###print(resposta)
    resposta[i] /= sistema[i, i]

## Printa o polinômio
polin = "f(x) = "
for i, coef in enumerate(resposta):
    if i == 0:
        polin += f"{coef}"
    if coef > 0:
        polin += f" + {coef}x^{i}"
    else :
        polin += f" {coef}x^{i}"
print(polin, "\n")

## Função obtido pelo mmq
def Polinomio(x):
    y = 0
    for i in range(grau + 1):
        y += resposta[i] * x**i
    return y

## Calculo do erro do ajuste Polinomial
err_quad = 0

for i in range(num_pontos):
    err_quad += (pontos[1, i] - Polinomio(pontos[0, i])) ** 2

print(f"O quadrado do erro do ajuste é de {err_quad}\n")

## Função dada D = 0.006V² + 405333333.3333(1/v²)
def F_Analitica(x):
    return 0.006 * x*2 + (0.95(16000*2))/(0.6(x**2))


## Seção Áurea do Polinomio
xl = 400
xu = 600
R = (math.sqrt(5) - 1)/2 ## Número de ouro
d = (xu - xl)*R
x1 = xl + d
x2 = xu - d
tol = 0.000001
err = xu - xl
n = 0
while err > tol and n < 200:
    n += 1
    if Polinomio(x1) > Polinomio(x2):
        xu = x1
        x1 = x2
        d = (xu - xl)*R
        x2 = xu - d
        err = xu - xl
    else:
        xl = x2
        x2 = x1
        d = (xu - xl)*R
        x1 = xl + d
        err = xu - xl
min_pol = (xu + xl)/2
print(f"Pelo método da seção áurea utilizado na aproximação polinomial o arrasto mínimo é de {Polinomio(min_pol)} com a velocidade de {min_pol}\n")

## Seção Áurea da Função Analítica.
xl = 400
xu = 600
R = (math.sqrt(5) - 1)/2 ## Número de ouro
d = (xu - xl)*R
x1 = xl + d
x2 = xu - d
tol = 0.000001
err = xu - xl
n = 0
while err > tol and n < 200:
    n += 1
    if F_Analitica(x1) > F_Analitica(x2):
        xu = x1
        x1 = x2
        d = (xu - xl)*R
        x2 = xu - d
        err = xu - xl
    else:
        xl = x2
        x2 = x1
        d = (xu - xl)*R
        x1 = xl + d
        err = xu - xl
min_analitica = (xu + xl)/2
print(f"Pelo método da seção áurea utilizado na função analítica o arrasto mínimo é de {F_Analitica(min_analitica)} com a velocidade de {min_analitica}\n")

## Calculo dos desvios entre a função dada e a aproximação polinomial
desviopad = 0
for i in range(num_pontos):
    desviopad += (F_Analitica(pontos[0, i]) - Polinomio(pontos[0, i]))**2
desviopad = (desviopad/num_pontos)**0.5
print(f"O desvio padrão da aproximação linear em relação a função analítica é de {desviopad}.\n")

## Calcula o y da aproximação polinomial
yfunction_pol = np.zeros(num_pontos)

for y in range(num_pontos):
    for g in range(grau + 1):
        yfunction_pol[y] += resposta[g] * pontos[0, y] ** g

## Calcula o y da função analítica
yfunction_analitica = np.zeros(num_pontos)

for y in range(num_pontos):
    yfunction_analitica[y] = F_Analitica(pontos[0, y])

plt.plot(min_analitica, F_Analitica(min_analitica), 'o', color='grey', label='Ponto Mínimo da Função Analítica')
plt.plot(min_pol, Polinomio(min_pol), 'o', color='brown', label='Ponto Mínimo da Aproximação Polinomial')
plt.plot(pontos[0], pontos[1],'o', color='blue', label='Dados Originais')
plt.plot(pontos[0], yfunction_pol, color = 'r', label='Ajuste Polinomial')
plt.plot(pontos[0], yfunction_analitica, color = 'green', label='Função Analítica')

plt.legend()

aux = plt.xlabel("Velocidade")
aux = plt.ylabel("Arrasto")

plt.show()
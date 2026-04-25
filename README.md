**Trabalho- Modelagem Computacional**

**Membros: Alessandro Cardinot Bernardo da Silveira e Guilherme Munhooz Verly**

Em engenharia, frequentemente são utilizados métodos quantitativos para a resolução de problemas de aplicação, visto que em geral as equações que descrevem os fenômenos e dependências físicas são de difícil resolução analítica ou são de elevado dispêndio computacional. No caso considerado foram obtidas medidas experimentais para o arrasto total de um aerofólio como função de sua velocidade, utilizando-se de dois métodos distintos que permitiram estipular uma previsibilidade matemática ao conjunto de dados obtidos.

Inicialmente, estavamos interessados em saber qual seria a velocidade ótima que minimize o arrasto total do aerofólio.
Para esta tarefa, foram realizadas as análises acerca dos itens abaixo:

(i) Determinar o grau do polinômio que melhor se ajustaria aos dados disponíveis, por meio de um estimador de mínimos
quadrados;

(ii) Utilizar o polinômio obtido para computar o valor ótimo da velocidade que fornece o mínimo arrasto total,
usando um qualquer método de otimização de nossa escolha;

Foi considerado o modelo dado pela equação abaixo, que se estima o arrasto total de um aerofólio fornecido pela literatura:

$𝐷 = 0,01𝜎𝑉^2 + \frac{0,95}{𝜎}\frac{(W)^2}{(V^2)} $

onde 𝐷 é o arrasto, 𝜎 é a razão da densidade do ar entre a altitude de vôo e o nível do mar, 𝑊 é o peso e 𝑉 é a velocidade.

Para 𝜎 = 0,6 e 𝑊 = 16.000,foi buscado determinar:

(i) O arrasto mínimo e a velocidade na qual ele ocorre;

(ii) Comparar o resultado obtido com a solução computada pelo algoritmo usando a aproximação por mínimos quadrados;

(iii) Calcular os desvios entre o modelo da equação acima e o modelo aproximado usando o estimador de mínimos
quadrados, para as velocidades em que há medidas disponíveis.

(iv) Forneer as curvas de ambas as aproximações sobrepostas, assim como os dados analisados.


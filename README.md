Trabalho- Modelagem Computacional

Considere que temos disponíveis os dados abaixo, que representam medidas do arrasto total de um aerofólio (𝐷) em
função da velocidade (𝑉):
𝑉 300,0 320,0 340,0 360,0 380,0 400,0 420,0 440,0 460,0 480,0 500,0
𝐷 5002,39 4596,20 4256,56 3889,62 3661,76 3542,03 3344,48 3246,15 3255,30 3243,25 3137,67
𝑉 520,0 540,0 560,0 580,0 600,0 620,0 640,0 660,0 680,0 700,0 –
𝐷 3155,84 3142,69 3064,64 3213,86 3321,36 3382,10 3439,77 3506,81 3721,41 3681,15 –
Inicialmente, estamos interessados em saber qual seria a velocidade ótima que minimize o arrasto total do aerofólio.
Para esta tarefa, faça as análises acerca dos itens abaixo:
(i) Determine o polinômio que melhor se ajusta aos dados disponíveis, por meio de um estimador de mínimos
quadrados;
(ii) Utilize o polinômio obtido para computar o valor ótimo da velocidade que fornece o mínimo arrasto total,
usando qualquer método de otimização da sua escolha;
Agora considere o modelo dado pela equação abaixo, que estima o arrasto total de um aerofólio,
𝐷 = 0,01𝜎𝑉! +
0,95
𝜎 -
𝑊
𝑉 /
!
onde 𝐷 é o arrasto, 𝜎 é a razão da densidade do ar entre a altitude de vôo e o nível do mar, 𝑊 é o peso e 𝑉 é a velocidade.
Se 𝜎 = 0,6 e 𝑊 = 16.000, determine:
(i) O arrasto mínimo e a velocidade na qual ele ocorre;
(ii) Compare o resultado obtido com a solução computada usando a aproximação por mínimos quadrados;
(iii) Calcule os desvios entre o modelo da equação acima e o modelo aproximado usando o estimador de mínimos
quadrados, para as velocidades em que há medidas disponíveis.
(iv) Forneça as curvas de ambas as aproximações sobrepostas, assim como os dados analisados.
(v) Discuta os pontos positivos e negativos de como a aproximação por mínimos quadrados pode ser útil neste
problema.

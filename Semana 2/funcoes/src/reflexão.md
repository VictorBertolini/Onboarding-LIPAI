# Questões a serem pensadas sobre o módulo `Funções`

### Qual função é mais flexível em relação ao uso: a do ex01 (que imprime) ou a do ex02 (que retorna o valor)? Por quê?

A mais flexível é a do ex02, dado que ela retorna o valor, o qual poderá ser utilizado em N outras aplicações, dando liberdade ao programador decidir se o resultado será usado em um outro cálculo ou salvar em algum local ou mesmo imprimir na tela. 

### Qual abordagem é mais flexível: a do ex02 (3 parâmetros fixos) ou a do ex03/ex04 (que permitem número variável de argumentos)?

A abordagem que permite um número variável de argumentos é muito mais flexível, visto que consegue se adaptar aos mais diferentes cenários e conjunto de valores, diferente do número fixo de parâmetros, que não permite utilizar nem mais e nem menos argumentos.

### As funções do ex03 e ex04 permitem enviar um número variável de parâmetros (tupla ou *args). Em que situações você prefere cada forma? Justifique.

Prefiro o uso de tupla quando adoto uma abordagem em que os parâmetros permanecem fixos ao longo do programa, partindo do princípio de que esse tipo de estrutura promove uma melhor organização do código. Embora ainda ofereça flexibilidade ao programador, a tupla impõe restrições próprias do tipo de dado `tuple`, o que contribui para maior previsibilidade e controle.
Já o uso de `*args` fornece uma liberdade máxima na definição da função, permitindo a passagem de um número arbitrário de parâmetros. Essa flexibilidade, entretanto, exige maior cuidado, especialmente em funções e aplicações mais complexas, pois demanda verificações adicionais e tratamento de possíveis erros. Ainda assim, quando utilizado de forma coerente, *args pode ser bastante útil para lidar tanto com pequenos quanto com grandes conjuntos de dados de maneira dinâmica.









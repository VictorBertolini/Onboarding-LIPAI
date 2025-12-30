# Questões do Módulo `arquivos` para serem refletidas

### Qual a vantagem de transformar cada linha do arquivo em dicionários em vez de trabalhar apenas com strings?

A vantagem clara é a organização e facilidade em encontrar uma informação dentro dos dicionários criados, trabalhar com strings tende a ser mais simples que pensar na conversão para dicionário, mas em um projeto um pouco maior e com um pouco mais de complexidade pode ser muito custoso trabalhar com os dados sem estarem organizados e sem uma facilidade em encontrar alguma informação dentro dos inúmeros dados.

### Em que situações pode ser útil retornar uma tupla de registros (como nos exercícios ex01 e ex02) em vez de apenas uma lista de linhas?


Pode ser útil quando se deseja manter os dados fixos, adicionar uma camada de segurança extra nos dados afim de que eles não sejam modificados em outra parte do código, eles são processados, "limpos" (como tirar espaços em branco ou letras maiúsculas) e depois armazenados em tuplas, as quais materão a imutabilidade deles durante o restante do programa.


### O que você achou mais desafiador: ler o arquivo ou transformar as linhas em estruturas de dados (dicionários)?

Achei mais desafiador transformar as linhas em estruturas de dados, visto que há uma necessidade de pensar a mais, enquanto ler o arquivo é um passo a passo já praticamente pré definido.


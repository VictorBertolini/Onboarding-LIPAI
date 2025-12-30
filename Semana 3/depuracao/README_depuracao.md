# Semana 2 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: 

## Código das videoaulas

### Aula 1 e 2 - Debug com `pdb` e `Vs code`

```python
""" Aula 01 e Aula 02 - Debug """

def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1, n2, n3):
    soma = somar(n1, n2, n3)
    media = soma / 3
    return media

# breakpoint()

nota1 = 10.0
nota2 = 3.0
nota3 = 5.5

media = calcular_media(nota1, nota2, nota3)
print(media)
```
---

### 
# Reflexão - Questões a serem pensadas sobre o módulo `Depuração`

### O que você conseguiu enxergar no debugger que não ficava tão claro apenas executando o programa normalmente (sem depuração)?

Foi possível observar o código em execução linha a linha, podendo entender a linha que ele se encontra e analisar os valores envolvidos, as variáveis locais, os parâmetros que estavam entrando nas funções.

### Em quais situações você acha mais prático usar o pdb pela linha de comando e em quais prefere o debugger visual do VS Code?

Além do uso obrigatório do debugger do VS Code em situações que não é 100% liberado lidar com o código diretamente. Achei mais prático o uso do pdb quando preciso de algo mais rápido, pois ele para passar linha a linha precisa colocar `next` ou mesmo `step` para adentrar as funções, já o debugger do próprio vs code eu vejo como mais vantajoso, pois sua forma de clicks com o mouse torna mais rápido quando se quer verificar uma linha e depois passar uma grande quantidade de linhas, sinto um controle maior do andamento da aplicação ao invés de ficar lidando com a linha de comando.

### Houve algum erro ou comportamento inesperado nos seus exercícios que você só percebeu por causa da depuração? Descreva brevemente.

Não houve nenhum comportamento inesperado, todavia foi interessante ver visualmente a linha de execução dos programas, ainda que simples, ver passando função por função, vendo a mudança dos parâmetros.
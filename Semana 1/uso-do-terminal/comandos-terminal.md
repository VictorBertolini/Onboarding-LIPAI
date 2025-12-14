# Comandos básicos Bash
## Comandos para Navegação
### Achar Diretório Atual
```bash
pwd
```

### Listar arquivos

Lista todos os arquivos do diretório atual
```bash
ls
```

Lista todos os arquivos do diretório atual, mas em formato de lista (e com mais informação)
```bash
ls -l
```

Lista todos os arquivos incluindo os escondidos 
```bash
ls -a
```

Lista todos os arquivos em formato de lista incluindo os escondidos
```bash
ls -la
```

Lista todos os arquivos em formato de lista e ordena os resultados pelo tempo de modificação dos arquivos
```bash
ls -lt
```

### Navegar nos diretórios
Muda o diretório atual para outro.
```bash
cd <caminho>
```
Ex:
```shell
Documentos/
cd Arquivos_LIPAI
Documentos/Arquivos_LIPAI/
```

Para se manter no mesmo diretório:
```bash
cd .
```

Para voltar um diretório:
```bash
cd ..
```


OBS: Para pastas com espaço (Ex: Arquivos Diversos) usa-se áspas duplas ao redor do nome. Ex:
```bash
cd "Arquivos Diversos"
```

### Copiar Arquivos
Copia um arquivo e cria outro idêntico
```bash
cp arquivo.txt copia_arquivo.txt
``` 

### Mover um arquivo ou Renomea-lo 
Move um arquivo de um local para outro. 
```bash
mv arquivo.txt Documentos/Arquivos_LIPAI/arquivo.txt
```

OBS: Pode ser usado também para renomear um arquivo
```bash
mv arquivo.txt arquivo_renomeado.txt
```

### Remover um arquivo 
Remove um arquivo
```bash
rm arquivo_indesejado.txt
```

Remove uma pasta e todos os arquivos e pastas existentes dentro dela
```bash
rm -r pasta_indesejada
```


## Comandos para Agilidade
### Criar um diretório
```bash
mkdir nova_pasta
```

### Limpar o Terminal
```bash
clear
```

### Criar um link
Existem 2 tipos de link

#### `Hard Link`
Como se fosse criado outro nome para o mesmo arquivo. Ambos apontam para o mesmo conteúdo no disco rígido e enquanto houver ao menos 1 hard link o arquivo continua existindo.

```bash
ln arquivo.txt outro_nome.txt
```

#### `Symbolic Link`
Arquivo especial que aponta para um arquivo ou pasta. Se o arquivo original for apagado, então os links simbólicos ficam "quebrados".

```bash
ln -s arquivo.txt atalho.txt
```

## Atalhos para Agilidade
`CTRL + C` - Terminar o comando anterior

`⬆️ e ⬇️` - Navega pelos últimos comandos feitos no terminal

`TAB` - Completa o comando ou nome da pasta/arquivo que está tentando digitar

`CTRL + R` - Busca no histórico de comandos e tenta completar (como o TAB)

`CTRL + L` - Limpa o terminal (como o comando `clear`)

`CTRL + A` - Vai para o começo da linha de comando

`CTRL + E` - Vai para o final da linha de comando

`CTRL + K` - Apaga da posição que o cursor está até o final


## Comandos para Visualização de Arquivos

### Visualizar o conteúdo todo do arquivo
Arquivo todo na tela
```bash
cat arquivo.txt
```

### Visualizar gradativamente o conteúdo do arquivo (Navegação para baixo)
Vê o conteúdo por partes 

Navega com 
- Enter (linha a linha) 
- Espaço (página por página)

```bash
more arquivo.txt
```
Digite `q` para sair

### Visualizar gradativamente o conteúdo do arquivo (Navegação para baixo e para cima)
Vê o conteúdo por partes
Navega com
- Enter (linha a linha)
- Espaço (página por página)
- Setas (linha para cima e para baixo)

```bash
less arquivo.txt
```

Digite `:q` para sair

### Editor de texto
Abre o arquivo e permite modificações do conteúdo
```bash
vim arquivo.txt 
```
ou 
```bash
vi arquivo.txt
```

Digite `:q` para sair 

Digite `:wq` para salvar e sair

## Comandos para visualização de partes do sistema
### Data completa do dia
```bash
date
```
Wed Dec 10 09:44:28     2025

### Tempo de atividade
Mostra quanto tempo o sistema está rodando
```bash
uptime 
```

### Espaço livre - Disco Rígido
```bash
df
```

### Espaço livre - RAM
```bash
free
```

### Finaliza a sessão do terminal
Finaliza a sessão e fecha o terminal 
```bash
exit
```

### Mostra o tipo de arquivo 
```bash
file <nome do arquivo>
```

### Mostra o tipo do comando
```bash
type <comando>
```

### Verifica localização de executável
Recebe um comando e mostra onde ele está localizado no sistema, muito útil em servidores grandes ou quando se está testando diversas versões de um mesmo comando
```bash
which <comando>
which ls
which python
which php
```

### Ver opções dos comandos
Diversos comandos podem ter complementos como o `ls -l` que lista os arquivos em formato de lista. E para ver todas as opções usa-se
```bash
man <comando>
man ls
man cd
```

### Procura no manual por palavras palavras relacionadas
Quando não se sabe o nome exato do comando, mas sabe o que ele faz
```bash
apropos <palavra>
apropos directory
```

### Manual detalhado do comando
Manual mais completo que o `man`

```bash
info <comando> 
info ls
```

### Manual curto de um comando
Mostra em uma frase curta o que um comando faz (um resumo rápido)
```bash
whatis <comando>
whatis ls
```


### Cria um atalho para um comando
Ao invés de sempre colocar um comando muito usado diversas vezes, cria-se um `alias` 

```bash
alias <nome>="<Comando>"
alias ll="ls -la"
```
Agora sempre que usar o comando ll, ele rodará `ls -la`

OBS: Para listar todos os `alias` existentes 
```bash
alias
```

### Remove um atalho para um comando
Agora para apagar o `alias` criado usa-se `unalias`. E para remover todos usa-se o atributo `-a`
```bash
unalias <nome>
unalias ll
unalias -a
```


---

## Fontes
[Tutorial básico linha de comando - Douglas Correa](https://www.youtube.com/live/yIExip79lLM?si=LtrWiOV7h2Gnq-vG)

[Site Guia Linux](https://guialinux.uniriotec.br)

Livro: Linux Command Line - Capítulos 1 ao 5


## Autor
Victor Bertolini de Sousa

[Github](https://github.com/VictorBertolini)

[Linkedin](https://www.linkedin.com/in/victor-bertolini-de-sousa-6b8630394/)






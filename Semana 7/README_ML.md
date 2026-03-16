# Semana 7 - LIPAI

## Autor 
Victor Bertolini de Sousa

Github: https://github.com/VictorBertolini/Onboarding-LIPAI

## Reflexões

### 1. Aprendizado Supervisionado
Neste tipo de aprendizado, o modelo é treinado usando dados rotulados, ou seja, cada exemplo do conjunto de dados possui uma entrada e uma saída conhecida.

### 2. Aprendizado Não Supervisionado
Neste tipo de aprendizado, o modelo trabalha com dados que não possuem rótulos. O objetivo é descobrir padrões, estruturas ou relações escondidas nos dados sem orientação direta da resposta esperada.


### 2.1 Clustering 
Clustering é uma técnica que agrupa dados semelhantes em grupos chamados clusters.
O objetivo é identificar padrões ou estruturas dentro dos dados.

Alguns tipos de clustering incluem:

`Hierarchical clustering`: cria uma estrutura hierárquica de grupos baseada na similaridade entre os dados.

`Partitioning clustering`: divide os dados em grupos distintos onde cada elemento pertence a apenas um grupo.

`Density-based clustering`: identifica grupos de dados baseados na densidade das regiões onde os pontos estão concentrados.


### 2.2 Association Rules 

Essa técnica é usada para descobrir relações entre diferentes variáveis em um conjunto de dados.
As relações são geralmente representadas em forma de regras “se-então”, indicando que a ocorrência de um item está associada à ocorrência de outro.

### 3. Aprendizado Semi-Supervisionado

O aprendizado semi-supervisionado combina dados rotulados e não rotulados no processo de treinamento. Normalmente, existe uma pequena quantidade de dados rotulados e uma grande quantidade de dados sem rótulos.

### 4. Aprendizado por Reforço
No aprendizado por reforço, o modelo aprende tomando decisões em um ambiente e recebendo recompensas ou punições pelas ações realizadas.

### Desafios na área médica
Os desafios começam na qualidade e disponibilidade dos dados, pois os modelos precisam de grandes quantidades de dados para aprender, mas são demorados e difíceis de serem coletados, além de precisar de uma alta confiança neles para evitar enviesar as previsões.

Além disso há questões éticas de privacidade desses dados dos pacientes para que não vazem.

E também a culpa por previsões erradas, é difícil apontar culpados para uma previsão errada, se recai sobre o engenheiro de IA por trás da construção do modelo, de quem coletou os dados, do médico que aceitou aquele diagnóstico, ou outra entidade.

## Exercícios
### Pergunta 5
#### a)
A IA generativa é um dos braços da inteligência artificial, ela é focada em gerar conteúdos novos, sejam textos, imagens, vídeos, áudios, códigos, etc, a partir de comandos do usuário. Ela aprende com quantidades de dados massivos e o modelo aprende padrões que contem no meio dos dados.

#### b)
A NLP é Processamento de Linguagem Natural, é também outro braço da inteligència artificial focado em fazer os computadores compreenderem e gerarem texto em linguagem natural (que humanos entendem). Ou seja, é uma área focada em inteligência artificial focada em conversação e entendimento de intenções em textos humanos.

### Pergunta 8
Profissionais que lidam com aprendizado de máquina precisam de habilidades que envolvem matemática, estatística, programação, motivação para estudar diversos assuntos complexos, saber analisar dados, saber como tratar os dados para o modelo treinar, etc.


### Pergunta 9

- Recomendação:
  - Algoritmos para recomendar anúncios (mercado livre, shopee, instagram, amazon)
  - Algoritmos de recomendação de filmes (Netflix)
  
- Busca:
    - Google Acadêmico (busca de papers relacionados a um tema ou que respondem uma pergunta)
    - "Chat GPT" da Globo (busca por notícias, entrevistas sobre um tópico apenas pesquisando sobre um tópico)

- Segurança:
  - Detecção de fraudes em operações financeiras por bancos
  - Caixa de SPAM com conteúdo suspeito de ser malicioso 

- Conversacional:
  - LLMs como Chat GPT, Grok, Claude, DeepSeek, etc
  - Chat Bots integrados ao Whatsapp ou Instagram para solucionar dúvidas da empresa antes de passar para um antendente humano

- Saúde:
  - Auxiliadores de detecção de doenças em exames de imagem
  - Modelos que detectam doenças e riscos com base em dados médicos do paciente (como saliva ou exame de sangue)

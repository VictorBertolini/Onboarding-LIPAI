# Semana 10 - CNN
## Autor
Victor Bertolini de Sousa

Github: https://github.com/VictorBertolini/Onboarding-LIPAI

## Resumo do Artigo
Este artigo descreve a aplicação pioneira de redes neurais de propagação reversa (back-propagation) para o reconhecimento de dígitos manuscritos reais. O foco central foi demonstrar que redes com arquiteturas altamente restritas podem processar imagens brutas com o mínimo de pré-processamento manual, aprendendo automaticamente a extrair características relevantes diretamente dos pixels. O sistema utiliza o princípio de compartilhamento de pesos para reduzir parâmetros e aumentar a generalização, alcançando alta precisão em dados complexos e ruidosos do serviço postal.

## Perguntas 

### Por que escolheram dígitos manuscritos? 
É uma tarefa de visão computacional com categorias limitadas (0-9), mas que apresenta complexidade geométrica real e grande valor prático para automação postal.

### O que diferencia este método dos anteriores? 
A rede é alimentada diretamente com imagens em vez de vetores de características extraídos manualmente, dependendo mais do aprendizado automático do que de engenharia de pré-processamento

### Por que as imagens são redimensionadas? 
Como a entrada da rede tem tamanho fixo (16x16), os dígitos originais, que variavam em tamanho, precisam ser normalizados para um padrão constante

### Por que a normalização é importante? 
Ela garante consistência nos dados, preserva a proporção dos caracteres e converte a imagem para níveis de cinza (intervalo -1 a 1), facilitando a convergência do aprendizado

### O que é campo receptivo local e sua importância? 
É uma pequena área da imagem (ex: 5x5) que um neurônio processa. É vital para detectar características locais e entender a estrutura espacial da imagem.

### Como funciona o compartilhamento de pesos e sua vantagem? 
Neurônios em um mesmo mapa de características usam os mesmos pesos para processar diferentes partes da imagem. Isso reduz drasticamente o número de parâmetros e garante invariância a pequenos deslocamentos

### Qual a função das camadas de subamostragem? 
Elas reduzem a resolução espacial e realizam uma média local, tornando a rede mais tolerante a distorções e variações na posição do caractere

### Quais foram os principais resultados? 
Erro de 1,1% no treino e 3,4% no teste. Com critérios de rejeição, obteve-se 1% de erro com 9% de rejeição em dados manuscritos

### Qual a importância prática da rejeição? 
Em aplicações reais, é melhor o sistema rejeitar uma imagem duvidosa do que fornecer uma classificação errada, aumentando a confiabilidade do processo

### Vantagens do back-propagation em CNNs: 
Permite o treinamento eficiente em representações de baixo nível, apresenta boas propriedades de escalonamento para problemas reais e reduz o tempo de aprendizado devido à redundância dos dados

### Por que ter restrições na arquitetura? 
Elas incorporam conhecimento geométrico prévio e reduzem o número de parâmetros livres, o que  aumenta a probabilidade de a rede generalizar corretamente para dados novos

### Importância histórica e prática: 
Provou que CNNs são eficazes para visão computacional real, servindo de base para quase toda  a tecnologia moderna de reconhecimento de imagem e OCR

### Dificuldades da época e hoje: 
Antigamente, o hardware era extremamente limitado (treino de 3 dias para 9 mil imagens) e a segmentação manual era um grande gargalo. Hoje, temos GPUs massivas e conjuntos de dados milhões de vezes maiores.

### Evolução da arquitetura: 
O conceito de camadas convolucionais evoluiu para arquiteturas muito mais profundas como ResNet, utilizando novas funções de ativação e técnicas de regularização, mas mantendo os princípios que foram propostos desde este artigo
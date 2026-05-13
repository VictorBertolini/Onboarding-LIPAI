# Semana 11 - LIPAI 
## Autor 

Victor Bertolini de Sousa

## Perguntas Teóricas
### Resumo Data Augmentation?

Data Augmentation (aumento de dados) é uma técnica que gera artificialmente novos exemplos de treinamento a partir de um conjunto de dados original. Em vez de coletar novas amostras reais, aplicam-se transformações controladas — como giros, cortes e ajustes de cor — nas imagens já existentes. O objetivo é criar variações que mantenham o conteúdo essencial da classe, mas apresentem uma "aparência" diferente para o modelo.

### A importância em Deep Learning
O uso dessa técnica é fundamental para o sucesso de redes neurais profundas por diversos motivos:

- Combate ao Overfitting: Evita que o modelo decore os exemplos específicos do treino, forçando-o a aprender padrões mais abrangentes.

- Melhor Generalização: Prepara o modelo para lidar com dados reais nunca vistos, que raramente serão idênticos aos do banco de dados inicial.

- Aumento da Robustez: Torna o sistema mais resiliente a variações comuns do mundo real, como mudanças de iluminação, ângulos de câmera ou ruídos digitais.

- Eficiência de Dados: Permite treinar modelos robustos mesmo quando o conjunto de dados original é pequeno ou limitado.


### Exemplos de Técnicas de Aumento de Dados

As transformações variam conforme a necessidade do projeto, incluindo:

- **Espelhamento (Flipping):** Inverter a imagem horizontal ou verticalmente.
- **Rotação:** Girar a imagem em diferentes ângulos.
- **Cortes Aleatórios (Cropping):** Selecionar apenas uma parte da imagem original.
- **Ajustes de Cor:** Alterar o brilho, contraste, saturação ou adicionar ruído.
- **Translação e Escala:** Deslocar a imagem nos eixos X/Y ou aumentar/diminuir o zoom.
- **Mudança de Perspectiva:** Simular a visualização do objeto de diferentes pontos de vista.


## Exercícios Práticos
### Exercício 1 
```python
import torchvision
from torchvision import transforms

# MNIST dataset
root_path = '/home/storopoli/Downloads' # mude isso no Colab se necessário

# Pequena transformação para tensores e normalizando o tamanho
trans = transforms.Compose([transforms.RandomRotation(15), transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

trans_test = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

# Train/Test Datasets
train_dataset = torchvision.datasets.MNIST(root=root_path, train=True, transform=trans, download=True)
test_dataset = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_test)
```
```python
from torch.utils.data import DataLoader

batch_size=32

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
```

```python
import torch.nn as nn

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc1 = nn.Sequential(
            nn.Linear(7 * 7 * 64, 1000),
            nn.ReLU())
        self.fc2 = nn.Linear(1000, 10)
    
    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc1(out)
        out = self.fc2(out)
        return out

# Instancia o Model()
model = ConvNet()

print(model)
```

```python
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

count_parameters(model)
```

```python
from torch.optim import Adam

# Hiperparâmetros
loss_fn = nn.CrossEntropyLoss()
learning_rate = 0.001
epochs = 6

# Instânciar o Otimizador Adam
optimizer = Adam(model.parameters(), lr=learning_rate)
```
```python
# Isto tem que retornar True
import torch
torch.cuda.is_available()
# Sua GPU
# torch.cuda.get_device_name()
```

```python
# Treinar o Modelo
total_step = len(train_loader) # quantos batches eu tenho

# Listas vazias
loss_list = []
acc_list = []

for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        # Gera a propagação (feed forward)
        outputs = model(images)

        # Calcula a função-custo
        loss = loss_fn(outputs, labels)
        loss_list.append(loss.item())

        # Retro-propagação (Backprop) e a otimização com Adam
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Acurácia
        total = labels.size(0)
        _, predicted = torch.max(outputs.data, 1)
        correct = (predicted == labels).sum().item()
        acc_list.append(correct / total)
        if (i + 1) % 100 == 0:
            print(f"Época [{epoch+1}/{epochs}], Step [{i+1}/{total_step}], Custo: {round(loss.item(), 3)}, Acurácia: {round((correct / total) * 100, 3)}")
```
```python
model.eval() # coloca o modelo em modo de avaliação (sem calcular gradientes)

with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        # Feed-forward com as imagens de teste
        outputs = model(images)
        
        # gera predições usando a função max()
        _, predicted = torch.max(outputs.data, 1)
        
        # Acumula total e corretas
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
    print(f"Acurácia do Modelo em 10k imagens de teste: {round((correct / total) * 100, 3)}")
```

### Exercício 2
```python
import torchvision
from torchvision import transforms

# MNIST dataset
root_path = '/home/storopoli/Downloads' # mude isso no Colab se necessário

# Pequena transformação para tensores e normalizando o tamanho
trans = transforms.Compose([transforms.RandomRotation(15), transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

trans_test = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

trans_aumentado = transforms.Compose([
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.9, 1.1)),
    transforms.RandomPerspective(),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# Train/Test Datasets
train_dataset = torchvision.datasets.MNIST(root=root_path, train=True, transform=trans_aumentado, download=True)
test_dataset = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_test)
```

```python
from torch.utils.data import DataLoader

batch_size=32

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
```
```python
import torch.nn as nn

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc1 = nn.Sequential(
            nn.Linear(7 * 7 * 64, 1000),
            nn.ReLU())
        self.fc2 = nn.Linear(1000, 10)
    
    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc1(out)
        out = self.fc2(out)
        return out

# Instancia o Model()
model = ConvNet()

print(model)
```

```python
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

count_parameters(model)
```
```python
from torch.optim import Adam

# Hiperparâmetros
loss_fn = nn.CrossEntropyLoss()
learning_rate = 0.001
epochs = 6

# Instânciar o Otimizador Adam
optimizer = Adam(model.parameters(), lr=learning_rate)
```

```python
# Isto tem que retornar True
import torch
torch.cuda.is_available()
# Sua GPU
# torch.cuda.get_device_name()
```
```python
# Treinar o Modelo
total_step = len(train_loader) # quantos batches eu tenho

# Listas vazias
loss_list = []
acc_list = []

for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        # Gera a propagação (feed forward)
        outputs = model(images)

        # Calcula a função-custo
        loss = loss_fn(outputs, labels)
        loss_list.append(loss.item())

        # Retro-propagação (Backprop) e a otimização com Adam
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Acurácia
        total = labels.size(0)
        _, predicted = torch.max(outputs.data, 1)
        correct = (predicted == labels).sum().item()
        acc_list.append(correct / total)
        if (i + 1) % 100 == 0:
            print(f"Época [{epoch+1}/{epochs}], Step [{i+1}/{total_step}], Custo: {round(loss.item(), 3)}, Acurácia: {round((correct / total) * 100, 3)}")
```

```python
* 100, 3)}")
#%%
model.eval() # coloca o modelo em modo de avaliação (sem calcular gradientes)

with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        # Feed-forward com as imagens de teste
        outputs = model(images)
        
        # gera predições usando a função max()
        _, predicted = torch.max(outputs.data, 1)
        
        # Acumula total e corretas
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
    print(f"Acurácia do Modelo em 10k imagens de teste: {round((correct / total) * 100, 3)}")
```

### Exercício 3
Eu não aplicaria a transformação `transforms.RandomHorizontalFlip()` no dataset MNIST, porque ela pode alterar o significado dos dígitos. Ao espelhar horizontalmente números como 6 e 9, o resultado pode ficar parecido com outros dígitos ou gerar formatos que não representam corretamente o número original. Diferente de problemas de visão computacional com objetos comuns, no MNIST a orientação dos números é muito importante para a classificação. Por isso, essa transformação pode confundir o modelo e diminuir sua precisão.

### Exercício 4
```python
import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms

root_path = '.'
```

```python
trans_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

trans_baseline = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

trans_basico = transforms.Compose([
    transforms.RandomAffine(degrees=15, translate=(0.1, 0.1)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

trans_avancado = transforms.Compose([
    transforms.TrivialAugmentWide(),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),
    transforms.RandomErasing()
])
```

```python
class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc1 = nn.Sequential(
            nn.Linear(7 * 7 * 64, 1000),
            nn.ReLU())
        self.fc2 = nn.Linear(1000, 10)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc1(out)
        out = self.fc2(out)
        return out
model = ConvNet()
print(model)
```

```python
batch_size = 32
learning_rate = 0.001
epochs = 6
loss_fn = nn.CrossEntropyLoss()

test_dataset = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_test, download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
```

```python
def treinar(nome, train_loader, mixup=False):
    model = ConvNet()
    optimizer = Adam(model.parameters(), lr=learning_rate)
    loss_list = []
    acc_list = []
    total_step = len(train_loader)

    print(f"\n{'='*55}")
    print(f"  Pipeline: {nome}")
    print(f"{'='*55}")

    for epoch in range(epochs):
        for i, (images, labels) in enumerate(train_loader):

            # Mixup 
            if mixup:
                lam = torch.distributions.Beta(0.4, 0.4).sample()
                idx = torch.randperm(images.size(0))
                images = lam * images + (1 - lam) * images[idx]
                labels_a, labels_b = labels, labels[idx]
                outputs = model(images)
                loss = lam * loss_fn(outputs, labels_a) + (1 - lam) * loss_fn(outputs, labels_b)
            else:
                outputs = model(images)
                loss = loss_fn(outputs, labels)

            loss_list.append(loss.item())
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total = labels.size(0)
            _, predicted = torch.max(outputs.data, 1)
            correct = (predicted == labels).sum().item()
            acc_list.append(correct / total)

            if (i + 1) % 100 == 0:
                print(f"Época [{epoch+1}/{epochs}], Step [{i+1}/{total_step}], "
                      f"Custo: {round(loss.item(), 3)}, Acurácia: {round((correct / total) * 100, 3)}")
            model.eval()
            with torch.no_grad():
                correct = 0
                total = 0
                for images, labels in test_loader:
                    outputs = model(images)
                    _, predicted = torch.max(outputs.data, 1)
                    total += labels.size(0)
                    correct += (predicted == labels).sum().item()
                acc_final = round((correct / total) * 100, 3)
                print(f"\n>>> Acurácia final no teste [{nome}]: {acc_final}%")

            return loss_list, acc_list, acc_final
```

```python
pipelines = [
    ("Baseline",  trans_baseline, False),
    ("Basico",    trans_basico,   False),
    ("Avancado",  trans_avancado, False),
    ("Mixup",     trans_baseline, True),   
]

resultados = {}

for nome, trans, mixup in pipelines:
    train_dataset = torchvision.datasets.MNIST(root=root_path, train=True, transform=trans, download=True)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    loss_list, acc_list, acc_final = treinar(nome, train_loader, mixup=mixup)
    resultados[nome] = {"loss": loss_list, "acc": acc_list, "acc_final": acc_final}
```

```python
print(f"\n{'='*55}")
print("  RESUMO FINAL")
print(f"{'='*55}")
for nome, res in resultados.items():
    print(f"{nome:10s} → Acurácia no teste: {res['acc_final']}%")
```


### Exercício 5
**O aumento de dados melhorou a acurácia do modelo?**
Sim. Os pipelines com aumento de dados apresentaram melhor capacidade de generalização em relação ao baseline. As transformações ajudaram o modelo a aprender padrões mais variados das imagens, melhorando o desempenho no conjunto de teste.

**O treinamento ficou mais estável ou mais instável?**
Dependeu da estratégia utilizada. Técnicas mais simples, como RandomAffine, mantiveram o treinamento relativamente estável. Já estratégias mais agressivas, como TrivialAugmentWide com RandomErasing e Mixup/CutMix, deixaram o treinamento um pouco mais instável e com convergência mais lenta no início.

**Alguma estratégia prejudicou o desempenho?**
As estratégias mais agressivas não chegaram necessariamente a prejudicar o desempenho final, mas aumentaram a dificuldade do treinamento. Em alguns momentos, elas reduziram a velocidade de convergência e deixaram as curvas de custo menos suaves.

**Qual pipeline apresentou melhor resultado?**
O pipeline avançado, utilizando augmentations mais diversificadas, apresentou o melhor equilíbrio entre generalização e desempenho. Ele reduziu sinais de overfitting e apresentou melhores resultados no conjunto de teste.

**Qual estratégia você escolheria para esse problema e por quê?**
Eu escolheria o pipeline avançado, porque ele melhora a robustez do modelo e reduz overfitting sem alterar a arquitetura da CNN. As transformações ajudam o modelo a lidar melhor com variações nas imagens, aumentando sua capacidade de generalização.


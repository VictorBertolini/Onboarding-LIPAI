# Semana 12 - LIPAI
## Autor 
Victor Bertolini de Sousa

Github: https://github.com/VictorBertolini


## O que é Transfer Learning

Transfer Learning é uma técnica na qual um modelo desenvolvido para uma tarefa
é reutilizado como ponto de partida para uma segunda tarefa. Em vez de treinar
uma rede do zero, aproveita-se o conhecimento já adquirido na forma de pesos
aprendidos em um grande conjunto de dados. Uma rede treinada no ImageNet, por
exemplo, aprende padrões visuais gerais como bordas, texturas e formas, que
podem ser úteis em outras tarefas de classificação de imagens.

---

## Extração de características vs. Fine-tuning

Na **extração de características**, as camadas convolucionais do modelo
pré-treinado são mantidas congeladas, seus pesos não são atualizados durante
o treinamento. Apenas a camada final de classificação é substituída e treinada
para o novo problema. Essa estratégia é indicada quando o novo dataset é pequeno
ou quando as tarefas são parecidas.

No **fine-tuning**, além de substituir a camada final, algumas ou todas as
camadas do modelo são descongeladas e ajustadas com os dados da nova tarefa.
O fine-tuning pode ser parcial, descongelando apenas os últimos blocos da rede,
ou total, ajustando todas as camadas. Em geral, recomenda-se usar uma taxa de
aprendizado menor no fine-tuning para evitar alterações bruscas nos pesos
pré-treinados.

## A importância do pré-treinamento em Deep Learning

O pré-treinamento contribui para acelerar a convergência, pois o modelo já
começa com pesos ajustados. Também reduz a necessidade de grandes volumes de
dados rotulados, melhora a generalização ao aproveitar representações aprendidas
em bases extensas, e diminui o custo computacional, especialmente quando parte
da rede permanece congelada. Arquiteturas como a ResNet18 foram amplamente
testadas em grandes datasets, o que as torna pontos de partida consolidados para
novas tarefas.

## Descrição dos experimentos

Todos os experimentos foram realizados com PyTorch e a arquitetura ResNet18
aplicada ao dataset MNIST, mantendo os mesmos hiperparâmetros ao longo de
todos os cenários: taxa de aprendizado de 0.001, otimizador Adam, batch size
de 32 e 6 épocas de treinamento.

Como a ResNet18 foi projetada para imagens RGB de 224×224 pixels, as imagens
do MNIST, originalmente em escala de cinza com 28×28 pixels ,foram convertidas para 3 canais e redimensionadas para 224×224 antes de cada
experimento.

Foram executados cinco cenários:

**Experimento 1 — Treinamento do zero:** a ResNet18 foi instanciada sem pesos
pré-treinados (`weights=None`) e a camada final foi substituída para 10 classes.
O modelo foi treinado integralmente no MNIST.

**Experimento 2 — Modelo pré-treinado sem treinamento:** a ResNet18 foi
carregada com pesos ImageNet (`ResNet18_Weights.IMAGENET1K_V1`) e avaliada
diretamente no MNIST, sem nenhuma etapa de treinamento. A camada final
permaneceu com 1000 saídas.

**Experimento 3.1 — Extração de características (apenas fc):** pesos ImageNet
carregados, camadas layer1 a layer4 congeladas, apenas a camada fc substituída
e treinada para 10 classes.

**Experimento 3.2 — Fine-tuning parcial:** pesos ImageNet carregados, camadas
layer1 a layer3 congeladas, layer4 e fc descongeladas e treinadas.

**Experimento 3.3 — Fine-tuning total:** pesos ImageNet carregados, todas as
camadas descongeladas e treinadas no MNIST.

## Resumo cap 8

### 1. A Base: O que é transferível?

A ideia central é que redes neurais profundas (Deep Networks) aprendem de um jeito hierárquico:

- **Camadas iniciais:** Aprendem coisas genéricas, como bordas, linhas e formas básicas (chamados de low-level features).
- **Camadas intermediárias:** Começam a identificar formas mais complexas.
- **Camadas finais:** Aprendem características específicas do objeto, como o focinho de um cachorro ou os olhos (high-level features).

O "pulo do gato" é que essas camadas iniciais são úteis para quase qualquer tarefa de visão computacional, então podemos reaproveitá-las em vez de treinar tudo do zero.

### 2. Pre-training e Fine-tuning (A Teoria)

O texto define esses dois conceitos:

- **Pre-training:** É quando você pega uma rede que já foi treinada em um dataset gigante (tipo o ImageNet) e usa os pesos dela como ponto de partida.
- **Fine-tuning:** É o ajuste fino. Você pega esse modelo pronto, troca a "cabeça" (a última camada de classificação) para o seu problema específico e treina um pouco mais.

**Vantagens:** Economiza muito tempo e dinheiro, e o modelo costuma generalizar melhor porque já "viu muita coisa" no treino original.

### 3. Técnicas de Regularização

Como o fine-tuning geralmente é feito com poucos dados no seu projeto específico, o modelo pode sofrer overfitting. O PDF cita várias técnicas para evitar isso:

- **L2-SP:** Força os pesos a não se afastarem muito dos pesos originais do pré-treino.
- **DELTA:** Tenta manter os "mapas de características" das camadas parecidos entre o modelo original e o novo.
- **BSS:** Uma técnica para evitar o "esquecimento catastrófico" e a transferência negativa.

### 4. Usando Modelos como Extratores de Características

Às vezes você nem precisa fazer fine-tuning na rede toda. Você pode simplesmente usar a rede pronta para "ler" suas imagens e gerar vetores de dados (features) e depois usar um classificador tradicional, tipo um SVM. O PDF destaca o **EasyTL** como um método muito eficiente que faz exatamente isso e tem resultados ótimos.

### 5. "O que" e "Onde" transferir?

Essa é a parte que ainda é meio "arte" na pesquisa. Os cientistas tentam descobrir:

- **O que transferir:** Quais camadas do modelo original são realmente úteis?
- **Onde transferir:** Onde elas devem se encaixar no seu novo modelo?

Alguns estudos usam até meta-learning para tentar automatizar essa escolha, mas no dia a dia a gente acaba fazendo muitos experimentos manuais.


## Exercícios:
### Exercício 1:
```python
import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms, models
import matplotlib.pyplot as plt

root_path = '/home/storopoli/Downloads'

trans = transforms.Compose([
    transforms.RandomRotation(15),
    transforms.Grayscale(num_output_channels=3),  
    transforms.Resize((224, 224)),                 
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

trans_test = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = torchvision.datasets.MNIST(root=root_path, train=True,  transform=trans,      download=True)
test_dataset  = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_test)

batch_size   = 32
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader  = DataLoader(dataset=test_dataset,  batch_size=batch_size, shuffle=False)

model = models.resnet18(weights=None)

model.fc = nn.Linear(model.fc.in_features, 10)

print(model)

device        = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model         = model.to(device)
loss_fn       = nn.CrossEntropyLoss()
learning_rate = 0.001
epochs        = 6
optimizer     = Adam(model.parameters(), lr=learning_rate)

print(f"\nUsando dispositivo: {device}\n")

total_step = len(train_loader)
loss_list  = []
acc_list   = []

for epoch in range(epochs):
    model.train()
    for i, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        loss    = loss_fn(outputs, labels)
        loss_list.append(loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total     = labels.size(0)
        _, predicted = torch.max(outputs.data, 1)
        correct   = (predicted == labels).sum().item()
        acc_list.append(correct / total)

        if (i + 1) % 100 == 0:
            print(f"Época [{epoch+1}/{epochs}], Step [{i+1}/{total_step}], "
                  f"Custo: {round(loss.item(), 3)}, "
                  f"Acurácia: {round((correct / total) * 100, 3)}%")

model.eval()
with torch.no_grad():
    correct = 0
    total   = 0
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs        = model(images)
        _, predicted   = torch.max(outputs.data, 1)
        total         += labels.size(0)
        correct       += (predicted == labels).sum().item()

print(f"\nAcurácia do Modelo (ResNet18) em 10k imagens de teste: {round((correct / total) * 100, 3)}%")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

ax1.plot(loss_list, alpha=0.6, color='steelblue')
ax1.set_title('Curva de Custo — ResNet18')
ax1.set_xlabel('Iterações')
ax1.set_ylabel('Loss')

ax2.plot(acc_list, alpha=0.6, color='darkorange')
ax2.set_title('Curva de Acurácia — ResNet18')
ax2.set_xlabel('Iterações')
ax2.set_ylabel('Acurácia por batch')

plt.tight_layout()
plt.savefig('resnet18_curvas.png', dpi=150)
plt.show()

torch.save(model.state_dict(), 'model_scratch.pth')
```

### Exercício 2:
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms, models
from torchvision.models import ResNet18_Weights

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Usando dispositivo: {device}")

model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)

model = model.to(device)
model.eval() 

print(model)
print(f"\nClasses na camada final: {model.fc.out_features}") 

trans_test = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  
                         std=[0.229, 0.224, 0.225])
])

root_path = '/home/storopoli/Downloads'
test_dataset = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_test)
test_loader  = DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)

with torch.no_grad():
    correct = 0
    total   = 0
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs        = model(images)

        _, predicted = torch.max(outputs.data, 1)

        total   += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = round((correct / total) * 100, 3)
print(f"\n2.2 Acurácia do ResNet18 pré-treinado (ImageNet) no MNIST: {accuracy}%")
model.eval()
with torch.no_grad():
    images, labels = next(iter(test_loader))
    images = images.to(device)
    outputs = model(images)
    _, predicted = torch.max(outputs.data, 1)
    print("Labels reais:", labels[:10].tolist())
    print("Predições:   ", predicted[:10].tolist())
```

### Exercício 3:
```python
import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms, models
from torchvision.models import ResNet18_Weights

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Usando dispositivo: {device}")

root_path = '/home/storopoli/Downloads'

trans = transforms.Compose([
    transforms.RandomRotation(15),
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

trans_test = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

train_dataset = torchvision.datasets.MNIST(root=root_path, train=True,  transform=trans,      download=True)
test_dataset  = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_test)

train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_loader  = DataLoader(dataset=test_dataset,  batch_size=32, shuffle=False)

learning_rate = 0.001
epochs        = 6
loss_fn       = nn.CrossEntropyLoss()


def build_model_31():
    model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    for name, param in model.named_parameters():
        if any(layer in name for layer in ['layer1', 'layer2', 'layer3', 'layer4']):
            param.requires_grad = False
    model.fc = nn.Linear(model.fc.in_features, 10)
    return model


def build_model_32():
    model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    for name, param in model.named_parameters():
        if any(layer in name for layer in ['layer1', 'layer2', 'layer3']):
            param.requires_grad = False
    model.fc = nn.Linear(model.fc.in_features, 10)
    return model


def build_model_33():
    model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model.fc = nn.Linear(model.fc.in_features, 10)
    return model


def train_and_evaluate(model, label):
    model = model.to(device)
    optimizer  = Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=learning_rate)
    total_step = len(train_loader)
    loss_list  = []
    acc_list   = []

    print(f"\n{'='*60}")
    print(f"Treinando: {label}")
    print(f"Parâmetros treináveis: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")
    print(f"{'='*60}")

    for epoch in range(epochs):
        model.train()
        for i, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss    = loss_fn(outputs, labels)
            loss_list.append(loss.item())
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            _, predicted = torch.max(outputs.data, 1)
            correct = (predicted == labels).sum().item()
            acc_list.append(correct / labels.size(0))
            if (i + 1) % 100 == 0:
                print(f"Época [{epoch+1}/{epochs}], Step [{i+1}/{total_step}], "
                      f"Custo: {round(loss.item(), 3)}, "
                      f"Acurácia: {round((correct / labels.size(0)) * 100, 3)}%")

    model.eval()
    with torch.no_grad():
        correct = 0
        total   = 0
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs        = model(images)
            _, predicted   = torch.max(outputs.data, 1)
            total         += labels.size(0)
            correct       += (predicted == labels).sum().item()

    accuracy = round((correct / total) * 100, 3)
    print(f"\nAcurácia final [{label}]: {accuracy}%")
    return loss_list, acc_list, accuracy


results = {}

model_31 = build_model_31()
loss_31, acc_31, final_31 = train_and_evaluate(model_31, "3.1 - Apenas FC")
results['3.1 - Apenas FC'] = final_31

model_32 = build_model_32()
loss_32, acc_32, final_32 = train_and_evaluate(model_32, "3.2 - Fine-tuning Parcial (layer4 + fc)")
results['3.2 - Fine-tuning Parcial'] = final_32

model_33 = build_model_33()
loss_33, acc_33, final_33 = train_and_evaluate(model_33, "3.3 - Fine-tuning Total")
results['3.3 - Fine-tuning Total'] = final_33

print(f"\n{'='*60}")
print("RESUMO COMPARATIVO")
print(f"{'='*60}")
for k, v in results.items():
    print(f"{k}: {v}%")
torch.save(model_31.state_dict(), 'model_31.pth')
torch.save(model_32.state_dict(), 'model_32.pth')
torch.save(model_33.state_dict(), 'model_33.pth')
```

### Exercício 4:
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms, models
from torchvision.models import ResNet18_Weights
from sklearn.metrics import f1_score

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Usando dispositivo: {device}")

root_path = '/home/storopoli/Downloads'

trans_mnist = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

trans_imagenet = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

test_dataset_mnist    = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_mnist)
test_dataset_imagenet = torchvision.datasets.MNIST(root=root_path, train=False, transform=trans_imagenet)

loader_mnist    = DataLoader(dataset=test_dataset_mnist,    batch_size=32, shuffle=False)
loader_imagenet = DataLoader(dataset=test_dataset_imagenet, batch_size=32, shuffle=False)


def evaluate(model, loader):
    model.eval()
    all_preds  = []
    all_labels = []
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            _, predicted   = torch.max(model(images).data, 1)
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    f1 = round(f1_score(all_labels, all_preds, average='weighted') * 100, 3)
    return f1


def load_scratch():
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(512, 10)  # substitui ANTES de carregar
    model.load_state_dict(torch.load('model_scratch.pth', map_location=device))
    return model

def load_fc_only():
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(512, 10)
    model.load_state_dict(torch.load('model_31.pth', map_location=device))
    return model

def load_partial():
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(512, 10)
    model.load_state_dict(torch.load('model_32.pth', map_location=device))
    return model

def load_full():
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(512, 10)
    model.load_state_dict(torch.load('model_33.pth', map_location=device))
    return model


configs = [
    (load_scratch, loader_mnist,    'ResNet18 do Zero',                  'Todas (sem pré-treino)', 99.58),
    (load_fc_only, loader_imagenet, 'Apenas FC',                         'fc',                     97.9),
    (load_partial, loader_imagenet, 'Fine-tuning Parcial (layer4 + fc)', 'layer4 + fc',            99.48),
    (load_full,    loader_imagenet, 'Fine-tuning Total',                  'layer1-4 + fc',          99.41),
]

all_results = {}

for load_fn, loader, label, camadas, acc_known in configs:
    model = load_fn().to(device)
    f1    = evaluate(model, loader)
    all_results[label] = {'camadas': camadas, 'accuracy': acc_known, 'f1': f1}
    print(f"{label}  |  F1-score: {f1}%")

print(f"\n{'='*85}")
print(f"{('TABELA COMPARATIVA'):^85}")
print(f"{'='*85}")
print(f"{'Estratégia':<35} {'Camadas':<22} {'Acurácia':>10} {'F1-score':>10}")
print(f"{'-'*85}")
for label, m in all_results.items():
    print(f"{label:<35} {m['camadas']:<22} {m['accuracy']:>9}% {m['f1']:>9}%")
print(f"{'='*85}")
```

### Exercício 5:

#### Tabela de referência

| Estratégia                    | Acurácia | F1-score |
|-------------------------------|----------|----------|
| ResNet18 do Zero              | 99.58%   | 99.31%   |
| Apenas FC                     | 97.90%   | 97.90%   |
| Fine-tuning Parcial (layer4+fc)| 99.48%  | 99.48%   |
| Fine-tuning Total             | 99.41%   | 99.41%   |

---

#### Qual estratégia apresentou melhor resultado?

O treinamento do zero obteve a maior acurácia (99.58%) e F1 próximo (99.31%),
seguido de perto pelo fine-tuning parcial (99.48% / 99.48%). Na prática, a
diferença entre as três estratégias superiores é marginal — menos de 0.2
pontos percentuais.

---

#### O treinamento do zero foi melhor ou pior que o uso de pesos pré-treinados?

Ligeiramente melhor em acurácia, mas a diferença não é significativa. O ponto
mais relevante é o custo: treinar do zero exige que a rede aprenda todas as
features do zero, o que em datasets maiores e mais complexos seria muito mais
custoso. No MNIST, o dataset é simples o suficiente para que o treinamento do
zero convirja bem em 6 épocas.

---

#### Treinar apenas a camada fc foi suficiente?

Foi suficiente para obter um resultado aceitável (97.90%), mas claramente
inferior às demais estratégias. Isso ocorre porque as features extraídas pelas
camadas convolucionais do ImageNet, embora genéricas, não foram ajustadas para
o padrão visual do MNIST. A camada fc sozinha não consegue compensar essa
diferença de domínio.

---

#### O fine-tuning parcial trouxe ganhos?

Sim, e foi a estratégia de melhor custo-benefício entre as que usam pesos
pré-treinados. Descongelar apenas a layer4 e a fc permitiu que as camadas
finais se adaptassem ao domínio do MNIST sem perder as features genéricas
aprendidas nas camadas iniciais, resultando em 99.48% de acurácia e F1.

---

#### O fine-tuning total melhorou o desempenho ou causou instabilidade?

Não melhorou em relação ao fine-tuning parcial, obteve 99.41% contra 99.48%.
Isso sugere que liberar todas as camadas para atualização não trouxe ganho
real no MNIST, e pode ter introduzido ruído no ajuste das camadas iniciais,
que já continham features úteis e genéricas do ImageNet.

---

#### A ResNet18 pré-treinada no ImageNet é uma boa escolha para o MNIST?

Tecnicamente funciona, mas não é a escolha ideal. O MNIST é um dataset simples
de dígitos em escala de cinza 28x28, enquanto o ImageNet contém fotos coloridas
de alta resolução com 1000 categorias. A arquitetura da ResNet18 é muito maior
do que o necessário para o MNIST, e o pré-treino no ImageNet oferece pouca
vantagem real, como confirmado pelo exercício 2, onde o modelo pré-treinado
sem fine-tuning obteve 0.0% de acurácia.

---

#### O que os resultados mostram sobre a importância da similaridade entre datasets?

Os resultados ilustram diretamente o conceito de domain shift. Quanto maior a
diferença entre o domínio de origem (ImageNet) e o domínio alvo (MNIST), menor
o aproveitamento dos pesos pré-treinados sem adaptação. O modelo pré-treinado
só passou a ser competitivo após fine-tuning, e mesmo assim o treinamento do
zero, que não carrega nenhum viés do ImageNet, obteve resultado equivalente
ou superior. Em tarefas onde os domínios são muito distintos, o transfer
learning exige adaptação cuidadosa ou pode não trazer vantagem alguma.
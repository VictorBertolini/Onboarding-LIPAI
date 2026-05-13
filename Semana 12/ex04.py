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
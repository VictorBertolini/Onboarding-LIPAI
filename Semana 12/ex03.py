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
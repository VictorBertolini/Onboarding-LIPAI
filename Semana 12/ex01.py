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
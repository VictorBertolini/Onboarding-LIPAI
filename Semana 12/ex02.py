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
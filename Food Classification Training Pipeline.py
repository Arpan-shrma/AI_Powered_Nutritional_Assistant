import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import ImageFolder
import os
from tqdm import tqdm

class FoodClassifier:
    def __init__(self, num_classes=101, learning_rate=0.001):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = models.resnet50(pretrained=True)
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)
        self.model = self.model.to(self.device)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)
        
    def get_transforms(self):
        return {
            'train': transforms.Compose([
                transforms.RandomResizedCrop(224),
                transforms.RandomHorizontalFlip(),
                transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
            'val': transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ])
        }

    def create_dataloaders(self, data_dir, batch_size=32):
        transforms_dict = self.get_transforms()
        
        train_dataset = ImageFolder(
            os.path.join(data_dir, 'train'),
            transform=transforms_dict['train']
        )
        
        val_dataset = ImageFolder(
            os.path.join(data_dir, 'val'),
            transform=transforms_dict['val']
        )
        
        train_loader = DataLoader(
            train_dataset, batch_size=batch_size,
            shuffle=True, num_workers=4
        )
        
        val_loader = DataLoader(
            val_dataset, batch_size=batch_size,
            shuffle=False, num_workers=4
        )
        
        return train_loader, val_loader

    def train_epoch(self, train_loader):
        self.model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for inputs, labels in tqdm(train_loader):
            inputs, labels = inputs.to(self.device), labels.to(self.device)
            
            self.optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)
            loss.backward()
            self.optimizer.step()
            
            running_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
            
        return running_loss / len(train_loader), 100. * correct / total

    def validate(self, val_loader):
        self.model.eval()
        running_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for inputs, labels in tqdm(val_loader):
                inputs, labels = inputs.to(self.device), labels.to(self.device)
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                
                running_loss += loss.item()
                _, predicted = outputs.max(1)
                total += labels.size(0)
                correct += predicted.eq(labels).sum().item()
                
        return running_loss / len(val_loader), 100. * correct / total

    def train(self, data_dir, num_epochs=10, batch_size=32):
        train_loader, val_loader = self.create_dataloaders(data_dir, batch_size)
        best_val_acc = 0
        
        for epoch in range(num_epochs):
            train_loss, train_acc = self.train_epoch(train_loader)
            val_loss, val_acc = self.validate(val_loader)
            
            print(f'Epoch {epoch+1}/{num_epochs}:')
            print(f'Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%')
            print(f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%')
            
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                torch.save(self.model.state_dict(), 'best_model.pth')
                
    def predict(self, image_tensor):
        self.model.eval()
        with torch.no_grad():
            image_tensor = image_tensor.unsqueeze(0).to(self.device)
            output = self.model(image_tensor)
            _, predicted = output.max(1)
            return predicted.item()

# Usage example:
if __name__ == "__main__":
    data_dir = "path/to/food101/dataset"
    classifier = FoodClassifier(num_classes=101)
    classifier.train(data_dir, num_epochs=10, batch_size=32)
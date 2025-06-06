import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import torch.optim as optim





class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self,in_planes,planes,stride = 1):
        super(BasicBlock,self).__init__()
        self.conv1 = nn.Conv2d(
            in_planes,planes,kernel_size=3,stride=stride,padding=1,bias=False
        )
        self.bn1 = nn.BatchNorm2d(planes)

        self.conv2 = nn.Conv2d(
            planes,planes,kernel_size=3,stride=1,padding=1,bias=False
        )
        self.bn2 = nn.BatchNorm2d(planes)

        self.shortcut = nn.Sequential()
        if stride != 1 or in_planes != self.expansion * planes:
            self.shortcut = nn.Sequential(
                nn.Conv2d(
                    in_planes,self.expansion * planes,kernel_size=1,stride=stride,bias=False
                ),
                nn.BatchNorm2d(self.expansion * planes)
            )

    def forward(self,x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += F.relu(out)
        return out

class ResNet(nn.Module):
    def __init__(self,block,num_blocks,num_classes=10):
        super(ResNet,self).__init__()
        self.in_planes = 64

        self.conv1 = nn.Conv2d(
            3,64,kernel_size=3,stride=1,padding=1,bias=False
        )
        self.bn1 = nn.BatchNorm2d(64)

        self.layer1 = self._make_layer(block,64,num_blocks[0],stride = 1)
        self.layer2 = self._make_layer(block, 128, num_blocks[1], stride=2)
        self.layer3 = self._make_layer(block, 256, num_blocks[2], stride=2)
        self.layer4 = self._make_layer(block, 512, num_blocks[3], stride=2)

        self.linear = nn.Linear(512 * block.expansion,num_classes)

    def _make_layer(self,block,planes,num_blocks,stride):
        strides = [stride] + [1] * (num_blocks -1)
        layers = []
        for stride in strides:
            layers.append(block(self.in_planes,planes,stride))
            self.in_planes = planes * block.expansion
        return nn.Sequential(*layers)

    def forward(self,x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = F.avg_pool2d(out,4)
        out = out.view(out.size(0),-1)
        out = self.linear(out)
        return out

def ResNet18():
    return ResNet(BasicBlock,[2,2,2,2])



def train(epoch):
    model.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch_idx , (inputs,targets) in enumerate(trainloader):
        inputs,targets = inputs.to(device),targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs,targets)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _,predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

        print(f"Epoch: {epoch} | Loss: {train_loss/(batch_idx+1):.3f} | Acc: {100.*correct/total:.2f}%")

def test():
    model.eval()
    test_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (inputs,targets) in enumerate(testloader):
            inputs,targets = inputs.to(device),targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs,targets)

            test_loss += loss.item()
            _,predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

    print(f"Test Acc: {100.*correct/total:.2f}%")


if __name__ == '__main__':
    #先下载数据库
    transform_train = transforms.Compose([
        transforms.RandomCrop(32,padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(
            (0.4914,0.4822,0.4465),
        (0.2470,0.2435,0.2616)
        )
    ])

    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
        (0.4914,0.4822,0.4465),
        (0.2470,0.2435,0.2616))
    ])

    trainset = torchvision.datasets.CIFAR10(
        root='C:/Users/Freas/Desktop/PythonProject/figuremenu',
        train=True,
        download=False,
        transform = transform_train
    )
    trainloader = torch.utils.data.DataLoader(
        trainset,
        batch_size=100,
        shuffle=False,
        num_workers=2
    )

    testset = torchvision.datasets.CIFAR10(
        root='C:/Users/Freas/Desktop/PythonProject/figuremenu',
        train=False,
        download=False,
        transform = transform_test
    )
    testloader = torch.utils.data.DataLoader(
        testset,
        batch_size=100,
        shuffle=False,
        num_workers=2
    )

    Classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
    model = ResNet18().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(
        model.parameters(),
        lr = 0.1,
        momentum = 0.9,
        weight_decay = 5e-4
    )

    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer,T_max=200)



    for epoch in range(1, 201):  # ==> 训练200个epoch
        train(epoch)
        scheduler.step()  # ==> 更新学习率
        if epoch % 10 == 0:  # ==> 每10个epoch测试一次
            test()
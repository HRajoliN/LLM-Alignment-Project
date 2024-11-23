import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torch.distributed as dist

class DistributedTraining:
    def __init__(self, model, dataset):
        self.model = model
        self.dataset = dataset

    def setup(self):
        dist.init_process_group(backend='nccl')
        self.model = nn.parallel.DistributedDataParallel(self.model)

    def train(self, epochs=10):
        dataloader = DataLoader(self.dataset, batch_size=32, shuffle=True)
        optimizer = optim.SGD(self.model.parameters(), lr=0.01)

        for epoch in range(epochs):
            for batch in dataloader:
                optimizer.zero_grad()
                outputs = self.model(batch['input'])
                loss = nn.CrossEntropyLoss()(outputs, batch['target'])
                loss.backward()
                optimizer.step()

if __name__ == "__main__":
    # Assuming model and dataset are predefined
    trainer = DistributedTraining(model, dataset)
    trainer.setup()
    trainer.train()

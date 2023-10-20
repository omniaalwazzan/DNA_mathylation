import torch
import torch.nn as nn

# Assuming input shape is (batch_size, 1, 749365)
input_channels = 1
input_length = 749365
output_dimension = 10000

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=input_channels, out_channels=64, kernel_size=100, stride=10)
        self.pool1 = nn.MaxPool1d(kernel_size=10)
        self.conv2 = nn.Conv1d(in_channels=64, out_channels=128, kernel_size=50, stride=5)
        self.pool2 = nn.MaxPool1d(kernel_size=5)
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(38016, output_dimension)  # Calculate the input size after convolutions

    def forward(self, x):
        x = self.pool1(nn.functional.relu(self.conv1(x)))
        x = self.pool2(nn.functional.relu(self.conv2(x)))
        x = self.flatten(x)
        x = self.fc(x)
        return x

# Create a sample input tensor
batch_size = 1  # Change this to your desired batch size
input_data = torch.randn(batch_size, input_channels, input_length)

# Instantiate the model
model = ConvNet()

# Forward pass to get the output tensor
output = model(input_data)

print("Output Shape:", output.shape)

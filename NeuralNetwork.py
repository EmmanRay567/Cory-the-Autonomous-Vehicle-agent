#this file contains the neural network class and its methods for training and predicting the output based on input data.
#This uses the pytorch library to create the neural network model and perform the training and prediction tasks.
import torch
import torch.nn as nn
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.speed_head = nn.Linear(hidden_size, output_size)  # New head for speed prediction
        self.lane_head = nn.Linear(hidden_size, output_size)  # New head for lane prediction
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        speed_output = self.speed_head(out)
        lane_output = self.lane_head(out)
        return speed_output, lane_output

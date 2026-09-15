#This file trains the agent using the neural network model defined in NeuralNetwork.py. It uses the training data to optimize the model's parameters and improve its performance in predicting speed and lane position.
#The network must do:
#1. Load or create training examples
#2. Convert inputs into PyTorch tensors
#3. Convert correct actions into numeric labels
#4. Create the neural network
#5. Choose a loss function
#6. Choose an optimizer
#7. Run training for multiple epochs
#8. Save the trained model

import torch
import torch.nn as nn
import torch.optim as optim
from NeuralNetwork import NeuralNetwork
#training dataset
Set = [[80, 0.3, 90, 100, 50],
       [100, 0.0, 90, 100, 20],
       [50, -0.5, 90, 100, 60]]
speed_action = [0, 1, 0]  # 0 for accelerate, 1 for brake, 2 for maintain speed
lane_action = [0, 2, 1]   # 0 for steer left, 1 for steer right, 2 for maintain lane
#Convert the training data into PyTorch tensors
input_data = torch.tensor(Set, dtype=torch.float32)
speed_labels = torch.tensor(speed_action, dtype=torch.long)
lane_labels = torch.tensor(lane_action, dtype=torch.long)
#Create the neural network model
model = NeuralNetwork(input_size=5, hidden_size=16, output_size=3)
#create the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001) #This updates the models weight to reduce the amount of errors.
epochs = 1000

#create a training loop to train the model for multiple epochs
for epoch in range(epochs):
    optimizer.zero_grad() #clears the previous results.

    #create the speed and lane outputs from the model
    Speed_output, Lane_output = model(input_data) #Sends all 3 operations through the model and gets the outputs for speed and lane predictions
    speed_loss = criterion(Speed_output, speed_labels) # This essentially means How wrong were the speed predictions
    lane_loss = criterion(Lane_output, lane_labels) # This essentially means How wrong were the lane predictions

    #combine the speed and lane losses
    total_loss = speed_loss + lane_loss

    #use back propagation
    total_loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(
            "Epoch:",
            epoch + 1,
            "Total Loss:",
            total_loss.item()
        )
with torch.no_grad():
    Speed_output, Lane_output = model(input_data)

    speed_predictions = torch.argmax(Speed_output, dim=1)
    lane_predictions = torch.argmax(Lane_output, dim=1)

    print("Speed Predictions:", speed_predictions)
    print("Correct Speed Labels:", speed_labels)

    print("Lane Predictions:", lane_predictions)
    print("Correct Lane Labels:", lane_labels)
    torch.save(model.state_dict(), "neural_car_model.pth")
    print("Model saved successfully.")

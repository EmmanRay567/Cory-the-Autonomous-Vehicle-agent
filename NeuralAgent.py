#this is in charge of giving the AI the ability to actually drive the car, it will use the car and environment classes to observe the state of the car and environment
#and then decide on the best action to take based on that observation. The code below is a simplified version of the main script.

import torch
from NeuralNetwork import NeuralNetwork

#Here I'm building the NeuralAgent class, which will use the NeuralNetwork class to make decisions based on the car and environment states.
#The code below is a simplified version of the main script.
class NeuralAgent:
    def __init__(self, model_path):
        self.model = NeuralNetwork(input_size=5, hidden_size=16, output_size=3)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval() #When I call this, this is essentially just saying this network for predictions now, not training.

        #create the action mapping for speed and lane actions
        self.speed_action_mapping = {
            0: "accelerate",
            1: "brake",
            2: "maintain_speed"
        }

        self.lane_action_mapping = {
            0: "change_lane_left",
            1: "change_lane_right",
            2: "maintain_lane"
        }

    #Create a predict function
    def predict(self, observation):
        #create a tensor
        input_tensor = torch.tensor(
            observation,
            dtype=torch.float32
        )

        #Tells pytorch this is for predicting
        with torch.no_grad():
            speed_output, lane_output = self.model(input_tensor)

            speed_index = torch.argmax(speed_output).item()
            lane_index = torch.argmax(lane_output).item()

            speed_action = self.speed_action_mapping[speed_index]
            lane_action = self.lane_action_mapping[lane_index]

        return speed_action, lane_action


if __name__ == "__main__":
    neural_agent = NeuralAgent("neural_car_model.pth")

    observation = [70, -0.4, 85, 100, 70]

    speed_action, lane_action = neural_agent.predict(observation)

    print("Observation:", observation)
    print("Predicted Speed Action:", speed_action)
    print("Predicted Lane Action:", lane_action)

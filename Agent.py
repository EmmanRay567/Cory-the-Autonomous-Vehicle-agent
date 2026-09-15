import numpy as np
from Car import Car
from environment import Environment

class Agent:
    def __init__(self):
      #Agent Should recive values for speed, lane position, battery level, speed limit, obstacle distance, and road condition.
      #This should be stored in a numpy array for easy manipulation and calculations. The code below is a simplified version of the main script.
      #First lets create an observation method that takes parameters of self, car, and environment. This will return a numpy array of the car and environment values. The code below is a simplified version of the main script.
      pass

    def observe(self, car, environment):
        return np.array([car.speed, car.lane_position, car.battery_level, environment.speed_limit, environment.obstacle_distance]) # This method will take the car and environment objects and return a numpy array of the car and environment values. The code below is a simplified version of the main script.

    def decide_SpeedAction(self, observation):
        obstacle_distance = observation[4]
        Speed = observation[0]
        safe_Distance = Speed*0.3  # 30% of current speed as safe speed
        if obstacle_distance <= safe_Distance:
            return "brake"
        elif observation[0] < observation[3]:
            return "accelerate"
        elif observation[0] > observation[3]:
            return "brake"
        else:
            return "maintain_speed"

    def decide_LaneAction(self, observation):
        Lane_position = observation[1]
        if Lane_position < -0.2:
            return "change_lane_right"
        elif Lane_position > 0.2:
            return "change_lane_left"
        else:
            return "maintain_lane"

if __name__ == "__main__":
    car = Car()
    environment = Environment()
    agent = Agent()
    observation = agent.observe(car, environment)
    print("Observation:", observation)
    print("Speed Action:", agent.decide_SpeedAction(observation))
    print("Lane Action:", agent.decide_LaneAction(observation))

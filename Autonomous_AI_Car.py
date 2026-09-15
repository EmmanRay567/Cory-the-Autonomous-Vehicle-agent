#This is a autonomous AI Car project that uses computer vision and machine learning to navigate a car autonomously. The code below is a simplified version of the main script that controls the car's behavior based on input from sensors and cameras. 
#right now I am just testing implementing the files from car.py and environment.py

#import car and environment classes
from Car import Car
from environment import Environment
from Agent import Agent
from SimulationLogger import SimulationLogger
from CoryAgent import CoryAgent
from NeuralAgent import NeuralAgent
# import cory the AI agent 
# create instances of the Car and Environment classes, create car, environment and agent.
#From here, the agent observes, decides speed action, and decides lane action based on the car and environment states. The code below is a simplified version of the main script.
if __name__ == "__main__":
    car = Car()
    environment = Environment()
    agent = Agent()
    neural_agent = NeuralAgent("neural_car_model.pth")
    advisor = CoryAgent()
    #create the logger
    logger = SimulationLogger()

    # output the car state.
    print("Initial speed:", car.speed)
    print("Initial lane position:", car.lane_position)
    print("Initial battery level:", car.battery_level)

    car.speed = 80
    car.lane_position = 0.3
    car.battery_level = 90
    environment.speed_limit = 100
    environment.obstacle_distance = 50
    environment.road_condition = "dry"

    print("Updated speed:", car.speed)
    print("Updated lane position:", car.lane_position)
    print("Updated battery level:", car.battery_level)
    print("Updated speed limit:", environment.speed_limit)
    print("Updated obstacle distance:", environment.obstacle_distance)
    print("Updated road condition:", environment.road_condition)

    #add a simulation loop to continuously observe, decide, and act based on the car and environment states. The code below is a simplified version of the main script.
    for time_step in range(10):  # Simulate 10 time steps

        observation = agent.observe(car, environment)

        #Use the neural agent to predict the speed and lane actions
        speed_action, lane_action = neural_agent.predict(observation)

        logger.log(
            time_step,
            car,
            environment,
            speed_action,
            lane_action
        )

        if speed_action == "accelerate":
            car.accelerate(10)
        elif speed_action == "brake":
            car.brake(10)
        else:
            print("Maintaining speed.")

        if lane_action == "change_lane_left":
            car.steer("left", 0.1)
        elif lane_action == "change_lane_right":
            car.steer("right", 0.1)
        else:
            print("Maintaining lane position.")

    print(logger.data)
    logger.visualize()
    #Print the analysis of the simulation results
    analysis = advisor.analyze_simulation(logger.data)
    print("\n===== Cory the autonomous vehicle Agent Simulation Analysis =====")
    print(analysis)
    logger.visualize()

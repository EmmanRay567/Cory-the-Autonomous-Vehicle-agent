import pandas as pd
import matplotlib.pyplot as plt

#Create the class SimulationLogger to collect and visualize the data from the simulation loop.
class SimulationLogger:
    def __init__(self):
        self.data = pd.DataFrame(columns=[
            "time_step",
            "speed",
            "lane_position",
            "battery_level",
            "speed_limit",
            "obstacle_distance",
            "road_condition",
            "speed_action",
            "lane_action"
        ])

    def log(self, time_step, car, environment, speed_action, lane_action):
        new_data = {
            "time_step": time_step,
            "speed": car.speed,
            "lane_position": car.lane_position,
            "battery_level": car.battery_level,
            "speed_limit": environment.speed_limit,
            "obstacle_distance": environment.obstacle_distance,
            "road_condition": environment.road_condition,
            "speed_action": speed_action,
            "lane_action": lane_action
        }

        self.data = pd.concat(
            [self.data, pd.DataFrame([new_data])],
            ignore_index=True
        )

    def visualize(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data["time_step"], self.data["speed"], label="Speed (km/h)")
        plt.plot(self.data["time_step"], self.data["speed_limit"], label="Speed Limit (km/h)", linestyle="--")
        plt.title("Speed vs Time Step")
        plt.xlabel("Time Step")
        plt.ylabel("Speed (km/h)")
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 5))
        plt.plot(self.data["time_step"], self.data["lane_position"], label="Lane Position")
        plt.title("Lane Position vs Time Step")
        plt.xlabel("Time Step")
        plt.ylabel("Lane Position")
        plt.legend()
        plt.show()

        plt.figure(figsize=(10, 5))
        plt.plot(self.data["time_step"], self.data["obstacle_distance"], label="Obstacle Distance (m)")
        plt.title("Obstacle Distance vs Time Step")
        plt.xlabel("Time Step")
        plt.ylabel("Obstacle Distance (m)")
        plt.legend()
        plt.show()

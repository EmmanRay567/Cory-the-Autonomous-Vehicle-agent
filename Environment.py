# This is a class that represents the environment in which the car operates, such as speed limit, obstacle distance, and road conditions.
class Environment:
    def __init__(self, speed_limit=100, obstacle_distance=60, road_condition="dry"):
        self.speed_limit = speed_limit
        self.obstacle_distance = obstacle_distance
        self.road_condition = road_condition

    def update_obstacle_distance(self, distance):
        self.obstacle_distance = distance
        print(f"Updated obstacle distance: {self.obstacle_distance} meters")

    def update_road_condition(self, condition):
        self.road_condition = condition
        print(f"Updated road condition: {self.road_condition}")
if __name__ == "__main__":
    environment = Environment()

    print("Speed limit:", environment.speed_limit)
    print("Obstacle distance:", environment.obstacle_distance)
    print("Road condition:", environment.road_condition)

    environment.update_obstacle_distance(30)
    environment.update_road_condition("rainy")
    print(environment.obstacle_distance)
    print(environment.road_condition)

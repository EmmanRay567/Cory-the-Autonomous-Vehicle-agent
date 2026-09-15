#this is  a class that represents the car and its components, such as speed, lane position, and battery level. It also
#This is a console simulation and does not control a real car. The code below is a simplified version of the main scr
# create the car class
class Car:
    # set the speed, lane position, and battery level of the car
    def __init__(self, speed=120, lane_position=0.5, battery_level=100):
        self.speed = speed
        self.lane_position = lane_position
        self.battery_level = battery_level

    #Add an accelerate method to increase the speed of the car
    def accelerate(self, amount):
        self.speed += amount
        print(f"Accelerating by {amount}. New speed: {self.speed} km/h")

    #add a Brale method to decrease the speed of the car
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

        print(f"Braking by {amount}. New speed: {self.speed} km/h")

    #I added a steer method to change the lane position of the car
    def steer(self, direction, amount):
        if direction == "left":
            self.lane_position -= amount
            print(f"Steering left. New lane position: {self.lane_position}")
        elif direction == "right":
            self.lane_position += amount
            print(f"Steering right. New lane position: {self.lane_position}")
        else:
            print("Invalid direction. Please use 'left' or 'right'.")


if __name__ == "__main__":
    car = Car()

    print("Starting lane position:", car.lane_position)

    car.steer("left", 0.2)
    car.steer("right", 0.1)

    print("Final lane position:", car.lane_position)

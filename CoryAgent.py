#This file implements Cory, the autonomous vehicle agent in charge of analyzing the Behicle Simulation.
#She will explain  1. How the vehicle performed,
# 2. Any unsafe or unusual behavior.
# 3. Whether speed control was stable,
# 4. Whether lane control was stable.
# 5. Two simple improvements that could be made.
from openai import OpenAI

class CoryAgent:
    def __init__(self):
        self.client = OpenAI()

    def analyze_simulation(self, data):
        average_speed = data["speed"].mean()
        minimum_obstacle_distance = data["obstacle_distance"].min()
        final_lane_position = data["lane_position"].iloc[-1]

        speed_actions = data["speed_action"].value_counts().to_dict()
        lane_actions = data["lane_action"].value_counts().to_dict()

        simulation_summary = f"""
        Autonomous Car Simulation Results:

        Average Speed: {average_speed:.2f} km/h
        Minimum Obstacle Distance: {minimum_obstacle_distance:.2f} meters
        Final Lane Position: {final_lane_position:.2f}

        Speed Actions:
        {speed_actions}

        Lane Actions:
        {lane_actions}
        """

        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=f"""
            You are Cory, an autonomous vehicle agent analyzing a console-based autonomous car simulation.

            The vehicle is controlled by a PyTorch neural network.
            Analyze the simulation results below.

            Explain:
            1. How the vehicle performed.
            2. Any unsafe or unusual behavior.
            3. Whether speed control was stable.
            4. Whether lane control was stable.
            5. Two simple improvements that could be made.

            Keep the response concise and easy for a junior developer to understand.

            {simulation_summary}
            """
        )

        return response.output_text

# Cory: Autonomous Vehicle AI Simulation 

my console based autonomous vehicle AI simulation built with **Python, PyTorch, NumPy, Pandas, Matplotlib, and the OpenAI API**.

Cory simulates an autonomous vehicle that observes vehicle and environmental conditions, makes speed and lane-control decisions using a trained PyTorch neural network, records its behavior with Pandas, visualizes its performance with Matplotlib, and uses an OpenAI-powered AI advisor named **Cory** to analyze the completed driving session.

> **Note:** my project is just a personal project software simulation built for fun. It does not control a real vehicle and is not intended for safety-critical autonomous driving.

---

# Project Demonstration

I included a recorded demonstration of the project shows the complete AI pipeline running from start to finish.

The demonstration includes:

- Vehicle and environment initialization
- PyTorch neural-network predictions
- Autonomous acceleration and braking
- Autonomous lane-control decisions
- Real-time console output
- Pandas simulation logging
- Matplotlib performance visualization
- Cory AI analyzing the completed driving session
- OpenAI API integration

# Project Overview

The goal of this project was to build a simplified autonomous vehicle AI system while learning how multiple technologies can work together inside one software project.

The vehicle operates inside a simulated environment containing information such as:

- Vehicle speed
- Lane position
- Battery level
- Speed limit
- Obstacle distance
- Road condition

The vehicle's current state is converted into an observation and sent to a trained PyTorch neural network.

The neural network then predicts:

### Speed Actions

- Accelerate
- Brake
- Maintain speed

### Lane Actions

- Change lane left
- Change lane right
- Maintain lane

The simulated vehicle executes those decisions.

Every simulation step is recorded using Pandas and later visualized using Matplotlib.

After the simulation finishes, Cory uses the OpenAI API to analyze the vehicle's behavior and provide engineering feedback.

---

# AI System Architecture

The project separates different responsibilities into individual components.

```text
Vehicle + Environment
        |
        v
    Observation
        |
        v
PyTorch Neural Network
        |
        +-------------------+
        |                   |
        v                   v
 Speed Decision        Lane Decision
        |                   |
        +---------+---------+
                  |
                  v
              Car Actions
                  |
                  v
          Simulation Logger
                  |
          +-------+-------+
          |               |
          v               v
      Pandas          Matplotlib
          |
          v
      Cory Agent
          |
          v
      OpenAI API
          |
          v
Simulation Performance Analysis
```

---

# Neural Agent

The autonomous driving decisions are performed by a neural network built with **PyTorch**.

The neural network receives five numerical inputs:

```text
1. Vehicle Speed
2. Lane Position
3. Battery Level
4. Speed Limit
5. Obstacle Distance
```

The neural network contains shared hidden layers followed by two separate output heads.

```text
                    Vehicle Observation
                           |
                           v
                    Input Layer
                           |
                           v
                    Hidden Layer
                           |
                          ReLU
                           |
                           v
                    Hidden Layer
                           |
                          ReLU
                     /             \
                    /               \
                   v                 v
           Speed Output         Lane Output
               Head                 Head
                |                    |
            3 Classes            3 Classes
```

The two-output-head design allows the neural network to make a speed decision and a lane decision at the same time.

---

# Neural Network Technologies

The model was built using:

- `torch.nn.Module`
- `nn.Linear`
- ReLU activation
- Cross-entropy loss
- Adam optimizer
- Backpropagation
- Supervised learning
- Multi-output classification
- Model saving
- Model loading
- Neural-network inference

The model weights are saved using:

```python
torch.save(model.state_dict(), "neural_car_model.pth")
```

The trained model is later loaded by the neural agent for inference.

---

# Neural Network Outputs

The speed output contains three possible classes:

```text
0 = Accelerate
1 = Brake
2 = Maintain Speed
```

The lane output also contains three possible classes:

```text
0 = Change Lane Left
1 = Change Lane Right
2 = Maintain Lane
```

The neural network produces raw class scores called **logits**.

PyTorch's `argmax()` function is then used to select the action with the highest predicted score.

---

# Supervised Learning

The neural network currently uses a small supervised-learning dataset.

Each training example contains:

```text
Speed
Lane Position
Battery Level
Speed Limit
Obstacle Distance
```

along with the correct speed and lane actions.

Example:

```text
Observation:
[80, 0.3, 90, 100, 50]

Speed Action:
Accelerate

Lane Action:
Change Lane Left
```

The project currently serves as a proof of concept for the neural-network architecture and inference pipeline.

A larger dataset would significantly improve generalization.

---

# Car Simulation

The `Car` class represents the simulated vehicle.

The vehicle contains state information such as:

```text
Speed
Lane Position
Battery Level
```

The vehicle can perform actions including:

```python
car.accelerate(10)
car.brake(10)
car.steer("left", 0.1)
car.steer("right", 0.1)
```

Example console output:

```text
Accelerating by 10. New speed: 90 km/h
Steering left. New lane position: 0.2
```

---

# Environment Simulation

The `Environment` class represents conditions surrounding the vehicle.

It currently stores:

```text
Speed Limit
Obstacle Distance
Road Condition
```

Example:

```text
Speed Limit: 100 km/h
Obstacle Distance: 50 meters
Road Condition: dry
```

The environment can later be expanded to include:

- Weather
- Traffic
- Multiple vehicles
- Road hazards
- Traffic lights
- Pedestrians
- Dynamic speed limits

---

# Rule-Based Agent

Before implementing the neural network, my project includes a rule-based agent.

The rule-based agent helped establish baseline autonomous-driving behavior.

It uses programmed conditions to determine whether the vehicle should:

```text
Accelerate
Brake
Maintain Speed
Change Lane Left
Change Lane Right
Maintain Lane
```

This created a useful comparison between:

```text
Rule-Based Decision Making
            vs
Machine-Learned Decision Making
```

The rule-based agent is also used to construct the observation sent to the neural-network agent.

---

# Pandas Simulation Logger

my project uses **Pandas** to record every simulation step.

Each row contains:

```text
Time Step
Speed
Lane Position
Battery Level
Speed Limit
Obstacle Distance
Road Condition
Speed Action
Lane Action
```

Example structure:

```text
time_step | speed | lane_position | battery | obstacle | speed_action | lane_action
---------------------------------------------------------------------------------
0         | 80    | 0.3           | 90      | 50       | accelerate   | left
1         | 90    | 0.2           | 90      | 50       | accelerate   | left
2         | 100   | 0.1           | 90      | 50       | brake        | left
3         | 90    | 0.0           | 90      | 50       | accelerate   | left
```

Using a Pandas DataFrame makes it easy to:

- Analyze vehicle behavior
- Calculate statistics
- Visualize performance
- Detect patterns
- Feed simulation information into Cory

---

# Matplotlib Visualization

**Matplotlib** is used to visualize the simulation.

The graphs help reveal behaviors that may be difficult to identify from raw console output alone.

Examples include:

- Speed changes over time
- Speed-limit comparisons
- Lane-position changes
- Obstacle-distance changes
- Oscillating speed behavior
- Lane drift

During testing, the neural agent produced behavior similar to:

```text
Speed:

80 → 90 → 100 → 90 → 100 → 90
```

The model repeatedly alternated between accelerating and braking near the speed limit.

The lane behavior also demonstrated:

```text
0.3
 ↓
0.2
 ↓
0.1
 ↓
0.0
 ↓
-0.1
 ↓
-0.2
 ↓
-0.3
```

This revealed that the neural network needed more diverse training examples.

---

#Cory AI Advisor

My project includes an AI advisor named **Cory**.

Cory uses the **OpenAI API** to analyze the completed autonomous-driving simulation.

Cory does **not** directly control the vehicle.

Instead, Cory operates as a high-level AI analysis system.

```text
PyTorch
   |
Controls Vehicle
   |
   v
Simulation
   |
   v
Pandas Data
   |
   v
Cory
   |
   v
OpenAI API
   |
   v
Engineering Analysis
```

Cory receives summarized simulation information such as:

- Average speed
- Minimum obstacle distance
- Final lane position
- Speed-action frequency
- Lane-action frequency

Cory then analyzes:

1. How the vehicle performed
2. Unsafe or unusual behavior
3. Speed-control stability
4. Lane-control stability
5. Possible improvements

---

# Example Cory Analysis

A Cory response may look similar to:

```text
===== Cory the Autonomous Vehicle Agent Simulation Analysis =====

The vehicle generally maintained a speed close to the configured speed
limit, but repeatedly alternated between accelerating and braking.

Speed control showed some instability because the vehicle oscillated
between approximately 90 km/h and 100 km/h.

Lane control was less stable. The neural network repeatedly selected
the left steering action, causing the vehicle to drift away from the
center lane.

Two possible improvements:

1. Train the neural network using a larger and more diverse dataset.
2. Add more lane-position examples so the model learns when to maintain
   or correct its lane position.
```

The exact response varies because Cory uses generative AI.

---

# OpenAI API Integration

Cory uses the OpenAI Python SDK.

The API client is initialized using:

```python
from openai import OpenAI

client = OpenAI()
```

The OpenAI API key is loaded securely through an environment variable.

The project does **not** store the API key inside the Python source code.

---

# API Key Setup

Create an OpenAI API key from the OpenAI Platform.

Then create an environment variable called:

```text
OPENAI_API_KEY
```

On Windows PowerShell:

```powershell
setx OPENAI_API_KEY "YOUR_API_KEY"
```

Restart Visual Studio or your terminal after setting the variable.

### Security Warning

Never place an API key directly inside:

```text
CoryAgent.py
README.md
GitHub
Screenshots
Demo videos
Source files
```

Never commit:

```text
.env
API keys
Passwords
Private credentials
```

to a public GitHub repository.

---

# Project Structure

```text
Cory-Autonomous-Vehicle-Agent/
│
├── Autonomous_AI_Car.py
├── Car.py
├── environment.py
├── Agent.py
├── NeuralNetwork.py
├── TrainNeuralAgent.py
├── NeuralAgent.py
├── SimulationLogger.py
├── CoryAgent.py
├── neural_car_model.pth
├── README.md
└── .gitignore
```

---

# File Responsibilities

| File | Purpose |
|------|---------|
| `Autonomous_AI_Car.py` | Main program that connects the complete simulation |
| `Car.py` | Represents the simulated autonomous vehicle |
| `environment.py` | Represents road and environmental conditions |
| `Agent.py` | Implements observation logic and rule-based behavior |
| `NeuralNetwork.py` | Defines the PyTorch neural-network architecture |
| `TrainNeuralAgent.py` | Trains and saves the neural-network model |
| `NeuralAgent.py` | Loads the trained model and performs predictions |
| `SimulationLogger.py` | Records simulation data with Pandas and visualizes it with Matplotlib |
| `CoryAgent.py` | Uses the OpenAI API to analyze simulation performance |
| `neural_car_model.pth` | Stores trained PyTorch model weights |
| `README.md` | Project documentation |
| `.gitignore` | Prevents unnecessary or sensitive files from being committed |

---

# Technologies Used

## Programming Language

- Python

## Machine Learning

- PyTorch
- Neural Networks
- Supervised Learning
- Multi-output Classification
- Model Training
- Model Inference

## Data Processing

- NumPy
- Pandas

## Visualization

- Matplotlib

## Generative AI

- OpenAI API
- OpenAI Responses API

## Software Engineering

- Object-Oriented Programming
- Modular Architecture
- Classes
- Model Persistence
- API Integration
- Environment Variables

## Development Tools

- Visual Studio
- Git
- GitHub

---

# ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd Cory-Autonomous-Vehicle-Agent
```

Install the required libraries:

```bash
pip install torch numpy pandas matplotlib openai
```

---

# Training the Neural Network

Run:

```bash
python TrainNeuralAgent.py
```

The training script:

```text
Loads training examples
        ↓
Creates PyTorch tensors
        ↓
Runs forward propagation
        ↓
Calculates speed loss
        ↓
Calculates lane loss
        ↓
Combines losses
        ↓
Runs backpropagation
        ↓
Updates weights using Adam
        ↓
Saves trained model
```

After training, the following model file is created:

```text
neural_car_model.pth
```

---

# Running the Complete Simulation

Run:

```bash
python Autonomous_AI_Car.py
```

The program will:

```text
1. Create the simulated vehicle
2. Create the simulated environment
3. Load the trained PyTorch model
4. Observe the vehicle and environment
5. Generate neural-network predictions
6. Execute speed decisions
7. Execute lane decisions
8. Record simulation information with Pandas
9. Calculate simulation statistics
10. Send the results to Cory
11. Receive OpenAI-generated performance feedback
12. Display Matplotlib visualizations
```

---

# Complete Program Flow

```text
START
  |
  v
Create Car
  |
  v
Create Environment
  |
  v
Load Neural Network
  |
  v
Observe Vehicle State
  |
  v
Convert Observation to Tensor
  |
  v
PyTorch Neural Network
  |
  +----------------+
  |                |
  v                v
Speed Action    Lane Action
  |                |
  +-------+--------+
          |
          v
     Execute Action
          |
          v
    Pandas Logger
          |
          v
   Continue Simulation
          |
          v
 Simulation Finished
          |
     +----+----+
     |         |
     v         v
   Cory    Matplotlib
     |
     v
OpenAI Analysis
     |
     v
    END
```

---

# Example Simulation

A simulation may begin with:

```text
Vehicle Speed: 80 km/h
Lane Position: 0.3
Battery Level: 90%
Speed Limit: 100 km/h
Obstacle Distance: 50 meters
Road Condition: dry
```

The neural network may then produce:

```text
Accelerating by 10. New speed: 90 km/h
Steering left. New lane position: 0.2

Accelerating by 10. New speed: 100 km/h
Steering left. New lane position: 0.1

Braking by 10. New speed: 90 km/h
Steering left. New lane position: 0.0
```

The complete session is then recorded by Pandas and analyzed after the simulation.

---

# Software Engineering Design

Rather than building the entire project inside one Python file, the project separates responsibilities.

For example:

```text
Car.py
        Vehicle behavior

environment.py
        Environmental state

Agent.py
        Observation and baseline logic

NeuralNetwork.py
        Neural architecture

TrainNeuralAgent.py
        Model training

NeuralAgent.py
        Model inference

SimulationLogger.py
        Data collection and visualization

CoryAgent.py
        AI-generated analysis

Autonomous_AI_Car.py
        Main integration
```

This modular structure makes the code easier to:

- Understand
- Test
- Debug
- Modify
- Expand
- Maintain

---

# Machine Learning Observations

One of the most important lessons from this project came from observing the neural network outside its original training examples.

The network correctly learned several examples from the training dataset.

However, during a longer simulation, the neural agent sometimes continued steering left even after passing the center lane.

For example:

```text
0.3
0.2
0.1
0.0
-0.1
-0.2
-0.3
-0.4
```

This demonstrated the difference between:

```text
Memorization
      vs
Generalization
```

A neural network can achieve excellent performance on its training examples while still making poor predictions when encountering new states.

This showed why machine-learning systems require:

- Larger datasets
- Diverse examples
- Training/testing splits
- Model evaluation
- Real-world validation

---

# Current Limitations

This project is intentionally simplified.

The current neural-network model was trained using a small proof-of-concept dataset.

Because of this, the model may:

- Overfit training examples
- Make incorrect predictions on unseen observations
- Drift from the desired lane
- Oscillate between acceleration and braking
- Produce imperfect autonomous-driving behavior

The current simulation also does not include:

- Real cameras
- Real computer vision
- LiDAR
- Radar
- GPS
- Real vehicle physics
- Real traffic
- Real pedestrians
- Real steering hardware
- Real braking hardware

This project should therefore be viewed as an **AI and software-engineering simulation**, not a production autonomous-driving system.

---

# Future Improvements

Possible future improvements include:

- Generate hundreds or thousands of driving scenarios
- Create larger training datasets
- Add training/testing splits
- Normalize neural-network inputs
- Measure model accuracy
- Add confusion matrices
- Improve lane-control training
- Improve speed-control behavior
- Add realistic braking-distance calculations
- Make obstacle movement depend on vehicle speed
- Add collision detection
- Add weather conditions
- Add multiple vehicles
- Add pedestrians
- Add traffic lights
- Add dynamic road conditions
- Add computer vision
- Add camera simulation
- Experiment with reinforcement learning
- Build a Gymnasium environment
- Experiment with PPO or DQN
- Compare rule-based and neural agents
- Build a graphical interface
- Create longer autonomous-driving scenarios

---

# What I Learned

This project helped me develop experience with:

- Python
- Object-oriented programming
- Software architecture
- PyTorch
- Neural networks
- Supervised learning
- Classification
- Forward propagation
- Backpropagation
- Cross-entropy loss
- Adam optimization
- Tensors
- NumPy
- Pandas
- Matplotlib
- Model training
- Model inference
- Saving and loading ML models
- API integration
- OpenAI API
- Prompt engineering
- Environment variables
- Debugging
- Data visualization
- AI-agent architecture
- Overfitting
- Generalization
- Modular software development

One of the most valuable lessons was seeing how a model could correctly learn its original training examples but still behave unexpectedly when introduced to new simulation states.

---

# Project Purpose

This project was created to strengthen my understanding of:

```text
Artificial Intelligence
Machine Learning
Autonomous Agents
Software Engineering
Data Analysis
API Integration
```

It also demonstrates how traditional machine learning and generative AI can work together inside the same software system.

```text
PyTorch
   ↓
Low-Level Decision Making

OpenAI / Cory
   ↓
High-Level Analysis
```

---

# Author

## Emmanuel Ray

Computer Science Student  
**Florida A&M University**

Areas of interest:

- Artificial Intelligence
- Machine Learning
- Autonomous Agents
- Software Engineering
- Audio Software
- Digital Signal Processing
- Creative Technology

---

# Repository

**Repository Name**

```text
Cory-Autonomous-Vehicle-Agent
```

**Suggested GitHub Description**

```text
Console-based autonomous vehicle AI simulation using Python, PyTorch, Pandas, Matplotlib, and the OpenAI API for neural driving decisions, data logging, visualization, and post-run analysis.
```

---

# Repository Configuration

Recommended GitHub settings:

```text
Visibility: Public

README: Enabled

.gitignore: Python

License: MIT License
```

A public repository allows recruiters and other developers to review the project without requesting access.

---

# License

This project can be distributed under the **MIT License**.

The MIT License allows others to view, use, modify, and distribute the project while preserving the original copyright notice.

---

# Final Project Pipeline

```text
                CORY
   AUTONOMOUS VEHICLE AI SIMULATION

                    |
                    v
            Vehicle Environment
                    |
                    v
              Observation
                    |
                    v
             NumPy Array
                    |
                    v
              PyTorch Model
               /        \
              /          \
             v            v
        Speed AI       Lane AI
             \            /
              \          /
                   v
             Vehicle Actions
                   |
                   v
              Pandas Logger
               /        \
              /          \
             v            v
      Matplotlib        Cory AI
      Visualization        |
                           v
                      OpenAI API
                           |
                           v
                 Performance Analysis
```

---

# Disclaimer

This project was created for fun.

It is just my simulated autonomous vehicle software project and is **not intended to operate, control, or make safety decisions for a real vehicle**.

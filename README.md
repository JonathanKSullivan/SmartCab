# SmartCab
Used reinforcement learning techniques to construct a demonstration of a smartcab operating in real-time.
## Purpose:
In this project I applied reinforcement learning techniques for a self-driving agent in a simplified world to aid it in effectively reaching its destinations in the allotted time. I first investigated the environment the agent operates in by constructing a very basic driving implementation. Once my agent was successful at operating within the environment, I then identified each possible state the agent can be in when considering such things as traffic lights and oncoming traffic at each intersection. With the states identified, I then implemented a Q-Learning algorithm for the self-driving agent to guide the agent towards its destination within the allotted time. Finally, I improve upon the Q-Learning algorithm to find the best configuration of learning and exploration factors to ensure the self-driving agent is reaching its destinations with consistently positive results.
## How to use:
This project contains three directories:
* /images/: This folder contains various images of cars to be used in the graphical user interface.
* /smartcab/: This folder contains the Python scripts that create the environment, graphical user interface, the simulation, and the agents.
It also contains two files:
* smartcab.ipynb: This is the main file where I answered questions and provide an analysis for your work.
* visuals.py: This Python script provides supplementary visualizations for the analysis.
* smartcab.pdf: Final Report
Finally, in /smartcab/ are the following four files:
agent.py: This is the main Python file where I performed my work on the project.
environment.py: This Python file will create the smartcab environment.
planner.py: This Python file creates a high-level planner for the agent to follow towards a set goal.
simulation.py: This Python file creates the simulation and graphical user interface.
### To view results 
Open up a browser window or tab. Click file then open. Navigate to the folder containing the project files and double click smartcab.pdf .
### To interact with ipynb file
In the Terminal or Command Prompt, navigate to the folder containing the project files, and then use the command jupyter notebook smartcab.ipynb to open up a browser window or tab to work with your notebook.

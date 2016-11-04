import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import numpy as np
import math, collections

#random.seed(0)
class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""
    
    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint

        # TODO: Initialize any additional variables here
        self.actions = ['forward', 'left', 'right', None]
    	self.matrix_dim_state = 6
    	self.matrix_dim_action = 4
    	self.Q_dictionary = collections.defaultdict(list)
    	self.state_last = None
    	self.opt_action_last = None
    	self.age = 1
        self.reward_total = 0

    def compute_Q(self, reward, q = 0.0, gamma = .5):
        return reward +  gamma * max(q)
    def reset(self, destination=None):
        self.planner.route_to(destination)
        self.reward_total = 0
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.age = self.age  + 1 

    def update(self, t):
        epsilon = [ 2, 2 * self.age]
        alpha = 1
        gamma = 1
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        
        self.state = (inputs['left'], inputs['light'], inputs['oncoming'], self.next_waypoint)
        
        # TODO: Select action according to your policy

        if random.randint(0,epsilon[1]) in range(epsilon[0]):
        	opt_action = random.randint(0,3)
        	action = self.actions[opt_action]
        else:
            opt_action = np.argmax(np.array(self.Q_dictionary[self.state])) if self.Q_dictionary[self.state] != [] else random.randint(0,3)
            action = self.actions[opt_action]
        # Execute action and get reward
        reward = self.env.act(self, action)

        # TODO: Learn policy based on state, action, reward
        
        if self.state_last != None: 
            if self.Q_dictionary[self.state_last] == []:
                self.Q_dictionary[self.state_last] = [4,4,4,4]
            if self.Q_dictionary[self.state] == []:
                self.Q_dictionary[self.state] = [4,4,4,4]
                self.Q_dictionary[self.state_last][self.opt_action_last] = (1-alpha) * self.Q_dictionary[self.state_last][self.opt_action_last] + alpha*self.compute_Q(reward=self.reward_last, q = self.Q_dictionary[self.state], gamma = gamma)
    	#print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]
        #print('('+str(self.state)+','+str(action)+')'+'->'+str(reward))
    	self.state_last = self.state
    	self.opt_action_last = opt_action
        self.reward_last = reward
        self.reward_total = self.reward_total + reward
        print "total"+str(self.reward_total)

def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=.0005, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()

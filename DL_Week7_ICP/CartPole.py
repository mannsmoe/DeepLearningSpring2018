# Importing the required packages
import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Identifying the number of times to run the game and learn from it
RunningTimes = 100

# Specifying the Agent characteristics 
class AgentFunc:
    def __init__(self, AgentSize, AgentChar):
        self.AgentSize = AgentSize
        self.AgentChar = AgentChar
        self.memory = deque(maxlen=2000)
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_min = 0.02
        self.epsilon_decay = 0.98
        self.learning_rate = 0.01
        self.model = self._build_model()
        
# Identifying the model layers
    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.AgentSize, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.AgentChar, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model
    def remember(self, Var1, Var2, Var3, Var4, RepVar5):
        self.memory.append((Var1, Var2, Var3, Var4, RepVar5))
    def act(self, Var1):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.AgentChar)
        Var6 = self.model.predict(Var1)
        return np.argmax(Var6[0])
    def replay(self, batch_size):
        BatchMin = random.sample(self.memory, batch_size)
        for Var1, Var2, Var3, Var4, RepVar5 in BatchMin:
            CompareVar7 = Var3
            if not RepVar5:
                CompareVar7 = (Var3 + self.gamma *
                          np.amax(self.model.predict(Var4)[0]))
            CompVar8 = self.model.predict(Var1)
            CompVar8[0][Var2] = CompareVar7
            self.model.fit(Var1, CompVar8, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
    def load(self, name):
        self.model.load_weights(name)
    def save(self, name):
        self.model.save_weights(name)

# Setting and identifying the game running model (Mountain Car Version 0)# Setting and identifying the game running model (Cart Pole Version 1)
if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    AgentSize = env.observation_space.shape[0]
    AgentChar = env.action_space.n
    agent = AgentFunc(AgentSize, AgentChar)
    RepVar5 = False
    batch_size = 32
    for e in range(RunningTimes):
        Var1 = env.reset()
        Var1 = np.reshape(Var1, [1, AgentSize])
        for time in range(500):
            env.render()
            Var2 = agent.act(Var1)
            Var4, Var3, RepVar5, _ = env.step(Var2)
            Var3 = Var3 if not RepVar5 else -10
            Var4 = np.reshape(Var4, [1, AgentSize])
            agent.remember(Var1, Var2, Var3, Var4, RepVar5)
            Var1 = Var4
            if RepVar5:
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, RunningTimes, time, agent.epsilon))
                break
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)

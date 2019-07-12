import gym
import gym_connect4
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy, MaxBoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory


#env = gym.make('gym_connect4:Connect4VsRandomBot-v0')

#episodes = 10
#score = 0

#for episode in range(0, episodes):
#    state = env.reset()
#    done = False
#    while not done:
#        action = np.random.choice(env.action_space)
#        n_state, reward, done, info = env.step(action)
#        score = score + reward
#    env.render()
#    print('episode {} score {}'.format(episode, score))


#env.close()
##############################################3
#for x in range(30):
#    temp = np.random.choice(env.action_space)
#    print('move: {}'.format(temp))
#    print('move: {}'.format(type(temp)))
#    env.step(temp)
##    print(env.done)
#    env.render()
#    if env.done:
#        print("Done!")
#        break

#env.render()
#env.step(0)
#env.step(0)
#env.step(0)
#env.step(0)
#print(env.check_winner())


########################################### KERAS STUFF AFTER HERE #############
class Metrics(keras.callbacks.Callback):
    def __init__(self, agent):
        keras.callbacks.Callback.__init__
        self.agent=agent

    def on_train_begin(self, logs={}):
        self.metrics = {key: [] for key in self.agent.metrics_names}

    def on_step_end(self, episode_step, logs):
        for ordinal, key in enumerate(self.agent.metrics_names, 0):
            self.metrics[key].append(logs.get('metrics')[ordinal])

env_name = 'gym_connect4:Connect4VsRandomBot-v0'
#env_name = 'gym_connect4:Connect4VsHuman-v0'
env = gym.make(env_name)

model = Sequential()
#model.add(Flatten(input_shape=(1,1)))
#model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Conv2D(16, (3,3), input_shape=(1, 6, 7), activation='relu', data_format='channels_first'))
model.add(MaxPooling2D((2,2)))
#model.add(Conv2D(16, (3, 3), activation='relu'))
#model.add(Conv2D(16, (3, 3), activation='relu'))
#model.add(Conv2D(16, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(7))
model.add(Activation('linear'))
print(model.summary())

memory = SequentialMemory(limit=1000000, window_length=1)
policy = MaxBoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=7, memory=memory, nb_steps_warmup=10, target_model_update=1e-2, policy=policy)

dqn.compile(Adam(lr=1e-3), metrics=['mae'])

metrics = Metrics(dqn)

dqn.load_weights('dqn_MaxBoltzmann_weights32.h5f'.format(env_name))

dqn.fit(env, nb_steps=1000000, visualize=False, verbose=2, callbacks=[metrics])

dqn.save_weights('dqn_MaxBoltzmann_weights32.h5f'.format(env_name), overwrite=True)

dqn.test(env, nb_episodes=100, visualize=False)

env.close()



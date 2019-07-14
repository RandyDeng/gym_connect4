import gym
import gym_connect4
import numpy as np
import pickle

from keras.callbacks import Callback
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy, MaxBoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory


class Metrics(Callback):
    def __init__(self, agent):
        Callback.__init__
        self.agent=agent

    def on_train_begin(self, logs={}):
        self.metrics = {key: [] for key in self.agent.metrics_names}

    def on_step_end(self, episode_step, logs):
        for ordinal, key in enumerate(self.agent.metrics_names, 0):
            self.metrics[key].append(logs.get('metrics')[ordinal])


def build_model():
    model = Sequential()
    model.add(Conv2D(16, (3,3), input_shape=(1, 6, 7), activation='relu', data_format='channels_first'))
    model.add(MaxPooling2D((2,2)))
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
    return model


def main():
    # Setup Environment
    # Available environments:
    # 'gym_connect4:Connect4VsRandomBot-v0'
    # 'gym_connect4:Connect4VsSelf-v0'
    #env_name = 'gym_connect4:Connect4VsHuman-v0'
    env_name = 'gym_connect4:Connect4VsRandomBot-v0'
    env = gym.make(env_name)

    # Build Neural Network Architecture for Reinforcement Learning
    model = build_model()
    memory = SequentialMemory(limit=1000000, window_length=1)
    policy = EpsGreedyQPolicy()
    dqn = DQNAgent(model=model,
                   nb_actions=7,
                   memory=memory,
                   nb_steps_warmup=10,
                   target_model_update=1e-2,
                   policy=policy)
    metrics = Metrics(dqn)

    # Train the Neural Network
    filename = 'dqn_EpsGreedy{}'
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    dqn.load_weights(filename.format('.weights32'))
    dqn.fit(env, nb_steps=1000000, visualize=False, verbose=2, callbacks=[metrics])
    dqn.save_weights(filename.format('.weights32'), overwrite=True)
    pickle.dump(metrics.metrics, open(filename.format('.metrics'), 'wb'))
    #dqn.load_weights(filename.format('.weights32'))
    dqn.test(env, nb_episodes=100, visualize=True)
    env.close()
    
    # Save metrics to file

if __name__ == "__main__":
    main()
 

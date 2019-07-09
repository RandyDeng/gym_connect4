import gym
import gym_connect4
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
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
env_name = 'gym_connect4:Connect4VsRandomBot-v0'
env = gym.make(env_name)

model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
#model.add(Flatten(input_shape=(1,1)))
#model.add(Dense(16))
#model.add(Activation('relu'))
#model.add(Dense(16))
#model.add(Activation('relu'))
#model.add(Dense(16))
#model.add(Activation('relu'))
model.add(Dense(7))
model.add(Activation('linear'))
print(model.summary())

memory = SequentialMemory(limit=50000, window_length=1)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=7, memory=memory, nb_steps_warmup=10, target_model_update=1e-2, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

dqn.fit(env, nb_steps=50000, visualize=True, verbose=2)

dqn.save_weights('dqn_{}_weights.h5f'.format(env_name), overwrite=True)

dqn.test(env, nb_episodes=5, visualize=True)

env.close()



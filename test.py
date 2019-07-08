import gym
import gym_connect4
import numpy as np


env = gym.make('gym_connect4:Connect4VsRandomBot-v0')

episodes = 10
score = 0

for episode in range(0, episodes):
    state = env.reset()
    done = False
    while not done:
        action = np.random.choice(env.action_space)
        n_state, reward, done, info = env.step(action)
        score = score + reward
    env.render()
    print('episode {} score {}'.format(episode, score))



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

env.close()

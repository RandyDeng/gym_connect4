import gym
import gym_connect4
import numpy as np


env = gym.make('gym_connect4:Connect4VsRandomBot-v0')
env.reset()


for x in range(30):
    temp = np.random.randint(7)
    print('move: {}'.format(temp))
    print('move: {}'.format(type(temp)))
    env.step(temp)
    print(env.done)
    env.render()
    if env.done:
        print("Done!")
        break

#env.render()
#env.step(0)
#env.step(0)
#env.step(0)
#env.step(0)
#print(env.check_winner())

env.close()

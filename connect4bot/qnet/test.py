import gym
import gym_connect4

env = gym.make('C4VsHuman-v0')
env._reset()

for x in range(10):
    env._render()
    temp = env.action_space.sample()
    print(temp)
    env._step(temp)

env.close()

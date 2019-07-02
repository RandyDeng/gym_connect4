import gym
import gym_connect4


env = gym.make('gym_connect4:Connect4VsRandomBot-v0')
env._reset()


# for x in range(30):
#     env._render()
#     temp = env.action_space.sample()
#     print('move: {}'.format(temp))
#     env._step(temp)

env._render()
env._step(0)
env._step(0)
env._step(0)
env._step(0)
print(env.check_winner())

env.close()

from gym.envs.registration import register


register(
	id='Connect4VsRandomBot-v0',
	entry_point='gym_connect4.envs:Connect4Env',
	#kwargs={'opponent' : 'random'},
)

register(
	id='Connect4VsSelf-v0',
	entry_point='gym_connect4.envs:Connect4Env',
	#kwargs={'opponent' : 'none'},
	# max_episode_steps=100,
	# reward_threshold=.0, # optimum = .0
)

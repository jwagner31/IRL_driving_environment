import gymnasium as gym
from custom_highway_env import CustomHighwayEnv

# Create the environment
env = CustomHighwayEnv()

# Reset the environment
obs, info = env.reset()

# Print initial observation shape and action space
print(f"Observation space: {env.observation_space}")
print(f"Action space: {env.action_space}")

# Run a few steps to test
for _ in range(5):
    action = env.action_space.sample()  # Random action
    obs, reward, done, truncated, info = env.step(action)
    print(f"\nAction taken: {action}")
    print(f"Reward: {reward}")
    print(f"Next state info: {info}")
    print(f"Done: {done}")
    print(f"Truncated: {truncated}") 
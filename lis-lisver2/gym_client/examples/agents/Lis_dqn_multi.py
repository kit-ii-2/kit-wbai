# coding:utf-8
import argparse
import six
from cnn_dqn_agent import CnnDqnAgent
import gym
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--gpu', '-g', default=-1, type=int,
                    help='GPU ID (negative value indicates CPU)')
parser.add_argument('--log-file', '-l', default='reward.log', type=str,
                    help='reward log file name')
parser.add_argument('--agent-count', '-', default=1, type=int,
                    help='number of agent')
args = parser.parse_args()

#agent = CnnDqnAgent()
agent_initialized = False
cycle_counter = 0
log_file = args.log_file
reward_sum_lis = [0]*args.agent_count
depth_image_dim = 32 * 32
depth_image_count = 1
total_episode = 10000
episode_count = 1
aglis = [CnnDqnAgent()]*args.agent_count
aclis = [0]*args.agent_count
observationlis = [0]*args.agent_count
rewardlis = [0]*args.agent_count
end_episodelis = [0]*args.agent_count
epslis = [0]*args.agent_count
q_nowlis = [0]*args.agent_count
obs_arraylis = [0]*args.agent_count

env = []*args.agent_count

while episode_count <= total_episode:
    if not agent_initialized:
        agent_initialized = True
        print ("initializing agent...")
        for i in six.moves.range(args.agent_count):
            print("asdfghgfdsdfghgfdsdfghjhgfdfghjhgfdsdfg")
            aglis[i].agent_init(
            use_gpu=args.gpu,
            depth_image_dim=depth_image_dim * depth_image_count)

        for i in six.moves.range(args.agent_count):
            print i
            env[i] = gym.make('Lis-v2')

        for i in six.moves.range(args.agent_count):
            observationlis[i] = env[i].reset()
        
        for i in six.moves.range(args.agent_count):
            aclis[i]=aglis[i].agent_start(observation[i])  
        
        observationlis, rewardlis, end_episode, _ = env[i].step(aclis)  

        with open(log_file, 'w') as the_file:
            the_file.write('cycle, episode_reward_sum_lis[i] \n')
    else:
        cycle_counter += 1 
        for i in six.moves.range(args.agent_count):
            reward_sum_lis[i] += rewardlis[i]

        if end_episode:
            for i in six.moves.range(args.agent_count):
                aglis[i].agent_end(rewardlis[i])

            for i in six.moves.range(args.agent_count):
                aclis[i]=aglis[i].agent_start(observationlis[i])  
        
            observationlis, rewardlis, end_episodelis, _ = env[i].step(aclis) #CHECK

            with open(log_file, 'a') as the_file:
                the_file.write(str(cycle_counter) +
                               ',' + str(reward_sum_lis) + '\n')
            
            for i in six.moves.range(args.agent_count):
                reward_sum_lis[i] = 0
            
            episode_count += 1

        else:
            for i in six.moves.range(args.agent_count):
                print aclis[i]
                print epslis[i]
                print q_nowlis[i]
                print obs_arraylis[i]
                print aglis[i]
                print rewardlis[i]
                print observationlis[i]

                aclis[i], epslis[i], q_nowlis[i], obs_arraylis[i] = aglis[i].agent_step(rewardlis[i], observationlis[i])  
                aglis[i].agent_step_update(rewardlis[i], aclis[i], epslis[i], q_nowlis[i], obs_arraylis[i])
            
            observationlis, rewardlis, end_episodelis, _ = env[i].step(aclis)  

for i in six.moves.range(args.agent_count):
    env[i].close()

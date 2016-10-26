# -*- coding: utf-8 -*-

import websocket
import msgpack
import gym
import io
from PIL import Image
from PIL import ImageOps
from gym import spaces
import numpy as np
import time

aglib = []

class GymUnityEnv(gym.Env):

    def port_number():
        port_number.count += 1
        print port_number.count
    port_number.count = 4649

    def __init__(self):
        websocket.enableTrace(True)
    	self.ws = websocket.create_connection("ws://localhost:"+ str(self.port_number.count) +"/CommunicationGym")
        self.action_space = spaces.Discrete(3)
        self.depth_image_dim = 32 * 32
        self.depth_image_count = 1
        self.observation, _, _ = self.receive()
        port_number()

    def reset(self):
        return self.observation



    def step(self, action):   #送信

        acstr = map(str,action)
        sendmsg = ':'.join(acstr)
        actiondata = msgpack.packb({"command": sendmsg})
        self.ws.send(actiondata)

        # Unity Process

        observation, reward, end_episode = self.receive()

        return observation, reward, end_episode, {}

    def receive(self): #Unityとの受信

        while True:

            statedata = self.ws.recv()

            if not statedata:
                continue

            state = msgpack.unpackb(statedata) #unpackして配列にキャスト、

            statelis = state[]
            
            observationlis = []
            rewardlis = []
            end_episodelis = []

            for j in range (0,2):
                image = []
                for i in xrange(self.depth_image_count):
                    image.append(Image.open(io.BytesIO(bytearray(state['image'][i]))))
                
                depth = []
                for i in xrange(self.depth_image_count):
                    d = (Image.open(io.BytesIO(bytearray(state['depth'][i]))))
                    depth.append(np.array(ImageOps.grayscale(d)).reshape(self.depth_image_dim))

                observation = {"image": image, "depth": depth}
                observationlis.append(observation)
                reward = state['reward']
                rewardlis.append(reward)
                end_episode = state['endEpisode']
                end_episodelis.append(end_episode)

            return observationlis, rewardlis, end_episodelis
            break

    def close(self):
        self.ws.close()

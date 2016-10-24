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

class port_number():
        def __init__(self):
            self.count = 4649

        def incliment(self):
            self.count += 1
            print self.count

class GymUnityEnv(gym.Env):

    def __init__(self):
        if 'pnum' in globals():
            self.pnum.incliment() 
        else:
            self.pnum = new port_number()
            
        websocket.enableTrace(True)
        print "ws://localhost:"+ str(pnum.count) +"/CommunicationGym" 
    	self.ws = websocket.create_connection("ws://localhost:"+ str(self.pnum.count) +"/CommunicationGym")

        print self.pnum.count
        self.action_space = spaces.Discrete(3)
        self.depth_image_dim = 32 * 32
        self.depth_image_count = 1
        self.observation, _, _ = self.receive()

    def reset(self):
        return self.observation

    def step(self, action):

        actiondata = msgpack.packb({"command": str(action)})
        self.ws.send(actiondata)

        # Unity Process

        observation, reward, end_episode = self.receive()

        return observation, reward, end_episode, {}

    def receive(self):

        while True:

            statedata = self.ws.recv()

            if not statedata:
                continue

            state = msgpack.unpackb(statedata)

            image = []
            for i in xrange(self.depth_image_count):
                image.append(Image.open(io.BytesIO(bytearray(state['image'][i]))))
            depth = []
            for i in xrange(self.depth_image_count):
                d = (Image.open(io.BytesIO(bytearray(state['depth'][i]))))
                depth.append(np.array(ImageOps.grayscale(d)).reshape(self.depth_image_dim))

            observation = {"image": image, "depth": depth}
            reward = state['reward']
            end_episode = state['endEpisode']

            return observation, reward, end_episode
            break

    def close(self):
        self.ws.close()u
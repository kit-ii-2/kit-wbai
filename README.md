# kit-wbai　project 2016/10/10
WBAI hackathons Summary

In this program, two agents learn movement and capturing targets with
the Deep Q-Network.

・Environment

When started, two agents and a target creature are placed at random on
a three-dimensional space.
The agents are of LIS_ver2.

・Task

The agents are to capture the fleeing target.
The target can move faster than the agents and repeats random movement.
If the agents come close to the target, it tries to avoid them by
setting its destination at random.

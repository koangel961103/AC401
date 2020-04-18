# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:25:28 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
import random
import time
pos=mc.player.getPos()
while True:
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    y=pos.y+30
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.1)
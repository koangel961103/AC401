# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:05:00 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
from random import randrange
for i in range(20):
    r=randrange(1,7)
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,169)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,169)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,169)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,169)
        z=z-4
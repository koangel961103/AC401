# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:00:10 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+2,z+1,x-1,y+4,z-1,18)
    mc.setBlocks(x,y,z,x,y+3,z,17)
for i in range(10):
    for j in range(5):
        for k in range(5):
            plantTree(x+i,y+k*i,z+j*i)
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 09:59:21 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
for i in range(5):
    mc.setBlock(x+i,y-1,z+i,169)
    mc.setBlock(x+i,y-1,z+i+1,169)
    mc.setBlock(x+i,y-1,z+i+2,169)
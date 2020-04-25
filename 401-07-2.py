# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:45:55 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+1,y+2,z+1,x-1,y+4,z-1,18)
mc.setBlocks(x,y,z,x,y+3,z,17)
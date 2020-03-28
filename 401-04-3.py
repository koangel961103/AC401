# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:16:53 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0
x,y,z=mc.player.getTilePos()
while t<20:
    mc.setBlocks(x-5 ,y-5 ,z ,x+5 ,y+5 ,z ,19 ,0)
    t=t+1
    z=z+10
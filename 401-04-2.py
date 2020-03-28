# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:42:13 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x ,y ,z ,38)
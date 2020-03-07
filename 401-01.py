# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:27:40 2020

@author: 學生
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create();
print(mc.player.getTilePos())
x=5267
y=74
z=3257
mc.player.setTilePos(x,y,z)
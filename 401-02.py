# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:39:45 2020

@author: User
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("x="+str(x)+",y="+str(y)+",z="+str(z))
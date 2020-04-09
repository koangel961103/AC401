# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:51:18 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x ,y ,z ,8)
    time.sleep(30)
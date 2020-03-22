# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:45:35 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x-1 ,y ,z+1 ,x+1 ,y+2 ,z-1 ,5 ,0 )
mc.setBlocks(x ,y ,z ,x ,y+2 ,z ,0 )
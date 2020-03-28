# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:04:47 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+5 ,y+5 ,z+5 ,x-5 ,y-5 ,z-5 ,5 ,2)
mc.setBlocks(x+4 ,y+4 ,z+4 ,x-4 ,y-4 ,z-4 ,0)
mc.setBlocks(x+4 ,y+5 ,z+4 ,x-4 ,y+5 ,z-4 ,0)
mc.setBlock(x ,y ,z, 169)
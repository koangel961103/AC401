# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+1 ,y-1 ,z, x-1, y-1 , z, 89)
mc.setBlocks(x+2 ,y-1 ,z-1 , x-2, y-1, z-1, 174)
mc.setBlock(x ,y-1 ,z+1 , 1, 4)

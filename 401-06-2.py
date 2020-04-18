# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:12:32 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'','1234567','1234567','')
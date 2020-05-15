# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:24:15 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
line1=[]
for i in [1,2,3]:
    line1.append(1*i)
line2=[]
for j in [1,2,3]:
    line2.append(2*i)
line3=[]
for i in [1,2,3]:
    line3.append(3*i)
    mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))
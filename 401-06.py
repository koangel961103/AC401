# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:07:35 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        Block=mc.getBlock(x,y,z)
        Block=str(Block)
        mc.setBlock(x ,y ,z ,41)
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:40:02 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.player.setTilePos(x,y,z)
        mc.spawnEntity(x,y,z,99)
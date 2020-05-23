# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:42:35 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange
x,y,z=mc.player.getTilePos()
r=randrange(1,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        Block=mc.getBlockWithData(hit.pos)
        data=Block.data
        if data==r:
            mc.postToChat("恭喜你找到我(・∀・)")
            mc.setBlock(hit.pos,57)
        elif data>r:
            mc.postToChat("找錯瞜,試試更小的子ID吧!")
        elif data<r:
             mc.postToChat("找錯瞜,試試更大的子ID吧!")
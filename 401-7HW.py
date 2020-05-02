# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:50:14 2020

@author: User
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
try:
    blockType=int(input("請輸入要放的方塊ID:"))
    h=int(input("請輸入屋子的高度:"))
    w=int(input("請輸入屋子的寬度:"))
    l=int(input("請輸入屋子的長度:"))
    hblockType=int(input("請輸入要的屋頂方塊ID:"))
    mc.setBlocks(x+l ,y+h ,z+w ,x-l ,y ,z-w ,blockType)
    mc.setBlocks(x+l-1 ,y+h-1 ,z+w-1 ,x-l+1 ,y+1,z-w+1,0)
    mc.setBlocks(x+l-1 ,y+h-1 ,z+w-1 ,x-l+1 ,y+h-1,z-w+1,hblockType)
    
    mc.postToChat("blockType"+str(blockType))
except:
    print("只能輸入數字!!!")
for i in range(5):
    mc.setBlock(x+i,y-1,z+i+l,169)
    mc.setBlock(x+i,y-1,z+i+l+1,169)
    mc.setBlock(x+i,y-1,z+i+l+2,169)
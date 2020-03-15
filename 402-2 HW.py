# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:31:20 2020

@author: User
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#匯入Minecraft
while True:
#讓while迴圈判斷是True 才能執行
    x,y,z=mc.player.getTilePos()
#取得玩家位置時會回傳三個值 因此給予三個變數存放
    mc.postToChat("x="+str(x)+",y="+str(y)+",z="+str(z))
#將變數裡的座標轉換成文字列印在Minecraft聊天室
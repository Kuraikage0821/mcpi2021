from mcpi.minecraft import Minecraft
mc = Minecraft.create()

t=0
while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('X:'+str(x)+'Y:'+str(y)+'Z:'+str(z))
    
    
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+100,y,z+100,x-100,y,z-100,46)







import random
import time
x,y,z=mc.player.getTilePos()

while True:
    r=random.randrange(0,16)
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,35)
    time.sleep(0.5)











from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+4,y+4,z+4,35)
mc.setBlocks(x+1,y+1,z+1,x+3,y+3,z+3,0)


import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.5)


while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(10)
x,y,z=mc.player.getTilePos()

a=0
while a<5:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z=z+5
    a=a+1
    
x,y,z=mc.player.getTilePos()
a=int(input('想放什麼方塊?'))
mc.setBlock(x,y,z,a)
    

name=input('enter your name:')
message=input('enter your messange:')
mc.postToChat('<'+ name +'>'+ message)

x,y,z,=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'hi','','','Kuraikage')


while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        x,y,z,=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z,)
        mc.postToChat('Block ID:'+str(Block))
        
    
while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        x,y,z,=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z,)
        mc.getBlock(x,y,z,)
        
        if block == 1:
            mc.setBlock(x,y,z,57)
            
            
x,y,z,=mc.player.getPos()
mc.spawnEntity(x,y,z,93)
        
         

       

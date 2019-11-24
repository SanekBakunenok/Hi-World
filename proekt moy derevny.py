from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import keyboard
import time
import mcpi.block as Block
vihod = 1

def build():
    h = 25
    distance = 5
    pos = mc.player.getPos()
    x = round(pos.x)
    y = round(pos.y)
    z = round(pos.z)
    #чистка
    mc.setBlocks(pos.x-5,pos.y,pos.z-5,pos.x+h,pos.y+h,pos.z+h,Block. AIR.id)

    #стены
    mc.setBlocks(x,y,z,x,y+4,z+7,Block.STONE.id)
    mc.setBlocks(x,y,z+7,x+12,y+4,z+7,Block.STONE.id)
    mc.setBlocks(x+12,y,z,x+12,y+4,z+7,Block.STONE.id)
    mc.setBlocks(x+12,y,z,x+12,y+4,z+7,Block.STONE.id)
    mc.setBlocks(x+12,y,z,x,y+4,z,Block.STONE.id)
      

    #пол и крыша
    mc.setBlocks(x,y-1,z,x+12,y-1,z+7,Block.STONE.id)
    mc.setBlocks(x,y+4,z,x+12,y+4,z+7,Block.STONE.id)

    #okna
    mc.setBlocks(x+3,y+2,z,x+3,y+2,z,Block.GLASS.id)
    mc.setBlocks(x+9,y+2,z,x+9,y+2,z,Block.GLASS.id)
    mc.setBlocks(x+3,y+2,z+7,x+3,y+2,z+7,Block.GLASS.id)
    mc.setBlocks(x+9,y+2,z+7,x+9,y+2,z+7,Block.GLASS.id)
    mc.setBlocks(x,y+2,z+3,x,y+2,z+4,Block.GLASS.id)
    mc.setBlocks(x+12,y+2,z+3,x+12,y+2,z+4,Block.GLASS.id)

    #door
    mc
    

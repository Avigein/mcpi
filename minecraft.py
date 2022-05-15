from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()
playerPos = mc.player.getTilePos()

class House(object):
    def __init__(self):
        self.x = playerPos.x
        self.y = playerPos.y
        self.z = playerPos.z - 5

    def HouseStartMessage(self):
        counts = reversed(range(1, 4))

        for count in counts:
            mc.postToChat(count)
            print(count)
            time.sleep(1)
            
        mc.postToChat("Start!")

    def Substructure(self):
        # Y : -1 ~ 2(4)
        for y in range(-1, 3):
            mc.setBlock(self.x, self.y + y, self.z, block.WOOD.id, 0)
            for x in range(1, 4):
                mc.setBlock(self.x + x, self.y + y, self.z, block.AIR.id)
            mc.setBlock(self.x + 4, self.y + y, self.z, block.WOOD.id, 0)

            for z in range(1, 4):
                for x in range(0, 5):
                    mc.setBlock(self.x + x, self.y + y, self.z + z, block.AIR.id)

            mc.setBlock(self.x, self.y + y, self.z + 4, block.WOOD.id, 0)
            for x in range(1, 4):
                mc.setBlock(self.x + x, self.y + y, self.z + 4, block.AIR.id)
            mc.setBlock(self.x + 4, self.y + y, self.z + 4, block.WOOD.id, 0)

            time.sleep(1)

        # Y : 3(1)
        mc.setBlock(self.x, self.y + 3, self.z, block.WOOD.id, 0)
        for x in range(1, 4):
            mc.setBlock(self.x + x, self.y + 3, self.z, block.WOOD.id, 4)
        mc.setBlock(self.x + 4, self.y + 3, self.z, block.WOOD.id, 0)

        for z in range(1, 4):
            mc.setBlock(self.x, self.y + 3, self.z + z, block.WOOD.id, 8)
            for x in range(1, 4):
                mc.setBlock(self.x + x, self.y + 3, self.z + z, block.AIR.id)
            mc.setBlock(self.x + 4, self.y + 3, self.z + z, block.WOOD.id, 8)

        mc.setBlock(self.x, self.y + 3, self.z + 4, block.WOOD.id, 0)
        for x in range(1, 4):
            mc.setBlock(self.x + x, self.y + 3, self.z + 4, block.WOOD.id, 4)
        mc.setBlock(self.x + 4, self.y + 3, self.z + 4, block.WOOD.id, 0)

        time.sleep(1)

    def Wall(self):
        #left - back - right - front
        mc.setBlocks(self.x, self.y - 1, self.z + 1, self.x, self.y + 2, self.z + 3, block.COBBLESTONE.id)
        time.sleep(1)
        mc.setBlocks(self.x + 1, self.y - 1, self.z, self.x + 3, self.y + 2, self.z, block.COBBLESTONE.id)
        time.sleep(1)
        mc.setBlocks(self.x + 4, self.y - 1, self.z + 1, self.x + 4, self.y + 2, self.z + 3, block.COBBLESTONE.id)
        time.sleep(1)
        mc.setBlocks(self.x + 1, self.y - 1, self.z + 4, self.x + 3, self.y + 2, self.z + 4, block.COBBLESTONE.id)
        time.sleep(1)

    def Floor(self):
        mc.setBlocks(self.x + 1, self.y - 1, self.z + 1, self.x + 3, self.y - 1, self.z + 3, block.WOOD_PLANKS.id)
        time.sleep(1)

    def Roof(self):
        #flat
        mc.setBlocks(self.x + 1, self.y + 4, self.z, self.x + 3, self.y + 4, self.z + 4, block.COBBLESTONE.id)
        mc.setBlocks(self.x + 1, self.y + 4, self.z + 1, self.x + 3, self.y + 4, self.z + 3, block.WOOD_PLANKS.id)
        time.sleep(1)

        #roof
        for increase in range(0, 3):
            mc.setBlocks(self.x - 1 + increase, self.y + 3 + increase, self.z - 1, self.x - 1 + increase, self.y + 3 + increase, self.z + 5, block.STAIRS_WOOD.id)

        for increase in reversed(range(-3, 0)):
            mc.setBlocks(self.x + 6 + increase, self.y + 2 + abs(increase), self.z - 1, self.x + 6 + increase, self.y + 2 + abs(increase), self.z + 5, block.STAIRS_WOOD.id, 1)
    
        mc.setBlocks(self.x + 2, self.y + 5, self.z - 1, self.x + 2, self.y + 5, self.z + 5, block.WOOD_PLANKS.id)

        for increase in reversed(range(-1, 1)):
            mc.setBlock(self.x + abs(increase), self.y + 3 + abs(increase), self.z + 5, block.STAIRS_WOOD.id, 5)
            mc.setBlock(self.x + abs(increase), self.y + 3 + abs(increase), self.z - 1, block.STAIRS_WOOD.id, 5)
            mc.setBlock(self.x + 4 + increase, self.y + 3 + abs(increase), self.z + 5, block.STAIRS_WOOD.id, 4)
            mc.setBlock(self.x + 4 + increase, self.y + 3 + abs(increase), self.z - 1, block.STAIRS_WOOD.id, 4)
        time.sleep(1)

    def Decoration(self):
        #door
        mc.setBlocks(self.x + 2, self.y, self.z + 4, self.x + 2, self.y + 1, self.z + 4, block.AIR)
        time.sleep(1)

        #glass
        mc.setBlock(self.x, self.y + 1, self.z + 2, block.GLASS.id)
        time.sleep(1)
        mc.setBlock(self.x + 2, self.y + 1, self.z, block.GLASS.id)
        time.sleep(1)
        mc.setBlock(self.x + 4, self.y + 1, self.z + 2, block.GLASS.id)

    def HouseEndMessage():
        mc.postToChat("End!")

    def build(self):
        self.HouseStartMessage()
        self.Substructure()
        self.Wall()
        self.Floor()
        self.Roof()
        self.Decoration()
        self.HouseEndMessage()

newHouse = House()
newHouse.build()
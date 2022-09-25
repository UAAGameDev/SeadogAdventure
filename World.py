import math

class Tile:
    def __init__(self, traversable = 5, prop = 0, solidProp = 0, isWalkable = False):
        self.traversable = traversable
        self.prop = prop
        self.solidProp = solidProp
        self.isWalkable = isWalkable

class Chunk:
    def __init__(self, xSize, ySize, traversable = 0, prop = 0, solidProp = 0, isWalkable = False):
        self.data = []
        for x in range(xSize):
            self.data.append([])
            for y in range(ySize):
                if (x % 5 == 0):
                    self.data[x].append(Tile(traversable=5))
                elif (x % 5 == 1):
                    self.data[x].append(Tile(traversable=9, prop=16))
                else:
                    self.data[x].append(Tile(traversable=9))


class World:
    def __init__(self):
        self.Chunks = {}
        self.ChunkXSize = 16
        self.ChunkYSize = 16

    def initChunk(self, x, y):
        chunkKey=(x,y)
        self.Chunks[chunkKey]=Chunk(self.ChunkXSize, self.ChunkYSize)

    def getTile(self,x, y):
        return self.Chunks[(math.floor(x / self.ChunkXSize), math.floor(y / self.ChunkYSize))].data[x % self.ChunkXSize][y % self.ChunkYSize]




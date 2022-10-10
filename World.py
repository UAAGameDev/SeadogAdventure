import math
ChunkXSize = 16
ChunkYSize = 16


class Tile:
    def __init__(self, land = 5, prop = 0, solidProp = 0, isWalkable = False):
        self.land = land
        self.prop = prop
        self.solidProp = solidProp
        self.isWalkable = isWalkable

class Chunk:
    def __init__(self, data: list = [], traversable = 0, prop = 0, solidProp = 0, isWalkable = False):
        self.data = data
        if not data:
            for x in range(ChunkXSize):
                self.data.append([])
                for y in range(ChunkYSize):
                    self.data[x].append(Tile(land=6))
    def getTile(self,x, y):
        return self.data[x][y]


class Level:
    def __init__(self, chunks : map):
        self.Chunks = chunks
    def getTile(self,x, y):
        chunkX = math.floor(x / ChunkXSize)
        chunkY = math.floor(y / ChunkYSize)
        return self.Chunks[(chunkX,chunkY)].getTile(x % ChunkXSize, y % ChunkYSize)




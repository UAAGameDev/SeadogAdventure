import math
class Tile:
    def __init__(self, land = 5, prop = 0, solidProp = 0, isWalkable = False):
        self.land = land
        self.prop = prop
        self.solidProp = solidProp
        self.isWalkable = isWalkable

class Chunk:
    ChunkXSize = 16
    ChunkYSize = 16
    def __init__(self, data = [], traversable = 0, prop = 0, solidProp = 0, isWalkable = False):
        self.data = data

        if not data:
            for x in range(Chunk.ChunkXSize):
                self.data.append([])
                for y in range(Chunk.ChunkYSize):
                    if (x % 5 == 0):
                        self.data[x].append(Tile(land=5))
                    elif (x % 5 == 1):
                        self.data[x].append(Tile(land=9, prop=14))
                    else:
                        self.data[x].append(Tile(land=9))
class Level:
    def __init__(self, chunks : map, entities : list):
        self.Chunks = chunks
        self.Entities = entities
    def getTile(self,x, y):
        return self.Chunks[(math.floor(x / self.ChunkXSize), math.floor(y / self.ChunkYSize))].data[x % self.ChunkXSize][y % self.ChunkYSize]
    def save(self):
        pass



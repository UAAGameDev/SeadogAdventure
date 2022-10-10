import pygame
from World import Chunk, Level, Tile

w = Tile(land = 5)
f = Tile(land = 6)


chunk00Data = [[w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,f,f,f,f,f,f,f,f,f,f,f,f,f,f,w],
               [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w]]

chunk00 = Chunk(data = chunk00Data)
chunk00Datamap = {(0,0) : chunk00}

firstLevel = Level(chunks = chunk00Datamap)
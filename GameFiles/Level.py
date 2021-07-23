
from sys import platform
from Platform import Platform
from Currency import *
from Bug import Bug



class Level():

    

    def __init__(self):
        self.sprites_list = []
      

    def process(self, data, images, coins, platforms, obstacles, sprites, end_spawn, TILE_SIZE):
        """Process level data."""
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    image = images[tile]
                    rect = image.get_rect()
                    rect.x = x * TILE_SIZE
                    rect.y = y * TILE_SIZE
                    tile_data = (image, rect)

                    # obstacle checking
                    if tile == 0:
                        # create coin
                        coin = Currency(tile_data)
                        coins.add(coin)
                        sprites.add(coin)
                        self.sprites_list.append(tile_data)

                    elif tile == 1:
                        # create bug
                        bug = Bug(tile_data)
                        obstacles.add(bug)
                        sprites.add(bug)
                        self.sprites_list.append(tile_data)

                    elif tile == 2:
                        # create floor (FIXME: this will likely be a platform now, as their behavior is the same)
                        floor = Platform(tile_data)
                        platforms.add(floor)
                        sprites.add(floor)
                        self.sprites_list.append(tile_data)

                    elif tile == 3:
                        # create platform
                        platform = Platform(tile_data)
                        platforms.add(platform)
                        sprites.add(platform)
                        self.sprites_list.append(tile_data)

                    elif tile == 4:
                        # create end location
                        end = Platform(tile_data)
                        end_spawn.add(end)
                        sprites.add(end)
                        self.sprites_list.append(tile_data)

    def draw(self, screen):
        for tile in self.sprites_list:
            screen.blit(tile[0], tile[1])

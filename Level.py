#AndrewID: nwatson

#The Level class contains the specifics of a level of the game: the map and the heroes.

class Level(object):
    
    def __init__(self, level, map, waves, startingGold, spawnpoint):
        self.level = level
        self.map = map
        self.waves = waves
        self.startingGold = startingGold
        self.waveNumber = 0 #Tracks the current wave of the level.
        self.heroNumber = 0 #Tracks the current hero within each wave.
        self.spawnpoint = spawnpoint #Provides the coordinates of the location in which heroes first appear.
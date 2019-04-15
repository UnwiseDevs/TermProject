#AndrewID: nwatson

#Heroes are enemies that appear in waves and attempt to break past the player's defenses.

#The Hero superclass contains the general attributes of heroes and their default methods.
class Hero(object):
    
    def __init__(self, maxHP, speed, gold, x, y, color):
        self.maxHP = maxHP
        self.HP = maxHP
        self.speed = speed
        self.gold = gold
        self.x = x
        self.y = y
        self.r = 5
        self.color = color
        
    def move(self):
        self.y += 1
        pass
        
    def damage(self, damage):
        pass
        
    def die(self):
        pass
        
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
    
  
#The Villager is the most generic Hero, with standard stats and no special abilities.
class Villager(Hero):
    
    def __init__(self, x, y):
        super().__init__(40, 1, 25, x, y, "goldenrod")
#AndrewID: nwatson

#Towers are placed by the player to defend their gems.

#The Tower superclass contains the attributes of a tower and the default methods for drawing and firing.
class Tower(object):
    
    def __init__(self, damage, fireRate, range, x, y, color):
        self.damage = damage
        self.fireRate = fireRate
        self.range = range
        self.XP = 0 #Not currently implemented.
        self.x = x
        self.y = y
        self.r = 10
        self.color = color
     
    #Draws the tower. Color supplied by the subclass.
    def draw(self, canvas, color):
        canvas.create_rectangle (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
    

#The Den subclass is a midrange tower that fires sporadically.     
class Den(Tower):
    
    #Specifices the default damage, fire rate, range, and color of dens.
    def __init__(self, x, y):
        super().__init__(20, 2, 2, x, y, "chartreuse2")


#The Crypt subclass is a long range tower that generates and fire charges.
class Crypt(Tower):
        
    #Specifices the default damage, fire rate, range, and color of crypts.
    def __init__(self, x, y):
        super().__init__(20, 3, 3, x, y, "SlateBlue1")
        self.charges = 0
        

#The Altar subclass is a short range tower that fires a constant beam.
class Altar(Tower):
    
    #Specifices the default damage, fire rate, range, and color of altars.
    def __init__(self, x, y):
        super().__init__(16, 1, 1.5, x, y, "firebrick2")
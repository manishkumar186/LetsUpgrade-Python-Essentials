import math
class cone:
    def __init__(self,r,h):
        self.radius=r
        self.height=h

    def volume(self):
        v = (1/3*math.pi*(self.radius)**2*self.height)
        print("volume :",v)

    def surface_area(self):
        base = math.pi*self.radius**2
        print("surface area of base: ",base)

        side = math.pi*self.radius*math.sqrt(self.radius**2+self.height**2)
        print(" surface area of side: ",side)

obj = cone(10,20)
obj.volume()
obj.surface_area()

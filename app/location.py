import json
class Location:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.route = None
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setRoute(self, route):
        self.route = route

    def getRoute(self):
        return self.route

    def toString(self):
        return "( " + str(self.x) + ", " + str(self.y) + " )"

    def toDict(self):
        color = "black"
        if self.route == "monday":
            color = "red"
        elif self.route == "tuesday":
            color = "green"
        elif self.route == "wednesday":
            color = "blue"
        elif self.route == "thursday":
            color = "yellow"
        elif self.route == "friday":
            color = "indigo"
        
        size = "small"
        if self.route == "FARM":
            size = "large"

        x = {
            "type" : "Feature",
            "geometry" : {"type" : "Point", "coordinates" : [self.x, self.y]},
            "properties" : {"day" : self.route, "marker-color" : color, "marker-size" : size}
        }
        return x


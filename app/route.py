import math
import sys

class Route:
    def __init__(self, day, farmLoc):
        self.day = day
        self.route = []
        self.locations = []
        self.origin = farmLoc
    
    def createRoute(self):
        self.route.append(self.origin)
        lastLoc =  self.origin
        for loc in self.locations:
            self.findClosest(loc)
            # lastLoc = loc

    def findClosest(self, location):
        min = sys.maxsize
        minLoc = location
        self.locations.remove(location)
        for loc in self.locations:
            if getDistance(loc, location) < min and minLoc != location:
                minLoc = loc
                min = getDistance(loc, location)
        # self.locations.remove(minLoc)
        self.route.append(minLoc)

    def addLocations(self, locations):
        self.locations = locations
    
    def print(self):
        string = self.day + ": " + self.origin.toString()
        for x in self.route:
            string += " -> " + x.toString()
        print(string)

    def test(self):
        string = ""
        for x in self.locations:
            string += x.toString() + " "
        print(string)

    def findTotalDistance(self):
        distance = 0
        for x in range(len(self.route) - 1):
            distance += getDistance(self.route[x + 1], self.route[x])
        return distance

#TODO: Replace with an actual distance estimate using something like the maps API instead of distance formula
def getDistance(loc1, loc2):
    return math.sqrt(math.pow(loc2.getX() - loc1.getX(), 2) + math.pow(loc2.getY() - loc1.getY(), 2))
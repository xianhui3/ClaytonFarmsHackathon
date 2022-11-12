import location
import csv
import math
import sys

class DeliveryZoneCreator:
    def __init__(self, farmLoc, locations = []):
        self.farm = farmLoc
        self.farm.setRoute("FARM")
        self.locations = locations
        self.locations.append(self.farm)
        self.zones = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": []}

    def addLocation(self, location):
        if len(self.zones["monday"]) == 0:
            location.setRoute("monday")
            self.zones["monday"].append(location)
        else:
            min = sys.maxsize
            for loc in self.locations:
                if getDistance(loc, location) < min:
                    if loc.getRoute() != "FARM":
                        min = getDistance(loc, location)
                        location.setRoute(loc.getRoute())
                    else:
                        for x in self.zones:
                            if len(self.zones[x]) == 0:
                                min = getDistance(loc, location)
                                location.setRoute(x)
                                break
                # if getAngle(loc, location) < min:
                #     if loc.getRoute() != "FARM":
                #         min = getAngle(loc, location)
                #         location.setRoute(loc.getRoute())
                #     else:
                #         for x in self.zones:
                #             if len(self.zones[x]) == 0:
                #                 min = getDistance(loc, location)
                #                 location.setRoute(x)
                #                 break
        if location.getRoute() != "FARM":
            self.zones[location.getRoute()].append(location)
        self.locations.append(location)

    def findClosestNonFarm(self, location):
        min = sys.maxsize
        minLoc = None
        for loc in self.locations:
            if loc.getRoute() != "FARM":
                if getDistance(loc, location) < min:
                    min = getDistance(loc, location)
                    minLoc = loc
        return minLoc

    #TODO: This can definitely be done better
    def printRoutes(self):
        monday = "MONDAY:"
        tuesday = "TUESDAY: "
        wednesday = "WEDNESDAY: "
        thursday = "THURSDAY: "
        friday = "FRIDAY: "
        for loc in self.zones["monday"]:
            monday += " (" + str(loc.getX()) + ", " + str(loc.getY()) +")" 
        for loc in self.zones["tuesday"]:
            tuesday += " (" + str(loc.getX()) + ", " + str(loc.getY()) +")" 
        for loc in self.zones["wednesday"]:
            wednesday += " (" + str(loc.getX()) + ", " + str(loc.getY()) +")" 
        for loc in self.zones["thursday"]:
            thursday += " (" + str(loc.getX()) + ", " + str(loc.getY()) +")" 
        for loc in self.zones["friday"]:
            friday += " (" + str(loc.getX()) + ", " + str(loc.getY()) +")" 
        print(monday)
        print(tuesday)
        print(wednesday)
        print(thursday)
        print(friday)

    def output(self):
        with open("zones.csv", "w", newline = "") as csvfile:
            fieldnames = ["monday", "tuesday", "wednesday", "thursday", "friday"]
            writer = csv.writer(csvfile)
            for x in fieldnames:
                lst = [x]
                for y in self.zones[x]:
                    lst.append(y.toString())
                writer.writerow(lst)
            csvfile.close()

    def getLocations(self):
        return self.locations

    def getDayLocations(self, day):
        return self.zones[day]

#TODO: Replace with an actual distance estimate using something like the maps API instead of distance formula
def getDistance(loc1, loc2):
    return math.sqrt(math.pow(loc2.getX() - loc1.getX(), 2) + math.pow(loc2.getY() - loc1.getY(), 2))

def getAngle(loc1, loc2):
    return math.atan2(loc2.getY() - loc1.getY(), loc2.getX() - loc1.getX())
import location
import deliveryzone
import random
import route
import json

def readFile(fileName, zone):
    with open(fileName, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            if line != "":
                arr = line.split("	")
                loc = location.Location(float(arr[0]), float(arr[1]))
                zone.addLocation(loc)
        f.close()

def toGeoJSON(zone):
    lst = []
    for loc in zone.getLocations():
        lst.append(loc.toDict())
    temp = {
        "type" : "FeatureCollection",
        "features" : lst
        }
    with open("zones.json", "w", encoding="utf-8") as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)

radius = 30 #miles

numLocations = 1000

farm = location.Location(-93.265015, 44.977753)
# farm = location.Location(0, 0)


zones = deliveryzone.DeliveryZoneCreator(farm)

# for x in range(numLocations):
#     loc = location.Location(random.randrange(-1 * radius, radius), random.randrange(-1 * radius, radius))
#     zones.addLocation(loc)
readFile("clayton-farms-hackathon/app/locations.txt", zones)

# loc1 = location.Location(42.022888, -93.675209)
# loc2 = location.Location(42.014747, -93.681650)

# zones.addLocation(loc1)
# zones.addLocation(loc2)

# loc3 = location.Location(41.590914, -93.623674)
# loc4 = location.Location(41.598446, -93.717121)
# zones.addLocation(loc3)
# zones.addLocation(loc4)

# loc5 = location.Location(41.981899, -91.661379)
# loc6 = location.Location(41.982761, -91.722464) 

# zones.addLocation(loc5)
# zones.addLocation(loc6)

zones.printRoutes()
zones.output()
toGeoJSON(zones)

# r = route.Route("MONDAY", farm)
# r.addLocations(zones.getLocations())
# r.createRoute()
# r.print()
# print(r.findTotalDistance())
# r.test()


# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


newLatLon = LatLon(5, 10)
print(newLatLon.lat)
print(newLatLon.lon)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f'Latitude: {self.lat}, Longitude: {self.lon}, Location Name: {self.name}'


newWaypoint = Waypoint(15, 20, 'Ronny')
print(newWaypoint.lat)
print(newWaypoint.lon)
print(newWaypoint.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, lat, lon, name, size, difficulty):
        super().__init__(lat, lon, name)
        self.size = size
        self.difficulty = difficulty

    def __str__(self):
        return f'Latitude: {self.lat}, Longitude: {self.lon}, Location Name: {self.name}, Size: {self.size}, Difficulty: {self.difficulty}'


newGeocache = Geocache(25, 30, 'Ronny', 35, 'Easy')
print(newGeocache.lat)
print(newGeocache.lon)
print(newGeocache.name)
print(newGeocache.size)
print(newGeocache.difficulty)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint.name, waypoint.lat, waypoint.lon)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# I went ahead and added the method to the Waypoint class above
print(waypoint)

# # Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# # YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 2, 1.5)

# # Print it--also make this print more nicely
print(geocache)

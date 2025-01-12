from collections import namedtuple
from operator import attrgetter

metro_data = [
    ("New York City", 8405837, 40.7128, -74.0060),
    ("Los Angeles", 3990456, 34.0522, -118.2437),
    ("Chicago", 2695598, 41.8781, -87.6298),
    ("Houston", 2320268, 29.7633, -95.3632),
    ("Phoenix", 1732526, 33.4484, -112.0739),
    ("Philadelphia", 1580863, 39.9526, -75.1652),
    ("San Antonio", 1510767, 29.4241, -98.4936),
    ("San Diego", 1423814, 32.7157, -117.1611),
    ("Dallas", 1341075, 32.7763, -96.7969),
    ("San Jose", 1035279, 37.3382, -121.8863)
]

Metro = namedtuple('Metro', 'name pop loc')
Loc = namedtuple('Loc', 'lat lon')
metros = [
    Metro(name, pop, Loc(lat, lon)) 
    for name, pop, lat, lon
    in metro_data
]

summary = attrgetter('name', 'loc.lon')
for city in sorted(metros, key=attrgetter('loc.lon')):
    print(summary(city))

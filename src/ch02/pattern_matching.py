cities = [
    ["New York", "USA", 8.42, (40.7128, -74.0060)],
    ["London", "UK", 8.93, (51.5074, -0.1278)],
    ["Paris", "FRA", 2.16, (48.8566, 2.3522)],
    ["Tokyo", "JPN", 13.9, (35.6895, 139.7670)],
    ["Beijing", "CHN", 21.5, (39.9042, 116.3974)],
    ["Mumbai", "IND", 12.4, (19.0760, 72.8777)],
    ["Shanghai", "CHN", 24.1, (31.2304, 121.4737)],
    ["Sao Paulo", "BRA", 21.3, (-23.5505, -46.6358)],
    ["Mexico City", "MEX", 21.8, (19.4326, -99.1332)],
    ["Cairo", "EGY", 20.4, (30.05, 31.25)],
]

print("A list of cities from the western hemisphere:")
for city in cities:
    match city:
        case [
                str(name),
                str(country),
                float(population),
                (float(lat), float(longitude)),
                ] if longitude > 0.0:
            print(f"{name:>10}, {country} {population:4.1f} M")

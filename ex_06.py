def my_create_continent(continent, world_map):
    world_map[continent]={}

def my_create_country(country, continent, world_map):
    world_map[continent][country]={}

def my_create_city(city, postal_code, country, continent, world_map):
    world_map[continent][country][city]=postal_code

def my_get_countries_of_continent(continent, world_map):
    for key in world_map[continent]:
        print(key)

def my_get_cities_of_country(country, continent, world_map):
    for key in world_map[continent][country]:
        print(key)

def my_get_city_postal_code(city, country, continent, world_map):
    if city in world_map[continent][country]:
        print(world_map[continent][country][city])
    else :
        print("country not found")
        return None



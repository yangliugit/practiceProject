def normalize(name):
    return name.capitalize()

r = map(normalize, ['ada', 'aDA', 'stRing'])

print r

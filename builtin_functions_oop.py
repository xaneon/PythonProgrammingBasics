class MeineKlasse(object):
    def __init__(self):
        self.attribut = 42

instanz = MeineKlasse()
print(instanz.attribut,
      getattr(instanz, "attribut"), "\n")

try:
    getattr(instanz, "nicht")
except AttributeError as err:
    print(err, "\n")

linie = "\n" + 40 * "-"
print("getattr:", getattr(instanz, "nicht", 9))
print(instanz.__dict__, linie)

print("vorher:", instanz.__dict__)
print("setattr", setattr(instanz, "doch", 43))
print("nacher:", instanz.__dict__, linie)

print("delattr:", delattr(instanz, "doch"))
print("nacher:", instanz.__dict__, linie)

class Unterklasse(MeineKlasse):
    pass

print(isinstance(instanz, MeineKlasse))
print(isinstance(instanz, Unterklasse))
print(issubclass(Unterklasse, MeineKlasse))
print(issubclass(Unterklasse, object))

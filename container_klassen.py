from collections.abc import Container

isCont = lambda x: isinstance(x, Container)
conts = [str(), list(), dict(), tuple()]
noconts = [int(), float()]

assert(any([isCont(x) for x in conts]))
# assert(any([isCont(x) for x in noconts]))

class IndizierbaresDictionary:
    def __init__(self, dictionary):
        self.elems = list(dictionary.items())
        self.schl = list(dictionary.keys())
        self.werte = list(dictionary.values())
    def __repr__(self):
        return str(dict(self.elems))
    def __getitem__(self, idx):
        return "{}:{}".format(self.schl[idx],
                              self.werte[idx])
    def __setitem__(self, idx, value):
        self.elems.insert(idx, value)
    def __contains__(self, item):
        schl = [x[0] for x in self.elems]
        return item in schl

d1 = {"a": 1, "b": 2, "c": 3}
instanz = IndizierbaresDictionary(d1)
print(instanz, "\n", instanz[2])
instanz[3] = ("d", 42)
print(instanz)
print("a" in instanz, "e" in instanz)

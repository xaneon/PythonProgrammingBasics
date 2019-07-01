from pprint import pprint
from copy import deepcopy
filter_chars = ">", "<", '"', "'"
clean = lambda x: "".join([a for a in str(type(x))
                           if a not in filter_chars]
                         ).replace("class ", "")
speicherID = lambda x: hex(id(x))
getID = lambda x: (x, clean(x), speicherID(x))
wertID = lambda x: (x, speicherID(x))
getIDs = lambda x: [wertID(elem) for elem in x]

int_1 = 42; float_1 = 42.42; str_1 = "hallo"
print(getID(int_1), getID(float_1), getID(str_1))

a = [1, 2, 3]; b = [2, 3, 1]; c = a
ai = getIDs(a); bi = getIDs(b); ci = getIDs(c)
pprint({"a": ai, "b": bi, "c": ci}); print()

a[2] = 42
ai = getIDs(a); bi = getIDs(b); ci = getIDs(c)
pprint({"a": ai, "b": bi, "c": ci}); print()

a = [1, 2, 3]; b = [2, 3, 1]; c = deepcopy(a)
a[2] = 42
ai = getIDs(a); bi = getIDs(b); ci = getIDs(c)
pprint({"a": ai, "b": bi, "c": ci})

liste1 = [1, 2, 3]; tuple1 = (5, 4, liste1)
pprint({"liste1": liste1, "tuple1": tuple1})
liste1[1] = "eintrag"
pprint({"liste1": liste1, "tuple1": tuple1})

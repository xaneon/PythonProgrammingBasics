import json
l1 = ["a", "b", "c"]
d1 = {42: "..ist die Antwort"}
d2 = {"Fragen?": l1}
print(json.dumps(l1))
goes_out = json.dumps(d1)
print(goes_out)
goes_in = json.loads(goes_out)
print(goes_in)
original = {int(key): val for (key, val) in goes_in.items()}
print(original)

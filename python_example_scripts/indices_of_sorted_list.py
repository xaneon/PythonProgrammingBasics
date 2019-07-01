from random import randint
import numpy as np

l1 = [randint(0, 9) for _ in range(0, 100)]
l2 = [randint(0, 9) for _ in range(0, 100)]
l2 = [randint(0, 9) for _ in range(0, 100)]

# print(sorted(l1)[:])

idcs1 = sorted(range(len(l1)), key=lambda idx: l1[idx])
l1_sorted1 = sorted(l1)
l1_sorted2 = [l1[idx] for idx in idcs1]
# l1[idcs] not allowed
print(l1_sorted1 == l1_sorted2)

l1_np = np.array(l1)
l1_sorted3 = np.sort(l1_np)
idcs1_np = np.argsort(l1_np)
print(l1_sorted3 == l1_np[idcs1_np])



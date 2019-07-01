from glob import glob
import re
import os

for file in glob("*.*"):
    if "kap" in file.lower():
        print(file)
        pref, endung = re.match("([Kk]ap[0-9_]+)(.*)", file).groups()
        os.system(f"git mv {file} {endung}")
    else:
        # os.system(f"git mv {file} {file.lower()}")
        os.system(f"mv {file} {file.lower()}")

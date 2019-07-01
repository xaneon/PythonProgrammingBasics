import os
from lxml import etree

tree = etree.parse("scify_movies.xml")
movies = tree.findall('Movie') # vs. find und findall nur auf der akt. Ebene
movie = tree.find("Movie")
print(movies)
directors = [el for el in tree.iter('Director')] # alle Elemente in beliebiger Tiefe
# print(movies)
for director in directors:
    print(type(director))
    print(director.text)

# Was ist der übergeordnete Knoten (Parent)?
for i in tree.iter('Director'):
    print(i.getparent().tag)
    print(i.text)
    pass

import pprint
import xml.etree.ElementTree as ET
import xml2json
import json

tree = ET.parse('Kap1_9_8_XML_Baum.xml')
root = tree.getroot()
out = xml2json.etree_to_dict(root)
with open('Kap1_9_8_JSON_Baum.json', 'w') as fp:
    fp.write(json.dumps(out))
pprint.pprint(out)

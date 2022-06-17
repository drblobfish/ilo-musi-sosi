import xml.etree.ElementTree as ET
import copy

tree = ET.parse('sosi-board-nimi.svg')

root = tree.getroot()

ns = {
	'svg':'http://www.w3.org/2000/svg',
	'ink':'http://www.inkscape.org/namespaces/inkscape'
}

label = '{http://www.inkscape.org/namespaces/inkscape}label'

for group in root.iterfind("svg:g",ns):
	if group.attrib.get(label,"")=="nimi":
		nimiLayer = group

template = nimiLayer.find("svg:g",ns)

new = copy.deepcopy(template)

new.set("id","new_id")

for child in new:
	child.set("x", str( float(child.get("x")) + 100 ))

nimiLayer.append(new)

print(ET.dump(nimiLayer))

tree.write("sosi-board-nimi-2.svg")
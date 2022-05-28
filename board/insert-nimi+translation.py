import xml.etree.ElementTree as ET
tree = ET.parse('sosi-board.svg')

root = tree.getroot()

ns = {
	'svg':'http://www.w3.org/2000/svg',
	'ink':'http://www.inkscape.org/namespaces/inkscape'
}

label = '{http://www.inkscape.org/namespaces/inkscape}label'

for group in root.iterfind("svg:g",ns):
	if group.attrib.get(label,"")=="nimi":
		nimiLayer = group

print(nimiLayer.attrib)

'''
def nimiGroup(name:str,trans:str,path:str):
	group = ET.Element('g',{'id':name + "Group"})
	image = ET.SubElement(
		group,
		'image',
		{
			"preserveAspectRatio":"none",
	        "inkscape:svg-dpi":"98",
	        "width":str(27.502115),
	        "height":str(31.312115),
	        "xlink:href":"../sitelen_pona_svg/"+path,
	        "id":"image914",
	        "x":str(91.24894),
	        "y":str(132.49698)
		}
		)
	text = ET.SubElement(
		group,
		'text',
		{
			"xml:space":"preserve",
	        "transform":"matrix(0.26458333,0,0,0.26458333,-3.8063069,-8.0142434)",
	        "id":"text7291",
	        #"style":"font-size:53.3333px;line-height:0.3;font-family:sans-serif;white-space:pre;shape-inside:url(#rect7293)",
	        "x":"19.491266",
	        "y":"0"
		})
	nimi = ET.SubElement(
		text,
		"tspan",
		{
			"style":"font-family:Karumbi;-inkscape-font-specification:Karumbi;text-align:center;text-anchor:middle",
			"id":"tspan49443"
		}
		)
	nimi.text = name
	translation = ET.SubElement(
		text,
		"tspan",
		{
			"style":"font-family:Karumbi;-inkscape-font-specification:Karumbi;text-align:center;text-anchor:middle",
			"id":"tspan49443"
		}
		)
	translation.text = trans
	return group
'''
#ponaGrp = nimiGroup('pona','good','Pona.svg')

#nimiLayer.append(ponaGrp)

#ET.indent(root)

#print(ET.dump(root))
import pandas as pd

spacing = 150
width = 103.945
height = 118.345

def nimiGroup(id,file_name,x,y,nimi,trans) :
    xmlGroup = '''
    <g
        id="g-{id}"
        transform="translate({x},{y})">
        <image
            preserveAspectRatio="none"
            inkscape:svg-dpi="96"
            width="{width}"
            height="{height}"
            xlink:href="../sitelen_pona_svg/{file_name}.svg"
            id="image{id}"
            x="-51.972"
            y="-59.1725" />
        <text
            xml:space="preserve"
            id="text{id}"
            style="font-size:16px;line-height:1.25;font-family:sans-serif;white-space:pre;"
            x="0"
            y="0"><tspan
                    x="0"
                    y="60"
                    id="tspan{id}1"><tspan
                    style="text-align:center;text-anchor:middle"
                    id="tspan{id}2">{nimi}</tspan></tspan><tspan
                x="0"
                y="75"
                id="tspan{id}3"><tspan
                    style="text-align:center;text-anchor:middle"
                    id="tspan{id}4">{trans}</tspan></tspan></text>
    </g>
    '''.format(id=id,file_name=file_name,x=x,y=y,width=width,height=height,nimi=nimi,trans=trans)
    return xmlGroup

def main():

    tokDict = pd.read_csv("../multilingual-toki-pona-dictionary/multilanguage-toki-pona-dictionary.csv")

    with open("sosi-board-nimi-test.svg") as emptyFile:
        emptyStr = emptyFile.read()

    nimisGroups = []

    nimisString = """
    """

    tokDict = pd.read_csv("../multilingual-toki-pona-dictionary/multilanguage-toki-pona-dictionary.csv",index_col= 0)
    #print(tokDict)
    for i,row in tokDict[["tok","en"]].iterrows():
        #print(row)
        nimisGroups.append(nimiGroup(1,row.tok.capitalize(),(i%10)*spacing,(i//10)*spacing,row.tok,row.en))

    nimisString = nimisString.join(nimisGroups)

    filledStr = emptyStr.replace("<!-- insert nimis -->",nimisString)
    with open("sosi-board-nimi-test-2.svg","w") as filledFile:
        filledFile.write(filledStr)

        


if __name__=="__main__" :
    main()
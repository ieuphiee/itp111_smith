# hw11_1.py
# Generating a map of Smith from compiled CSV file
# Jiamin Li, Heather Chau

from graphics import *

WIDTH = 750
HEIGHT = 730


def keyBox( win ):
    
    # This function just creates the key for the map
    titleBox = Rectangle( Point( 260, 70 ), Point( 446 , 90 ) )
    titleBox.setFill( color_rgb(194,209,89) )
    label = Text(Point(350, 81), "MAP KEY" )
    label.setFace('courier')
    label.setTextColor( 'white' )
    titleBox.setOutline( color_rgb(109,43,92) )
    titleBox.setWidth( 0 )
    label.setSize(15)

    keyBox = Rectangle( Point( 260, 90 ), Point( 445 , 210 ) )
    keyBox.setFill( color_rgb(255, 255, 255) )
    keyBox.setOutline( color_rgb(203,232,107)  )
    keyBox.setWidth( 1 )

    pave = Rectangle( Point( 270, 100 ), Point( 320 , 115 ) )
    pave.setFill( 'grey' )
    pave.setOutline( 'black'  )
    pave.setWidth( 0 )
    pavename = Text(Point(380, 105), "parking/streets" )
    pavename.setFace('helvetica')
    pavename.setTextColor( 'black' )
    pavename.setSize(12)
    pavename.setStyle( 'italic' )

    b17 = Rectangle( Point( 270, 120 ), Point( 320 , 135 ) )
    b17.setFill( color_rgb(98, 145, 204) )
    b17.setOutline( 'black'  )
    b17.setWidth( 0 )
    b17name = Text(Point(380, 128), "built: 1700s-1800s")
    b17name.setFace('helvetica')
    b17name.setTextColor( 'black' )
    b17name.setSize(10)
    b17name.setStyle( 'italic' )

    b18 = Rectangle( Point( 270, 140 ), Point( 320 , 155 ) )
    b18.setFill( color_rgb(255,105,96) )
    b18.setOutline( 'black'  )
    b18.setWidth( 0 )
    b18name = Text(Point(380, 148), "built: 1800s-1900s")
    b18name.setFace('helvetica')
    b18name.setTextColor( 'black' )
    b18name.setSize(10)
    b18name.setStyle( 'italic' )

    b19 = Rectangle( Point( 270, 160 ), Point( 320 , 175 ) )
    b19.setFill( color_rgb(255,207,96) )
    b19.setOutline( 'black'  )
    b19.setWidth( 0 )
    b19name = Text(Point(380, 168), "built: 1900s-2000s")
    b19name.setFace('helvetica')
    b19name.setTextColor( 'black' )
    b19name.setSize(10)
    b19name.setStyle( 'italic' )

    b20 = Rectangle( Point( 270, 180 ), Point( 320 , 195 ) )
    b20.setFill( color_rgb(244,253,179) )
    b20.setOutline( 'black'  )
    b20.setWidth( 0 )
    b20name = Text(Point(370, 188), "built: 2000s >>" )
    b20name.setFace('helvetica')
    b20name.setTextColor( 'black' )
    b20name.setSize(10)
    b20name.setStyle( 'italic' )

    titleBox.draw( win )
    label.draw( win )
    keyBox.draw( win )
    pave.draw( win )
    pavename.draw( win )
    b17.draw( win )
    b17name.draw( win )
    b18.draw( win )
    b18name.draw( win )
    b19.draw( win )
    b19name.draw( win )
    b20.draw( win )
    b20name.draw( win )

class Pave:
    def __init__( self, fL ):
        self.polygon = Polygon( fL )

    def setFill( self, win ):
        self.polygon.setFill( color_rgb(224,224,224)  )

    def draw( self, win ):
        self.polygon.draw( win )

    def setOutline( self, win ):
        self.polygon.setOutline( 'white' )

    def setWidth( self, win ):
        self.polygon.setWidth( 2 )

class Building: # includes houses
    def __init__( self, fL ):
        self.polygon = Polygon( fL )

    def setFill( self, win, co ):
        self.polygon.setFill( co )

    def draw( self, win ):
        self.polygon.draw( win )

    def setOutline( self, win ):
        self.polygon.setOutline( 'white' )

    def setWidth( self, win ):
        self.polygon.setWidth( 2 )

def findYear( nameElement ):
    file = open( "constructionDates.txt", "r" )
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip().lower()
        if nameElement in line:
            year = int(line[0:4])
            return year
        
    return None # in case we don't find it

def sortText( lines ):
    masterList = {}
    # exclude these two-word house names
    keywords = [ "chase duckett", "cutter ziskind", "king scales", "morrow wilson",
                 "comstock wilder", "northrop gilette", "cushing emerson" ]
    
    for line in lines:
            line = line.strip()
            fields = line.split(",")
            if len( line ) <= 1 or len( fields ) <= 1:
                continue

            # Defining element, aka object
            # And name of the element, e.g. "house" or "building"
            element = fields[0].lower().strip()
            nameElement = fields[1].lower().strip()
            
            # Only mapping building, house, and parking lots
            if element not in [ "building", "house", "road", "parking"]:
                continue
            
            # Element names should only be one word length, e.g. "house"
            # to remove lines that have element and name of element
            # positioned incorrectly
            if len( element.split() ) >= 2: 
                continue
    
            if len( nameElement ) <= 1: # remove empty nameElement fields
                continue

            # Remove lines containing houses with two words, e.g. "cutter ziskind"
            # And also remove two-word houses formatted with hyphen and slash
            if nameElement in keywords or nameElement.find("/") != -1 or nameElement.find("-") != -1:
                continue

            # Cleaning up spelling errors and extraneous words in line
            replaceList = [ "street", "st.", "rd.", "road", "lane", "ln.",
                            "admissions", "botanic garden", "botanic garden",
                            "botanic gaens", "botanic gaen", "jmg", "lily",
                            "house", "hall", "alamnae", "alumne", "theatre",
                            "14", "library", "gym", "(quadrant2)",
                            "lymann conservatory", "northrop gillet", "piercce",
                            "west street", "college lane", "greent st", "green street",
                            "paradise road", "prospet", "prospect street", "bedford ter" ]
            for word in replaceList:
                nameElement = nameElement.replace( word, "" ).strip()
               
            if len( nameElement ) <= 1 or len( nameElement.split(' ') ) >= 3:
                continue

            # Defining quadrants and remove lines that do not label quadrant number
            quadrant = fields[4].strip()
            if not quadrant in ['1', '2', '3', '4' ]:
                continue

            # Defining coordinates
            coordinates = fields[5:]
            coordinates = ''.join( coordinates ).strip().lower().split()
            coordinates = [int(i) for i in coordinates] # Strings --> Integers
            if coordinates[0] in ["strohbeck"] or len(coordinates) <= 1:
                continue

            # Finding and correlating year with object
            year = findYear( nameElement )

            # If name of object is not in the dictionary, add into dictionary
            if not nameElement in masterList.keys():
                masterList[ nameElement ] = nameElement, element, year, coordinates
        
    return nameElement, masterList



def main():
    global WIDTH, HEIGHT

    win = GraphWin( "Smith Map", WIDTH, HEIGHT )
    win.setBackground( color_rgb( 255,247,243 ) )

    file = open( "SmithMapCSV.txt", "r" )
    lines = file.readlines()
    file.close()

    nameElement, masterList = sortText( lines )

    #for nameElement in masterList.keys():
        #print( masterList[ nameElement ] )
        
    finalList = [] # empty list for coordinates
    for nameElement in masterList.keys():
        coordList = masterList[ nameElement ][3]
        
        if masterList[ nameElement ][1] == "parking" or masterList[ nameElement ][1] == "road":
            try:
                for i in range( 0, len(coordList), 2 ):
                    x = coordList[i]
                    y = coordList[i+1]
                    point = Point( x, y )
                    finalList.append( point )
                pavement = Pave( finalList )
                pavement.setFill( win )
                pavement.setOutline( win )
                pavement.setWidth( win )
                pavement.draw( win )
                finalList.clear()
            except IndexError:
                continue
            
        if masterList[ nameElement ][1] == "house" or masterList[ nameElement ][1] == "building":
            if masterList[ nameElement ][2] == None: # houses/buildings with no year recorded
                for i in range( 0, len(coordList), 2 ):
                    x = coordList[i]
                    y = coordList[i+1]
                    point = Point( x, y )
                    finalList.append( point )
                co = color_rgb(255, 155, 110)
                building = Building( finalList )
                building.setFill( win, co )
                building.setOutline( win )
                building.setWidth( win )
                building.draw( win )
                finalList.clear()
            elif 1700 <= masterList[ nameElement ][2] <= 1800:
                for i in range( 0, len(coordList), 2 ):
                    x = coordList[i]
                    y = coordList[i+1]
                    point = Point( x, y )
                    finalList.append( point )
                co = color_rgb(98, 145, 204)
                building17_18 = Building( finalList )
                building17_18.setFill( win, co )
                building17_18.setOutline( win )
                building17_18.setWidth( win )
                building17_18.draw( win )
                finalList.clear()
            elif 1800 <= masterList[ nameElement ][2] <= 1900:
                for i in range( 0, len(coordList), 2 ):
                    x = coordList[i]
                    y = coordList[i+1]
                    point = Point( x, y )
                    finalList.append( point )
                co = color_rgb(255,105,96)
                building18_19 = Building( finalList )
                building18_19.setFill( win, co )
                building18_19.setOutline( win )
                building18_19.setWidth( win )
                building18_19.draw( win )
                finalList.clear()
            elif 1900 <= masterList[ nameElement ][2] <= 2000:
                for i in range( 0, len(coordList), 2 ):
                    x = coordList[i]
                    y = coordList[i+1]
                    point = Point( x, y )
                    finalList.append( point )
                co = color_rgb(255,207,96)
                building19_20 = Building( finalList )
                building19_20.setFill( win, co )
                building19_20.setOutline( win )
                building19_20.setWidth( win )
                building19_20.draw( win )
                finalList.clear()
            else:
                for i in range( 0, len(coordList), 2 ):
                    x = coordList[i]
                    y = coordList[i+1]
                    point = Point( x, y )
                    finalList.append( point )
                co = color_rgb(244,253,179)
                building20_ = Building( finalList )
                building20_.setFill( win, co )
                building20_.setOutline( win )
                building20_.setWidth( win )
                building20_.draw( win )
                finalList.clear()         
    keyBox( win )           
    win.getMouse()
    win.close()
    
main()






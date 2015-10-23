'''
    Created to identify the magnitude of the brightest star within a specific field of view
    Baselined: September 2, 2015
    Modified: September 3, September 5, September 6, September 7 (2015)
    @author: Swagata Mukherjee (szm0081)
'''


from math import pi
import os
import re


class StarCatalog(object):
    '''StarCatalog contains an inventory of the stars that are visible from earth. Each star has a catalog identifier, magnitude of brightness, right ascension angle and angle of declination'''

    
    def __init__(self):
        '''Creates an instance of StarCatalog using 4 different lists'''
        self.catalogIdentifier = []
        self.magnitude = []
        self.rightAscension = []
        self.declination = []

        self.count = 0
        
        
    def loadCatalog(self, starFile=None):
        '''Loads the star catalog from a text file containing star data'''
        
        # Check if starFile is given
        if (starFile is None):
            raise ValueError ("loadCatalog: No input file given.")
        
        # Check if the contents of starFile is string
        if (type(starFile) is not str):
            raise ValueError ("loadCatalog: The file violates the parameter specifications - Please only use string parameters  in the file")
        
        # Open the input file to start reading
        if (os.path.isfile(starFile)):
            loadFile = open(starFile, 'r') 
        else:
            raise ValueError ("loadCatalog: No file exists by the specified filename.")
        
        # Create a new set
        newSet = set()
        # Read starFile data using regular expressions (Take each element separated by white spaces as an individual string element and store in newFile)
        for item in loadFile:  
            newFile = re.split('\s+', item)
            # If newFile element count is greater than 4, remove all the elements after 4th count
            if (len(newFile) > 4):
                newFile.pop(4)
            
            # Load data starFile to StarCatalog
            try:
                self.catalogIdentifier.append(int(newFile[0]))
                newSet.add(int(newFile[0]))
                
                self.magnitude.append (float(newFile[1]))
                                
                self.rightAscension.append(float(newFile[2]))
                
                self.declination.append(float(newFile[3]))
                                
                self.count = self.count + 1    
            
            except ValueError:
                print "loadCatalog: File loading failed."
                raise 
        
        # Detect duplicate stars    
        if len(newSet) != len(self.catalogIdentifier): 
            raise ValueError("loadCatalog: An attempt to add a duplicate star.")
      
        return self.count
    
    
    def emptyCatalog(self):
        '''Empty the catalog'''
        
        # Remove data from all lists
        self.catalogIdentifier = []
        self.magnitude = []
        self.rightAscension = []
        self.declination = []
        
        deletedStarsCount = self.count  
        self.count = 0  
        
        return deletedStarsCount
        
            
    def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        '''To get the count of stars between given magnitudes of brightness'''
        # If StarCatalog is empty
        if (self.catalogIdentifier == None):
            raise ValueError ("getStarCount: No stars in StarCatalag.")
        
        # If no magnitudes are given, return count of all stars in StarCatalog
        if (lowerMagnitude == None and upperMagnitude == None):
            return self.count
        
        # Check if input magnitudes are floats
        try:
            (isinstance(lowerMagnitude, (float, int)) == True) and (isinstance(upperMagnitude, (float, int)) == True)
        except ValueError:
            print "getStarCount: Attempt to get a count of stars using invalid magnitude"
          
        # Get the count of stars between Lower Magnitude and Upper Magnitude
        count = 0
        for magnitude in self.magnitude:
            if(lowerMagnitude == None and upperMagnitude >= 0):
                if magnitude <= upperMagnitude:
                    count = count + 1
                    
            elif(lowerMagnitude >= 0 and upperMagnitude == None):
                if magnitude >= lowerMagnitude:
                    count = count + 1
                    
            else:
                if(lowerMagnitude > upperMagnitude):
                    raise ValueError ("getStarCount: Lower Magnitude greater than Upper Magnitude.")
                else:
                    if (magnitude >= lowerMagnitude and magnitude <= upperMagnitude):
                        count = count + 1
             
        return count
        
            
    def getMagnitude(self, rightAscensionCenterPoint=None, declinationCenterPoint=None, fieldOfView=None):
        '''To get the magnitude of the brightest star within a square area of a given field of view'''
        
        # Create a new list
        starList = []
        
        # If StarCatalog is empty
        if (self.catalogIdentifier == None):
            raise ValueError ("getMagnitude: No stars in StarCatalag.")
        
        # Check if the input is valid
        try:
            (isinstance(rightAscensionCenterPoint, (float, int)) == True) and (isinstance(declinationCenterPoint, (float, int)) == True) and (isinstance (fieldOfView, (float, int)) == True)
        except ValueError: 
            print "getMagnitude: Please enter float or integer value."
        
        # Right Ascension value should be between 0 and 2pi
        if (rightAscensionCenterPoint < 0 or rightAscensionCenterPoint > 2 * pi):
            raise ValueError ("getMagnitude: Right Ascension Center Point - value invalid.")
        
        # Declination Angle value should be between -pi/2 and +pi/2
        if (declinationCenterPoint < -pi / 2 or declinationCenterPoint > pi / 2):
            raise ValueError ("getMagnitude: Declination Center Point - value invalid.")
        
        # Field of view value should be between 0 and 2pi
        if (fieldOfView < 0 or fieldOfView > 2 * pi):
            raise ValueError ("getMagnitude: Field Of View - value invalid.")
        
        # Loop through the length of StarCatalog 
        for k in range(0, self.count):
            ra = float(self.rightAscension[k])
            dec = float(self.declination[k])
            fov = float(fieldOfView)
        
            # Get the range of applicable Right Ascension and Declination from the given data
            if (((ra >= rightAscensionCenterPoint - fov / 2) and (ra <= rightAscensionCenterPoint + fov / 2)) and ((dec >= declinationCenterPoint - fov / 2) and (dec <= declinationCenterPoint + fov / 2))):
                # Get range of magnitudes for the applicable Right Ascension and Declination
                starList.append(self.magnitude[k])
        
        # Sort the list of magnitudes obtained in the given Field of View
        starList.sort()
        
        # Return the magnitude of the brightest star
        if (len(starList) == 0):
            return None
        else:
            return starList[0]
        
        

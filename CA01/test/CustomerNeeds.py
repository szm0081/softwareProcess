import CA01.prod.StarCatalog as StarCatalog

stars = StarCatalog.StarCatalog()
           
starCount = stars.loadCatalog(starFile="sample.txt")            


try:        
    stars.loadCatalog(starFile="aValidStarFile.txt")        
except ValueError as e:        
    diagnosticString1 = e.args[0]        
print diagnosticString1


starsBetween2And5 = stars.getStarCount(2,5)        
print "Stars between 2 and 5: {0}".format(starsBetween2And5)


starsLE5 = stars.getStarCount(upperMagnitude=5)        
print "Stars with magnitude <= 5: {0}".format(starsLE5)


starsGE3 = stars.getStarCount(lowerMagnitude=3)            
print "Stars with magnitude >= 3: {0}".format(starsGE3)


allStars = stars.getStarCount()            
print "Count of all stars: {0}\n".format(allStars)


try:            
    stars.getStarCount('a', 5)            
except ValueError as e:            
    diagnosticString2 = e.args[0]            
print diagnosticString2


brightestStar = stars.getMagnitude(4.71239554, 0.9452005, 0.17453)            
print "magnitude of the brightest star: {0}".format(brightestStar)   


try:            
    stars.getMagnitude(597, 0.9452005, 0.017453)            
except ValueError as e:            
    diagnosticString2 = e.args[0]            
print diagnosticString2   


starsDeleted = stars.emptyCatalog()            
print "Count of stars deleted: {0}".format(starsDeleted)         


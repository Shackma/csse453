'''
Created on Mar 15, 2016

@author: schackma
'''

class city(object):
    '''
    classdocs
    '''
    


    def __init__(self, name):
        '''
        Constructor
        '''
        
        self.name = name
        self.neighbors = []
    
        
    def addNeighbor(self,city,path):
        self.neighbors.append((city,path))
        return
                          



class path(object):
    
    
    def __init__(self,dist, pher,rho):
        
        self.dist =dist
        self.pher = pher
        self.decayRate = rho
        
        
    def decay(self):
        self.pher = self.pher*(1-self.decayRate)
            

        

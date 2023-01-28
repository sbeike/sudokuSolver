class CSPSolver(object):
    
    def __init__(self, dim, gameString):
        self.dim = dim
        self.expandedNodes = 0
        self.board = []
        
        gameLines = gameString.split("\n")
        
        for i in range(self.dim):
            self.board.append([int(n) for n in str(gameLines[i])])
            
    def __str__(self):
         
        string = ""
         
        for row in self.board:
            for x in row:
                string += str(x) + " "
            string += "\n"
        
        string += "There was {} expanded nodes".format(str(self.expandedNodes))
        return string
    
    
    #Choosing the location with the minimal remainig values
    def nextLocation(self):
        return (-1,-1)
    
    #forward checking the variables to be assigned. return True if non empty dimensions, else return False
    def forwardCheck(self):
        return False
    
    #Checking if any of the values in the dimension is applicable
    def remaingDomain(self):
        for x in range(self.dim):
            for y in range(self.dim):
                
                
    
    def useCSPToSolve(self):
        i = 1
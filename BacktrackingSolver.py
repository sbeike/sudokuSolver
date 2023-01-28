

class SudokuBacktrack(object):
    
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
    
    #Gets the next available field that contains the value of "0"
    def getNextLocation(self):
        for x in range(self.dim):
            for y in range(self.dim):
                if self.board[x][y] == 0:
                    return (x,y)
        return (-1,-1)
    
    #Checks if the assigned value is ok to perform
    def isLegalAssignment(self, location, number):
        
        #Checking the Column
        for col in range(self.dim):
            if self.board[col][location[1]] == number:
                return False

        #Checking the column
        for row in range(self.dim):
            if self.board[location[0]][row] == number:
                return False
            
        #Checking the square
        
        boxW = location[0] - location[0] % 3
        boxH = location[1] - location[1] % 3
        
        for x in range(3):
            for y in range(3):
                if self.board[boxW + x][boxH+y] == number:
                    return False
        return True
    
    def backtrackSolver(self):
        location = self.getNextLocation()
        
        if location == (-1,-1):
            return True
        
        for i in range(1, self.dim + 1):
            if self.isLegalAssignment(location, i):
                self.expandedNodes += 1
                self.board[location[0]][location[1]] = i
                if self.backtrackSolver():
                    return True
                
                self.board[location[0]][location[1]] = 0
        
        return False
    
solver = SudokuBacktrack(9, """010000430
700000000
000254900
170040206
000090003
003006080
001470060
000508120
090060304""")

solver.backtrackSolver()
print(str(solver))
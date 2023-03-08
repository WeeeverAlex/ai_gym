from aigyminsper.search.Graph import State
from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme

class U2(State):

    def __init__(self, bono, adam, larry, edge, lanterna, operator):
        self.bono = bono
        self.adam = adam
        self.larry = larry
        self.edge = edge
        self.lanterna = lanterna
        self.operator = operator

    
    def sucessors(self):
        
        sucessors = []
        
        #bono vai
        if (self.bono == self.lanterna) and (self.bono == False):
            sucessors.append(U2(True, self.adam, self.larry, self.edge, True, 'Bono vai'))
        elif (self.bono == self.lanterna) and (self.bono == True):
            sucessors.append(U2(False, self.adam, self.larry, self.edge, False, 'Bono volta'))
        
        #adam vai
        if (self.adam == self.lanterna) and (self.adam == False):
            sucessors.append(U2(self.bono, True, self.larry, self.edge, True, 'Adam vai'))
        elif (self.adam == self.lanterna) and (self.adam == True):
            sucessors.append(U2(self.bono, False, self.larry, self.edge, False, 'Adam volta'))
        
        #larry vai
        if (self.larry == self.lanterna) and (self.larry == False):
            sucessors.append(U2(self.bono, self.adam, True, self.edge, True, 'Larry vai'))
        elif (self.larry == self.lanterna) and (self.larry == True):
            sucessors.append(U2(self.bono, self.adam, False, self.edge, False, 'Larry volta'))
        
        #edge vai
        if (self.edge == self.lanterna) and (self.edge == False):
            sucessors.append(U2(self.bono, self.adam, self.larry, True, True, 'Edge vai'))
        elif (self.edge == self.lanterna) and (self.edge == True):
            sucessors.append(U2(self.bono, self.adam, self.larry, False, False, 'Edge volta'))

        #bono, edge vai
        if (self.bono == self.lanterna) and (self.edge == self.lanterna) and (self.bono == False) and (self.edge == False):
            sucessors.append(U2(True, self.adam, self.larry, True, True, 'Bono, Edge vai'))
        elif (self.bono == self.lanterna) and (self.edge == self.lanterna) and (self.bono == True) and (self.edge == True):
            sucessors.append(U2(False, self.adam, self.larry, False, False, 'Bono, Edge volta'))

        #bono, larry vai
        if (self.bono == self.lanterna) and (self.larry == self.lanterna) and (self.bono == False) and (self.larry == False):
            sucessors.append(U2(True, self.adam, True, self.edge, True, 'Bono, Larry vai'))
        elif (self.bono == self.lanterna) and (self.larry == self.lanterna) and (self.bono == True) and (self.larry == True):
            sucessors.append(U2(False, self.adam, False, self.edge, False, 'Bono, Larry volta'))
        
        #bono, adam vai
        if (self.bono == self.lanterna) and (self.adam == self.lanterna) and (self.bono == False) and (self.adam == False):
            sucessors.append(U2(True, True, self.larry, self.edge, True, 'Bono, Adam vai'))
        elif (self.bono == self.lanterna) and (self.adam == self.lanterna) and (self.bono == True) and (self.adam == True):
            sucessors.append(U2(False, False, self.larry, self.edge, False, 'Bono, Adam volta'))

        #edge, larry vai
        if (self.edge == self.lanterna) and (self.larry == self.lanterna) and (self.edge == False) and (self.larry == False):
            sucessors.append(U2(self.bono, self.adam, True, True, True, 'Edge, Larry vai'))
        elif (self.edge == self.lanterna) and (self.larry == self.lanterna) and (self.edge == True) and (self.larry == True):
            sucessors.append(U2(self.bono, self.adam, False, False, False, 'Edge, Larry volta'))

        #edge, adam vai
        if (self.edge == self.lanterna) and (self.adam == self.lanterna) and (self.edge == False) and (self.adam == False):
            sucessors.append(U2(self.bono, True, self.larry, True, True, 'Edge, Adam vai'))
        elif (self.edge == self.lanterna) and (self.adam == self.lanterna) and (self.edge == True) and (self.adam == True):
            sucessors.append(U2(self.bono, False, self.larry, False, False, 'Edge, Adam volta'))

        #larry, adam vai
        if (self.larry == self.lanterna) and (self.adam == self.lanterna) and (self.larry == False) and (self.adam == False):
            sucessors.append(U2(self.bono, True, True, self.edge, True, 'Larry, Adam vai'))
        elif (self.larry == self.lanterna) and (self.adam == self.lanterna) and (self.larry == True) and (self.adam == True):
            sucessors.append(U2(self.bono, False, False, self.edge, False, 'Larry, Adam volta'))
        
        

        
        return sucessors

    
    def is_goal(self):
        if self.bono == True and self.adam == True and self.larry == True and self.edge == True and self.lanterna == True:  
            return True
        else:
            return False
    
    
    def description(self):
        return 'U2'
    
    def cost(self):
        if self.operator == 'Bono vai':
            return 1
        elif self.operator == 'Edge vai':
            return 2
        elif self.operator == 'Adam vai':
            return 5
        elif self.operator == 'Larry vai':
            return 10
        
        elif self.operator == 'Bono volta':
            return 1
        elif self.operator == 'Edge volta':
            return 2
        elif self.operator == 'Adam volta':
            return 5
        elif self.operator == 'Larry volta':
            return 10
        
        elif self.operator == 'Bono, Edge vai':
            return 2
        elif self.operator == 'Bono, Larry vai':
            return 10
        elif self.operator == 'Bono, Adam vai':
            return 5
        elif self.operator == 'Edge, Larry vai':
            return 10
        elif self.operator == 'Edge, Adam vai':
            return 5
        elif self.operator == 'Larry, Adam vai':
            return 10
        
        elif self.operator == 'Bono, Edge volta':
            return 2
        elif self.operator == 'Bono, Larry volta':
            return 10
        elif self.operator == 'Bono, Adam volta':
            return 5
        elif self.operator == 'Edge, Larry volta':
            return 10
        elif self.operator == 'Edge, Adam volta':
            return 5
        elif self.operator == 'Larry, Adam volta':
            return 10
        
        
    
    def print(self):
        return str(self.operator)
    
    def env(self):
        return self.operator
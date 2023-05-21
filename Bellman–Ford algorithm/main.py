import copy

#print(float('inf') < 10) 


class Node: 
    

    
    def __init__(self,NumberofNode, NodeValue):

        self.NodeValue = NodeValue
        self.NumberofNode = NumberofNode
        self.path = None 
        
class Network:

    Nodes = []
    Conections = []
    
    def __init__(self, NumberofNodes):
        
        self.NumberofNodes = NumberofNodes
    
        #Appends the first node, so is node 0 and 0 value. 
        self.Nodes.append(Node(0,0))
        
        
        #Apends the next nodes, but starting at infinity. 
        for i in range(1,NumberofNodes): 
            self.Nodes.append(Node(i,float('inf'))) 
            
    
    
    
    def NewConection(self,Network_,*args):
        '''
        Parameters
        ----------
        *args : TUPLE OF (NODE 1, NODE 2, WEIGHT).

        Returns
        -------
        None.

        '''
        #Fills the atribute of conections, with the two conected nodes and weight.
        n1,n2,w = args
        self.Conections.append((n1,n2,w))
        
        
    def BF(self): 
      
        for relaxation in range(self.NumberofNodes - 1): 
            self.Nodes = self.Relaxation(self.Nodes)
            
        
        
        #We run the relaxation again to verify if the distances are not convergin. 
        for conection in self.Conections:            
            Node1,Node2,W = conection 

            if self.Nodes[Node1].NodeValue + W < self.Nodes[Node2].NodeValue:      
                raise Exception('Negative cycles detected')
        
            if self.Nodes[Node1].NodeValue == float('inf'):
                raise Exception(f'Node {Node1} no reachable')
            
                
           
                
            
        return self.Nodes
        
    
  
        
    
    def Relaxation(self,Nodes):
        
        #Nodes should be an array 
        for conection in self.Conections: 
           
            Node1,Node2,W = conection 
            
            if Nodes[Node1].NodeValue + W < Nodes[Node2].NodeValue:      
                Nodes[Node2].NodeValue = Nodes[Node1].NodeValue + W 
                self.Nodes[Node2].path = self.Nodes[Node1]
                
                
            
            
        return Nodes
        
     
    def GetPath(self): 
        Paths = []
        
        for i in range(self.NumberofNodes):
            print('\n ------------')
            print(f' \n Distance for node {i}: {self.Nodes[i].NodeValue} , path for node {i}: ') 
            print(f' {i}  ', end = '')
            while self.Nodes[i].path != None:
                
                
                print(f'<-  {self.Nodes[i].path.NumberofNode} ', end = '')
                
                self.Nodes[i] = self.Nodes[i].path 
                
            
if __name__ == '__main__':
    
   
    
    Conections = [(0, 1, -3), (0, 2, 1), (3, 2, -3), (2, 1, 4), (1,3,5)]
    
    
    
    
    #Conections = [(0,2,5),(1,0,-10),(2,1,3)]

    
    network = Network(NumberofNodes = 4)


    

    for conection in Conections:     
        network.NewConection(network,*conection) 
        
        
    network.BF()
    
    # for i in range(network.NumberofNodes):
        
    #     print(f'Node {i} value: {network.Nodes[i].NodeValue}')
    
        
    
    network.GetPath()
    
    
    
    
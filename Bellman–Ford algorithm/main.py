"""
Bellman-Ford Algorithm. 
This program allow you to create a network with nevative or non negative wheights and find shortest
paths using Bellman-Ford algorithm with negative cycles detection. 
Mail: verdi.resendiz.miguel@gmail.com

Class:
- Node: A class to create node objects with and integer id, a distance value, and a path. 
- Network: A class to create a network object, with nodes and conections, this can create conections,
and then calculate the shortes path using the Bellman-Fortd algorithm. 
"""




class Node: 
    """
    Creates and object called node. 

    Attributes:
    - No atributtes.
    
    Methods:
    
    - No methods. 
    """
    def __init__(self,NumberofNode, NodeValue):
        '''
        Parameters
        ----------
        NumberofNode : Integer value.
        NodeValue : Numerical value.
        Returns
        -------
        None.

        '''
        self.NodeValue = NodeValue
        self.NumberofNode = NumberofNode
        self.path = None 
        
        
class Network:
    """
    Creates and object called node. 

    Attributes:
    - Nodes: An array where the node objects are stored.
    - Conections: An array where the conections are stored.
    
    Methods:
    
    - NewConection(): It takes the network object, and node 1, node 2, and weight to append
    a conection to the Conections atribute. 
    
    - BF(): A function that runs a relaxation V-1 times where V is the number of nodes, then it checks
    if the network has unreachable nodes or negative cycles and raise an exception. 
    
    - _Relaxation(): A private function that checks if the distance of the past node and the wheight 
    of the conection is less than the current node distance, and if it is, updates its value.
    
    - GetPath(): If the algorithm was run succesfuly, it iterates throught each node and recreates the
    path that was followed. 

    """
    Nodes = []
    Conections = []
    
    def __init__(self, NumberofNodes):
        '''
        Parameters
        ----------
        NumberofNodes : Integer value of the number of nodes that network would have.

        Returns
        -------
        None.

        '''
        self.NumberofNodes = NumberofNodes
    
    
        #Appends the first node, so is node 0 and 0 value. 
        self.Nodes.append(Node(0,0))
        
        
        #Apends the next nodes, but starting their distance as infinity. 
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
        '''
        Raises
        ------
        Exception: When negative cycles or infinite path to nodes are detected.

        Returns
        -------
        Nodes: The Nodes atribute updated.

        '''
        #Runs the relaxation V -1 times and updates the nodes atribute. 
        for relaxation in range(self.NumberofNodes - 1): 
            self.Nodes = self._Relaxation(self.Nodes)
            
        
        
        #Runs the relaxation again to verify if negative cycles are detected. 
        for conection in self.Conections:   #Over each conection. 
            Node1,Node2,W = conection 

            if self.Nodes[Node1].NodeValue + W < self.Nodes[Node2].NodeValue:      
                raise Exception('Negative cycles detected') #If the distance changed the V iteration.
            if self.Nodes[Node1].NodeValue == float('inf'):
                raise Exception(f'Node {Node1} no reachable')
            
        return self.Nodes
        
    
  
        
    
    def _Relaxation(self,Nodes):
        '''
        Parameters
        ----------
        Nodes : An array of node objects.
        Returns
        -------
        Nodes : The nodes array updated.

        '''
        for conection in self.Conections: 
           
            Node1,Node2,W = conection 
            #Node 1,2: Firts and second node of a conection, this determinates the direction.  
            #The main algorithm, if the distance of the node2 is bigger than the distance
            #of node 1 plus the wheight it updates the node 2 value.
            if Nodes[Node1].NodeValue + W < Nodes[Node2].NodeValue: 
                Nodes[Node2].NodeValue = Nodes[Node1].NodeValue + W 
                #Appends the last node to the path of the current Node. 
                self.Nodes[Node2].path = self.Nodes[Node1]     
                
        return Nodes
        
     
    def GetPath(self): 
        '''
        Returns
        -------
        None.

        '''
        print('Results of the algorithm')
        
        for i in range(self.NumberofNodes):
            print('\n ------------')
            print(f' \n Distance for node {i}: {self.Nodes[i].NodeValue} , path: ') 
            print(f' {i}  ', end = '')
            
            #Follow the path that was followed to get the shortest distance.
            while self.Nodes[i].path != None:      
                print(f'<-  {self.Nodes[i].path.NumberofNode} ', end = '')
                self.Nodes[i] = self.Nodes[i].path 
                
                
            
if __name__ == '__main__':
    
    network = Network(NumberofNodes = 4 )
    Conections = [(0, 1, -3), (0, 2, 1), (3, 2, -3), (2, 1, 4), (1,3,5)]
    #Conections = [(0,2,5),(1,0,-10),(2,1,3)]

    for conection in Conections:     
        network.NewConection(network,*conection) 
        
    network.BF()
    network.GetPath()
    
    
    
    
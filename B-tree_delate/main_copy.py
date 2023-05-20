class Node:    
    def __init__(self,node): 
        self.node = node
        self.left = None
        self.right = None
    
    
class BinaryTree: 
    
  
    def __init__(self): 
        self.CurrentNode = None
        
        
        
    def Insert(self, CurrentNode, NewNode): 
 
        if CurrentNode is None:            
            CurrentNode = Node(NewNode) #Creation of the first Node
        else: 
            CurrentNode = self.TreeInsertion(CurrentNode, NewNode)
            
        return CurrentNode
            
    
    
    def TreeInsertion(self, CurrentNode, NewNode):
     
        if CurrentNode.node > NewNode:
            
            if CurrentNode.left is None: 
                CurrentNode.left = Node(NewNode)
                
                #print(f'-L{CurrentNode.left.node}---', end='')
            else:
                #print(' \n / ')
                self.TreeInsertion(CurrentNode.left, NewNode)
                
        else: 
            if CurrentNode.right is None: 
                CurrentNode.right = Node(NewNode)
                #print(f'-R{CurrentNode.right.node}---', end  = '')
                
            else:
                
                #print('\n \ ')
                self.TreeInsertion(CurrentNode.right, NewNode)
        
        return CurrentNode
        
    
    
    
    
      
    def Show(self, CurrentNode): 
        if CurrentNode is not None:          
            self.Show(CurrentNode.left)
            print(f' {CurrentNode.node}', end='')
            self.Show(CurrentNode.right)
            
            
    def NextNode(self,CurrentNode): 
        
        CurrentNode = CurrentNode.right
        
        while CurrentNode.left is not None:
            CurrentNode = CurrentNode.left
            
        return CurrentNode
            
    def Delete(self, CurrentNode, Item): 
        
       
        if CurrentNode is not None: 
            # Search for the node to be deleted.
            
            if Item < CurrentNode.node: 
                CurrentNode.left = self.Delete(CurrentNode.left, Item)
                
            elif Item > CurrentNode.node: 
                CurrentNode.right = self.Delete(CurrentNode.right, Item)
            
            
            elif Item == CurrentNode.node: 
                # The deletion algorithm.
                # We have 3 cases.
                
                if CurrentNode.right is not None or CurrentNode.left is not None: 
                    
                    # Case one, the node has one child.
                    if CurrentNode.right is None: 
                        CurrentNode = CurrentNode.left
                        
                        
                    if CurrentNode.left is None: 
                        CurrentNode = CurrentNode.right
                    
                
                    #Two children      
                    else: 
                        
                        
                        #Delate the next element. 
                        Nextnode = self.NextNode(CurrentNode)
                        CurrentNode.node = Nextnode.node
                        
                        
                        
                        CurrentNode.right = self.Delete(CurrentNode.right, Nextnode.node)
          
                
                else:
                    CurrentNode = None
              
        
        return CurrentNode
  
    
  

if __name__ == '__main__': 
    tree = BinaryTree()
    Topology = [15,10,20,8,12,16]
    
    for element in Topology: 
        tree.CurrentNode = tree.Insert(tree.CurrentNode, element)
       
    print('New structure --> ')
    tree.Show(tree.CurrentNode) 
    
    tree.CurrentNode = tree.Delete(tree.CurrentNode, Item= 12)
    
    
    print('\nNew structure --> ')
    tree.Show(tree.CurrentNode)



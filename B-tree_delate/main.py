"""
B-Tree delate algorithm. 
This program is an algorithm to create a bolean tree, with showing, inserting and delating 
methods.  
Author: Miguel Angel Verdi Resendiz
Mail: verdi.resendiz.miguel@gmail.com

Class:
-Node: Creates and object of a node with the value of the node and left and right roots.
-BinaryTree: Creates the binarytree with posibility of insert, show and delate in the tree.
"""




class Node: 
    
    """
    Creates and object called node. 

    Attributes:
    - No atributtes.
    
    Methods:
    
    - No methods. 
    """

    def __init__(self,node): 
        '''
        Parameters
        ----------
        node: Integer value of the node.

        Returns
        -------
        None.
        '''
        self.node = node
        self.left = None
        self.right = None
    
    
    
    
    
    
class BinaryTree: 
    
    """
    Creates and object called node. 

    Attributes:
    - No atributtes.
    
    Methods:
    
    - Insert(): Takes a node object, a numerical value of the new node and looks
    if the BinaryTree object if empty or not, is it is empty it creates the first node,
    if not, it calls the TreeInsertion function to append the next nodes.
    
    -_TreeInsertion(): It is suposed to be a private method,
    takes and node object, and the value of the new node, and returns 
    the node object updated. 
    
    -Show(): It takes a node object and prints in order every node object value.
    
    -NextNode(): Takes a node object and finds the next value to it.
    
    -Delate(): Takes a node object and a value to be delated, and returns the
    node object updated without the delated value. 
        
    
    """
  
    def __init__(self): 
        '''
        Parameters
        ----------
        No parameters.

        Returns
        -------
        None.
        '''
        self.CurrentNode = None
        
        
        
    def Insert(self, CurrentNode, NewNode): 
        '''
        Parameters
        ----------
        CurrentNode: A node object.
        NewNode: The value of the new node

        Returns
        -------
        CurrentNode: The node object given, but updated wit the new node object. 
        '''
        
        #We check if the node is empty or not.
        if CurrentNode is None:       
            
            #Creation of the first Node
            CurrentNode = Node(NewNode) 
            
        else:
            
            #If it is not the first node, we append the newnode in the Current.
            CurrentNode = self._TreeInsertion(CurrentNode, NewNode)
        
        return CurrentNode
            
    
    
    
    
    
    
    def _TreeInsertion(self, CurrentNode, NewNode):
        '''
        Parameters
        ----------
        CurrentNode: A node object.
        NewNode: The value of the new node

        Returns
        -------
        CurrentNode: The node object given, but updated wit the new node object.
        '''
        #Desition of the side of the new node, right or left. 
        #Left side
        if CurrentNode.node > NewNode:
            
            #If the left root of the current node is empty, 
            #The new node is inserted, if not, it keeps searching recursively.
            if CurrentNode.left is None: 
                CurrentNode.left = Node(NewNode)
                
            else:          
                self._TreeInsertion(CurrentNode.left, NewNode)
                
        #Right side
        else:
            
            #If the right root of the current node is empty, 
            #The new node is inserted, if not, it keeps searching recursively.
            if CurrentNode.right is None: 
                CurrentNode.right = Node(NewNode)
              
            else:
                self._TreeInsertion(CurrentNode.right, NewNode)
        
        
        
        return CurrentNode
        
    
    
    
    
      
    def Show(self, CurrentNode): 
        '''
        Parameters
        ----------
        CurrentNode: A node object.
        
        Returns
        -------
        None.
        '''
        #It search until the node is empty. 
        if CurrentNode is not None:    
            #Firts looks recursively to the most left values.
            self.Show(CurrentNode.left)
            print(f' {CurrentNode.node}', end='')
            
            #Then search for the right values.
            self.Show(CurrentNode.right)
            
            
            
            
            
    def NextNode(self,CurrentNode): 
        '''
        Parameters
        ----------
        CurrentNode: A node object.
        
        Returns
        -------
        CurrentNode: A node object. 
        '''
        #The next value is first at the right. 
        CurrentNode = CurrentNode.right
        
        #Then we seach until the most left value after the first right.
        while CurrentNode.left is not None:
            CurrentNode = CurrentNode.left
            
        return CurrentNode
            
    
    
    
    def Delete(self, CurrentNode, Item): 
        '''
        Parameters
        ----------
        CurrentNode: A node object.
        Item: Integer numer to be delated.
        
        Returns
        -------
        CurrentNode: A node object updated without the item. 
        '''
       
        #Search if we are no delating an empty object.
        if CurrentNode is not None: 
            
            #First we have to finde the item to be delated.
            
            #We move trought the roots making the comparation of values.
            if Item < CurrentNode.node: 
                CurrentNode.left = self.Delete(CurrentNode.left, Item)
        
            
            elif Item > CurrentNode.node: 
                CurrentNode.right = self.Delete(CurrentNode.right, Item)
            
            
            #This condition is truen when the item is found.
            elif Item == CurrentNode.node: 
                
                #main delate algorithm, there are 3 posibilities. 
                
                
                #Case 1 and 2: it has more than 0 child.
                if CurrentNode.right is not None or CurrentNode.left is not None: 
                    
                    # Case 1: The node has one child, we just copy and paste the non none,
                    # side of the root. 
                    if CurrentNode.right is None: 
                        CurrentNode = CurrentNode.left
                        
                        
                    if CurrentNode.left is None: 
                        CurrentNode = CurrentNode.right
                    
                    
                    #Case 2: The node has 2 sub-roots of children. 
                    else: 
                        
                        #It finds the next node of the node to be delated.
                        Nextnode = self.NextNode(CurrentNode)
                        
                        #We just update the value of the current node,
                        #For the value of the next value.
                        CurrentNode.node = Nextnode.node
                        
                        #It is now necesarry tho erase the "next-value", so we do recursively,
                        #It has to take the right side because the next value if alwas at the 
                        #right side of the root. 
                        CurrentNode.right = self.Delete(CurrentNode.right, Nextnode.node)
          
                
                 
                
                #Case 3: It has no child, so we simply delate the object.
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



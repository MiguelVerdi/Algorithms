import math


"""
Bucket sort algorithm. 
This program reads a csv file with a column of numbers and sort them.
Author: Miguel Angel Verdi Resendiz
Mail: verdi.resendiz.miguel@gmail.com

Class:
-Bucket_sort: Sorts an array of data using the bucket sort algorithm. 
"""


class bucket_sort(): 
    
    """
   Sorts an array of data using the bucket sort algorithm. 

    Attributes:
    - No atributtes.
    
    Methods:
    
    - get_data(): Opens an csv file, and converts it to a data float array.     
    - extreme_values(): Gets the max an min value of an array. 
    - sort(): sorts recursively an array of data with the bucket sort algorithm. 
    """

    def __init__(self,n):
        '''
        Parameters
        ----------
        n : BUCKETS LENGHT.

        Returns
        -------
        None.
        '''
        self.List = []  #List to be open 
        self.n = n
        
        
        
        
    def get_data(self,File): 
        '''
        Parameters
        ----------
        File : SHOULD BE THE DIRECTION OF THE FILE (csv format)

        Returns
        -------
        None.

        '''
        with open(File,'r') as _file_:
            for line in _file_: self.List.append(float(line.strip()))
            
        
           
        
        
        
    def extreme_values(self,Array):
        '''
        Parameters
        ----------
        Array : SHOULD BE AN ARRAY TYPE.

        Returns
        -------
        min_v : MINIMUN VALUE OF ARRAY.
        max_v : MAXIMUN VALUE OF ARRAY.

        '''
        
        extreme_values = []
        
        if len(Array) > 1: 
            min_v = Array[0]
            max_v = Array[0]
            
            
            
            #Finding maximun and minimun value. 
            for i in range(0,len(Array)): 
                
                if min_v >= Array[i]: 
                    min_v = Array[i]#Minimun item
                    
                if max_v <= Array[i]:
                    max_v = Array[i]#Maximun item

            
            extreme_values = [max_v,min_v]
        
      
        else: 
            extreme_values = False
            
            
        return extreme_values

        
        
    
    def sort(self, Array):
        '''
        Parameters
        ----------
        Array : ARRAY TO BE SORTED (Array type).

        Returns
        -------
        Sorted array (Array type).

        '''
        sorted_list = [] #List where the items will be stored.
        buckets = [[] for i in range(0,self.n)] #Creates n numbers of buckets 
        min_item,max_item = self.extreme_values(Array) #Gets the max an min item. 
        
        
        
        #Creation 
        for number in Array: 
            
            if number != max_item: 
                #If the number is not the max item, we put in in one of the buckets.
                
                index = math.floor(self.n*(number - min_item)/(max_item - min_item))
                
                
            else:
                #If the number is the max item, it goes at the last bucket. 
                index = -1
        
        
            buckets[index].append(number)
        


        for bucket in buckets:  
            
            if len(bucket) > 1: 
                
                sorted_ = True 
                
                for i in range(0,len(bucket) -1): 
                    if bucket[i] < bucket[i+1]:
                        sorted_ = False 
                        

                if not sorted_: 
                    bucket = self.sort(bucket)
                    
                
            sorted_list += bucket 
               
        
        return sorted_list
    
  
        
    def show(self,original_array, sorted_array):
        print("Result of sorting algorithm:")
        print("---------------------------------------")
        print("Sorted data:")
        print(", ".join(map(str, sorted_array)))
        print("---------------------------------------")
        print('Original data:')
        print(", ".join(map(str, original_array)))
        print("---------------------------------------")

        
if __name__ == "__main__":

    file = 'Numbers.csv'
    New_sort = bucket_sort(n = 5)
    New_sort.get_data(file)
    
    
    sort1 = New_sort.sort(New_sort.List) 
     
    
    New_sort.show(New_sort.List,sort1)
    
    
    


    
 
        
        
        
    




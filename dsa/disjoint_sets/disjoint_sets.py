class DisjointSet:
    def __init__(self, N : int):
        """
        N - number of elements in set
        s - underlying collection for sets, a collection of tree represented with array
        """
        self.N = N
        # the index is used to represent the element
        # -1 represents that the node is a root
        self.s = [-1] * self.N
        return
     
    def find(self, x : int):
        if self.s[x] < 0:
            # If x is root, return
            return x
        else:
            # if x is not root, check the parent of x
            return self.find(self.s[x])
        
    
    def simpleUnionSets(self, root1 : int, root2 : int):
        """
        Union two disjoint sets by changing root2's parent
        Not the best way
        """
        self.s[root2] = root1
    
    def unionBySize(self, root1 :int, root2: int):
        """

        """
        return

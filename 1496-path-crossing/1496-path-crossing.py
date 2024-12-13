class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        i=0
        j=0
        visited =[[0,0]]
        for s in path:
            if s=='N':
                i-=1
            if s=='S':
                i+=1
                
            if s=='W':
                j-=1
            
            if s=='E':
                j+=1
            
            if [i,j] in visited:
                return True
            visited.append([i,j])
        return False
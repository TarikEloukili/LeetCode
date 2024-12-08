class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result =[]
        from math import sqrt
        
        
        for i in range(len(points)):
            dist = sqrt(points[i][0]**2 + points[i][1]**2)
            result.append((points[i], dist))
        result.sort(key= lambda x:x[1])
        output=[]
        for i in range(len(result)):
            output.append(result[i][0])
        return output[:k]
        
            
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        sorted_map = dict()
        for s in strs:
            L= tuple(sorted(s))
            if L not in sorted_map.keys():
                sorted_map[L] = []
            sorted_map[L].append(s)
            
        for v in sorted_map.values():
            output.append(v)
        return(output)
        
                
                    
                
                
            
        
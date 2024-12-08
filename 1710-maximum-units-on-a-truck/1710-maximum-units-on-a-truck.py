class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        
        maximum_units=0
        
        for boxes, units in boxTypes:
            if truckSize ==0:
                break
            boxes_to_take = min(truckSize, boxes)
            maximum_units += boxes_to_take*units
            truckSize -= boxes_to_take
        return maximum_units
        
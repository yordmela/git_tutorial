from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if the intervals list is empty, return an empty list
        if not intervals:
            return []

        # sort the intervals based on the start time
        intervals.sort(key=lambda x:x[0])
        merged=[]

        # iterate through the intervals
        for interval in intervals:
            # if no overlap, add the interval in to the list
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            # if there is an overlap, merge the intervals
            elif merged[-1][0]<=interval[0]<=merged[-1][1]:
                merged[-1][1]= max(merged[-1][1], interval[1])
        return merged

            
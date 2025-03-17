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
            # if the merged list is empty or the end time of the last interval in the merged list is less than the start time of the current interval, append the interval to the merged list
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            # if the last interval in the merged list is less than the start time of the current interval, append the interval to the merged list
            elif merged[-1][0]<=interval[0]<=merged[-1][1]:
                # update the end time of the last interval in the merged list
                merged[-1][1]= max(merged[-1][1], interval[1])
        return merged


def test_merge():
    solution = Solution()
    
    # Test case 1: Typical input
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert solution.merge(intervals) == [[1, 6], [8, 10], [15, 18]]

    # Test case 2: Empty intervals list
    assert solution.merge([]) == []

    # Test case 3: Non-overlapping intervals
    assert solution.merge([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

    # Test case 4: Nested intervals
    assert solution.merge([[1, 5], [2, 4]]) == [[1, 5]]

    # Test case 5: Intervals that can be merged
    assert solution.merge([[1, 3], [2, 6], [5, 10]]) == [[1, 10]]

    print("All test cases passed.")

# Run the test function
test_merge()
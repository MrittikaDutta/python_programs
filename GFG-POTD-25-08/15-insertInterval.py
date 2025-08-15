class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        result = []
        i = 0
        n = len(intervals)

        # 1. Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 3. Add the merged newInterval
        result.append(newInterval)

        # 4. Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

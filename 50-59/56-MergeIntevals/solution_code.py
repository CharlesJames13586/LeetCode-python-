class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda interval: interval[0])
        megerIntervals = [intervals[0]]
        for interval in intervals:
            if megerIntervals[-1][0] <= interval[0] <= megerIntervals[-1][1]:
                if interval[1] > megerIntervals[-1][1]:
                    megerIntervals[-1][1] = interval[1]
            else:
                megerIntervals.append(interval)

        return megerIntervals


if __name__ == "__main__":
    solution = Solution()
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[2, 6], [1, 3], [15, 18], [8, 10]]
    intervals = [[1, 4], [4, 5]]
    print(solution.merge(intervals))
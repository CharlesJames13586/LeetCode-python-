class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combination = [0] * k
        results = []
        self.DFS(0, 0, n, k, combination, results)

        return results

    def DFS(self, now, all, n, k, combination, results):
        if all == k:
            # results.append(combination.copy())
            results.append(combination[:])
            return
        for j in range(now, n):
            combination[all] = j + 1
            self.DFS(j+1, all+1, n, k, combination, results)
            combination[all] = 0


if __name__ == "__main__":
    solution = Solution()
    n = 4
    k = 2
    print(solution.combine(n, k))
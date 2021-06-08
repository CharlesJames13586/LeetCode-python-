import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        labels = [i for i in range(1, n+1)]
        rest = k
        for i in range(n):
            for j in range(n):
                if math.factorial(len(labels)-1) * (j+1) >= rest:
                    result += str(labels[j])
                    rest = rest - math.factorial(len(labels)-1) * j
                    del labels[j]
                    break

        return result


if __name__ == "__main__":
    n = 4
    k = 9
    solution = Solution()
    print(solution.getPermutation(n, k))
class Solution(object):


    def groupAnagrams_1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        outputs = []
        result = []
        for i in range(len(strs)):
            output = self.embedd(strs[i])
            if output not in outputs:
                outputs.append(output)
                result.append([strs[i]])
            else:
                index = outputs.index(output)
                result[index].append(strs[i])

        return result

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for i in range(len(strs)):
            # output = self.embedd(strs[i])
            # key = ''
            # for num in output:
            #     key = key + ' ' + str(num)
            output = sorted(strs[i])
            key = tuple(output)
            if key not in hashmap:
                hashmap[key] = [strs[i]]
            else:
                hashmap[key].append(strs[i])

        return list(hashmap.values())

    def embedd(self, str):
        output = [0]*26
        for i in range(len(str)):
            output[ord(str[i])-ord('a')] = output[ord(str[i])-ord('a')] + 1

        return output


if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = [""]
    # strs = ["a"]
    print(solution.groupAnagrams(strs))

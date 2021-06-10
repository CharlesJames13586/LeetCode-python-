import math
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line_num = 0
        line_start_index = 0
        line_characters = 0
        result = []
        while line_start_index < len(words):
            while line_start_index+line_num < len(words) and len(words[line_start_index+line_num]) + line_characters + line_num < maxWidth:
                line_characters += len(words[line_start_index+line_num])
                line_num += 1
            rest_space = maxWidth - line_characters
            line = ""
            for i in range(line_num-1):
                if line_start_index + line_num <= len(words):
                    # last_space = int(math.ceil(rest_space / (line_num - 1 - i)))
                    # leetcode的math.ceil()好像有bug
                    last_space = rest_space // (line_num - 1 - i)
                    if rest_space % (line_num - 1 - i) > 0:
                        last_space += 1
                else:
                    last_space = 1
                line += words[line_start_index+i] + ' '*last_space
                rest_space -= last_space
            line += words[line_start_index + line_num - 1]
            line += (maxWidth - len(line)) * ' '
            result.append(line)

            line_start_index = line_start_index + line_num
            line_characters = 0
            line_num = 0

        return result


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    for line in result:
        print(line)

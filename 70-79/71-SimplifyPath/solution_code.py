class Solution(object):
    def simplifyPath_1(self, path):
        """
        这个方法太笨了，哈哈，相当于手动实现栈
        :type path: str
        :rtype: str
        """
        result = "/"
        index = 0
        cur_dir = ""
        while index < len(path):
            if path[index] == '/':
                if result[-1] != '/':
                    result += '/'
                result += cur_dir
                # 跳过其它连续的的'/'
                while index+1 < len(path) and path[index+1] == '/':
                    index += 1
                cur_dir = ""
            elif cur_dir == '' and path[index] == '.':
                if index+1 == len(path):
                    pass
                elif index+1 < len(path) and path[index+1] == '/':
                    pass
                elif index+1 < len(path) and path[index+1] == '.' and (index+2 < len(path) and path[index+2] == '/' or index+2 == len(path)):
                    index += 2
                    # 回溯到上一个目录
                    if len(result) > 1:
                        result = result[1:]
                    else:
                        continue
                    if result[-1] == '/':
                        result = result[:-1]
                    result_tmp = result.split('/')
                    result = ""
                    for item in range(len(result_tmp)-1):
                        result += '/' + result_tmp[item] 
                    if result == "":
                        result = "/"
                else:
                    cur_dir += path[index]
            else:
                cur_dir += path[index]

            index += 1 

        if cur_dir != "":
            if result[-1] != '/':
                result += '/' + cur_dir
            else:
                result += cur_dir
        if len(result) > 1 and result[-1] == '/':
            result = result[:-1]

        return result

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = [dir for dir in path.split('/') if dir != ""]

        stack = []
        for dir in dirs:
            if dir == '.':
                continue
            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        result = "/" + '/'.join(stack)

        return result
                

if __name__ == "__main__":
    # path = "/home/"
    # path = "/../"
    # path = "/home//foo/"
    # path = "/a/./b/../../c/"
    # path = "/a//b////c/d//././/.."
    path = "/..."
    # path = "/.hidden"
    solution = Solution()
    print(solution.simplifyPath(path))
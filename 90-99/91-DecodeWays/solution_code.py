class Solution:
    def __init__(self):
        self.memo = {}
    # A B C D E F G H I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
    
    def numDecodings(self, s: str) -> int:
        # 如果备忘录中有函数结果就直接调用
        if s in self.memo.keys():
            return self.memo[s]
        
        if len(s) == 0:
            return 1
        one, two = 0, 0
        if len(s) > 0:
            if s[0] in ['0']:                    # 解析出错，没有首位为0的情况
                return 0                     
            if s[0] in ['1']:
                one = self.numDecodings(s[1:])         # 解析为A
                if len(s) > 1:
                    two = self.numDecodings(s[2:])     # 解析为JKLMNOPQRS的其中一个
            elif s[0] in ['2']:
                one = self.numDecodings(s[1:])         # 解析为B
                if len(s) > 1:
                    if s[1] in ['0', '1', '2', '3', '4', '5', '6']:
                        two = self.numDecodings(s[2:]) # 解析为TUVWXYZ的其中一个
                    else:
                        two = 0                        # 解析出错，没有27-29
            else:
                one = self.numDecodings(s[1:])         # 解析为CDEFGHI

        if s not in self.memo.keys():
            self.memo[s] = one + two
        
        return one + two

if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("111111111111111111111111111111111111111111111"))
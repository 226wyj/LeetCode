class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # T: O(N)
        # S: O(N)
        # 思想: 前缀和
        # 设前缀和数组, prefix[i], 代表前i个字符中1的个数
        # 则以 i 作为分界的时候若想将整个字符串翻转到递增,则 i 前面
        # 的1要被尽可能翻转成0, i 后面的0要被尽可能翻转成1
        # 因此总的翻转次数为 prefix[i] + len(s) - i - (prefix[-1] - prefix[i])
        # 其中，prefix[i] 代表前 i 个字符中 1 的个数，之后我们要找后面子串中 0 的个数
        # 已知总字符串长度是 len(s)，则后面子串的长度是 len(s) - i
        # 后面的子串中包含的 1 的数量是 prefix[-1] - prefix[i]
        # 则后面子串中 0 的数量是 len(s) - i - (prefix[-1] - prefix[i])
        # 遍历整个前缀和数组取最小值即可
        prefix = [0]
        for char in s:
            prefix.append(prefix[-1] + int(char))
        
        res = float('inf')
        for i in range(len(prefix)):
            res = min(res, prefix[i] + len(s) - i - (prefix[-1] - prefix[i]))
        return res

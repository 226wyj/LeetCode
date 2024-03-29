# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # T: O(N), N 为嵌套元素总数
        # S: O(D), D 为最大嵌套深度
        res = 0
        
        def dfs(x: NestedInteger, level):
            tmp = 0
            if x.isInteger():
                return level * x.getInteger()
            for l in x.getList():
                tmp += dfs(l, level + 1)
            return tmp

        for x in nestedList:
            res += dfs(x, 1)
        return res

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        
        # 贪心，h按照从高到低的顺序排序，k按从低到高排序
        # lambda 返回的是一个元组，当-x[0]相同时，再根据x[1]进行排序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        result = []
        for p in people:
            result.insert(p[1], p)
        return result

"""
In python we do not have max heap, so we need to multipy all with negative 1
and then convert to min heap so the max order is maintained.
example,

input = [2,7,4,1,8,1]
after heapifying
[-8,-7,-4,-2,-1,-1]

"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first :
                heapq.heappush(stones, first-second) # need to push the negative difference so we do first - second

        stones.append(0)
        return abs(stones[0])
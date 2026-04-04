class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            count[num]+=1
        
        arr = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res
        

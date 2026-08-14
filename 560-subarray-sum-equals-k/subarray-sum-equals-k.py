class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_cnt = 0   
        cnt_sum = 0   
        d = {0:1}
        for i in nums:
            cnt_sum += i     # Required prefix sum(prefix(l-1),history)
            req =cnt_sum - k # Check if req om d prefixes so far
            if req in d:
                sub_cnt += d[req]    # add the no of times we seen in d prefixes
            d[cnt_sum] = d.get(cnt_sum,0) + 1
        return sub_cnt

            





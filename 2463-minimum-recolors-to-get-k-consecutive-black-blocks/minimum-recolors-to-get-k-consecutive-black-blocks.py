class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        cnt_whites = 0
        ans = float('inf')
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                cnt_whites += 1
            while right - left + 1 > k :
                if blocks[left] == 'W':
                    cnt_whites -= 1
                left += 1
            if right - left + 1 == k:
                ans = min(cnt_whites,ans)
        return ans
                


       
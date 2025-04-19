def longestOnes(nums, k):
        maxlen=0
        left = 0
        r = 0
        
        zero = 0
        while r<len(nums):
            print("for r = ",r)
            if nums[r]==0:
                print(f"{nums[r]}==0")
                zero+=1
            while zero > k:
                if nums[left]==0:
                    zero  -=1
                left +=1
            maxlen = max(maxlen, r - left + 1)
            r+=1

        return maxlen
        
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],k=2))
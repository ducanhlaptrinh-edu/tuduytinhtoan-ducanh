def length_of_lis(nums):
    if not nums:                  # Dòng 1
        return 0                  # Dòng 2
    
    dp = [1] * len(nums)          # Dòng 3
    
    for i in range(len(nums)):    # Dòng 4
        for j in range(i):        # Dòng 5
            if nums[i] > nums[j]: # Dòng 6
                dp[i] = max(dp[i], dp[j] + 1) # Dòng 7
                
    return max(dp)                # Dòng 8
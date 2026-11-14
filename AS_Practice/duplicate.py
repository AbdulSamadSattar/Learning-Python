nums = [4, 7, 2, 9, 4, 1, 7] 
def duplicates(nums):
    dup_list = []
    for i in nums:
        if nums.count(i) >= 2 and i not in dup_list :
            dup_list.append(i)
    print(dup_list)
        
duplicates(nums)

# Output:
# [4, 7]    


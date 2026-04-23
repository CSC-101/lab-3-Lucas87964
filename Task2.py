def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num  #num=4 total=4, num=9 total=13, num=2 total=15, num=1 total=16
    return total

result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    newlist = []
    for idx in range(len(nums)):
        newlist.append(nums[idx]) # idx=0 new=[4], idx=1 new=[4, 9], idx=2 new=[4, 9, 2], idx=3 new=[4, 9, 2, 1]
    return newlist                #this returns the full list, not the total value like above

result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    newlist = []
    for value in nums:
        newlist.append(value + 1) #value=4 new=[5], value=9 new=[5, 10], value=2 new=[5, 10, 3], value=1 new=[5, 10, 3, 2]
    return newlist

result = increment_all([4, 9, 2, 1])
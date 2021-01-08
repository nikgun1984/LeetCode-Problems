def numIdenticalPairs(self, nums: List[int]) -> int:
    # Step 1: Create dictionary
    # Step 2: If an element in dict add 1
    #         if not add elem and set to 0
    # Step 3: Calculate total pairs and sum them up
    num_pairs = dict()
    for num in nums:
        num_pairs[num] = num_pairs.setdefault(num,0)+1
    count = 0
    for num in num_pairs.values():
        count += num*(num-1)/2
    return int(count)
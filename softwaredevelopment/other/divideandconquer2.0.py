import random

def find_max(nums):
    if len(nums) == 1:
        return nums[0]
    first = nums[0]
    max_of_rest = find_max(nums[1:])
    return first if first > max_of_rest else max_of_rest

numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)
print("Maximum value:", find_max(numbers))
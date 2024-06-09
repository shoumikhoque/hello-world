import math
import random
from collections import Counter




def numberOfpairs(nums1, nums2, k):
    nums1 = [num // k for num in nums1 if num % k == 0]
    if len(nums1) == 0:
        return 0
    freqs = Counter(num for num in nums2)
    counts = [0] * (max(nums1) + 1)
    for num, count in freqs.items():
        for multiplier in range(num, len(counts), num):
            counts[multiplier] += count
    return sum(counts[num] for num in nums1)

def generate_test_cases(number_of_cases=1000):
    for i in range(number_of_cases):
        n=random.randint(1,100000)
        m = random.randint(1, 100000)
        k=random.randint(1, 1000)
        nums1=[random.randint(1, 1000000) for _ in range(n)]
        nums2 = [random.randint(1, 1000000) for _ in range(n)]
        print(numberOfpairs(nums1, nums2, k))
if __name__ == '__main__':
    nums1=[2,8,17,6]
    nums2=[3,1,1,8]
    k = 2
    print(numberOfpairs(nums1, nums2, k))

    # generate_test_cases(1000)


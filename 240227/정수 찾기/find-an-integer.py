n1 = int(input())
nums1 = set(map(int, input().split()))

n2 = int(input())
nums2 = list(map(int, input().split()))

for n in nums2:
    if n in nums1:
        print(1)
    else:
        print(0)
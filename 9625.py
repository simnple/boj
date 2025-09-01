# B -> BA
# A -> B

"""
규칙 찾기 -> 피보나치 수열임.
word = "A"
K = int(input())
for i in range(K):
    result = []
    for s in word:
        if s == "A":
            result.append("B")
        else:
            result.append("BA")
    word = "".join(result)
    print(i+1, word.count("A"), word.count("B"))
"""

K = int(input())
nums = [0] * (K + 1)
nums[1] = 1
for i in range(2, K+1):
    nums[i] = nums[i-1] + nums[i-2]
print(nums[K-1], nums[K])
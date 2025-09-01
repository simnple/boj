"""
총 16
킹1
퀸1
룩2
비숍2
나이트2
폰8
"""

_ = [1, 1, 2, 2, 2, 8]

__ = list(map(int, input().split(" ")))

_ = map(str, [_[i] - __[i] for i in range(len(_))])

print(" ".join(_))
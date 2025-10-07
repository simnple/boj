_ = list(map(int, input().split(" ")))
__ = _[0] * 60 + _[1] - 45
___ = __//60

print(___ if ___ >= 0 else "23", __%60)
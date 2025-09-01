items = list(set([input() for _ in range(int(input()))]))
items_to_length = {}

for _ in items:
    if len(_) in items_to_length:
        items_to_length[(len(_))].append(_)
    else:
        items_to_length[len(_)] = [_]

items_to_length = sorted(items_to_length.items())

for _ in items_to_length:
    __ = _[1]
    __.sort()

    for ___ in __:
        print(___)
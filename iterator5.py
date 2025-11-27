def flatten_generator(sequence):
    for i in sequence:
        if isinstance(i, list):
            for j in flatten_generator(i):
                yield j
        else:
            yield i

for i in flatten_generator([1, 2, [3, [4], 5]]):
    print(i)
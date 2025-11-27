class ZipIterator:
    def __init__(self, *sequences):
        self.index_in_sequence = 0
        self.sequences = sequences
        self.len_of_sequence = len(sequences[0])

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_in_sequence < self.len_of_sequence:
            self.index_in_sequence += 1
            return [x[self.index_in_sequence-1] for x in self.sequences]
        raise StopIteration


for i in ZipIterator([1, 2], [3, 4], [5, 6]):
    print(i)
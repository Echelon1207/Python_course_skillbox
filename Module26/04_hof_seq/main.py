class QHofstadter:
    def __init__(self, seq):
        self.seq = seq
        self.cnt = 2

    def __next__(self):
        self.cnt += 1
        try:
            Q = self.seq[self.cnt - self.seq[self.cnt - 2] - 1] + self.seq[self.cnt - self.seq[self.cnt - 3] - 1]
            self.seq.append(Q)
            return self.seq
        except IndexError:
            raise StopIteration()
    def __iter__(self):
        return self
x = 0
q_hofstadter = QHofstadter([1,1])
for i in q_hofstadter:
    if x > 30:
        break
    print(i)
    x += 1
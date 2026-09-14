class vector:
    def __init__(self, l):
        self.l = l  

    def __len__(self):
        return len(self.l)




v1 = vector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len(v1))

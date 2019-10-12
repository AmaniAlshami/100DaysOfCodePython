class Numbers :
    def __iter__(self):
        self.x = 1
        return self
    def __next__(self):
        if self.x <= 10:
             y = self.x
             self.x+=1
             return y
        else:
            raise StopIteration

obj = Numbers()
itr = iter(obj)

print(next(itr))
print(next(itr))
print(next(itr))

for a in itr:
    print(a)

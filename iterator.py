
class Iterator:
    def __init__(self,bag):
        self.bag=bag
        self.it=0

    def next(self):
        if self.bag.size() != 0:
            if self.it<self.bag.size():
                self.it+=1
                self.bag.getElem(self.it)
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("The bag is empty")

    def first(self):
        if self.bag.size() != 0:
            self.it=0
            return self.bag[self.it]
        else:
            raise ValueError("The bag is empty")

    def getCurrent(self):
        if self.bag.size() != 0:
            e=self.bag[self.it]
            return e
        else:
            raise ValueError("The bag is empty")

    def valid(self):
        if self.it<self.bag.size():
            return True
        else:
            return False
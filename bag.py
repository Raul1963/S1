from iterator import Iterator
class Bag:
    def __init__(self):
        self.b=[]

    def add(self,el):
        self.b.append(el)

    def print(self):
        print(self.b)

    def getElem(self,i):
        return self.b[i]
    def search(self,e):
        if len(self.b)!=0:
            for i in range(len(self.b)):
                if self.b[i]==e:
                    return True
            return False
        else:
            return False

    def size(self):
        return len(self.b)

    def nrOccurrences(self,e):
        nr=0
        for i in range(len(self.b)):
            if self.b[i]==e:
                nr+=1
        return nr

    def destroy(self):
        self.b=None

    def iterator(self):
        it=Iterator(self)

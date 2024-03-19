from bag import Bag
from iterator import Iterator

bag=Bag()
bag.add(1)
bag.add(2)
bag.add(3)
bag.add(4)
bag.add(2)
bag.print()
assert bag.search(2)==True
assert bag.size()==5
assert bag.nrOccurrences(2)==2
# bag.destroy()
# bag.print()
it=Iterator(bag)
it.next()

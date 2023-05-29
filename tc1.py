from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *
m3 = NFA()
m3.setSigma(['a','b', 'c'])
m3.addState('s0')
m3.addState('s1')
m3.addState('s2')
m3.setInitial([0])
m3.addFinal(1)
m3.addTransition(0, 'c', 0)
m3.addTransition(0, 'c', 1)
m3.addTransition(0, 'b', 1)
m3.addTransition(0, 'b', 2)
m3.addTransition(1, 'a', 0)
m3.addTransition(1, 'a', 2)
m3.addTransition(2, 'c', 2)
m3.addTransition(2, 'a', 0)
m3.addTransition(2, 'b', 0)


m3
print(m3, "\n\n")

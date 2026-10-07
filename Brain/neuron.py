import random
goal = 14
weight1 = 0.0
weight2 = 0.0
weight3 = 0.0
import Memory.memory
from Memory.memory import memory, save
def test():
    inp1 = 1
    inp2 = 4
    inp3 = 3
    def weights():
        global weight1, weight2, weight3, lowchange, highchange
        lowchange = memory['closestlow'] * 10
        highchange = memory['closesthigh'] * 10
        weight1 = random.randint(lowchange, highchange)
        weight2 = random.randint(lowchange, highchange)
        weight3 = random.randint(lowchange, highchange)
        weight1 / 10
        weight2 / 10
        weight3 / 10
    weights()
    bias = 1
    sum = (inp1 * weight1) + (inp2 * weight2) + (inp3 * weight3) + bias
    #goal is 14 IMA BOUT TO TURN 14
    if sum < goal:
        if memory['closestlow'] < weight1:
            memory['closestlow'] = weight1
            print('q')
        if memory['closestlow'] < weight2:
            memory['closestlow'] = weight2
            print('w')
        if memory['closestlow'] < weight3:
            memory['closestlow'] = weight3
            print('e')
    if sum > goal:
        if memory['closesthigh'] > weight1:
            memory['closesthigh'] = weight1
            print('r')
        if memory['closesthigh'] > weight2:
            memory['closesthigh'] = weight2
            print('t')
        if memory['closesthigh'] > weight3:
            memory['closesthigh'] = weight3
            print('y')
    print(weight1)
    print(weight2)
    print(weight3)
    if sum == goal:
        memory['totalachived'] = True
        memory['totalnum'] = goal
    save()
while memory['totalachived'] == False:
    test()

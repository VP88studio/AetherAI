import random, os
goal = 14
from Brain.config import WipeMem, testprint, SaveState
weight1 = 0.0
weight2 = 0.0
weight3 = 0.0
cmulti = 1
nounfloat = True
import Brain.Memory.memory
from Brain.Memory.memory import memory, save
if WipeMem:
    print("Wiping Memory...")
    os.remove('Brain/Memory/memory.json')
    print('! WIPEDMEM !')
    quit()
print(memory['closestlow'])
print(memory['closesthigh'])
def test():
    inp1 = 1
    inp2 = 4
    inp3 = 3
    def weights():
        global weight1, weight2, weight3, lowchange, highchange, cmulti, nounfloat
        lowchange = memory['closestlow'] * 10
        highchange = memory['closesthigh'] * 10
        while nounfloat:
            if type(lowchange) == float or type(highchange) == float:
                lowchange = lowchange * 10
                highchange = highchange * 10
                cmulti += 1
            elif type(lowchange) == int and type(highchange) == int:
                nounfloat = False
        weight1 = random.randint(lowchange, highchange)
        weight2 = random.randint(lowchange, highchange)
        weight3 = random.randint(lowchange, highchange)
        for i in range(cmulti):
            weight1 = weight1 / 10
            weight2 = weight2 / 10
            weight3 = weight3 / 10
        cmulti = 1
        nounfloat = True
    weights()
    bias = 1
    sum = (inp1 * weight1) + (inp2 * weight2) + (inp3 * weight3) + bias
    #goal is 14 IMA BOUT TO TURN 14
    def testcheck():
        global SaveState
        if sum < goal:
            if memory['closestlow'] < weight1:
                memory['closestlow'] = weight1
                SaveState = True
                print('q')
                print(weight1)
            if memory['closestlow'] < weight2:
                memory['closestlow'] = weight2
                SaveState = True
                print('w')
                print(weight2)
            if memory['closestlow'] < weight3:
                memory['closestlow'] = weight3
                SaveState = True
                print('e')
                print(weight3)
        if sum > goal:
            if memory['closesthigh'] < weight1:
                memory['closesthigh'] = weight1
                SaveState = True
                print('r')
                print(weight1)
            if memory['closesthigh'] < weight2:
                memory['closesthigh'] = weight2
                SaveState = True
                print('t')
                print(weight2)
            if memory['closesthigh'] < weight3:
                memory['closesthigh'] = weight3
                SaveState = True
                print('y')
                print(weight3)
        if testprint:
            print(weight1)
            print(weight2)
            print(weight3)
            print(memory['closesthigh'])
            print(memory['closestlow'])
        if sum == goal:
            memory['totalachived'] = True
            memory['totalnum'] = goal
            print('goalreached')
        if SaveState == True:
            if testprint:
                print('saved')
            save(memory)
            SaveState = False
    testcheck()
while memory['totalachived'] == False:
    test()

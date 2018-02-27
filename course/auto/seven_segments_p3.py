from math import *

def HopfieldNetwork(pattern):
    print ("Hello world! \n")

    weightMatrix = []
    this_sum = 0;
    for val_i in range(0,len(pattern)):
        for val_j in range(0,len(pattern)):
            if(val_i == val_j): continue;
            this_sum += (pattern[val_i] * pattern[val_j])

        this_sum = this_sum / len(pattern)
        weightMatrix[val_i].append(this_sum)
        this_sum = 0;

    print(this_sum)
    print(weightMatrix)



def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False


    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")

    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "

        if d3:
            word+="_"
        else:
            word+=" "

        if d2:
            word+="|"
        else:
            word+=" "

        print(word)



    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))



six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

print("Hopfield Matrix! ")
HopfieldNetwork(three)


print("test1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

seven_segment(test)

print("test2")

#here the network should run printing at each step

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]

seven_segment(test)

#here the network should run printing at each step

from math import *
import numpy as np

def HopfieldNetworkLearn(patterns):
    print ("Hello world! \n")

    numOfPatterns = len(patterns)
    weightMatrix = np.empty([len(patterns[0])+1,len(patterns[0])+1])

    # Aim is loop through all i,j values
    # Add up the pairs of all the numOfPatterns
    # that results in the value for the weight matrix.

    for i_val in range(0,len(patterns[0])):
        for j_val in range(0,len(patterns[0])):
            if(i_val == j_val):
                weightMatrix[i_val,j_val] = 0
            else:
                this_sum = 0
                for pattern in patterns:
                    this_sum += pattern[i_val] * pattern[j_val]
                weightMatrix[i_val,j_val] = this_sum / len(patterns)

    # print(weightMatrix)

    return weightMatrix

def HopfieldNetworkApplied(weightMatrix, pattern):
    haveChangedBool = True;
    new_pattern = np.zeros(len(pattern));
    numberOfIterations = 0
    while(haveChangedBool): #until convergence
        haveChangedBool = False;
        for i_val in range(0,len(pattern)):
            sum_val = 0
            for j_val in range(0,len(pattern)):
                sum_val += (weightMatrix[i_val,j_val] * pattern[j_val])
            if(sum_val >0):
                if(new_pattern[i_val] != 1): haveChangedBool = True;
                new_pattern[i_val] = 1
            else:
                if(new_pattern[i_val] != -1): haveChangedBool = True;
                new_pattern[i_val] = -1
        pattern = np.copy(new_pattern)
        seven_segment(pattern)
        numberOfIterations +=1

    print("Number of Iterations! : {0}".format(  numberOfIterations));


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

patternsList = []
patternsList.extend([six, three, one]);
print("Hopfield Matrix! ")
hop_weights = HopfieldNetworkLearn(patternsList)


print("----------------------")
print("test1")
print("----------------------")
test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
HopfieldNetworkApplied(hop_weights, test);
print("----------------------")

print("test1 Original")
print("----------------------")
test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
seven_segment(test);
print("----------------------")


print("test2")
print("----------------------")
test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
HopfieldNetworkApplied(hop_weights, test);
print("----------------------")

print("test2 Original")
print("----------------------")
test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
seven_segment(test);
print("----------------------")

# print("test2")
#
# #here the network should run printing at each step
#
#
# HopfieldNetworkApplied(hop_weights,test)
#
# print("Test 2 original")
# seven_segment(test)

#here the network should run printing at each step

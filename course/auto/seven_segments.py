from math import *


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



    pattern_b=map(to_bool,pattern) # applies the to_bool function over the pattern array

    hor(pattern_b[0]) # horizontal rows
    vert(pattern_b[1],pattern_b[2],pattern_b[3]) #vertical row 1
    vert(pattern_b[4],pattern_b[5],pattern_b[6]) #vertical row 2

    number=0
    for i in range(0,4):
        if pattern_b[7+i]: # look at the number (0 = tru?)
            number+=pow(2,i) # binary
    print(int(number))



six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

print("-------------")
seven_segment(three)
print("-------------")
seven_segment(six)
print("-------------")
seven_segment(one)
print("-------------")

print("Hopfield Three")
HopfieldNetwork(three)


print("-------------")
print("test1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

seven_segment(test)

print("-------------")
print("test2")

#here the network should run printing at each step

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]

seven_segment(test)

#here the network should run printing at each step

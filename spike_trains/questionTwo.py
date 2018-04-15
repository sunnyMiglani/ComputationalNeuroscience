import numpy as np

def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array


# ######## Steps ##############
#
#  Step for finding the fano factor,
#  first step is to take the fact that it comes in the function as binary which
#  means that we must create the list of the time intervals between each spike
#
#  This can be done quite simply, by taking the fact that we know it's a 2
#  ms gap between the values, which means we just see when the next 1 shows up
#  and multiply the number of 0s in between to see how many MS b/w them.
#
#  Once we've done that, we can simply use the same fanofactor formulae to
#  get the values we want
#
#  #############################

def getTimeIntervals(binary_list):
    listOfTimeIntervals = []
    ms = 0.001;
    time_dif = 2*ms;
    counter_mid = 0;
    found = False;
    for ind in range(0,len(binary_list)):
        this_val = binary_list[ind];
        if(this_val == 1):
            new_val = 0
            while(new_val != 1 and ind+1 < len(binary_list)):
                counter_mid+=1; # increment distance between indices.
                ind+=1; # increment the counter
                new_val = binary_list[ind]
                found = True;
            if(found):
                listOfTimeIntervals.append(time_dif * counter_mid);
                # print("Found a value! the number of mids : {0}".format(counter_mid));
                counter_mid = 0;
                found = False;

    if(len(listOfTimeIntervals) == 0): print("Problem! There is something wrong\
    in the time interval checks");
    return listOfTimeIntervals;


def findFanoFactor(spikes_binary):
    # First get the list of time intervals
    time_intervals = getTimeIntervals(spikes_binary)
    # Now we follow the steps on finding the fino factor


    ## Step 1: Split into the three main window sizes
    ms = 0.001
    limOne = 10*ms
    limTwo = 50*ms
    limThree = 100*ms

    listOne = []
    listTwo = []
    listThree = []

    for ind in (range(0,len(time_intervals))):
        val = time_intervals[ind];
        if(val > 0 and val <= limOne ):
            listOne.append(val)
        elif(val > limOne and val <= limTwo):
            listTwo.append(val)
        elif(val > limTwo):
            listThree.append(val)

    ## Step 2: Now calculate the coefficient of each of these windows

    coefficient_ofOnes = np.var(listOne) / np.mean(listOne)
    coefficient_ofTwos = np.var(listTwo) / np.mean(listTwo)
    coefficient_ofThrees = np.var(listThree) / np.mean(listThree)

    ## Step 3: Calculatet he fanoFactor of these three windows again
    ## Step 3 is WRONG

    fano_Ones = np.var(listOne)/ np.mean(listOne)
    fano_Twos = np.var(listTwo) / np.mean(listTwo)
    fano_Threes = np.var(listThree) / np.mean(listThree)

    ## Results :

    print("Window Size of 10ms : FanoFactor {0}\n Coefficient {1}".format(fano_Ones,coefficient_ofOnes));
    print("Window Size of 50ms : FanoFactor {0}\n Coefficient {1}".format(fano_Twos,coefficient_ofTwos));
    print("Window Size of 100ms : FanoFactor {0}\n Coefficient {1}".format(fano_Threes,coefficient_ofThrees));





#spikes=[int(x) for x in load_data("rho.dat")]
spikes=load_data("rho.dat",int)

print(len(spikes))
print(spikes[0:100])

findFanoFactor(spikes);

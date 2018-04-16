import numpy as np

def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array

def getTimeIntervalsFromIndex(binary_list):
    listOfTimeIntervals = []
    ms = 0.001;
    time_dif = 2*ms;
    for ind in range(0,len(binary_list)):
        if(binary_list[ind] == 1):
            listOfTimeIntervals.append((ind) * time_dif);

    return listOfTimeIntervals;


def calculateVarianceOfIntervals(this_train, shouldReturnIntervals=False):
    len_train = len(this_train);
    list_intervals = []
    for ind in range(0,len_train -1):
        a_val = this_train[ind]; # take two spikes and find the difference
        b_val = this_train[ind+1];
        list_intervals.append( b_val - a_val ); # difference = interval between spikes.

    varianceOfIntervals = np.var(list_intervals); ## calculates the variance of the intervals
    if(shouldReturnIntervals):
        return varianceOfIntervals, list_intervals;

    return varianceOfIntervals

def fanoHelper(this_train, windowSize):

    listCount = []
    currentTime = windowSize;
    currentCount = 0;

    for spikeTime in this_train:
        if (spikeTime > currentTime):
            listCount.append(currentCount);
            currentTime += windowSize;
            while (spikeTime > currentTime):
                listCount.append(0)
                currentTime += windowSize;
            currentCount = 1;

        else:
            currentCount += 1;
    listCount.append(currentCount);
    return listCount;


def findFanoFactor(spikes_binary):
    # First get the list of time intervals
    time_intervals = getTimeIntervalsFromIndex(spikes_binary)
    # Now we follow the steps on finding the fino factor



    ## Step 1: Split into the three main window sizes
    ms = 0.001
    limOne = 10*ms
    limTwo = 50*ms
    limThree = 100*ms

    listOneCount = fanoHelper(time_intervals, limOne);
    listTwoCount = fanoHelper(time_intervals, limTwo);
    listThreeCount = fanoHelper(time_intervals, limThree);

    _ , listOne  = calculateVarianceOfIntervals(time_intervals,True);



    ## Step 2: Now calculate the coefficient of each of these windows

    coefficient_ofOnes = np.std(listOne) / np.mean(listOne)

    ## Step 3: Calculatet he fanoFactor of these three windows again

    fano_Ones = np.var(listOneCount)/ np.mean(listOneCount)
    fano_Twos = np.var(listTwoCount) / np.mean(listTwoCount)
    fano_Threes = np.var(listThreeCount) / np.mean(listThreeCount)

    ## Results :

    print("Window Size of 10ms : FanoFactor {0}\n".format(fano_Ones));
    print("Window Size of 50ms : FanoFactor {0}\n".format(fano_Twos));
    print("Window Size of 100ms : FanoFactor {0}\n".format(fano_Threes));

    print("Coefficient of variation : {0}\n".format(coefficient_ofOnes));




#spikes=[int(x) for x in load_data("rho.dat")]
spikes=load_data("rho.dat",int)

# print(spikes[0:100])

findFanoFactor(spikes);

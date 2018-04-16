import random as rnd
import numpy as np

def get_spike_train(rate,big_t,tau_ref):

    if 1<=rate*tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []


    exp_rate=rate/(1-tau_ref*rate)

    spike_train=[]

    t=rnd.expovariate(exp_rate)

    while t< big_t:
        spike_train.append(t)
        t+=tau_ref+rnd.expovariate(exp_rate)

    return spike_train

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
    # print("sum(listcount) : {0}, len(this_train) : {1}, len(listcount) : {2}".format(sum(listCount), len(this_train), len(listCount)))
    return listCount;


def calculateFanoFactor(this_train, intervals_list):
    # Main aim is to find the std of the intervals, the mean of the intervals and follow
    # the formula for calculation of the fano factor.
    # c_v = variance / mean

    varianceOfIntervals = np.std(intervals_list)
    meanOfIntervals = np.mean(intervals_list);

    coefficientOfVariation = varianceOfIntervals / meanOfIntervals;

    ms = 0.001;

    listOneCount   = fanoHelper(this_train, 10*ms); ## ----------- THIS IS IN SECONDS, MUST BE IN MILLISECONDS ---------------------- ##
    listTwoCount   = fanoHelper(this_train, 50*ms);
    listThreeCount = fanoHelper(this_train, 100*ms);

    print ("variance : {0}, mean : {1} for listOne ".format(np.var(listOneCount), np.mean(listOneCount)))

    fano_Ones = (np.var(listOneCount)) / np.mean(listOneCount)
    fano_Twos = (np.var(listTwoCount)) / np.mean(listTwoCount)
    fano_Threes = (np.var(listThreeCount)) / np.mean(listThreeCount)

# shahla.perween@edfenergy.com


    print("Window Size of 10ms : FanoFactor {0}\n".format(fano_Ones));
    print("Window Size of 50ms : FanoFactor {0}\n".format(fano_Twos));
    print("Window Size of 100ms : FanoFactor {0}\n".format(fano_Threes));

    print("Coefficient of Variance : {0}".format(coefficientOfVariation));


#######################################################################
 # This function takes the difference in the runtimes of the spike trains
 # and therefore calculates the intervals
#######################################################################
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


#####################
#
# Calculate the Fano factor of the spike count
# and coefficient of variation of the inter-spike interval for 1000 seconds of spike
# train with a firing rate of 35 Hz, both with no refractory period and with a
# refractory period of 5 ms.
#
# Fano factor the count should be
# performed over windows of width 10 ms, 50 ms and 100 ms
#
#####################

def solveQuestionOne():
    sec = 1.0;
    Hz = 1.0;
    #1000 seconds of spike
    time = 1000*sec;
    #firing rate of 35hz
    fire_rate = 35 * Hz;
    # refractory period of 0ms and 5ms
    ms = 0.001;
    refOne = 0*ms;
    refTwo = 5*ms;


    print("\n------First spike_train values----------\n")
    # the spike train for firing rate 35hz, with time = 1000s in total, and a refectory period of 0.
    firstTrain = get_spike_train(fire_rate, time, refOne);
    # print (firstTrain);
    print("Length of spike train : {0}".format(len(firstTrain)));

    # Next steps is to calculate the fano factor of the spike count.
    # and the variation of the inter-spike interval.

    # calculating a variation, is as simple as taking the list
    # then calculating the difference between each value
    ## saving this difference in a new list, and use numpy to calculate the
    ## variance of that list.
    firstVar, intervals_list  = calculateVarianceOfIntervals(firstTrain, True);

    # Calculating the Fano Factor of the spike count.
    calculateFanoFactor(firstTrain,intervals_list);


    # Now applying the same steps for part 2.
    print("\n------Second spike_train values----------\n")
    secondTrain = get_spike_train(fire_rate, time, refTwo); # using 5ms refectory period
    print("Length of spike train: {0}".format(len(secondTrain)));
    secondVar, intervals_list  = calculateVarianceOfIntervals(secondTrain, True);
    calculateFanoFactor(secondTrain, intervals_list);




Hz=1.0
sec=1.0
ms=0.001

rate=15.0 *Hz
tau_ref=5*ms

big_t=5*sec

spike_train=get_spike_train(rate,big_t,tau_ref)

# print(len(spike_train)/big_t)

# print(spike_train)
solveQuestionOne();

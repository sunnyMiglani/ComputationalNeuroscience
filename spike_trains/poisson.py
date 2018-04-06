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


def calculateFanoFactor(this_train, intervals_list):
    # Main aim is to find the std of the intervals, the mean of the intervals and follow
    # the formula for calculation of the fano factor.
    # c_v = variance / mean

    varianceOfIntervals = np.var(intervals_list)
    meanOfIntervals = np.mean(intervals_list);
    coefficientOfVariation = varianceOfIntervals / meanOfIntervals;

    ms = 0.001
    limOne = 10*ms
    limTwo = 50*ms
    limThree = 100*ms

    listOne = []
    listTwo = []
    listThree = []

    for ind in (range(0,len(intervals_list))):
        val = intervals_list[ind];
        if(val > 0 and val <= limOne ):
            listOne.append(val)
        elif(val > limOne and val <= limTwo):
            listTwo.append(val)
        elif(val > limTwo):
            listThree.append(val)


    coefficient_ofOnes = np.var(listOne) / np.mean(listOne)
    coefficient_ofTwos = np.var(listTwo) / np.mean(listTwo)
    coefficient_ofThrees = np.var(listThree) / np.mean(listThree)

    fano_Ones = np.var(listOne)**2 / np.mean(listOne)
    fano_Twos = np.var(listTwo)**2 / np.mean(listTwo)
    fano_Threes = np.var(listThree)**2 / np.mean(listThree)

    print("Window Size of 10ms : FanoFactor {0}\n Coefficient {1}".format(fano_Ones,coefficient_ofOnes));
    print("Window Size of 50ms : FanoFactor {0}\n Coefficient {1}".format(fano_Twos,coefficient_ofTwos));
    print("Window Size of 100ms : FanoFactor {0}\n Coefficient {1}".format(fano_Threes,coefficient_ofThrees));



def calculateVarianceOfIntervals(this_train, shouldReturnIntervals=False):
    len_train = len(this_train);
    list_intervals = []
    for ind in range(0,len_train -1):
        a_val = this_train[ind];
        b_val = this_train[ind+1];
        list_intervals.append( b_val-a_val );

    varianceOfIntervals = np.var(list_intervals);
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
    #1000 seconds of spike
    time = 1000;
    #firing rate of 35hz
    fire_rate = 35;
    # refractory period of 0ms and 5ms
    ms = 0.001;
    refOne = 0;
    refTwo = 5*ms;

    # Windows of 10, 50 and 100 ms
    wind_one = 10*ms;
    wind_two = 50*ms;
    wind_three = 100*ms;

    # the spike train for firing rate 35hz, with time = 1000s in total, and a refectory period of 0.
    firstTrain = get_spike_train(fire_rate, time, refOne);
    # print (firstTrain);
    print("Length : {0}".format(len(firstTrain)));

    # Next steps is to calculate the fano factor of the spike count.
    # and the variation of the inter-spike interval.

    # calculating a variation, is as simple as taking the list
    # then calculating the difference between each value
    ## saving this difference in a new list, and use numpy to calculate the
    ## variance of that list.
    firstVar, intervals_list  = calculateVarianceOfIntervals(firstTrain, True);
    print("Variance in intervals : {0}".format(firstVar));

    # Calculating the Fano Factor of the spike count.
    # Fano Factor is defined with the use of intervals.
    ## you divide the spike-train into intervals and work out the spike count for each interval.
    # First interval is 10ms.
    calculateFanoFactor(firstTrain,intervals_list);


    # Now applying the same steps for part 2.
    print("\n------Second spike_train values----------\n")
    secondTrain = get_spike_train(fire_rate, time, refTwo); # using 5ms refectory period
    print("Length: {0}".format(len(secondTrain)));
    secondVar, intervals_list  = calculateVarianceOfIntervals(secondTrain, True);
    print("Variance in intervals : {0}".format(secondVar));
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

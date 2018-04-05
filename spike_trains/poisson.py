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


def calculateFanoFactor(this_train, interval_size, intervals_list):
    # Main aim is to find the std of the intervals, the mean of the intervals and follow
    # the formula for calculation of the fano factor.
    # c_v = variance / mean

    varianceOfIntervals = np.var(intervals_list)
    meanOfIntervals = np.mean(intervals_list);

    coefficientOfVariation = varianceOfIntervals / meanOfIntervals;



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
    print (firstTrain);
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

    firstFanoFactor = calculateFanoFactor(firstTrain, wind_one, intervals_list);



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

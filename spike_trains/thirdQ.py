import numpy as np
import matplotlib.pyplot as plt

def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array



def calc(spikes,stimulus,windowSize):
    ms = 0.001;
    reverseInd = int(windowSize / (2*ms));
    stim = []

    for spike_ind in range(0,len(spikes)):
        spike = spikes[spike_ind];
        if(spike == 1):
            stim.append(stimulus[spike_ind - reverseInd]);

    return np.mean(stim);



def plotActivity(spikes,stimulus):
    ms = 0.001;
    time = 100*ms
    timeIntervals = 2*ms;

    avgs = []
    rangeOfTimes = np.arange(0*ms, 102*ms, 2*ms);
    for time in rangeOfTimes:
        t_avg = calc(spikes,stimulus,time);
        avgs.append(t_avg);

    plt.plot(rangeOfTimes, avgs);
    plt.scatter(rangeOfTimes, avgs, s= 7, color = "green");
    plt.xlabel('Time Intervals');
    plt.ylabel('Average Stimulus Value');
    plt.title("Plotting the Neural Activity");

    plt.show();




#spikes=[int(x) for x in load_data("rho.dat")]
spikes=load_data("rho.dat",int)

#stimulus=[float(x) for x in load_data("stim.dat")]
stimulus=load_data("stim.dat",float)

plotActivity(spikes,stimulus);

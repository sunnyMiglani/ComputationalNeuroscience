import numpy as np
import matplotlib.pyplot as plt

def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array



# ##### Steps for getting data to plot ############
# Basically loop through the list, 50 at a time
# anytime you see a one, take the corresponding value
# and average it
# Once the averages are over through the list
# that's the values needed to plot for the program
# ##################################################

def plotActivity(spikes,stimulus):
    ms = 0.001
    time = 100*ms
    timeIntervals = 2*ms;

    numNeededForAvg = time / timeIntervals;

    counter = 0;
    avgs_list = []
    thisAvgList = []
    for ind in range(0,len(spikes)): # for each spike, check if it's valid and add to mean
        this_spike = spikes[ind];
        counter+=1;
        if(this_spike == 1):
            thisAvgList.append(stimulus[ind]);
        if(counter >= numNeededForAvg):
            # print("Reset at {0}".format(ind));
            meanVal = np.mean(thisAvgList)
            counter = 0;
            avgs_list.append(meanVal);
            thisAvgList = [];


    plt.plot(range(0,len(avgs_list)), avgs_list, '-', color = "green");
    plt.scatter(range(0,len(avgs_list)), avgs_list, s= 5, color = "green");
    plt.title("Plotting the Neural Activity");

    plt.legend();
    plt.show();



#spikes=[int(x) for x in load_data("rho.dat")]
spikes=load_data("rho.dat",int)

#stimulus=[float(x) for x in load_data("stim.dat")]
stimulus=load_data("stim.dat",float)

print("hello");
plotActivity(spikes,stimulus);

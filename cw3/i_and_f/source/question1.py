import numpy as np;
import math;
import matplotlib.pyplot as plt;

'''
Aim is to simulate an integrate and fire neuron.
This model uses a system of equations to calculate whether a neuron spikes based
on a specific threshold value.

The following parameters have been set and defined:

timeConstant = 10ms;
E_l = -70mV;
resetVoltage = -70mV;
thresholdVoltage = -40mV;
R_m = 10 MOhm;
InputCurrent = 3.1 nA;
timesteps = 1ms;

The main formula used for the Integrate and fire model is this:

t_m V' = E_l - V + Rm*I

'''
## Defining units in the system


ms = 0.001;
mV = 0.001;

nA = 10**(-9);
MOhm = 10**6;
s = 1;

def rhs_IandF(timeConstant, E_l, Voltage, R_m, I):
    value = E_l - Voltage + (R_m*I);
    value = value/timeConstant;
    return value;

def IandFModel():
    timeConstant = 10 * ms;
    E_l = -70 * mV;
    resetVoltage = -70 * mV;
    thresholdVoltage = -40 * mV;
    R_m = 10 * MOhm;
    InputCurrent = 3.1 * nA;
    timesteps = 1 * ms;

    print("Units -> ms : {0}, mV : {1}, nA : {2}, MOhm : {3}".format(ms,mV,nA,MOhm));

    v_0 = resetVoltage;
    listOfVoltages = []


    numberOfSteps =  math.ceil(s/ms); ## 1 second, 1ms each timestep.
    print("Number of steps : {0}".format(numberOfSteps));
    for ind in range(0,numberOfSteps):
        v_1 = v_0  + (timesteps * rhs_IandF(timeConstant, E_l, v_0, R_m, InputCurrent));
        listOfVoltages.append(v_1);
        if(v_1  > thresholdVoltage):
            v_1 = resetVoltage;
        v_0 = v_1;

    # print(listOfVoltages);
    plt.plot(range(0,numberOfSteps),listOfVoltages,'g');
    plt.scatter(range(0,numberOfSteps),listOfVoltages, s=3);
    plt.title("Plot of Voltage against time.");
    plt.xlabel("Timesteps (ms)");
    plt.ylabel("Voltage (mV)");
    plt.show();


IandFModel();

## Run
import numpy as np;
import math;
import matplotlib.pyplot as plt;
import random

ms = 0.001;
mV = 0.001;

nA = 10**(-9);
MOhm = 10**6;
s = 1;


'''

E_l - V + Rm*I
Eₗ - Vₐ + Rₘ * Iₑ + gₛ * (Eₛ - Vₐ)

'''
def rhs_IandF(timeConstant, E_l, Voltage, R_m, I, g_s, E_s):
    value = E_l - Voltage + (R_m*I) + (g_s * (E_s - Voltage));
    value = value/timeConstant;
    return value;

def getGsValue(timeConstant, s_val,):
    this_sval = (-s_val / timeConstant);
    print ("s : {0}, time  : {1}".format(s_val,timeConstant));

    return this_sval;

def neuronLoops(E_s_Val):
    timeConstant = 10 * ms;
    E_l = -70 * mV;
    resetVoltage = -70 * mV;
    thresholdVoltage = -40 * mV;
    R_m = 10 * MOhm;
    InputCurrent = 3.1 * nA;
    timesteps = 1 * ms;

    E_s = E_s_Val * mV;
    RmGs = 0.15;

    P = 0.5;

    print("Units -> ms : {0}, mV : {1}, nA : {2}, MOhm : {3}".format(ms,mV,nA,MOhm));

    neuronA_v_0 = random.uniform(resetVoltage, thresholdVoltage);
    neuronB_v_0 = random.uniform(resetVoltage, thresholdVoltage);
    while(neuronB_v_0 == neuronA_v_0):
        neuronB_v_0 = random.uniform(resetVoltage, thresholdVoltage);

    neuronA_listOfVoltages = []
    neuronB_listOfVoltages = []

    neuronA_sval = 1;
    neuronB_sval = 1;



    numberOfSteps =  math.ceil(s/ms); ## 1 second, 1ms each timestep.
    print("Number of steps : {0}".format(numberOfSteps));
    for ind in range(0,numberOfSteps):

        print("neuronA : {0}".format(neuronA_sval));
        if(neuronA_sval == math.inf): break;

        neuronA_sval = neuronA_sval + (timesteps *  getGsValue(timesteps,neuronA_sval));
        neuronB_sval = neuronB_sval + (timesteps *  getGsValue(timesteps,neuronB_sval))


        neuronA_v_1 = neuronA_v_0  + (timesteps * rhs_IandF(timeConstant, E_l, neuronA_v_0, R_m, InputCurrent, neuronA_sval, E_s));
        print ("neuronA_v_1 : {0}".format(neuronA_v_1));
        if(neuronA_v_1  > thresholdVoltage):
            neuronA_v_1 = resetVoltage;
            neuronB_sval += P;

        neuronA_listOfVoltages.append(neuronA_v_1);

        neuronB_v_1 = neuronB_v_0 + (timesteps * rhs_IandF(timeConstant, E_l, neuronB_v_0, R_m, InputCurrent, neuronB_sval, E_s));
        if(neuronB_v_1  > thresholdVoltage):
            neuronB_v_1 = resetVoltage;
            neuronA_sval += P;
        neuronB_listOfVoltages.append(neuronB_v_1);

        neuronA_v_0 = neuronA_v_1;
        neuronB_v_0 = neuronB_v_1;

        neuronA_sval = neuronA_sval;
        neuronB_sval = neuronB_sval;

    plt.plot(range(0,numberOfSteps),neuronA_listOfVoltages,'g');
    plt.plot(range(0,numberOfSteps),neuronB_listOfVoltages,'r');
    plt.title("Plot of Voltage against time.");
    plt.xlabel("Timesteps (ms)");
    plt.ylabel("Voltage (mV)");
    plt.show();


neuronLoops(0);
neuronLoops(-80);

import numpy as np;

'''
Aim is to simulate an integrate and fire neuron.
This model uses a system of equations to calculate whether a neuron spikes based
on a specific threshold value.

The following parameters have been set and defined:

timeConstant = 10ms;
E_l = -70mV;
resetVoltage = -70mV;
thresholdVoltage = =40mV;
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
mOhm = 10**6;

## Run

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

def getGsValue(timeConstant, s_val, ):
    this_sval = (-s_val / timeConstant);


    return;

def neuronLoops():
    timeConstant = 10 * ms;
    E_l = -70 * mV;
    resetVoltage = -70 * mV;
    thresholdVoltage = -40 * mV;
    R_m = 10 * MOhm;
    InputCurrent = 3.1 * nA;
    timesteps = 1 * ms;

    E_s = 0*mV;

    P = 0.5;

    print("Units -> ms : {0}, mV : {1}, nA : {2}, MOhm : {3}".format(ms,mV,nA,MOhm));

    neuronA_v_0 = random.uniform(resetVoltage, thresholdVoltage);
    neuronB_v_0 = random.uniform(resetVoltage, thresholdVoltage);
    while(neuronB_v_0 != neuronA_v_0):
        neuronB_v_0 = random.uniform(resetVoltage, thresholdVoltage);

    neuronA_listOfVoltages = []
    neuronB_listOfVoltages = []

    neuronA_sval = 0;
    neuronB_sval = 0;



    numberOfSteps =  math.ceil(s/ms); ## 1 second, 1ms each timestep.
    print("Number of steps : {0}".format(numberOfSteps));
    for ind in range(0,numberOfSteps):

        neuronA_sval = getGsValue(timeConstant,neuronA_sval);
        neuronB_sval = getGsValue(timeConstant,neuronB_sval);


        neuronA_v_1 = neuronA_v_0  + (timesteps * rhs_IandF(timeConstant, E_l, neuronA_v_0, R_m, InputCurrent, neuronA_sval, E_s));
        listOfVoltages.append(neuronA_v_1);
        if(neuronA_v_1  > thresholdVoltage):
            neuronA_v_1 = resetVoltage;
            neuronB_sval += P;


        neuronB_v_1 = neuronB_v_0 + (timesteps * rhs_IandF(timeConstant, E_l, neuronB_v_0, R_m, InputCurrent, neuronB_sval, E_s));
        listOfVoltages.append(neuronB_v_1);
        if(neuronB_v_1  > thresholdVoltage):
            neuronB_v_1 = resetVoltage;
            neuronA_sval += P;

        neuronA_v_0 = neuronA_v_1;
        neuronB_v_0 = neuronB_v_1;

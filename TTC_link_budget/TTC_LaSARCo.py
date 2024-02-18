#This file explains the detailed procedure and link budget of the TT&C subsystem.

import math

def dB2dBm(dB):
    P = 10**(dB/10) #in W
    dBm = 10*math.log10(P/1e-3)
    return dBm
 


def dBm2dB(dBm):
    P = 10**(dBm/10)*1e-3 #in W
    dB = 10*math.log10(P)
    return dB



def W2dBm(W):
    dBm = 10*math.log10(W/1e-3)
    return dBm

# Parameters

bandwidth = 250 #MHz 

# Distance
d = 700000 #m Distance 

# Frequency
f =  25500 #MHz

# Boltzmann`s constant 
k = 1.38e-23 

#Antennas  type:Ka-BAND ANTENNA https://www.miwv.com/horn-lens-antennas/
antennasGain = 33 #dBi 
antennasTemperature = 290 #K

#Transceiver  type:Ka-BAND TRANSCEIVER  https://satsearch.co/products/tui-swift-xtrx
transmittingPower = 35 #dbm  35dbm 
cableLoss = 1 #dB usually 0.5dB/km 
receiverGain = 16 #dB #
receiverLoss = 3 #dB
receiverTemperature = 410 #K


# Link Budget Analysis

EIRP = dBm2dB(transmittingPower) - cableLoss + antennasGain #in dB

# Receiver power
receiverPower = dBm2dB(dB2dBm(EIRP) - (20*math.log10(d) + 20*math.log10(f*1e6) - 147.5) + dB2dBm(receiverGain - receiverLoss)) #in dBm

# Noise power
receiverNoise = dBm2dB(W2dBm(k * (antennasTemperature + receiverTemperature) * bandwidth * 1e6)) #in dBm
SNR = receiverPower - receiverNoise # dB



# Result of Link Budget Analysis

print("SNR=", SNR, "dB")
print("Receiver Power=", receiverPower, "dB")
print("Receiver Noise=", receiverNoise, "dB")





IS = IE2 = IC2 = 5e-3
V0 = 12
VR = 5.6
hfe = 407
IC_max = 80e-3
VI_max = 15
VBE = 0.7

Rs = (V0 - VR) / IS
IB2 = IC2 / hfe
I1 = hfe * IB2
V2 = VR + VBE
R1 = V2 / I1
IB1 = (IC_max + I1 + IS) / hfe
I = IB1 + IC2
R3 = (VI_max - (VBE + V0)) / I
RL_min = 12 / IC_max

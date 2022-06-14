# --------------------------------------------------------
# File plot_demux_output.py
# Written by L. Ravera (IRAP) on mai 16 2022
#
# This function simulates a 7 keV pulse on a LPA2.5a pixel
# and plots an estimate of the corresponding data at 
# DEMUX output.
# --------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------
# Definition of constants

# Trise / Tfall at L for LPA2.5A pixel
taurise=96.8e-6
taufall=796e-6

# Modulation depth for a 7 keV photon
modulation_depth = 0.65

# Baseline level
nbits = 16
FSR = 2**nbits
margin = 0.05 # Pour ne pas coller la baseline au FSR
baseline_lvl = FSR*(1-margin)

# --------------------------------------------------------
# Computation of the DEMUX output signal

# Sampling frequency
Fframe = 125e6/(20*34)
print("Fframe: {0:6.3f} kHz".format(Fframe/1e3))

# Time array with the correct sampling frequency (Fframe)
npts = 4096
t=np.arange(npts)/Fframe

pulse=np.zeros(len(t))
i1=200  # pour ne pas commencer le pulse directement à t=0
pulse[i1:]=np.exp(-t[:-i1]/taurise)-np.exp(-t[:-i1]/taufall)
pulse_height = pulse.max()-pulse.min()
signal = baseline_lvl * (1 + modulation_depth * pulse / pulse_height)

# --------------------------------------------------------
# Doing the plot

fig=plt.figure(1,(7,5))
ax=fig.add_subplot(1,1,1)

c='slategrey'
# Signal
ax.plot(t*1e3, signal, linewidth=3, color=c)
# Baseline indicator
ax.plot([0,10], [baseline_lvl, baseline_lvl], '--k', linewidth=1)
ax.text(2.5, baseline_lvl+1000, 'baseline (~95% of FSR)', color='k', horizontalalignment='center', rotation='horizontal')
# Pic of the pulse
ax.plot([0.5,2.8], [signal.min(), signal.min()], '-k', linewidth=1)
ax.set_xlabel('Time (ms)')
ax.set_ylabel('DEMUX output (ADU)')
ax.set_xlim(0, 5)
ax.set_ylim(0, FSR)

ax.arrow(4.5, FSR/2, 0, FSR/2, 
        length_includes_head=True, head_width=0.1, head_length=2000, 
        width=0.01, fc='k', ec='k')
ax.arrow(4.5, FSR/2, 0, -FSR/2, 
        length_includes_head=True, head_width=0.1, head_length=2000, 
        width=0.01, fc='k', ec='k')
ax.text(4.5-0.2, FSR/2, 'FSR', color='k', verticalalignment='center', rotation='vertical')

ax.arrow(2.5, baseline_lvl, 0, -baseline_lvl*modulation_depth, 
        length_includes_head=True, head_width=0.1, head_length=2000, 
        width=0.01, fc='k', ec='k')
ax.text(2.5-0.2, baseline_lvl * (1 - modulation_depth/2), 'Modulation depth', color='k', verticalalignment='center', rotation='vertical')

fig.tight_layout()
plt.savefig('demux_out.png', dpi=300, bbox_inches='tight')

# --------------------------------------------------------
# Exporting the data in a text file
filename = "demux_out.txt"
fout = open(filename, 'w')
for line in range(len(signal)):
    fout.write(str(int(signal[line]))+"\n")
fout.close()

# --------------------------------------------------------

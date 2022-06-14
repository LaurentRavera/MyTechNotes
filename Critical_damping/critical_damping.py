import numpy as np
import matplotlib.pyplot as plt
from pylab import Arrow, gca, sys
from matplotlib import rc

#rc('text', usetex=True)
#rc('font', family='serif')

DPIVAL = 600
ftsz = 24   # fontsize
ftsz2 = 24   # fontsize

fs=1e6
duration=5e-3
npts=fs*duration
t=np.arange(npts)*duration/npts

# to specify ticks sizes
def set_ticks():
    frame = gca()
    for xlabel_i in frame.axes.get_xticklabels():
        xlabel_i.set_fontsize(24.0)
    for xlabel_i in frame.axes.get_yticklabels():
        xlabel_i.set_fontsize(24.0)

T=0.6e6
taucrit=286e-6
pulse=18+T*(t*np.exp(-t/taucrit))

fig = plt.figure(figsize=(14, 8))

ax1 = fig.add_subplot(1,1,1)
ax1.plot(1e3*t, pulse, linewidth=3)
ax1.set_xlabel(R'time (ms)', fontsize=ftsz)
ax1.set_ylabel(R'Resistance (m$\Omega$)', fontsize=ftsz)
set_ticks()

#fig.tight_layout()

#plt.savefig('Pulse.png', bbox_inches='tight')
plt.savefig('Pulse.png')

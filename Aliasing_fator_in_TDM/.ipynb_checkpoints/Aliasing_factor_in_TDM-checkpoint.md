# Aliaising factor in TDM

In TDM we have:

$$t_{frame}=N_{mux}t_{row}$$

With:
- $t_{row}$: the row period (i.e. time spend to read a TES)
- $t_{frame}$: the frame period (i.e. time required to read a column)
- $N_{mux}$: the multiplexing fator (i.e. number of pixels per column)

In order to reduce the cross-talk between successive pixels the bandwidth of the system shall be high enough. In other words, the time constant $\tau$ of the signal shall be much lower than $t_{row}$. Empirically an optimised setting seems to be [Doriese 2006]:

$$t_{row}=2\pi\tau$$

![title](images/row.png)

The cut-off frequency of the system is then:

$$f_c=1/(2\pi\tau)=1/t_{row}$$

Also:

$$t_{frame}=2\pi N_{mux}\tau$$

The ADC samples the white noise of the amplification chain, which lies between DC and $fc$, at the frequency $f_{frame}$.

The aliasing factor is then:

$$\sqrt{f_c/f_{frame}}=\sqrt{t_{frame}/ (2\pi\tau)}=\sqrt{N_{mux}}$$
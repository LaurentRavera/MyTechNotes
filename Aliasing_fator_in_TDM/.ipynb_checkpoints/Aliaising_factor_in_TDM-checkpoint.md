# Aliaising factor in TDM

In TDM we have:

$$t_{frame}=N_{mux}t_{row}$$

With:
- $t_{row}$: the row period (i.e. time spend to read a TES)
- $t_{frame}$: the frame period (i.e. time required to read a column)
- $N_{mux}$: the multiplexing fator (i.e. number of pixels per column)

In order to reduce the cross-talk between successive pixels the bandwidth of the system shall be high enough. In other words, the time constant $\tau$ of the signal shall be much lower than $t_{row}$. Empirically an optimised setting seems to be [Doriese 2006]:

$$\tau=\frac{t_{row}}{2\pi}$$

We have then:

$$\tau=\frac{t_{frame}}{2\pi N_{mux}}=\frac{1}{2\pi N_{mux}f_{frame}}$$

![title](images/row.png)

Ideally we would sample the signal at the frequency $f_s=ENB/2$ where $ENB$ is the Equivalent Noise Bandwidth.
In reality this is not possible and we sample the signal at the frequency $f_{frame}$.

Assuming a first order low pass filter we have (![see this note](../ENB/ENB_order1.md)):

$$ENB=\frac{1}{4\tau}=\frac{\pi N_{mux}f_{frame}}{2}$$

And the signal is aliased by the following factor:

$$A_F=\sqrt{\frac{ENB}{f_{frame}/2}}=\sqrt{\pi N_{mux}}$$

----

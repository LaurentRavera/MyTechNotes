# Setting of kmix

${E(n)}$ and ${FB(n)}$ are respectively the error and the feedback signals at the Mux SQUID interfaces. $\widehat{E(n)}$ and $\widehat{FB(n)}$ are respectively the error and the feedback signals in the firmware. $G_{FW}$ and $G_{FB}$ are respectively the gains in the forward and the feedback paths. $ki$ is the loop gain. $\widehat{ki}$ is the contribution of the firmware to the loopgain ($ki=G_{FW}G_{FB}\widehat{ki}$). $\widehat{kmix}$ is the "mixing" gain parameter in the firmware which allows to compute the science output signal from the feedback and the error signals.

At Mux SQUID we have:

$$TES(n)=FB(n)+E(n)$$

with:

$$FB(n+1)=ki E(n) = G_{FW} G_{FB} \widehat{ki}E(n)$$

To set the loop gain to 1 we need to have:

$$\widehat{ki}=\widehat{ki_1}=\frac{1}{G_{FW}G_{FB}}$$

In the firmware we compute:

$$\widehat{Sc(n)}=\widehat{FB(n)} + \widehat{kmix}\widehat{E(n)}$$

Which corresponds to:

$$\widehat{Sc(n)}=\frac{FB(n)}{G_{FB}} + \widehat{kmix}G_{FW}E(n)$$
Then to have $\widehat{Sc(n)}$ proportionnal to $TES(n)$ we need to have:

$$\frac{1}{G_{FB}}=\widehat{kmix}G_{FW} \Longleftrightarrow \widehat{kmix}=\frac{1}{G_{FW}G_{FB}}=\widehat{ki_1}$$
This means that the correct setting of $\widehat{kmix}$ corresponds to $\widehat{ki_1}$ which is the setting of $ki$ for a loop gain of 1.
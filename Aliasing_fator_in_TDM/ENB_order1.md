# Effective Noise Bandwidth (ENB) of a first order low pass filter

The transfer function of a first order filter with a time constant $\tau$ is:

$$TF(f)=\frac{1}{1+2\pi j f \tau}$$

And its module is:

$$H(f)=\frac{1}{\sqrt{1+(2\pi f\tau)^2}}$$

If we have a white noise with a noise spectral density $e_{in}$ at the filter input, the $rms$ of the noise at the output is:

$$rms(e_{out})=\sqrt{\int_0^\infty{e_{in}^2 H(f)^2 df}}$$

$$\Rightarrow rms(e_{out})=e_{in}\sqrt{\frac{1}{2\pi\tau}\int_0^\infty{\frac{df}{\sqrt{1+f^2}}}}$$

$$\Rightarrow rms(e_{out})=e_{in}\sqrt{\frac{1}{2\pi\tau}\big[\arctan(x)\big]^{\infty}_0}$$

$$\Rightarrow rms(e_{out})=e_{in}\sqrt{\frac{\pi/2}{2\pi\tau}}$$

$$\Rightarrow rms(e_{out})=\frac{e_{in}}{\sqrt{4\tau}}$$

Which means that the $ENB$ is equal to $1/(4\tau)$. 

----
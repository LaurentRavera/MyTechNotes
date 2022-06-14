# Temperature drift requirements

In X-IFU IRD version 4 the DRE temperature stability requirement is expressed as follows:
0.06 K rms on [0.5 mHz - 500 Hz].
This corresponds to a linear drift of 0.2 K over 2000 s.

Indeed, for a linear drift with a slope A, the rms is:

$$rms=\sqrt{\frac{1}{2T}\int_{-T}^T{(At)^2.dt}}=\sqrt{\frac{1}{2T}\left[\frac{A^2}{3}.T^3\right]_{-T}^T}=\frac{AT}{\sqrt{3}}$$

If D is the total drift, we have

$D=2AT$ and $rms=\frac{D}{\sqrt{12}}$

Then a rms of 0.06K on [0.5mHz - 500Hz] corresponds to a linear drift of 

$$0.06\times \sqrt{12}=0.2\textrm{ K}$$ 

over

$$\frac{1}{0.5\textrm{ mHz}}=2000\textrm{ s}$$.

----

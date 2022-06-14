# Bruit de quantification d'un ADC et d'un DAC

## Le rapport signal sur bruit

>Le ***rapport signal sur bruit (SNR : Signal to Noise Ratio)*** d'un ADC ou d'un DAC est généralement exprimé comme le rapport des valeurs *rms* du signal sinusoïdal pleine échelle et du bruit de quantification.

Pour un DAC ou un ADC dont le pas de quantification est noté $q$ et le nombre de bits $N_b$, on a donc :

$$S=\frac{q\times 2^{N_b}}{2\sqrt{2}}$$

et

$$N=\frac{q}{\sqrt{12}}$$

On a alors :

$$SNR=\frac{2^{N_b}\sqrt{12}}{2\sqrt{2}}$$

Exprimé en $dB$ on a :

$$SNR_{dB}=20\log(2)N_b+20\log\left(1/2\sqrt{6}\right)$$

et on retrouve la formule connue [Data Conversion Handbook, Kester, 2004] :

>$$SNR_{dB}=6.02N_b+1.76$$

***Remarque :*** Pour certaines applications, en particulier quand les signaux traités ne sont pas des sinusoïdes, on peut préférer utiliser la valeur crète-à-crète du signal (c'est à dire la pleine échelle de l'ADC ou du DAC). Dans ce cas on a :

$$SNR=2^{N_b}\sqrt{12}$$

et en $dB$ :

$$SNR_{dB}=6.02N_b+10.79$$

## La dynamique spectrale de bruit

>La ***dynamique spectrale de bruit (DRD : Dynamic Range Density)*** d'un ADC ou d'un DAC est généralement exprimée comme le rapport de la valeur *rms* du signal sinusoïdal pleine échelle et de la densité spectrale de bruit de quantification.

Le densité spectrale de bruit s'obtient à partir de la valeur *rms* du bruit et de la largeur de bande du signal $B$. Pour un ADC ou un DAC on a $B=f_s/2$ et donc :

$$D=\frac{N}{\sqrt{f_{s}/2}}$$

On a donc :

$$DRD=\frac{SNR}{\sqrt{f_{s}/2}}=\frac{2^{N_b}\sqrt{12}}{2\sqrt{2}}\sqrt{f_s/2}$$

Et :

$$DRD_{dB.Hz}=6.02N_b+1.76+10\log(f_s/2)$$

***Remarque :*** Dans le cas ou on prends en compte la pleine échelle de l'ADC ou du DAC au lieu de la valeur *rms* on a :

$$DRD=2^{N_b}\sqrt{12}\sqrt{f_s/2}$$

Et :

$$DRD_{dB.Hz}=6.02N_b+10.79+10\log(f_s/2)$$

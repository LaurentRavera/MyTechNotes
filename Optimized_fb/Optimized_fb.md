# Feedback architectures

Traditionnal integrator feedback:

$\Phi_{FB}(n+1)=\Phi_{FB}(n)+K_i\times V_{Err}(n)$

OPtimized integrator feedback as proposed by Malcolm:

$\Phi_{FB}(n+1)=\Phi_{FB}(n)+K_i\times V_{Err}(n)+\Phi_{FB}^{'}(n)$
$\Phi_{FB}^{'}(n)=\Phi_{FB}^{'}(n-1)+\frac{K_i}{5}\times V_{Err}(n)$

Then we have:

$$\Phi_{FB}^{'}(n)=\frac{K_i}{5}\sum_{k=0}^{n-1}V_{Err}(k)$$

And:

$$\Phi_{FB}(n+1)=K_i\sum_{m=0}^{n}\left[V_{Err}(m)+\frac{1}{5}\sum_{k=0}^{m-1}V_{Err}(k)\right]$$

----

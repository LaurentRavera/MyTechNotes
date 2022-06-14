# Impact du bruit de quantification du DAC Feedback

## Définitions

J'utilise les notations suivantes :

- $E$ est le signal d'erreur dans le SQUID.
- $TES$ est le signal du TES en entrée du SQUID (celui que l'on veut mesurer).
- $FB$ est le signal de feedback calculé par le firmware.
- $OUT$ est le signal en sortie du firmware, on veut $OUT = TES$.
- $G_{FW}$ est le gain dans le "forward path" entre le MUX SQUID et le firmware TDM.
- $G_{FB}$  est le gain dans le "feedback path" entre le firmware TDM et le SQUID.
- $k_i$ est le gain du système en boucle ouverte.

Si on veut compenser exactement le signal d'erreur en une itération du TDM on choisit $k_i=1$. Dans la réalité on préfère sur-compenser et prendre $k_i>1$.

## 1) Cas où l'ADC, le firmware et le DAC sont parfaits (pas de quantification)

Au niveau du SQUID le signal d’erreur découle du signal du TES et du signal de feedback calculé depuis les données de l’itération précédente. On a donc :

$$E[n] = TES[n] - G_{FB} . FB[n-1]$$

Dans le firmware on va donc estimer le signal du TES en calculant :

$$OUT[n] = k_{mix} . E[n] + k_i . FB[n-1]$$

## 2) Cas où l'ADC et le firmware sont parfaits et le DAC est sur N bits

Le firmware va générer un signal de feedback "exact" $FB$ et la quantification du DAC va ajouter une erreur $Q$ à chaque itération :

$$FB’[n] = FB[n] + Q[n]$$

Le firmware va donc estimer le signal du TES en calculant :

$$OUT[n] = k_{mix} . \left(E[n] - Q[n-1]\right) + k_i . FB[n-1] $$

On retrouve donc du bruit de quantification dans la mesure.

## 3) Cas où l'ADC est parfait et le firmware et le DAC font une quantification sur N bits parfaite

Si le firmware réalise la même quantification que le DAC alors il va estimer le signal du TES en calculant :

$$OUT[n] = k_{mix} \left(E[n] - Q[n-1]\right) + k_i \left(FB[n-1] + Q[n-1]\right)$$

qui ne contient pas d'erreur de quantification si $k_i=k_{mix}$. Dans ce cas l'erreur de quantification faite par le firmware et le DAC est corrigée quand on prend en compte le signal d'erreur.

## 4) Dans la réalité

En pratique il semble difficile d'appliquer exactement le même type de quantification dans le firmware et dans le DAC : le DAC va apporter d'autres imperfections comme la DNL ou l'INL qui vont induire des écarts entre le feedback en sortie du DAC et le feedback dans le firmware de telle sorte que l'erreur ne sera probablement pas compensée.

----

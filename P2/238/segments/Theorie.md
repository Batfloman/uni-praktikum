## Leistungsanpassung
Wir betrachten folgenden Stromkreis
![[Abb 238.1.png]]

Wir schließen einen Widerstand an eine reale Spannungsquelle und betrachten dies komplex
Der Strom zu einem beliebigen Zeitpunkt muss über den Stromkreis erhalten bleiben
$$
I = I_L = I_Z
$$
mit dem ohmschen Gesetz $U = RI$ folgt:
$$
\frac{U_L}{Z_i + Z} = \frac{U}{Z}
$$
war wir zu Gleichung $(238.1)$ umformen können:
$$
U = \frac{Z}{Z_i + Z} \cdot U_L
\tag{238.1}
$$

Die Leistung lässt sich mit $P = U \cdot I$ berechnen (Herleitung mit Arbeit => Wegintegral über Coulombkraft). Hier betrachten wir Wechselströme also gilt:
$$
\begin{align*}
U(t) &= U_0 \cdot \exp(i\omega t) \\
I(t) &= I_0 \cdot \exp(i\omega t - i\varphi)
\end{align*}
$$
Setzen wir dies ein:
$$
\begin{align*}
P_S &= U_0 \cdot \exp(i\omega t) \cdot I_0 \cdot \exp(i\omega t - i\varphi) \\
&= U_0 \cdot I_0 \cdot \exp(i\varphi)
\end{align*}
$$

## Transformatorgleichung

## Betriebsverhalten Transformator
Induktivitäten $L_i$ proportional zum Quadrat der Windungszahlen $n_i$
Gegeninduktivität $M$ ist proportional zu $n_1 \cdot n_2$

### Magnetfluss
realer Magnetfluss "streut" sich
Dafür definieren wir den Streungsfaktor $\sigma$
$$
\sigma = 1 - \frac{M^2}{L_1 L_2}
$$
Ein minimaler Streuungsfaktor $\sigma = 0$ impliziert $M^2 = L_1 L_2$

### Verluste
Es gibt Kupfer/-Spulenverluste durch den ohmschen Widerstand $R_i$ der Spulen.
$$
P_{V,Cu} = R_1 \cdot I_1^2 + R_2 \cdot I_2^2
$$

## Impedanzmatrix

## Symmetrischer Transformator
Es gilt $L_1 = L_2$ und $R_1 = R_2$

## Zeigerdiagramm
Betrachten wir folgenden Aufbau
![[Abb 238.3.png]]

### rechter Teil
Dann gilt für den rechten Teil mit der Maschenregel:
$$
0 = U_{ind} + U_L + U_R
$$
Also
$$
0 = M_{1\to2} \cdot \dot{I_1} + L_2 \cdot \dot{I_2} + Z I_2  
$$
Formen wir dies zu
$$
0 = M \cdot i\omega I_1 + L_2 \cdot i\omega I_2 + R I_2  
$$
Wir fangen an und zeichnen einen Pfeil für $RI_2$. Dann senkrecht dazu einen Pfeil für $i\omega L_2 I_2$. Dann schließen wir das Dreieck durch den Pfeil für $i\omega MI_2$

### linker Teil
Hier gilt mit der Maschenregel
$$
U_1 = U_L + U_{ind}
$$
Also 
$$
U_1 = i\omega L_1I_1 + i\omega M I_2
$$
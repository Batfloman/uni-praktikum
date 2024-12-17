## Fadenstrahlrohr
### 242.a
Nur [[Praktikum/P2/242/segments/Durchführung|Durchführung]]
### 242.b
> [!Aufgabe]-
> 1. Erweitern Sie Gleichung 242.1 um einen Zusatzterm für eine störende magnetische Flussdichte 𝐵E. (𝐵S sei das durch die Spulen erzeugte Feld, 𝐵E die Komponente des Erdmagnetfeldes in Richtung von 𝐵S).
> 2. Eliminieren Sie 𝐵E mit den Messungen in beiden Orientierungen des Fadenstrahlrohrs und berechnen Sie 𝐵S aus den Spulendaten und dem Strom 𝐼.
> 3. Stellen Sie die Messdaten in einem Diagramm (𝑟 𝐼)2 gegen 𝑈 dar.
> 4. Bestimmen Sie mit Hilfe des Diagramms 𝑒/𝑚. Geben Sie 𝑒/𝑚 in C/kg an. 
> 5. Berechnen Sie die Größe von 𝐵E in Tesla.

> [!Aufgabe]
Erweitern Sie Gleichung 242.1 um einen Zusatzterm für eine störende magnetische Flussdichte 𝐵E. (𝐵S sei das durch die Spulen erzeugte Feld, 𝐵E die Komponente des Erdmagnetfeldes in Richtung von 𝐵S).

$$
F_L = e \cdot v \cdot B
\tag{242.1}
$$
Erweitern mit $B = B_S + B_E$
$$
F_L = e \cdot v \cdot \bb{B_S + B_E}
$$

> [!Aufgabe]
Eliminieren Sie $B_E$ mit den Messungen in beiden Orientierungen des Fadenstrahlrohrs und berechnen Sie $B_S$ aus den Spulendaten und dem Strom $I$.

Wir haben das externe Feld relativ zum Aufbau um $180^\circ$ gedreht, deshalb gilt:
$$
\vec{B}_{E,1} = -\vec{B}_{E,2}
$$
d.h. es gilt:
$$
\begin{align}
B_1 = B_{S,1} - B_{E} \\
B_2 = B_{S,2} + B_{E} \\
\end{align}
$$

Mit dem Biot-Savart Gesetz folgt Gleichung $(242.5)$ und damit ein **linearer Zusammenhang** von $B_S$ und $I$
$$
B_S = 0.716 \cdot \mu_0 \cdot \frac{n}{R} \cdot I
\tag{242.5}
$$
wobei $n$ die Windungszahl einer Spule und $R$ der Spulenradius ist.
Da wir $r$ und $U_B \Rightarrow v$ bei einer Messung konstant gehalten haben gilt:
$$
B_1 = B_2 
$$
Und somit 
$$
B_{S,1} - B_E = B_{S,2} + B_{E} 
$$
Wegen der Linearität von $B_{S}$ folgt für den Strom ohne Erdmagnetfeld
$$
I = \frac{1}{2} (I_2 + I_1)
$$


> [!Aufgabe]
Stellen Sie die Messdaten in einem Diagramm (𝑟 𝐼)2 gegen 𝑈 dar.

![[242b.png]]

> [!Aufgabe]
Bestimmen Sie mit Hilfe des Diagramms 𝑒/𝑚. Geben Sie 𝑒/𝑚 in C/kg an. 

es gilt:
$$
\frac{e}{m} = \frac{2}{r^2 B^2} U
\tag{242.4}
$$
mit Gleichung $(242.5)$ gilt:
$$
\frac{e}{m} = \frac{2 R^2}{\bb{0.716}^2 \mu_0^2 n^2} \frac{1}{r^2 I^2} U
$$
Dabei gilt $m_{graph} = \frac{r^{2}I^{2}}{U}$
somit folgt:
$$
\frac{e}{m} = \frac{2 R^2}{\bb{0.716}^2 \mu_0^2 n^2} \frac{1}{m_{graph}}
$$

> [!Aufgabe]
Berechnen Sie die Größe von 𝐵E in Tesla.

Auf der Kreisbahn gilt:
$$
\begin{align}
F_L &= F_{zp} \\
\Leftrightarrow e v B &= \frac{m v^2}{r} \\
\Leftrightarrow B &= \frac{m}{e} \frac{v}{r}
\end{align}
$$
Da wir $r$ und $U_B \Rightarrow v$ bei einer Messung konstant gehalten haben gilt:
$$
\begin{align}
B_1 &= B_2 \\
B_{S,1} + B_E &= B_{S,2} - B_E \\
2B_E &= B_{S,2} - B_{S,1} \\
B_E &= \frac{1}{2} \bb{ B_{S,2} - B_{S,1}} \\
\end{align}
$$

## Millikan Versuch
### 242.c - 242.f
Nur [[Praktikum/P2/242/segments/Durchführung|Durchführung]]
### 242.g
> [!Aufgabe]-
Näherungsweise Bestimmung der Gesamtladung auf den Tröpfchen und des Teilchenradius ohne Cunningham-Korrektur: Aus der Zimmertemperatur wird die Viskosität der Luft durch Interpolation der Werte in Tabelle 242.1 bestimmt. Dann wird mit den Gleichungen 242.8 und 242.9 die ungefähre Ladung 𝑞S,𝑖 und der Radius 𝑟𝑖 mit der unkorrigierten Stokesschen Viskositätsformel (d.h. mit 𝜂Luft anstatt mit 𝜂eff) aus den gemessenen Geschwindigkeiten für jedes Tröpfchen 𝑖 berechnet.

$$
r = \sqrt{ \frac{9\eta_{Luft} \bb{v_{\downarrow} - v_{\uparrow}}}{4g \bb{\rho_{Öl} - \rho{_{Luft}}}} }
\tag{242.8}
$$
$$
q_{S,i} = Ne = 3\pi \eta_{Luft} r \frac{v_{\downarrow}+v_{\uparrow}}{E}
$$
mit $E = \frac{U}{d}$
$$
q_{S,i} = 3\pi \eta_{Luft} (v_{\downarrow}+v_{\uparrow}) r \frac{d}{U}
$$
### 242.h
> [!Aufgabe]-
Bestimmung der Anzahl 𝑁𝑖 der Ladungen auf den Tröpfchen: Man suche den größten gemeinsamen Teiler für alle gefundenen Ladungen 𝑞S,𝑖. Damit kennt man die ganzahlige Anzahl 𝑁𝑖 der Elementarladungen auf jedem Teilchen und erhält so eine Reihe von ungefähren Werten 𝑒S,𝑖 = 𝑞S,𝑖/𝑁𝑖 für die Elementarladung. Tipp: Hierfür kann es nützlich sein, die Daten graphisch aufzutragen.
### 242.i
> [!Aufgabe]-
Anbringen der Cunningham-Korrektur: Aus den Gleichungen 242.8 und 242.9 kann man ableiten, dass die unkorrigierten Werte 𝑒S,𝑖 für die Elementarladungen mit dem korrigiertem Wert 𝑒0 durch 𝑒0 = 𝑒S,𝑖 ×  1 + 𝐴 𝑟𝑖 − 3 2 (242.11) verbunden sind. Umgestellt lautet Gleichung 242.11 (𝑒S,𝑖) 2 3 = (𝑒0) 2 3 ×  1 + 𝐴 𝑟𝑖  . (242.12) Ein Graph von (𝑒S,𝑖)2/3 gegen 1/𝑟𝑖 ergibt eine Gerade, aus deren Achsenabschnitt man die gesuchte Elementarladung 𝑒0 bestimmt. Der Graph bietet gleichzeitig eine augenfällige Kon- trolle, ob man die Anzahl 𝑁𝑖 auf den einzelnen Tröpfchen richtig bestimmt hat
### 242.j
> [!Aufgabe]-
Beweisen Sie Gleichung 242.11

$$
e_{0} = e_{S,i} \cdot \bb{1 + \frac{A}{r_{i}}}^{-\frac{3}{2}}
\tag{242.11}
$$

### 242.k
> [!Aufgabe]-
Berechnen Sie die Masse des Elektrons aus den bestimmten Fundamentalkonstanten $e/m$ und $e_0$.

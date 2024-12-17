### 238.a

### 238.b
> [!aufgabe]
Auswertung: Zeichnen Sie das Zeigerdiagramm für diese Schaltung. Berechnen Sie $P_S$ und $\cos\varphi$ (𝜑 = Phasenwinkel);

> [!Aufgabe]
Tragen Sie 𝑃W, 𝑃S und 𝑃S cos(𝜑) gegen $R$ auf. 
Es gilt $R = \frac{U_R}{I}$, $P_S = UI$, $\cos\varphi = \frac{U_R}{U}$

Für $R$ gilt:
$$
R = \frac{U}{I}
$$
Damit für den Fehler
$$
\Delta R 
= \sqrt{\bb{\pd{U}R \cdot \Delta U}^2 + \bb{\pd{I}R \cdot \Delta I}^2}
$$
mit
$$
\pd{U}R = \frac{1}{I} 
\quad \text{und} \quad
\pd{I}R = \frac{U}{I^2}
$$


Für $P_S$
$$
P_S = U \cdot I
$$
$\Delta P_S$
$$
\Delta P_S 
= \sqrt{\bb{\pd{U}P_S \cdot \Delta U}^2 + \bb{\pd{I}P_S \cdot \Delta I}^2} 
$$
mit
$$
\begin{align*}
\pd{U}P_S = I
\quad \text{und} \quad
\pd{I}P_S = U
\end{align*}
$$

Für $\cos\varphi$
$$
\cos\varphi = \frac{U_R}{U_B}
$$
Plotten wir dies:

![[238b.png]]

> [!Aufgabe]
Bestimmen Sie die maximale Leistung $P_{W,max}$ welche die Schaltung der Spannungsquelle entnehmen kann, und den entsprechenden Widerstand. Markieren Sie diese Werte in dem entsprechenden Diagramm

Nehmen wir an das die Spannungsquelle ideal ist und die Impedanz 
### 238.c
> [!aufgabe]
Legen Sie eine Tabelle für alle Messgrößen und für die durch Auswertung zu bestimmenden Größen 
Für die folgende Auswertung beachten Sie: Die in der Auswertungsanleitung angegebenen quantitativen Beziehungen sind teilweise Näherungen.  

> [!Aufgabe]
Füllen Sie die angefangene Tabelle vollständig aus (Berechnung von 𝑃S,2, etc.).
> * $P_{S,1} = U_1\cdot I_1$ Scheinleistung (primär)
> * $P_{S,2} = U_2 \cdot I_2$ Scheinleistung (sekundär)
> * $P_V = P_{W,1} − P_{W,2}$ Verlustleistung 
> * $P_{Cu} = R_1 I_2^2 + R_2 I_2^2$ Kupferverluste
> * $P_{Fe} = P_V - P_{Cu}$ Eisenverluste
> * $\eta = P_{W,2} - P_{W,1}$ Wirkungsgrad


> [!Aufgabe]
Tragen Sie die beiden Wirkleistungen $P_{W,1}$ und $P_{W,2}$, die Verlustleistungen $P_{Cu}, P_{Fe}$ sowie den Wirkungsgrad $\eta$ gegen $I_2$ auf.

![[238c_P.png]]

![[238c_PV.png]]

![[238c_eta.png]]

### 238.d
> [!Aufgabe]
Bestimmen Sie 𝜔𝐿 mit 3 unterschiedlichen Methoden. Leiten Sie die gegebenen Zusammen- hänge für die Bestimmung von 𝜔𝐿 aus den Gleichungen 238.26, 238.27 bzw. 238.28 her. 
> * aus dem gemessenen Betrag der Eingangsimpedanz im Leerlauf (𝑅 = ∞Ω): 𝜔𝐿 = 𝑈1/𝐼1
> * aus dem gemessenen Betrag der Eingangsimpedanz bei näherungsweise verlustfreiem Trafo (𝑅V = 0Ω und 𝜎 = 0) im Fall von 𝑈1/𝐼1 = 𝑅/√2: 𝜔𝐿 = 𝑅 
> * aus der gemessenen Stromübertragung bei vernachlässigbarem Streukoeffizienten (𝜎 = 0) im Fall von 𝐼2/𝐼1 = 1/√2: 𝜔𝐿 = 𝑅 + 𝑅V) 
> 
Vergleichen Sie die 3 Ergebnisse und diskutieren Sie die jeweiligen systematischen Messun- sicherheiten!
### 238.e
> [!Aufgabe]
Streukoeffizient: Bestimmen Sie 𝜎 = 1 − 𝑀2/𝐿2 mit folgenden 3 unterschiedlichen Methoden. Leiten Sie auch den jeweils angegeben Zusammenhang her. 
> * aus der gemessenen Stromübertragung im Kurzschlussfall (𝐼2/𝐼1 = 𝑀/𝐿 = √1 − 𝜎)
> * aus der gemessenen Spannungsübertragung im Leerlauf (𝑈2/𝑈1 = 𝑀/𝐿) 
> * aus den gemessenen Beträgen der Eingangsimpedanzen für Kurzschluss und Leerlauf: Verhältnis = 𝜎. Berücksichtgen Sie, dass 𝑅𝑣 ≪ 𝜔𝐿 gilt. 
> 
> Stellen Sie die verschiedenen experimentellen Werte für 𝜎 zusammen und diskutieren Sie die systematischen Messunsicherheiten!

### 238.f
> [!aufgabe]
Tragen Sie die gemessenen Werte für die Spannungsübertragung 𝑈2/𝑈1 gegen 𝐼2 auf. Berechnen Sie – mit den gemessenen Werten für 𝑀/𝐿 und 𝜔𝐿 (siehe Aufgaben 238.e,f) und 𝑅 = 𝑈2/𝐼2 sowie den auf den Spulen angegebenen Werten für 𝑅V – das Verhältnis 𝑈2/𝑈1 und tragen Sie die berechneten Werte in das Diagramm ein.
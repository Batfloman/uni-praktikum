### 238.A
> [!Aufgabe]
> Erklären Sie die Begriffe Schein-, Wirk- und Blindleistung und diskutieren Sie die Zusammenhänge anhand eines Diagramms/Skizze

Wenn Strom und Spannung phasenverschoben sind treten Schein-, Wirk- und Blindleistung auf:

* Scheinleistung:
Die Gesamtleistung die von einer Wechselstromquelle geliefert wird.
$$
P_S = U \cdot I = \sqrt{P_W^2 + P_B^2}
$$
* Wirkleistung:
Ist der Realteil der Scheinleistung und wird in nutzbare Arbeit umgewandelt 
$$
P_W = \mathcal{Re}(P_S)
$$
* Blindleistung:
Imaginärteil der Scheinleistung. Pendelt zwischen Wechselstromquelle und Verbraucher hin und her ohne in nutzbare Arbeit umgewandelt zu werden.
$$
P_B = \mathcal{Im}(P_S)
$$

![[Wechselstromleistung.png]]

### 238.B
> [!Aufgabe]
> Wovon hängen die Kupferverluste ab?

Die Kupferverluste hängen von dem Widerstand der Spulen und der Stromstärke ab. (Und Temperatur)
### 238.C
> [!Aufgabe]
> Wovon hängen die Eisenverluste – getrennt nach Hysterese- und Wirbelstromverlusten – ab?

Hysterese - Ummagnetisierung:
* Wechselstrom Frequenz
Wirbelstomverluste
* Widerstand Eisen
### 238.D
> [!Aufgabe]
> Leiten Sie für die Stromübersetzung ausgehend von Gleichung 238.11 die Gleichung 238.26 für den symmetrischen Transformator her.

Die Ausgangsgleichung lautet
$$
\frac{I_2}{I_1} = \frac{-Z_{2,1}}{Z + Z_{2,2}}
\tag{238.11}
$$
Durch vergleichen von Gleichung $(238.7)$ und $238.8$ folgt:
$$
\begin{align*}
Z_{2,1} = Z_{1,2} = i\omega M \\
Z_{2,2} = i\omega L_2 + R_2
\end{align*}
\tag{238.17}
$$
Wir betrachten hier einen symmetrischen Transformator also gilt:
$$
\begin{align*}
L \equiv L_1 = L_2 \\
R_V \equiv R_1 = R_2
\end{align*}
$$
Da wir einen einfachen Widerstand an die Sekundärspule angeschlossen haben gilt $Z = R$
Setzen wir alles in $(238.11)$ ein:
$$
\frac{I_2}{I_1} = \frac{-i\omega M}{R + i\omega L + R_V}
$$
Da wir hier die effektiven Werte betrachten gilt:
$$
\frac{I_{2,eff}}{I_{1,eff}} 
= \frac{\frac{1}{\sqrt 2} I_{2,max}}{\frac{1}{\sqrt 2} I_{1,max}} 
= \frac{\frac{1}{\sqrt 2} |I_2|}{\frac{1}{\sqrt 2} |I_1|} 
= \left| \frac{I_2}{I_1} \right|
$$
Also bekommen wir:
Erweitern wir mit $\frac{L}{L}$
$$
\left| \frac{I_2}{I_1} \right| 
= \left| \frac{M}{L} \frac{-i\omega L}{R + i\omega L + R_V} \right|
$$
$$
\frac{I_2}{I_1} 
= \left| \frac{M}{L} \frac{1}{\frac{R + i\omega L + R_V}{-i\omega L}} \right|
$$
Splitten wir den Bruch unten auf
$$
\frac{I_2}{I_1} 
= \left| \frac{M}{L} \frac{1}{\frac{i\omega L}{-i\omega L} + \frac{ R + R_V}{-i\omega L}} \right|
$$
Kürzen
$$
\frac{I_2}{I_1} 
= \left| \frac{M}{L} \frac{1}{(-1) - \frac{R + R_V}{i\omega L}} \right|
$$
Da $\frac{M}{L}$ positiv sind, können wir den Betrag nur auf den Nenner anwenden
$$
\frac{I_2}{I_1}
= \frac{M}{L} \frac{1}{\left| (-1) - \frac{R + R_V}{i\omega L}\right|} 
$$
Lösen wir den Betrag
$$
\frac{I_2}{I_1} = \frac{M}{L} \frac{1}{\sqrt{1 + \left(\frac{R+R_V}{\omega L
}\right)^2}}
\tag{238.26}
$$
### 238.E
> [!Aufgabe]
> Leiten Sie für die Spannungsübersetzung ausgehend von Gleichung 238.10 die Gleichung 238.27 für den symmetrischen Transformator her.

Die Ausgangsgleichung lautet:
$$
\frac{U_2}{U_1} 
= \frac{Z \cdot Z_{2,1}}{Z \cdot Z_{1,1} + \mathbf{D}}
\tag{238.10}
$$
Betrachten wir wieder die Zusammenhänge aus Gleichung $(238.17)$ (Direkt mit Symmetrie-Eigenschaften)
$$
\begin{align*}
Z_{2,1} &= i \omega M \\
Z_{1,1} &= i \omega L + R_V 
\end{align*}
$$
Und Gleichung $(238.18)$
$$
\mathbf{D} = -\sigma \omega^2 L^2 + R_V^2 + i2\omega LR_V
$$
Setzen wir dies in Gleichung $(238.10)$ ein:
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{R \cdot (i\omega L + R_V) - \sigma \omega^2 L^2 + R_V^2 + i 2\omega L R_V}
$$
Ordnen wir den Nenner neu:
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{R_V(R + R_V) - \sigma \omega^2 L^2 + i\omega L(R + 2R_V)}
$$
Erweitern wir einen Teil
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{R_V(R + R_V) - \sigma \omega^2 L^2 \frac{R + R_V}{R + R_V} + i\omega L(R + 2R_V)}
$$
Und klammern $(R+R_V)$ aus:
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{(R + R_V)\cdot (R_V - \sigma \omega^2 L^2 \frac{1}{R + R_V}) + i\omega L(R + 2R_V)}
$$
Jetzt nutzen wir $R_V \ll \omega L$
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{(R + R_V)\cdot \left( - \sigma \omega^2 L^2 \frac{1}{R + R_V} \right) + i\omega L(R + 2R_V)}
$$
Jetzt kürzen sich $R+R_V$ weg
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{- \sigma \omega^2 L^2 + i\omega L(R + 2R_V)}
$$
Klammern wir unten $i\omega L(R + 2R_V)$ aus
$$
\frac{U_2}{U_1}
= \frac{i \omega R M}{\left( -\frac{\sigma \omega L}{i(R+R_V)} + 1 \right) \cdot i\omega L(R + 2R_V)}
$$
Es kürzen sich $i\omega$ weg
$$
\frac{U_2}{U_1}
= \frac{R M}{\left( -\frac{\sigma \omega L}{i(R+2R_V)} + 1 \right) \cdot L(R + 2R_V)}
$$
Stellen wir das ein bisschen um:
$$
\frac{U_2}{U_1}
= \frac{R}{(R + 2R_V)} \frac{M}{L} \frac{1}{1 -\frac{\sigma \omega L}{i(R+ 2R_V)}}
$$
Auch hier betrachten wir die effektiven Werte 
$$
\frac{U_2}{U_1}
= \frac{R}{(R + 2R_V)} \frac{M}{L} \frac{1}{\left| 1 -\frac{\sigma \omega L}{i(R+ 2R_V) } \right|}
$$
Damit ergibt sich die Endgleichung:
$$
\frac{U_2}{U_1} = \frac{R}{R + 2R_V} \cdot \frac{M}{L}\frac{1}{\sqrt{1 + \left( \frac{\sigma\omega L}{R + 2 R_V} \right)^2}}
\tag{238.27}
$$
### 238.F
> [!Aufgabe]
> Wie groß muss die zulässige Stromstärke des Schiebewiderstandes sein?
### 238.G
> [!Aufgabe]
> Ergänze die Schaltungsskizze aus Abb. 238.5 um die benötigten Messgeräte und zeichne sie ins Protokollheft!

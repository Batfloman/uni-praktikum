### 232.A
> [!Aufgabe]+
Definieren Sie eine ideale Stromquelle. Zeichnen Sie das Ersatzschaltbild für eine reale Stromquelle

Eine ideale Spannungsquelle liefert eine vom entnommenen Strom unabhängige Spannung
Ersatzbild:

```handwritten-ink
{
	"versionAtEmbed": "0.2.6",
	"filepath": "Ink/Writing/2024.11.23 - 0.24am.writing"
}
```

### 232.B
> [!Aufgabe]+
Leiten Sie die Gleichung für die Klemmenspannung 𝑈 in (Gleichung 232.1) her

$$
U_{R} = U_{0} - R_{i}I = U_{0} \cdot \frac{R_{a}}{R_{a} + R_{i}} = U_{0} \cdot \frac{1}{1 + \frac{R_{a}}{R_{i}}}
\tag{232.1}
$$
Nach der Maschenregel gilt:
$$
U_{0} = U_{R} + U_{S} 
$$
Nach dem ohm'schen Gesetz gilt
$$
\begin{align}
U_{0} &= R_{ges} I \\
U_{S} &= R_{i} I \\
\end{align}
$$

### 232.C
> [!Aufgabe]+
Geben Sie eine Messvorschrift zur Bestimmung der Leerlaufspannung $U0$ und des Innenwiderstands $R_{i}$ einer realen Spannungsquelle an.
### 232.D
> [!Aufgabe]+
Leiten Sie die Beziehung $R_{X} = \frac{R_{1}}{R_{2}} \cdot R_{Y}$ für die abgeglichene Schaltung ($I = 0$) ab (Abb. 232.5).

![[Abb.232.5 Wheatstonesche Brücke.png]]

Wenn kein Strom zwischen beiden Widerstandsreihen lauft dann gilt:
$$
\begin{align}
I_{R_{X}} = I_{R_{Y}} \equiv I_{1} \\
I_{R_{1}} = I_{R_{2}} \equiv I_{2}
\end{align}
$$
Die Spannungen müssen gleich sein, da sonst Strom fließen würde.
$$
\begin{align}
R_{X} I_{1} = R_{1} I_{2} \\
R_{Y} I_{1} = R_{2} I_{2} \\
\end{align}
$$
Stellen wir diese um
$$
\begin{align}
R_{X} = \frac{R_{1} I_{2}}{I_{1}} \\
I_{1} = \frac{R_{2} I_{2}}{R_{Y}} \\
\end{align}
$$
Setzen wir jetzt die zweite in die erste ein
$$
R_{X} = R_{1} I_{2} \cdot \frac{R_{Y}}{R_{2} I_{2}} = \frac{R_{1}}{R_{2}} R_{Y}
$$
### 232.E
> [!Aufgabe]+
Sie wollen mit einem Ampèremeter mit Vollausschlag 1 mA und Innenwiderstand 𝑅𝑖 = 1 Ω einen Strom von 4 A messen. Schlagen Sie eine geeignete Schaltung dafür vor.

![[Abb.232.2 Aufbau Mavometer.png]]

Es sollte nur maximal $1~mA$ durch das Amperemeter fließen, der "überschüssige" Strom muss dann mit einem Shunt am Amperemeter vorbeiführen. Dabei ist die Spannung über das Amperemeter und den Shunt gleich:
$$
R_{i} I_{A} = R_{S} I_{S}
$$
Dabei soll der Shunt dann den Reststrom übertragen
$$
I_{S} = I_{0} - I_{A}
$$
Damit folgt:
$$
R_{i} I_{A} = R_{S} \left( I_{0} - I_{A} \right) 
$$
$$
\Leftrightarrow 
R_{S} = R_{i} \frac{I_{A}}{\left( I_{0} - I_{A} \right)}
$$
### 232.F
> [!Aufgabe]+
Sie wollen mit einem Voltmeter mit Vollausschlag 1 V und Innenwiderstand 𝑅𝑖 = 100 kΩ einen Strom von 10 μA messen. Was müssen Sie tun?
### 232.G
> [!Aufgabe]+
Können Sie mit einem Ampèremeter Spannungen messen? Welche Bedingungen müssen erfüllt sein?
### 232.H
> [!Aufgabe]+
Geben Sie die Formeln für die Klemmenwiderstände 𝑅𝐴 und 𝑅𝐵 (in Abb. 232.6 (A) und (B)) über den Spannungsmesser an. Berücksichtigen Sie bei Ihrer Rechnung alle relevanten Widerstände, inklusive des einstellbaren Widerstandes 𝑅E, sowie der Innenwiderstände 𝑅𝐼 und 𝑅𝑈 von Strom- und Spannungsmesser! Für welche Größen(-Ordnung) des zu bestimmenden Widerstandes 𝑅𝑥 ist welche Schaltung (A oder B) geeignet?

![[Abb.232.6 Schaltung zur Bestimmung von Widerstäneden mit einer Storm und Spannugnsmessung.png]]
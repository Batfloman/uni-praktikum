> [!Warning]
Es ist unbedingt vor dem Versuch die Betriebsanleitung des Oszillographen zu studieren.

Weder ist der Ausgang der Signalgeneratoren erdfrei, noch der Eingang der Oszillographen. Bei den in Abb. 234.1, 234.2, 234.4 und 234.7 dargestellten Schaltungen besteht die Gefahr eines Kurzschluss.

## 234.2.1 Messung von Wechselstromwiderständen
### 234.a
> [!Aufgabe]+
Mit der in Abb. 234.1 dargestellten Schaltung ist die Kapazität eines Kondensators zu messen.

![[Abb.234.1 Wheatstonesche Brücke Kondensator.png]]

Es gilt:
$$
\frac{R_{x}}{R_{y}} = \frac{C_{x}}{C_{1}}
\tag{234.2}
$$

> [!Messung]
Wir messen $R_{x}, R_{y}, C_{1}$ um $C_{x}$ bestimmen zu können
### 234.b
> [!Aufgabe]+
Mit der in Abb. 234.2 dargestellten Schaltung ist die Induktivität einer Spule zu messen.

![[Abb.234.2 Wheatstonesche Brücke Spule.png]]

Es gilt:
$$
\frac{R_{X}}{R_{Y}} = \frac{L_{1}}{L_{2}} = \frac{R_{1} + R_{A}}{R_{2} + R_{B}}
\tag{234.4}
$$

> [!Messung]
Wir messen:
> * 1\. Potentiometer $R_{X}, R_{y}, R_{max}$
> * bekannte Spule $L_{1}, R_{1}$
> * (?) 2\. Potentiometer $R_{X}, R_{y}, R_{max}$
### 234.c
> [!Aufgabe]+
Mit der in Abb. 234.5 dargestellten Schaltung ist die in Aufgabe 234.b benutzte Spule auszumessen. Dabei ist der Einfluss der Messgeräte auf die Messung zu diskutieren. Es ist unter Benutzung des bekannten Spulenwiderstandes (mit einem Unigor oder einem DMM zu messen) ein Zeigerdiagramm zu zeichnen und hieraus 𝐿 und 𝜑 zu bestimmen. Vergleichen Sie den erhaltenen Wert von 𝐿 mit dem aus Aufgabe 234.b.

![[Abb.234.5 Strom-Spannungsmessung Wechselstomwiderstand.png]]

> [!Messung]
Die Spule aus 234.b soll mit Abb.234.5 gemessen werden.
Wir messen:
> * Spannung $U_{RL}$ und Strom $I$
> * $R_{X}$

> [!Messung]
Die Spule aus 234.b soll mit DMM gemessen werden.
## 234.2.2 Phasenschieber
### 234.d
> [!Aufgabe]+
Bei der in Abb. 234.4 dargestellten Schaltung ist 𝑅 von 0 bis 𝑅𝑚𝑎𝑥 und 𝑅 = ∞ zu variieren und eine Tabelle der Wertepaare 𝑈𝑅 und 𝑈𝐶 aufzunehmen. Dann wird das Zeigerdiagramm maßstäblich gezeichnet und alle Paare 𝑈𝐶 , 𝑈𝑅 eingetragen, um zu zeigen, dass der Punkt 𝐵 (Abb. 234.3) immer auf dem Halbkreis mit dem Durchmesser 𝑈𝐸 liegt. Beobachten Sie die Vorgänge auf dem Oszillographen auch im sogenannten XY-Modus und diskutieren Sie die Figuren. Frage: Was ist eine Lissajous-Figur? Wie kann man sie auf dem Oszillographenschirm sichtbar machen?

![[Abb.234.4 Phasenschieber.png]]

> [!Messung]
Einmal $U_{e}$ messen 
$\Rightarrow$ Schöner Kreis (Plot)

> [!Messung]
Für $R$ von $0$ bis $200$ und $\infty$ (Kabel getrennt) sollen:
> * $U_R$
> * $U_C$
> * Phasenverschiebung $\varphi$ 
>
gemessen werden.
Dabei soll man zusätzlich die Vorgänge im XY-Modus des Oszillographen.
### 234.e
> [!Aufgabe]+
Machen Sie auch die Phasenverschiebung auf dem Oszillographen sichtbar, indem Sie die Phasenlage zwischen $U_{AB}$ und $U_{E}$ vermessen. Vergleich Sie die Werte mit den Phasenwinkeln im erstellten Zeigerdiagram aus der vorherigen Aufgabe

> [!Messung]
Messen der Phasenverschiebung mit Oszillographen
## 234.2.3 Frequenzabhängige Spannungsteiler
### 234.f
> [!Aufgabe]+
Für alle drei Schaltungen in Abb. 234.6 ist die Ausgangsspannung $U_{A}(\nu)$ für festgehaltene Amplitude der Eingangsspannung $U_{E}$ im Frequenzbereich von ($200$ – $5000$) Hz zu messen und doppeltlogarithmisch in normierten Koordinaten darzustellen. 
> 1. Halten Sie die Amplitude von 𝑈𝐸 immer konstant
> 2. Verteilen Sie Ihre zu messenden Frequenzen so, dass diese in einer logarithmischen Frequenzdarstellung einigermaßen gleichmäßig verteilt sind.
> 3. Für die grafische Darstellung normieren Sie wie folgt: 
> 	 * Abszisse: Ω = 𝜈/𝜈gr → für Tief- und Hochpass: 2𝜋𝜈gr = 𝜔gr = 1/𝑅𝐶 → für das Sperrfilter: 𝜈gr = 𝜈0 (aus der Messung) • Ordinate: 𝐴 = 𝑈𝐴/𝑈𝐸 (𝐴 = „Übertragungsfunktion“) • 𝐴 wird gegen Ω doppeltlogarithmisch aufgetragen. 
> 1. Tragen Sie in dieser Darstellung eine dB-Skala für die Ordinate ein.

![[Abb.234.6 Frequenzfilter.png]]

> [!Warning]
Die Induktivität 𝐿 ist eine reine Luftspule mit großem Streufeld. Achten Sie darauf, dass diese nicht nahe bei anderen Geräten und nicht direkt auf der Tischplatte, sondern erhöht steht; der Tisch hat einen metallischen Unterbau, und das Resopal hat oft eine Metalleinlage mit entsprechender Rückwirkung auf das Magnetfeld.

> [!Messung]
Einmal anliegende Spannung $U_{E}$ und Spulendaten messen

> [!Messung]
Bei konstanter Spannung $U_{E}$ soll $U_{A}$ für alle 3 Schaltungen als Funktion von $\nu$ ($200 \to 5000$ Hz) gemessen werden, dabei sollten die Frequenzen logarithmisch gleich verteilt sein
### 234.g
> [!Aufgabe]+
Für Tief- und Hochpass sind die Grenzfrequenzen 𝜈gr, bei denen 𝑈𝐴 = 𝑈𝐸 · 1/√2 ist, zu bestimmen, in den Diagrammen aufzutragen und mit dem theoretischen Wert 2𝜋𝜈gr = 𝜔gr = 1/𝑅𝐶 zu vergleichen.

### 234.h
> [!Aufgabe]+
Für das Sperrfilter ist die Unterdrückungsgüte 
> $$
Q'_{exp} = \frac{\nu_{0}}{\Delta\nu} = \frac{\omega_{0}}{\Delta \omega}
\tag{234.12}
> $$
zu bestimmen; 
$\Delta \nu$ ist der Frequenzbereich, innerhalb dessen $U_{A} < U_{E}/\sqrt{2}$ ist. Vergleichen Sie den gefundenen Wert $Q'_{exp}$ mit dem theoretischen Wert:
> $$
Q'_{theo} = \frac{\omega_{0}}{\Delta \omega(3dB)} = \omega_{0} \frac{L}{R} = \frac{1}{\omega_{0}RC}
\tag{234.13}
> $$
Beachten Sie: Dieses 𝑄′ ist die „Unterdrückungsgüte“ und nicht die Kreisgüte 𝑄; letztere wäre ∞, da wir einen verlustlosen Kreis (d.h. der Ohmsche Widerstand der Induktivität wird vernachlässigt) vorausgesetzt haben. Auch für reale Filteranordnungen ist die Kreisgüte 𝑄 immer noch viel größer als die Unterdrückungsgüte 𝑄′.
### 234.i
> [!Aufgabe]+
Wodurch wird für das Sperrfilter das größte Abschwächungsverhältnis bestimmt?
## 234.2.4 Elektrischer Schwingkreis
![[Abb.234.7 Elektrischer Schwingkreis.png]]
### 234.j
> [!Aufgabe]+
Messen Sie die Resonanzkurve (Spannung über dem Kondensator) mit der vorgesehenen Spule ($R_{L}$ bekannt) und einer Kapazität von etwa $1.5 ~\mu F$ im Bereich von ungefähr (0 – 2000) Hz.
>
Bestimmen Sie aus dieser Messung: Die Eigen(kreis)frequenz 𝜔0, die (Kreis-)Frequenz 𝜔max, bei der die Spannungsamplitude maximal wird, 𝐿 und 𝑄, letzteres aus Resonanzbreite, Resonanzhöhe sowie aus 𝜔0, 𝐿 und 𝑅𝐿 , also auf drei Weisen. 
> 1. Achten Sie bei der Aufnahme der Resonanzkurve darauf, dass die Amplitude von 𝑈𝐸 immer konstant bleibt, was Sie dadurch erreichen können, dass Sie am Tonfrequenzgenerator den Pegel verändern. 
> 2. Verteilen Sie Ihre Messpunkte so, dass Sie im Bereich der Resonanz mehr Punkte haben als auf den Flanken. 
> 3. Zeichnen Sie die Resonanzkurve auf Millimeter-Papier; Sie können hier als Abszisse einfacherweise 𝜈 wählen. 
> 4. Dann bestimmen Sie:
> 	 * 𝑄 aus der Resonanzüberhöhung: 𝑈𝐴 (𝜔max) = 𝑄 · 𝑈𝐴 (𝜔 = 0), 
> 	 * 𝑄 aus der Resonanzbreite: 𝜔0 = 𝑄 · Δ𝜔 (Δ𝜔 aus 1/√2-Wert), 
> 	 * 𝜔max und 𝜔0 aus 𝜔max = 𝜔0√︁ 1 − 1/(2𝑄2), 
> 	 * 𝐿 aus 𝜔0 und 𝐶, • 𝑄 aus 
> 	 * 𝑄 = 𝜔0 · 𝐿/𝑅𝐿 .

> [!Messung]
Spulendaten, Kapazität

> [!Messung]
Bei konstantem $U_E$, und ($0 \to 2000$), bei Resonaz genauer messen!. Der actuall peak-wert $U_{A}$ wäre cool
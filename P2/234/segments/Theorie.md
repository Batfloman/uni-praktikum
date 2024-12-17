Die Eigenschaften von Serien- und Parallelschaltkreisen mit Impedanzen (Widerstand 𝑅, Kapazität 𝐶, Induktivität 𝐿) bei anliegender Wechselspannung 𝑈0 folgen – wie auch bei Gleichspannungs- schaltungen – aus den Kirchhoffschen Regeln, also aus der Erhaltung der elektrischen Ladung und der Energie.
## 234.1.1 Messung von Kapazitäten
Betrachten wir den Aufbau:
![[Abb.234.1 Wheatstonesche Brücke Kondensator.png]]

Mit dem Oszillator können wir das Spannungsverhältnis links zu rechts messen. 
$$
\frac{U_{R_{x}}}{U_{R_{y}}} = \frac{U_{C_{1}}}{U_{C_{X}}}
$$
> [!Herleitung]-
Die Spannung am Potentiometer ist
> $$
\begin{align}
U_{R_{x}} = R_{x} \cdot I_{x} \\
U_{R_{y}} = R_{y} \cdot I_{y} \\
\end{align}
> $$
> Wenn kein Strom zwischen beiden Impedanz-Reihen fließt gilt $I_{x} = I_{y}$ 
> Für die Spannung an den Kondensatoren gilt:
> $$
\begin{align}
U_{C_{1}} = \frac{Q_{1}}{C_{1}} \\
U_{C_{x}} = \frac{Q_{x}}{C_{x}} \\
\end{align}
> $$
> Wenn kein Strom zwischen beiden Impedanz-Reihen fließt gilt $Q_{1} = Q_{x}$ 

Damit folgt
$$
\frac{R_{x}}{R_{y}} = \frac{C_{x}}{C_{1}}
\tag{234.2}
$$
## 234.1.2 Messung von Induktivitäten
Bei Spulen lässt sich der Ohmsche Widerstand meist nicht vernachlässigen. Die Abgleichbedingung ergibt dann zunächst: 𝑅𝑋 𝑅𝑌 = 𝑅1 + 𝑖𝜔𝐿1 𝑅2 + 𝑖𝜔𝐿2 ⇒ 𝑅𝑋 𝑅𝑌 = 𝐿1 𝐿2 = 𝑅1 𝑅2 .
Beide Bedingungen zugleich lassen sich im allgemeinen nicht ohne weiteres erfüllen. Deshalb benutzen wir ein weiteres Potentiometer 𝐻2 zum Phasenabgleich (Abb. 234.2). Dann lautet die Abgleichbedingung: 𝑅𝑋 𝑅𝑌 = 𝐿1 𝐿2 = 𝑅1 + 𝑅𝐴 𝑅2 + 𝑅𝐵 .
## 234.1.3 RC-Phasenschieber
Ein Phasenschieber ist eine Schaltung, die es gestattet, die Phase 𝜑 einer Ausgangsspannung 𝑈𝐴𝐵 relativ zur Eingangsspannung 𝑈𝐸 zu variieren und dabei die Ausgangsspannung konstant zu lassen. Eine Prinzipschaltung mit zugehörigem Zeigerdiagramm ist in Abb. 234.3 dargestellt.
## 234.1.4 Messung von Impedanzen
## 234.1.5 Elektrischer Schwingkreis
Versuch 234 Wechselstromwiderstände, Phasenschieber, RC-Glieder und Schwingungen Beachten Sie: Hier wird die Phase zweier Spannungen gegeneinander verschoben! Es gibt außerdem noch weitere Phasendifferenzen, so z.B. die zwischen Spannung und Strom im 𝑅𝐶-Zweig. Wo ist dieser Phasenwinkel im Zeigerdiagramm zu finden? 234.1.4 Messung von Impedanzen Wechselstromwiderstände können auch durch eine Strom-Spannungsmessung bestimmt werden (siehe Abb. 234.5).Signal- generator UR_L I R X L X 𝐿𝑥 = Induktivität der unbekannten Spule 𝑅𝑥 = Ohmscher Widerstand der unbekannten Spule 𝐼, 𝑈 = Messinstrumente für Strom und Spannung Abbildung 234.5: Strom–Spannungmessung zur Bestimmung eines Wechselstromwiderstands. 234.1.5 Elektrischer Schwingkreis Hier soll verstanden werden, wie die Resonanzkurve, Güte, Eigenfrequenz etc. eines elektri- schen Schwingungskreises durch formale „Übersetzung“ der gleichen Größen eines mechanischen Schwingkörpers, in diesem Falle des Drehpendels, gewonnen werden können. Dazu muss man eine Differentialgleichung der erzwungenen Schwingung aufstellen, die formal der des periodisch angeregten Drehpendels gleicht. Für den Serienschwingkreis (siehe Abb. 234.7) gilt: 𝑈𝐿 (𝑡) + 𝑈𝑅 (𝑡) + 𝑈𝐶 (𝑡) = 𝑈𝐸 cos(𝜔𝑡). (234.5) 𝜔 ist die Kreisfrequenz von 𝑈𝐸 , also am Generator einstellbar. Die Spannungen auf der linken Seite können durch den Strom 𝐼 (𝑡), der überall gleich ist, ausgedrückt werden: 𝐿 ¤𝐼 + 𝑅𝐼 + 1 𝐶 ∫ 𝐼 d𝑡 = 𝑈𝐸 cos(𝜔𝑡). (234.6) Der Strom kann durch die fließende Ladung ausgedrückt werden: 𝐼 (𝑡) = ¤𝑞(𝑡): 𝐿 ¥𝑞 + 𝑅 ¤𝑞 + 1 𝐶 𝑞 = 𝑈𝐸 cos(𝜔𝑡). 
Die Lösung von Gleichung 234.7 für 𝑞(𝑡) lautet (vgl. Anhang A2): 𝑞(𝑡, 𝜔) = 𝑞0 (𝜔) cos(𝜔𝑡 − 𝛼) mit 𝑞0 (𝜔) = 𝑈𝐸 𝐿 · 1√︂  𝜔2 0 − 𝜔2 2 + 𝜔2 0𝜔2/𝑄2 (234.8) und tan 𝛼 = 1 𝑄 · 𝜔0𝜔 𝜔2 0 − 𝜔2 . (234.9) Weiter erhält man durch Einsetzen in die entsprechenden Ausdrücke für die Eigen(kreis)frequenz 𝜔0, die Güte 𝑄 und die Resonanz(kreis)frequenz 𝜔max: 𝜔2 0 = 1 𝐿𝐶 , 𝑄 = 𝜔0 𝐿 𝑅 = 1 𝜔0 𝑅𝐶  = 1 𝑅√︁ 𝑍𝐶 𝑍𝐿  , 𝜔max = 𝜔0√︄ 1 − 1 2𝑄2 . (234.10) Hierbei bezeichnet 𝜔0 die Eigen(kreis)frequenz und 𝑄 die Güte (vgl. Anhang A2). Die Ladung 𝑞(𝑡) kann leicht als Spannung am Kondensator gemessen werden: 𝑈 (𝑡, 𝜔) = 𝑞(𝑡, 𝜔)/𝐶 und andererseits 𝑈 (𝑡, 𝜔) = 𝑈 (𝜔) cos(𝜔𝑡 − 𝛼) mit der „Resonanzkurve“ 𝑈 (𝜔) = 𝑈𝐸 𝜔2 0 1√︂  𝜔2 0 − 𝜔2 2 + 𝜔2 0𝜔2/𝑄2 . (234.11) Für 𝜔 = 𝜔0 folgt daraus im Maximum 𝑈0 = 𝑈 (𝜔0) = 𝑈𝐸 𝑄. Außerdem ist wie beim Drehpendel: 𝜔0/Δ𝜔  𝑄.
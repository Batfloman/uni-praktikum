
## Widerstand Bestimmung
### 232.a
> [!Aufgabe]-
Aufgabe 232.a: Messen und zeichnen Sie die 𝑈-𝐼-Abhängigkeit in einer der beiden Schaltungen aus Abb. 232.6. Benutzen Sie hierbei zwei Mavometer, deren Messbereiche Sie mit Parallel- bzw. Vorwiderständen geeignet einstellen (Abb. 232.2). Bestimmen sie aus der $U$-$I$-Kurve zu Schaltung A bzw. B deren effektiven Widerstand $R_{A}$ bzw. $R_{B}$, über den $U$ und $I$ verknüpft sind

> [!Auswertung]
zeichnen Sie die $U$-$I$-Abhängigkeit in einer der beiden Schaltungen

![[plot_232a.png]]

> [!Auswertung]
Bestimmen sie aus der $U$-$I$-Kurve zu Schaltung A bzw. B deren effektiven Widerstand $R_{A}$ bzw. $R_{B}$, über den $U$ und $I$ verknüpft sind

### 232.b
> [!Aufgabe]-
Bestimmen Sie den Wert des Widerstandes $R_{x}$ unter Berücksichtigung der Innenwiderstände der Messinstrumente. Tragen Sie dann zusätzlich die Gerade $U = R_{x} \cdot I$ in das Diagramm ein.

> [!Auswertung]
Bestimmen Sie den Wert des Widerstandes $R_{x}$ unter Berücksichtigung der Innenwiderstände der Messinstrumente.

Für $R_{B}$ gilt (nach der Voraufgabe 232.H):
$$
R_{B} = R_{X} + R_{i}
$$

> [!Auswertung]
Tragen Sie dann zusätzlich die Gerade $U = R_{x} \cdot I$ in das Diagramm ein.

![[plot_232b.png]]
### 232.c
> [!Aufgabe]-
Überprüfen Sie den Wert des Widerstandes $R_{x}$ mit einem Digitalmultimeter.

> [!Auswertung]
Vergleichen von gemessenen und berechneten $R_{x}$
## Belastete Potentiometerschaltung

![[Abb.232.9 Belastete Potentiometerschaltung.png]]
### 232.d
Nur [[Praktikum/P2/232/segments/Durchführung|Durchführung]]
### 232.e
> [!Aufgabe]+
Betrachten Sie die Spannungsteilerschaltung (Spannungsquelle + Spannungsteiler) (Abb. 232.3) als neue Spannungsquelle (die die über 𝑅2 abfallende Spannung liefert) und das entsprechende Ersatzschaltbild (Abb. 232.1). Bestimmen Sie aus den gemessenen Werten die Größen Innenwiderstand 𝑅𝑆 𝑖 und Leerlaufspannung 𝑈𝑆 0 . Zeichnen Sie hierzu ein U-I-Diagramm und verifizieren Sie die Relation: 
> $$
U = \frac{R_{2}}{R_{1} + R_{2}} \cdot U_{0} - \frac{R_{1} \cdot R_{2}}{R_{1} + R_{2}} \cdot I = U_{0}^s - R_{i}^s I
\tag{232.8}
> $$
Hierbei bezeichnet 𝑈0 die Spannung der Spannungsquelle, die am Spannungsteiler ange- schlossen ist. Was könnten Sie tun, um unter Beibehaltung des Wertes von 𝑈𝑆 0 den Innenwi- derstand 𝑅𝑆 𝑖 zu verkleinern? Warum kann man das nicht beliebig weit treiben?

![[Abb.232.3 Spannungsteiler Potentiometerschaltung.png]]

> [!Auswertung]+
Bestimmen des Innenwiderstand $R_{S,i}$ und der Leerlaufspannung $U_{S,0}$
Dazu soll ein $U$-$I$-Diagramm gezeichnet werden

![[plot_232d.png]]

> [!Auswertung]+
Was könnten Sie tun, um unter Beibehaltung des Wertes von $U_{0}^s$ den Innenwiderstand $R_{i}^s$ zu verkleinern? Warum kann man das nicht beliebig weit treiben?
### 232.f
> [!Aufgabe]-
> Setzen Sie nun anstelle des Spannungsteilers das Potentiometer (Helipot) ein (Abb. 232.9, es werden jeweils nur die Messinstrumente in die Schaltung eingebaut, die benötigt werden.) Bestätigen Sie ohne Last (𝑅𝐿 = ∞ Ω) die lineare Relation 
> $$
U_{I\_L} = \frac{R_{Y}}{R_{Y} + R_{X}} U_{0} = \frac{x}{l} U_{0}
\tag{232.9}
> $$
> Beim Helipot werden die Größen 𝑥 und ℓ in Skalenteilen abgelesen und angegeben. Wieder- holen Sie die Messung für die Lastwiderstände 𝑅𝐿 = 20 Ω und 𝑅𝐿 = 50 Ω. Zeichnen Sie alles zusammen in ein Diagramm ein und diskutieren Sie das Ergebnis.

> [!Auswertung]
>  Bestätigen Sie ohne Last (𝑅𝐿 = ∞ Ω) die lineare Relation 
> $$
U_{I\_L} = \frac{R_{Y}}{R_{Y} + R_{X}} U_{0} = \frac{x}{l} U_{0}
\tag{232.9}
> $$

> [!Auswertung]
Für $R_{L} \in \left\{ 20, 50, \infty \right\}\Omega$ soll ein Diagramm gezeichnet werden und das Ergebnis diskutiert werden.

![[plot_232f.png]]
## Messung der Leerlaufspannung einer Batterie
### 232.g
Nur [[Praktikum/P2/232/segments/Durchführung|Durchführung]]
### 232.h
> [!Aufgabe]+
Messen Sie die Leerlaufspannung einer Batterie (mit unbekannter Spannung) mit Hilfe der kalibrierten Anordnung (Abb. 232.4). Wie variiert der Messfehler mit dem 𝑦-Wert? Wäre es gut, ein Spannungselement von 10 V zu verwenden?

> [!Auswertung]
> Wie variiert der Messfehler mit dem 𝑦-Wert? Wäre es gut, ein Spannungselement von 10 V zu verwenden?
### 232.i
> [!Aufgabe]-
Messung der Leerlaufspannung derselben Batterie mit Mavometer und mit Digitalmessgerät. Erklären Sie, warum das Mavometer die Batteriespannung nicht richtig misst.

> [!Auswertung]
Erklären Sie, warum das Mavometer die Batteriespannung nicht richtig misst.
## Widerstandsmessung mit der Wheatstoneschen Brücke
### 232.j
> [!Aufgabe]-
Bestimmen Sie hiermit einen unbekannten Widerstand 𝑅1. Als Potentiometer wird ein „Helipot“ (Präzisions-Potentiometer mit 1000 Skalenteilen) benutzt.

> [!Auswerung]
Berechnung des unbekannten Wiederstandes 
### 232.k
> [!Aufgabe]-
Welchen Wert sollte der Widerstand 𝑅𝐵𝑜𝑥 ungefähr haben, wenn er – bei nicht gedrücktem Taster T – einerseits das Nullinstrument 𝑈 ausreichend vor Überlastung schützen, andererseits die Empfindlichkeit nicht übermäßig reduzieren soll?

> [!Auswertung]
Welchen Wert sollte der Widerstand $R_{Box}$ ungefähr haben, damit das Nullinstrument 𝑈 ausreichend vor Überlastung geschützt und die Empfindlichkeit nicht übermäßig reduziert ist?
## Messung der Temperaturabhängigkeit des elektrischen Widerstandes
### 232.l
Nur [[Praktikum/P2/232/segments/Durchführung|Durchführung]]
### 232.m
> [!Aufgabe]-
Berechnen Sie aus diesen Daten 𝑅(𝑇) und tragen Sie auf: 
> * Für die metallischen Leiter und den Kohleschichtwiderstand: 𝑅 als Funktion von 𝜗 (Celsius-Temperatur) auf Millimeter-Papier. Berechnen Sie 𝛼 einschließlich einer Fehlerabschätzung und diskutieren Sie das Verhalten von 𝑅 bei der Annäherung an den absoluten Nullpunkt der Temperatur.
> * Für den Halbleiter: Den natürlichen Logarithmus des Widerstands ln (𝑅/Ω) als Funktion von 1/𝑇 (𝑇 = absolute Temperatur) auf Millimeter-Papier, oder einfacher: 𝑅 als Funktion von 1/𝑇 auf halblogarithmischem Papier. Bestimmen Sie die Gap-Energie 𝐸G in eV einschließlich einer Fehlerabschätzung.
> * Für den PTC-Widerstand: Tragen Sie den natürlichen Logarithmus des Widerstandes ln (𝑅/Ω) als Funktion von 𝜗 (Celsius-Temperatur) auf. Schätzen Sie aus dem Graphen die Lage der Curie-Temperatur ab (inklusive Angabe der Unsicherheit)!

> [!Auswertung]
Für metallische Leiter und den Kohleschichtwiderstand soll
$R$ als Funktion von $T [°C]$ gezeichnet werden
$\alpha$ inklusive Fehlerabsätzung bestimmen

> [!Auswertung]
Für Halbleiter
$\ln(R)$ als Funktion von $1/T$ aufragen
$E_{G}$ in $eV$ bestimmen

> [!Auswertung]
Für PTC:
$\ln(R)$ als Funktion von $T [°C]$ auftragen
Lage der Curie-Temperatur abschätzen



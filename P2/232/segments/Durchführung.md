## Widerstand Bestimmung

### 232.a

> [!Aufgabe]+
Messen und zeichnen Sie die 𝑈-𝐼-Abhängigkeit in einer der beiden Schaltungen aus Abb. 232.6. Benutzen Sie hierbei zwei Mavometer, deren Messbereiche Sie mit Parallel- bzw. Vorwiderständen geeignet einstellen (Abb. 232.2). Bestimmen sie aus der $U$-$I$-Kurve zu Schaltung A bzw. B deren effektiven Widerstand $R_{A}$ bzw. $R_{B}$, über den $U$ und $I$ verknüpft sind

![[Abb.232.6 Schaltung zur Bestimmung von Widerstäneden mit einer Storm und Spannugnsmessung.png]]

> [!Messung]
Wir sollen die $U$-$I$ Abhängigkeit einer der beiden Schaltungen $A$ oder $B$ messen.
Dazu nutzen wir zwei Mavometer, die wir mit Vorwiderständen geeignet einstellen sollen

![[Abb.232.2 Aufbau Mavometer.png]]
### 232.b
> [!Aufgabe]+
Bestimmen Sie den Wert des Widerstandes $R_{x}$ unter Berücksichtigung der Innenwiderstände der Messinstrumente. Tragen Sie dann zusätzlich die Gerade $U = R_{x} \cdot I$ in das Diagramm ein.

Nur [[Praktikum/P2/232/segments/Auswertung|Auswertung]]
### 232.c
> [!Aufgabe]+
Überprüfen Sie den Wert des Widerstandes $R_{x}$ mit einem Digitalmultimeter.

> [!Messung]
Mess den unbekannten Widerstand $R_{x}$ mit einem Digitalmultimeter
$R_{x} = ~?$
## Belastete Potentiometerschaltung
### 232.d
> [!Aufgabe]+
Messen Sie für verschiedene Lastwiderstände $R_{L}$ (maximal 10 verschiedene $R_{L}$) den Strom $I$ durch den Lastwiderstand und die Spannung $U_{I\_{R}}$ über dem Lastwiderstand und dem Ampèremeter. Verwenden Sie das Mavometer zur Strommessung und zur Spannungs- messung. Der Innenwiderstand des Mavometers ist bekannt und soll berücksichtigt werden (Abb. 232.2).

![[Abb.232.9 Belastete Potentiometerschaltung.png]]
mit $R_{X} = 20~\Omega, R_{Y} = 50~\Omega$

> [!Messung]
 Für 10 verschiedene Lastwiderstände $R_{L}$ ($0 \to 130~\Omega$) soll der Strom $I$ und die Spannung $U_{L}$ am Widerstand gemessen werden.
 Dazu soll das Mavometer benutzt werden und der Innenwiderstand berücksichtigt werden
### 232.e
Nur [[Praktikum/P2/232/segments/Auswertung|Auswertung]]
### 232.f
> [!Aufgabe]+
> Setzen Sie nun anstelle des Spannungsteilers das Potentiometer (Helipot) ein (Abb. 232.9, es werden jeweils nur die Messinstrumente in die Schaltung eingebaut, die benötigt werden.) Bestätigen Sie ohne Last (𝑅𝐿 = ∞ Ω) die lineare Relation 
> $$
𝑈𝐼 𝐿 = 𝑅𝑌 𝑅𝑋 + 𝑅𝑌 · 𝑈0 = 𝑥 ℓ · 𝑈0 . 
\tag{232.9}
> $$
> Beim Helipot werden die Größen 𝑥 und ℓ in Skalenteilen abgelesen und angegeben. Wieder- holen Sie die Messung für die Lastwiderstände 𝑅𝐿 = 20 Ω und 𝑅𝐿 = 50 Ω. Zeichnen Sie alles zusammen in ein Diagramm ein und diskutieren Sie das Ergebnis.

> [!Messung]
Jetzt sind $R_{X}$ und $R_{Y}$ variable, also ändern wir $x$ bzw. $y$ am Potentiometer. 
Wir messen die Spannung $U_{L}$ wie in 232.d in Abhängigkeit von $x$, für alle $R_{L} \in \left\{ 20, 50, \infty \right\}\Omega$ 
## Messung der Leerlaufspannung einer Batterie
![[Abb.232.4 Kompensationsschaltung nach Poggendorff.png]]
### 232.g
> [!Aufgabe]+
Unter Verwendung eines stabilisierten Netzgeräts wird eine Hilfsspannungsquelle (Spannungsteiler) durch das Weston Element (Abb. 232.4) kalibriert. Als Potentiometer wird ein Schleifdrahtpotentiometer verwendet. Zum Schutz des Normalelements und des Nullinstruments muss zu Beginn ein relativ hoher Widerstand vorgeschaltet werden. Nach erfolgtem groben Abgleich wird dieser zur Erhöhung der Empfindlichkeit mit dem Taster überbrückt. Widerstand und Taster sind in einem Kästchen eingebaut.

> [!Warning]
> Zum Schutz des Normalelements und des Nullinstruments muss zu Beginn ein relativ hoher Widerstand vorgeschaltet werden.
### 232.h
> [!Aufgabe]+
Messen Sie die Leerlaufspannung einer Batterie (mit unbekannter Spannung) mit Hilfe der kalibrierten Anordnung (Abb. 232.4). Wie variiert der Messfehler mit dem 𝑦-Wert? Wäre es gut, ein Spannungselement von 10 V zu verwenden?

> [!Messung]
Leerlaufspannung einer Batterie = $U_{y}$ wenn kein Strom durchs Amperemeter fließt 
### 232.i
> [!Aufgabe]+
Messung der Leerlaufspannung derselben Batterie mit Mavometer und mit Digitalmessgerät. Erklären Sie, warum das Mavometer die Batteriespannung nicht richtig misst.

> [!Messung]
Leerlaufspannung der Batterie mit Mavometer und Digitalmessgerät
## Widerstandsmessung mit der Wheatstoneschen Brücke

![[Abb.232.5 Wheatstonesche Brücke.png]]
### 232.j
> [!Aufgabe]+
Bestimmen Sie hiermit einen unbekannten Widerstand 𝑅1. Als Potentiometer wird ein „Helipot“ (Präzisions-Potentiometer mit 1000 Skalenteilen) benutzt.
### 232.k
> [!Aufgabe]+
Welchen Wert sollte der Widerstand 𝑅𝐵𝑜𝑥 ungefähr haben, wenn er – bei nicht gedrücktem Taster T – einerseits das Nullinstrument 𝑈 ausreichend vor Überlastung schützen, andererseits die Empfindlichkeit nicht übermäßig reduzieren soll?
## Messung der Temperaturabhängigkeit des elektrischen Widerstandes
### 232.l
> [!Aufgabe]+
Heizen Sie mit dem Thermostaten die Temperatur im Reagenzglas langsam von Raumtemperatur auf knapp 100 °C auf und messen Sie dabei immer abwechselnd die Wider- stände der fünf Leiter: Bei jeder Widerstandsmessung lesen Sie auch das Temperaturanzeige des Thermostaten ab und tragen die Werte in eine Tabelle ein. Achtung: Die Wasserbecken nie ohne oder mit zu wenig Wasser betreiben! Um eine Beschädigung der Platine zu vermeiden, stecken Sie bitte beim Wechsel von einem Widerstand zum nächsten die Kabel am Multimeter um. Die Stecker in den Platinenbuchsen sollen nicht entfernt werden.

> [!Messung]
> Die Widerstände der fünf Leiter sollen in abhängigkeit der Temperatur (Raumtemp $\to 100~^\circ$C) 

> [!Warning]
> Die Wasserbecken nie ohne oder mit zu wenig Wasser betreiben!

> [!Warning]
> Um eine Beschädigung der Platine zu vermeiden, stecken Sie bitte beim Wechsel von einem Widerstand zum nächsten die Kabel am Multimeter um. Die Stecker in den Platinenbuchsen sollen nicht entfernt werden.
### 232.m
Nur [[Praktikum/P2/232/segments/Auswertung|Auswertung]]
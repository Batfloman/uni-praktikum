## Kenntnisse
Ohmsches Gesetz, 
Kirchhoffsche Gesetze, 
Stromrichtige und Spannungsrichtige Messung, 
elektrische Leitfähigkeit von Leitern, 
Halbleitern und Isolatoren, 
Temperaturabhängigkeit des elektrischen Widerstandes, 
Leitungsmechanismen Ideale und reale Spannungsquelle, 
Innenwiderstand von Spannungsquellen,
Leerlauf- und Klemmenspannung,
Aufbau und Wirkungsweise eines Normalelementes und einer Batterie, 
Spannungsteiler, 
Lastanpassung Ampère- und Voltmeter, 
Innenwiderstand dieser Messgeräte, 
Veränderung des Messbereichs durch Parallel- bzw. Serien-/Vorwiderstand und deren Einfluss auf die Messung;
Potentiometerschaltung, 
Wheatstonesche Brückenschaltung, 
Kompensationsschaltung
## 232.1.1 Spannungs- und Stromquellen
Ideale Spannungsquelle $\Rightarrow$ keinen Innenwiderstand
reale Spannungsquelle, hat Innenwiderstand $\Rightarrow$ Spannungsabfall in Stromquelle $U_{i} = R_{i} \cdot I$, also von $I$ abhängig

![[Abb.232.1 reale Spannungsquelle.png]]

Klemmspannung $U$ = Spannung mit Spannungsabfall
Leelaufspannung $U_{0}$ = Spannung ohne Spannungsabfall, denn für $R_{a} \to \infty \Rightarrow U \to U_{0}$ 

Die Klemmenspannung 𝑈 beträgt 
$$
U = U_{0} - U_{i} = U_{0} − R_{i} \cdot I = U_{0} \cdot \frac{R_{a}}{R_{a} + R_{i}} = 𝑈0 · 1 1 + 𝑅𝑖 𝑅𝑎 
\tag{232.1}
$$
Sie ist lastabhängig. 
Für eine gegebene Spannungsquelle sind 𝑈0 und 𝑅𝑖 i.a. Konstanten. 𝑅𝑖 ist differentiell definiert: 𝑅𝑖 := 𝜕𝑈 𝜕𝐼 .

## 232.1.2 Messgeräte
### Drehspulaglvanometer
Drehspulgalvanometer, siehe Versuch 236

Ströme lassen sich direkt mithilfe von Drehspulgalvanometern messen; wird die Spule von einem elektrischen Strom durchflossen, kommt es zu einer Auslenkung des Zeigerinstruments, die pro- portional zur Stromstärke ist. Durch das Nutzen bekannter Widerstände lässt sich der gemessene Strom in Spannung umrechnen.

### Mavometer (Milliampere-Volt-Meter)
Ein spezielles Drehspulgalvanometer, dass je nach Schaltung Strom oder Spannung messen kann

![[Abb.232.2 Aufbau Mavometer.png]]

* Shunt (parallel): 
	kann zur Umleitung von Strom genutzt werden, damit man nur $x$% des Stromes misst und den rest mit dem Widerstand des Shunt bestimmen kann
* Vorwiderstand (in Reihe):
	kann zur Verringerung der Spannung am Galvanometer benutzt werden
## 232.1.3 Spannungsteiler- und Potentiometerschaltung

![[Abb.232.3 Spannungsteiler Potentiometerschaltung.png]]

Häufig möchte man sich mit einer vorhandenen Spannungsquelle $U_{0}$ eine geeignete Klemmenspannung $U_{K}$ herstellen. Dies kann man entweder durch eine Spannungsteilerschaltung (𝑅1 und 𝑅2 fest) oder durch eine Potentiometerschaltung, bei der sich der Gesamtwiderstand 𝑅 = 𝑅𝑋 + 𝑅𝑌 kontinuierlich teilen lässt (Abb. 232.3) realisieren. Einstellbare Spannungsteiler sind häufig so ausgebildet, dass man statt der Widerstandswerte 𝑅𝑋 (oder 𝑅𝑌 ) dazu proportionale Größen wie z.B. eine Länge 𝑥 (beim Schiebewiderstand) oder Skalenteile (beim Helipot = helixförmig gewi- ckeltes Langdrahtpotentiometer) abliest.



## 232.1.4 Kompensationsschaltung
![[Abb.232.4 Kompensationsschaltung nach Poggendorff.png]]
Stromlos => Leerlaufspannung einer unbekannten Spannungsquelle (hier Batterie) kann ermittelt werden

Wir verstellen $R_{y}$ durch das Potentiometer, so dass 
$$
U_{unbekannt} = U_{y} = R_{y} I
$$
die Gleichheit der Spannungen kann man an dem Stromfluss am Amperemeter ablesen. Fließt kein Strom, so sind die Spannungen gleich (Durch $R_{y}$ fließt Strom!)

Ist dieser Zustand erreicht, muss die angelegte Spannung gleich der unbekannten Spannung (hier: der Batterie) sein. Da die Messung der unbekannten Spannung durch diese Methode stromlos funktioniert (das Strommessgerät zeigt keinen Ausschlag mehr!) kann so vergleichsweise einfach die Leerlaufspannung einer Spannungsquelle gemessen werden. Das Weston-Element mit bekannter Spannung dient zur Kalibration des Spannungsteilers.
## 232.1.5 Wheatstonesche Brücke
![[Abb.232.5 Wheatstonesche Brücke.png]]
Die „Wheatstonesche Brücke“ kann für jegliche Messungen von elektrischen Widerständen gebraucht werden. Dabei werden zwei Spannungsteiler parallel geschaltet und durch ein Strommessgerät miteinander „verbunden“ (Abb. 232.5). Ist das Verhältnis der Widerstände der Spannungsteiler gleich groß, herrscht auf beiden Seiten das gleiche Potential und es fließt kein Strom zwischen Ihnen.
Aus den Verhältnissen können nun beliebige (die Widerstände betreffende) Größen berechnet werden (z.B. die Größe eines unbekannten Widerstands oder relative Widerstandsänderungen). Die Wheatstonesche Brückenschaltung wird bspw. oft bei Sensoren o.ä. eingesetzt, da schon kleine Temperatur- oder Längenänderungen relative Widerstandsänderungen bewirken.

## 232.1.6 Temperaturabhängigkeit des elektrischen Widerstandes
### Metall Leiter
Nur Positive Leiter
Zahl Elektronen $\approx$ Zahl Atome
Beweglichkeit $\mu$ wird durch Gitterschwingungen verringert, Vorstellung als Quasi-Teilchen "Phononen", Gitterschwindungen nehmen mit Temperatur zu. $\mu \propto \frac{1}{T}$
Restwiderstand durch Unreinheiten im Metall

Die Temperaturabhängigkeit des elektrischen Widerstandes 𝑅 ist für verschiedene Materialien charakteristisch und soll exemplarisch für • einen reinen Halbleiter („Heißleiter“, oder NTC1-Widerstand) • eine metallische Legierung (Konstantan-Widerstand) • einen PTC2-Widerstand („Kaltleiter“) • einen reinen metallischen Leiter (Platin) • einen Kohleschicht-Widerstand untersucht werden. Ihr grundlegendes Verhalten soll diskutiert und verstanden werden. Es gibt folgende fundamentale Beziehung elektrische Leitfähigkeit: 𝜎 = 𝑒 · (𝑛−𝑧− 𝜇− + 𝑛+𝑧+ 𝜇+), (232.2) mit: 𝑛± = positive bzw. negative Ladungsträgerdichte (Anzahl pro Volumen), 𝑧± = Wertigkeiten der pos. bzw. neg. Ladungsträger, 𝜇± = Beweglichkeiten der pos. bzw. neg. Ladungsträger. Im metallischen Leiter tragen ausschließlich die Elektronen zur Stromleitung bei. Dadurch vereinfacht sich der Ausdruck für die elektrische Leitfähigkeit (Gleichung 232.2) in Metallen zu 𝜎 = 𝑒 · 𝑛− 𝜇−. Die Zahl der beteiligten Elektronen im Metall ist durch die Zahl der Atome bestimmt: Jedes Atom stellt im Mittel ein Leitungselektron zur Verfügung, unabhängig von der Temperatur. Die Beweglichkeit der Elektronen wird durch ihre Streuung an den „Phononen“ auf dem Weg durch den Kristall bestimmt. Phononen sind als Quasi-Teilchen aufgefasste Gitterschwingungen, deren Anzahl von der Temperatur bestimmt wird: je höher die Temperatur, desto mehr Phononen, desto mehr Streuung und desto geringere Beweglichkeit. Eine komplizierte Rechnung zeigt: 𝜇 ∝ 1/𝑇. Daraus folgt unmittelbar für die elektrische Leitfähigkeit 𝜎 in Metallen: 𝜎 = 𝑒 · 𝑛− 𝜇− (𝑇) ∝ 1/𝑇 bzw. 1/𝜎 = 𝜌 ∝ 𝑅 ∝ 𝑇 . (232.3) Eine genaue Messung des Widerstandsverlaufs bei tiefen Temperaturen ergibt, dass mit sinkender Temperatur der spezifische Widerstand 𝜌 einen temperaturunabhängigen Wert annimmt, der vom Reinheitsgrad des Metalls abhängt3 (siehe Abb. 232.7). Je mehr Störstellen das Material aufweist, desto größer ist der spezifische Restwiderstand 𝜌𝑖. In reinen Halbleitern (Ge, Si, Cu2O, GaAs, usw.) wird die elektrische Leitfähigkeit mit Hilfe des Bändermodells (siehe Abb. 232.8) wie folgt beschrieben: Bei sehr tiefen Temperaturen sind alle Zustände im Valenzband (VB) gefüllt, das Leitungsband (LB) ist völlig leer; zwischen beiden
Bändern gibt es ein verbotenes Gebiet, in dem es bei reinen Halbleitern keine möglichen Zustände gibt. Die Breite dieses verbotenen Gebietes wird als „Gap“-Energie 𝐸G bezeichnet. Bei sehr tiefen Temperaturen (𝑇 ≈ 0 K) ist ein reiner Halbleiter ein perfekter Isolator. Wird die Temperatur erhöht, werden einzelne Elektronen in das LB angeregt, wobei sie Löcher im VB hinterlassen; diese Löcher entsprechen positiven Ladungen. Beide Ladungsträgerarten zusammen sorgen für die sogenannte Eigenleitung. Die Anzahldichten der negativen und positiven Ladungen 𝑛− und 𝑛+ sind gleich groß und gleich 𝑛. Die quantenmechanische Berechnung von 𝑛 ergibt: 𝑛(𝑇) ∝ 𝑇+ 3 2 · e− 𝐸G 2𝑘𝑇 . (232.4) Die Größe 𝑘 kennzeichnet hierbei für die Boltzmann-Konstante. Die Beweglichkeiten 𝜇− und 𝜇+ sind im Allgemeinen einander ähnlich und von der Temperatur abhängig. Die Beweglichkeit wird wie im Fall der metallischen Leitung durch Phononenstreuung bestimmt, und die Berechnung ergibt für den Fall des Halbleiters: 𝜇(𝑇) ∝ 𝑇− 3 2 . (232.5) Damit kann die elektrische Leitfähigkeit 𝜎 wie folgt berechnet werden: 𝜎 = 2𝑒 · 𝑛(𝑇) · 𝜇(𝑇) ∝ 𝑇+ 3 2 · e− 𝐸G 2𝑘𝑇 · 𝑇− 3 2 = e− 𝐸G 2𝑘𝑇 . (232.6) Dies gilt für reine Halbleiter ohne Dotierung, also reine Eigenleitung (intrinsic conduction). Der elektrische Widerstand nimmt mit steigender Temperatur ab, daher der Name „Heißleiter“ bzw. „ne- gative temperature coefficient“-Widerstand oder kurz NTC-Widerstand. Zur Auswertung des Ex- perimentes wird der Widerstand 𝑅 wegen 𝑅 ∝ 𝜌 = 1/𝜎 angesetzt zu: 𝑅 = 𝑅0 · e 𝐸G 2𝑘𝑇 . (232.7) Um einen Eindruck von der Größenordnung der Gap-Energien 𝐸G zu bekommen, hier ein paar Beispiele:
Die meisten PTC-Widerstande bestehen aus dotierten polykristallinen Keramiken. Die Kerami- ken weisen einen hohen elektrischen Widerstand auf, durch die Dotierung bekommen die Materia- lien jedoch gewisse Halbleitereigenschaften. Unterhalb und oberhalb der sog. materialspezifischen Curie-Temperatur sind die elektrischen Eigenschaften stark verschieden. Bei kleinen Temperaturen zeigen PTC-Widerstände ein NTC-Verhalten. Nach Durchschreiten eines minimalen Widerstand- wertes, kommt es jedoch wieder zu einem Anstieg. Nähert man sich der Curie-Temperatur, kommt es durch den Phasenübergang zu einem rasenten Anstieg des elektrischen Widerstandes mit der Temperatur. Nach Erreichen eines Maximalwertes stellt sich schließlich wieder NTC-artiges Ver- halten ein. Insgesamt ergibt sich also ein hochgradig nichtlineares Verhalten.
> [!Note]
Hinweis 1: Bei den folgenden Versuchsteilen darf der auf einem Widerstand vermerkte maximal zulässige Strom **keinesfalls** überschritten werden! Diese Gefahr besteht inbesondere, falls bei den Schiebewiderständen zu kleine Werte eingestellt werden.
Bringen Sie daher die Schiebewiderstände vor dem Anlegen der Spannung zunächst in Mittelstellung.

> [!Note]
Hinweis 2: Bei der Strommessung mit dem Amperemeter muss darauf geachtet werden, zuvor den richtigen Messbereich für hohe Ströme auszuwählen und die Messung nur für ein paar Sekunden durchzuführen, da ansonsten das Messgerät zerstört werden kann!
## Vorversuch
### 238.a
> [!aufgabe]
Messen Sie für eine RC-Serienschaltung (Abb. 238.5 bei festem Kondensator $C$ für 10 verschiedene (zu berechnende) Widerstandswerte $R$ die Größen Spannung $U_B$, Strom $I_A$, Wirkleistung $P_W$ und die Spannung $U_R$ über dem Widerstand mit dem CASSY-System und parallel mit Volt- bzw. Amperemeter zum Vergleich. 
Folgende Bauteile stehen zur Verfügung: 
> * 50 Hz-Spannungsquelle $U_{eff} \approx 47$ V; 
> * diverse Schiebewiderstände mit verschiedenen Widerstandsbereichen; 
> * Kondensator ca. $80$ μF

![[Abb 238.5.png]]

> [!Messung]
> für $10$ (zu berechnenden) Widerstände die
> * Spannung $U_B$
> * Spannung $U_R$
> * Strom $I_A$
> * Wirkleistung $P_W$
> 
mit CASSY und "normalen" Messgeräten

### 238.b
> [!aufgabe]
Auswertung: Zeichnen Sie das Zeigerdiagramm für diese Schaltung. Berechnen Sie 𝑃S und cos(𝜑) (𝜑 = Phasenwinkel);
Tragen Sie 𝑃W, 𝑃S und 𝑃S cos(𝜑) gegen 𝑅 (𝑅 = 𝑈𝑅/𝐼, 𝑃S = 𝑈𝐼, cos(𝜑) = 𝑈𝑅/𝑈) auf. Bestimmen Sie die maximale Leistung 𝑃W,max, welche die Schaltung der Spannungsquelle entnehmen kann, und den entsprechenden Widerstand. Markieren Sie diese Werte in dem entsprechenden Diagramm.

## Messungen am Transformator

![[Abb 238.6.png]]
### 238.c
> [!aufgabe]
Schließen Sie die Primärseite des Trafos an die Spannungsquelle (blaue Buchsen im grauen Kästchen an der Wand) an und die Sekundärseite mit geeigneten Widerständen ab. Messen Sie die Wirkleistungen 𝑃W,1 und 𝑃W,2, ferner 𝐼2, 𝐼1, 𝑈2 und 𝑈1. Beginnen Sie mit dem Leerlauffall $(I_2 = 0A)$ und erhöhen Sie 𝐼2 in geeigneten Schritten bis zum Kurzschlussstrom. Ggfs. sind verschiedene Schiebewiderstände zu benutzen. 
Legen Sie eine Tabelle für alle Messgrößen und für die durch Auswertung zu bestimmenden Größen 
𝑃S,1 = 𝑈1 𝐼1 Scheinleistung (primär) 𝑃S,2 = 𝑈2 𝐼2 Scheinleistung (sekundär) 𝑃V = 𝑃W,1 − 𝑃W,2 Verlustleistung 𝑃Cu = 𝑅1 𝐼2 1 + 𝑅2 𝐼2 2 Kupferverluste 𝑃Fe = 𝑃V − 𝑃Cu Eisenverluste 𝜂 = 𝑃W,2/𝑃W,1 Wirkungsgrad
Für die folgende Auswertung beachten Sie: Die in der Auswertungsanleitung angegebenen quantitativen Beziehungen sind teilweise Näherungen. Füllen Sie die angefangene Tabelle vollständig aus (Berechnung von 𝑃S,2, etc.). Tragen Sie die beiden Wirkleistungen 𝑃W,1 und 𝑃W,2, die Verlustleistungen 𝑃Cu, 𝑃Fe sowie den Wirkungsgrad 𝜂 gegen 𝐼2 auf.

> [!Messung]
> Primärseite an Spannungsquelle und Sekundärseite zuerst Leelauffall $R_2 = 0 \Omega$ bis zum Kurzschlussfall in *geeigneten* Schritten
>
> * Wirkleistung $P_{W,1}$  und $P_{W,2}$
> * Strom $I_2$ und $I_1$
> * Spannung $U_2$ und $U_1$
>
>
### 238.d
> [!aufgabe]
Bestimmen Sie 𝜔𝐿 mit 3 unterschiedlichen Methoden. Leiten Sie die gegebenen Zusammen- hänge für die Bestimmung von 𝜔𝐿 aus den Gleichungen 238.26, 238.27 bzw. 238.28 her. • aus dem gemessenen Betrag der Eingangsimpedanz im Leerlauf (𝑅 = ∞Ω): 𝜔𝐿 = 𝑈1/𝐼1 • aus dem gemessenen Betrag der Eingangsimpedanz bei näherungsweise verlustfreiem Trafo (𝑅V = 0Ω und 𝜎 = 0) im Fall von 𝑈1/𝐼1 = 𝑅/√2: 𝜔𝐿 = 𝑅 • aus der gemessenen Stromübertragung bei vernachlässigbarem Streukoeffizienten (𝜎 = 0) im Fall von 𝐼2/𝐼1 = 1/√2: 𝜔𝐿 = 𝑅 + 𝑅V) Vergleichen Sie die 3 Ergebnisse und diskutieren Sie die jeweiligen systematischen Messun- sicherheiten!

> [!Messung]
> $\omega L$ soll bestimmt werden indem wir messen:
> * Eingangsimpedanz im Leerlauf
> * Eingangsimpedanz verlustfreier Trafo für $\frac{U_1}{I_1} = \frac{R}{\sqrt{2}}$ und $\omega L = R$
> * Stromübertragung $\frac{I_2}{I_1} = \frac{1}{\sqrt{2}}$ und $\omega L = R + R_V$
### 238.e
> [!aufgabe]
Bestimmen Sie 𝜎 = 1 − 𝑀2/𝐿2 mit folgenden 4 unterschiedlichen Methoden. Leiten Sie auch den jeweils angegeben Zusammenhang her. • aus der gemessenen Stromübertragung im Kurzschlussfall (𝐼2/𝐼1 = 𝑀/𝐿 = √1 − 𝜎) • aus der gemessenen Spannungsübertragung im Leerlauf (𝑈2/𝑈1 = 𝑀/𝐿) • aus den gemessenen Beträgen der Eingangsimpedanzen für Kurzschluss und Leerlauf: Verhältnis = 𝜎. Berücksichtgen Sie, dass 𝑅𝑣 ≪ 𝜔𝐿 gilt. Stellen Sie die verschiedenen experimentellen Werte für 𝜎 zusammen und diskutieren Sie die systematischen Messunsicherheiten!

> [!Messung]
> $\sigma$ soll bestimmt werden indem wir messen:
> * Stromübertragung im Kurzschluss
> * Spannungsübertragung im Leerlauf
> * Eingangsimpedanz im Kurzschluss
> * Eingangsimpedanz im Leerlauf
### 238.f
> [!aufgabe]
Tragen Sie die gemessenen Werte für die Spannungsübertragung 𝑈2/𝑈1 gegen 𝐼2 auf. Berechnen Sie – mit den gemessenen Werten für 𝑀/𝐿 und 𝜔𝐿 (siehe Aufgaben 238.e,f) und 𝑅 = 𝑈2/𝐼2 sowie den auf den Spulen angegebenen Werten für 𝑅V – das Verhältnis 𝑈2/𝑈1 und tragen Sie die berechneten Werte in das Diagramm ein.
**These instructions are currently available in German only!**

Help with translation to English would be appreciated.


Installation der Referenzdaten
==============================

**Die hier beschriebenen Schritte können nur über einen Galaxy-Admin account
durchgeführt werden!**

Das empfohlene ``quay.io/bgruening/galaxy-exome-seq:miracum_20.09`` Image
bringt ein vorkonfiguriertes Admin-Konto mit:

```
Galaxy-Nutzername: admin
Passwort: password
```

Mit diesen Zugangsdaten kann man sich im Galaxy-Webinterface, erreichbar unter
http://localhost:8080, unter ``Login or Register`` -> ``Login`` als
Admin-Nutzer anmelden.

Nach erfolgreicher Anmeldung sollte im Reiter ganz oben auf der Seite die
Auswahl ``Admin`` zur Verfügung stehen. Diese bitte anklicken um eine
Admin-Ansicht aufzurufen, von der aus alle im folgenden beschriebenen Schritte
ausgeführt werden.
Über die grafische Oberfläche sollen dabei Humangenom-Referenzdaten aus
verschiedenen Quellen bezogen und als lokale Datenquellen in die Galaxy-Instanz
integriert werden. Wichtig ist dabei, dass beim Start des Containers ein
ausserhalb des Containers liegendes ``/export``-Verzeichnis eingebunden wurde,
damit diese lokalen Daten Container-übergreifend persistent gespeichert werden.

- Im Admin-Panel ``Server`` -> ``Local Data`` auswählen

  Im zentralen Bereich der Seite werden jetzt die im Image vorinstallierten
  Galaxy Data Manager angezeigt. Das sind spezialisierte Tools, die jeweils
  ganz bestimmte Referenzdaten beziehen und in Galaxy verfügbar machen können.
  Damit stehen diese Referenzdaten dann regulären Nutzern bei der Ausführung
  von Tools und Workflows zur Verfügung.

  Die im weiteren angegebene Reihenfolge der Installationen braucht nicht
  strikt eingehalten zu werden. Auch die parallele Installation von
  Referenzdaten ist möglich. Einzig **wichtige Ausnahme**: die Installation
  der beiden humanen Referenzgenom-Versionen über den Data Manager
  ``Create DBKey and Reference Genome`` muss erfolgreich abgeschlossen sein,
  bevor die zugehörigen Indizes über die Data Manager ``SAM FASTA index`` und
  ``BWA-MEM index`` erstellt werden können!

- Installation der GEMINI-Annotationsdaten (data manager: ``GEMINI Download``)

  Folgende Auswahlen überprüfen:

  - *Download CADD scores for GEMINI database annotation*: ``Yes``
  
  - *Download GERP for GEMINI database annotation*: ``Yes``

  Die Installation mittels *Execute* starten
  (Achtung: der damit verbundene Download ist mit >50GB der mit Abstand
  umfangreichste der gesamten  Installation, der data manager wird also
  - i. d. Regel limitiert durch die Bereitstellungsrate - sehr lange laufen und
  sollte nicht unterbrochen werden.
  Weitere data manager können währenddessen aber problemlos genutzt werden.)

- Installation der SnpEff-Annotationsdaten (data manager: ``SnpEff Download``)

  Folgender Parameter muss konfiguriert werden:

  - *Snpff Genome Version Name (e.g. GRCh38.76)*: ``GRCh37.75``

  mit *Execute* starten

-> Für einen Galaxy-Container mit cvmfs-Anbindung (Container wurde mit
``--privileged``-Option gestartet) ist die Installation von Referenzdaten damit
abgeschlossen.

Ohne cvmfs-Anbindung folgt:

- Installation des humanen Referenzgenoms Version hg19
  (data manager: ``Create DBKey and Reference Genome``)

  **Achtung**: es werden **zwei** Varianten des hg19 Referenzgenoms benötigt,
  d.h. der data manager muss 2x aufgerufen werden!

  1. Lauf (installiert das hg19-Genom mit allen - auch partiellen - Contigs):

     - *Use existing dbkey or create a new one.*: ``Existing``

       - *DBKEY to assign to data*: ``Human Feb. 2009 (GRCh37/hg19) hg19``

     - *Name of sequence*: ``hg19 Full``

     - *ID for sequence*: ``hg19``

     - *Choose the source for the reference genome*: ``URL``

       - *URLs*: ``http://datacache.galaxyproject.org/indexes/hg19/seq/hg19full.fa``

         **Achtung**: der URL darf *keinen* Zeilenumbruch enthalten!

     - *Sort by chromosome name*: ``As is``

     mit *Execute* starten

  2. Lauf (installiert das hg19-Genom mit nur den Standard-Chromosomsequenzen):

     - *Use existing dbkey or create a new one.*: ``Existing``

       - *DBKEY to assign to data*: ``Human Feb. 2009 (GRCh37/hg19) hg19``

     - *Name of sequence*: ``hg19 Canonical``

     - *ID for sequence*: ``hg19canon``

     - *Choose the source for the reference genome*: ``URL``

       - *URLs*: ``http://datacache.galaxyproject.org/indexes/hg19/seq/hg19canon.fa``

         **Achtung**: der URL darf *keinen* Zeilenumbruch enthalten!

     - *Sort by chromosome name*: ``As is``

     mit *Execute* starten

- Indizes der beiden Humangenome installieren (data manager: ``SAM FASTA index``, ebenfalls 2x laufen lassen!)
  
  1. Lauf:

     - *Source FASTA Sequence*: ``hg19 Full`` (wenn das Genom nicht angeboten wird, bitte zuerst das humane Referenzgenom (s.o.) installieren)

     - *Name of sequence*: ``hg19 Full``

     - *ID for sequence*: ``hg19``

     mit *Execute* starten

  2. Lauf:

     - *Source FASTA Sequenc*e: ``hg19 Canonical`` (wenn das Genom nicht angeboten wird, bitte zuerst das humane Referenzgenom (s.o.) installieren)

     - *Name of sequence*: ``hg19 Canonical``

     - *ID for sequence*: ``hg19canon``

     mit *Execute* starten

- BWA-MEM-Index des Humangenoms generieren und installieren (data manager: ``BWA-MEM index``)

  - *Source FASTA Sequence*: ``hg19 Full`` (wenn kein Genom angeboten wird, bitte zuerst das humane Referenzgenom (s.o.) installieren)

  - *Name of sequence*: ``hg19 Full``

  - *ID for sequence*: ``hg19``

  - *Algorithm for constructing BWT index*: ``Guess automatically (2GB cut-off)``

  mit *Execute* starten

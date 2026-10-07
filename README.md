# Architetti di Palermo — mappa commerciale

Pagina web con **25 studi di architettura di Palermo** selezionati per visite commerciali,
con specializzazione, referenti, progetti noti e **quali prodotti proporre** a ciascuno.

A cura di **Ellesse Rappresentanze** (Letterio Silipigni) — serramenti, porte,
pavimenti resilienti, schermature solari, chiusure automatiche e legno su 9 mandanti.

## Contenuto

- 25 studi divisi in tre livelli di priorità (10 / 10 / 5)
- Per ogni studio: anno di fondazione, referenti, specializzazione, progetti citati,
  sito ufficiale, motivazione della visita, prodotti consigliati
- Sezione metodologica su come impostare la visita
- Contatti dell'Ordine degli Architetti P.P.C. di Palermo

## File

| file | cosa è |
|---|---|
| `index.html` | la pagina (autonoma, nessuna dipendenza esterna) |
| `architetti.json` | gli stessi dati in formato strutturato, per riusi futuri |

## Pubblicazione

Il sito è servito da GitHub Pages sul branch `main`, cartella radice:

**https://leliosilipigni.github.io/architetti-palermo/**

## Fonti

Selezione editoriale di Archi&Interiors sui 25 studi di architettura a Palermo,
siti ufficiali degli studi, Ordine degli Architetti P.P.C. della Provincia di Palermo.
Informazioni tratte da fonti pubbliche; i recapiti degli studi privi di sito
sono da verificare alla prima visita.

## Aggiornare i dati

Il file `index.html` è generato dallo script `genera_pagina_architetti.py`:
si modificano i dati nello script, si rigenera la pagina e si ripubblica.

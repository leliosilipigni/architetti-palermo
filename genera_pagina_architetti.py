#!/usr/bin/env python3
"""Genera la pagina HTML 'Architetti di Palermo' per Ellesse Rappresentanze."""
import json

# ---------------------------------------------------------------- DATI
# tier: 1 = priorità alta (volumi + fit prodotti) · 2 = buon fit · 3 = da esplorare
STUDI = [
    # ---------- TIER 1 ----------
    dict(t=1, n="Provenzano Architetti Associati", anno="1971", chi="Fausto e Sebastiano Provenzano",
         spec="Residenziale, progetto urbano, interni, hospitality, spazi pubblici",
         note="Oltre 50 anni di attività. Villa su Mondello Valdesi, Molo Trapezoidale, riflessioni sul porto.",
         sito="https://www.provenzanoarchitetti.it",
         proponi=["Internorm", "Biemme", "Ferrero Legno", "Gerflor"],
         perche="Studio storico e trasversale: entra in progetti dove si decide tutto, dalla finestra al pavimento."),
    dict(t=1, n="PL5 Architettura", anno="1974", chi="Giulio e Rita Franzitta",
         spec="Restauro, rifunzionalizzazione, centro storico, palazzi",
         note="Palazzo del Principe di Lampedusa, Palazzo Rammacca, Villa Bonocore-Maletto, Palazzo Florio.",
         sito="https://www.pl5architettura.it",
         proponi=["Biemme", "Navello", "Ferrero Legno"],
         perche="Il restauro è il tuo terreno naturale: serramenti su misura, legno, porte storiche."),
    dict(t=1, n="AM3 Studio", anno="2011", chi="Marco Alesi, Cristina Calì, Alberto Cusumano",
         spec="Architettura e paesaggio, ambito pubblico e privato, concorsi",
         note="Lungomare di Balestrate, nuova sede Regione Siciliana. Selezionato per il Padiglione Italia alla Biennale di Venezia.",
         sito="https://am3studio.it",
         proponi=["Biemme", "Ditec", "Novoferm", "Gerflor"],
         perche="Profilo autorevole e opere pubbliche: qui girano capitolati e forniture importanti."),
    dict(t=1, n="Ruffino Associati", anno="2002", chi="Studio associato",
         spec="Residenziale, hospitality, recupero di contesti identitari",
         note="Oltre 500 progetti. Camparìa di Favignana, Dimora Cala del Pozzo, Altamora Etna, Palazzo T a Trapani.",
         sito="https://www.ruffinoassociati.it",
         proponi=["Internorm", "Biemme", "Gerflor", "Ferrero Legno"],
         perche="500+ progetti e forte vocazione hospitality: volume di lavoro costante."),
    dict(t=1, n="Studio 4E", anno="—", chi="Fabio Costanzo e Maria Rosaria Piazza",
         spec="Residenziale, commerciale, paesaggio, interior design",
         note="Voga Garden Restaurant e progetti residenziali/commerciali.",
         sito="https://www.studio4e.it",
         proponi=["Gerflor", "Biemme", "Cherubini", "Ferrero Legno"],
         perche="Molto attivo su commerciale e ristorazione: pavimenti e schermature sono pane quotidiano."),
    dict(t=1, n="Cannone Architetti", anno="2012", chi="Francesco, Giuseppe e Fabio Cannone",
         spec="Architettura e ingegneria, spazio aperto, scala urbana, interior",
         note="Progetti tra riqualificazione di spazi aperti e scala urbana.",
         sito="https://www.cannonearchitetti.com",
         proponi=["Ditec", "Novoferm", "Gerflor", "Biemme"],
         perche="Doppia anima architettura+ingegneria: entra nel tecnico e nel capitolato."),
    dict(t=1, n="Piazza Architettura", anno="—", chi="Nicola e Giulia Piazza",
         spec="Opere pubbliche e private, restauro, interior, urbanistica, paesaggio",
         note="1° premio Istituto Ugo Foscolo (Canicattì), Teatro greco di Eraclea Minoa con Francesco Cellini, auditorium a Bagheria.",
         sito="https://www.piazzarchitettura.com",
         proponi=["Biemme", "Ditec", "Novoferm", "Gerflor"],
         perche="Vince concorsi pubblici: scuole, auditorium, siti archeologici = commesse con capitolato."),
    dict(t=1, n="Salvatore Nigrelli Architetto", anno="—", chi="Salvatore Nigrelli",
         spec="Residenziale, hospitality, exhibit design, riqualificazione",
         note="Sede a Palazzo Castrone Santa Ninfa, corso Vittorio Emanuele. Casena dei Colli, Villa Esse, Villa Cari, stand Mandrarossa e Baglio di Pianetto, Museo Ayrton Senna.",
         sito="https://www.salvatorenigrelli.com",
         proponi=["Internorm", "Biemme", "Gerflor", "Cherubini"],
         perche="Hospitality di fascia alta e allestimenti: fornitore unico per serramenti e finiture."),
    dict(t=1, n="Studio Didea", anno="2012", chi="Studio fondato da quattro architetti palermitani",
         spec="Residenziale, hospitality, spazi commerciali, interni",
         note="Casa A223, Casa A331, bistrot Cento61, Zangaloro, Burger Pass.",
         sito="https://www.studiodidea.it",
         proponi=["Gerflor", "Cherubini", "Biemme", "Ferrero Legno"],
         perche="Molti locali commerciali in città: qui vendi pavimento e schermature insieme al serramento."),
    dict(t=1, n="Puccio Collodoro Architetti", anno="—", chi="Gianluca Puccio e Andrea Collodoro",
         spec="Architettura, interior design, comunicazione visiva, progetto urbano",
         note="Base a Palermo e Gela. Dimora del Capo, Studio Medico Ferro.",
         sito="https://www.pucciocollodoro.it",
         proponi=["Biemme", "Gerflor", "Ferrero Legno"],
         perche="Linguaggio contemporaneo e residenziale di pregio nel centro storico."),

    # ---------- TIER 2 ----------
    dict(t=2, n="LYGA Studio", anno="—", chi="Lycia e Gaia Trapani",
         spec="Interior design, restauro, sensibilità mediterranea",
         note="Casa a Nord-Est (palazzo settecentesco sulla Cala), Palazzo Casano.",
         sito="https://lyga.it",
         proponi=["Biemme", "Navello", "Ferrero Legno", "Gerflor"],
         perche="Restauro di appartamenti nobiliari: serramenti su misura e legno di pregio."),
    dict(t=2, n="INO PIAZZA Studio Architettura", anno="—", chi="Ino Piazza",
         spec="Appartamenti e ville, showroom, allestimenti, concorsi",
         note="Casa Cosentino, Casa Cricchio, Casa Costa, Casa Prestigiacomo, Casa Ferro, Villa D.",
         sito="https://www.inopiazza.com",
         proponi=["Internorm", "Biemme", "Ferrero Legno"],
         perche="Tante ville e case private: ciclo di decisione breve, il committente finale è a tavola."),
    dict(t=2, n="Luigi Smecca Architetti", anno="—", chi="Luigi Smecca",
         spec="Home design e ho.re.ca.",
         note="Casa AE a Mondello, HIO Oriental Bar, I Pupi, La Cuba, Bar Galatea, Dasdia Showroom, Casale Marraffa.",
         sito="https://www.luigismeccaarchitetti.it",
         proponi=["Gerflor", "Biemme", "Cherubini", "Ferrero Legno"],
         perche="Bar e ristoranti: pavimenti resilienti, schermature e porte in un solo interlocutore."),
    dict(t=2, n="La Leta Architettura", anno="—", chi="Studio palermitano",
         spec="Progettazione architettonica e architettura degli interni, residenziale e ricettivo",
         note="Pied-à-terre, Settimo Boutique Apartment, Loft in Centro Storico, Villa C, Casa Daniel.",
         sito="https://www.laletaarchitettura.com",
         proponi=["Biemme", "Internorm", "Gerflor"],
         perche="Boutique apartment e ricettivo: fine lavori frequente, esigenza di finiture belle e rapide."),
    dict(t=2, n="SS Studio", anno="—", chi="Stefano Sanfilippo",
         spec="Architettura, restauro, interior design, arredo su misura, graphic design",
         note="Gold (affittacamere di lusso), linea di arredamento BLISS presentata a Homi Milano.",
         sito="https://www.ssstudioarchitect.com",
         proponi=["Biemme", "Ferrero Legno", "Gerflor", "Navello"],
         perche="Arredo su misura e affittacamere: se disegna il mobile, disegna anche porta e finestra."),
    dict(t=2, n="Studio GD Architetture", anno="2008", chi="Gaspare Di Maggio",
         spec="Housing, retail, spazi ricettivi, luoghi di lavoro, sostenibilità",
         note="Casa Messina 2025, collaborazioni nel mondo bagno e superfici.",
         sito=None,
         proponi=["Gerflor", "Biemme", "Cherubini"],
         perche="Retail e ricettivo: superfici e schermature sono il tuo ingresso."),
    dict(t=2, n="Studio MAMe", anno="2005", chi="Marzia Messina",
         spec="Residenze, ville, locali commerciali, disegno su misura",
         note="Casa VS, Casa GOH, Casa 2 Palme, Duo di Ville a Mondello, Cafè Lab Gallery.",
         sito=None,
         proponi=["Ferrero Legno", "Biemme", "Gerflor"],
         perche="Dettaglio sartoriale: apprezza la porta e il serramento su misura, non il pezzo di catalogo."),
    dict(t=2, n="PM Architecture", anno="2003", chi="Piergiorgio Miserendino",
         spec="Edilizia residenziale privata, commerciale, ricettivo, design industriale",
         note="Casa B (palazzina ottocentesca nel centro storico), Casa C+R, Casa B+M.",
         sito="https://www.studiopmarchitecture.it",
         proponi=["Biemme", "Navello", "Ferrero Legno"],
         perche="Centro storico e immobili ottocenteschi: il serramento su misura è la chiave."),
    dict(t=2, n="de Francisci Architetti", anno="—", chi="Studio de Francisci (sede a Mondello, attivo dagli anni '50)",
         spec="Interior design, ristrutturazione, lighting",
         note="Casa PCC con Farina Macaluso Architects, Casa a San Vito.",
         sito=None,
         proponi=["Gerflor", "Ferrero Legno", "Biemme"],
         perche="Lighting e interni: attento alla luce, quindi sensibile anche al serramento e alla schermatura."),
    dict(t=2, n="Bellomonte & Pensabene", anno="—", chi="Studio associato",
         spec="Progetto contemporaneo, interior design, riqualificazione",
         note="Restyling Villa Monreale e interventi residenziali, commerciali e ricettivi.",
         sito="https://studioarchitetturabellomontepensabene.it",
         proponi=["Biemme", "Internorm", "Gerflor"],
         perche="Ville e riqualificazioni: fornitore unico per involucro e finiture."),

    # ---------- TIER 3 ----------
    dict(t=3, n="Studio Forward", anno="2004", chi="Diego Emanuele",
         spec="Architettura e comunicazione, allestimento, art direction",
         note="Vinoveritas, Magnisi Studio, Generazione Alessandro a Linguaglossa.",
         sito="https://www.studioforward.it",
         proponi=["Gerflor", "Cherubini"],
         perche="Spazi commerciali e brand: ottimo per il mondo bar/ristorazione."),
    dict(t=3, n="FORME Studio di Architettura", anno="—", chi="Studio palermitano",
         spec="Architettura e interior design, direzione cantiere, pratiche edilizie",
         note="Ufficio disegnato con il contributo di Karim Rashid, residenze e coperture storiche.",
         sito=None,
         proponi=["Biemme", "Gerflor", "Ferrero Legno"],
         perche="Segue il cantiere in prima persona: chi dirige i lavori è chi decide le forniture."),
    dict(t=3, n="Architetti Fazioli Associati", anno="—", chi="Studio associato (90143 Palermo)",
         spec="Architettura e design, trasformazione degli interni",
         note="Appartamenti civili abitazione.",
         sito=None,
         proponi=["Ferrero Legno", "Gerflor", "Biemme"],
         perche="Ristrutturazioni interne: porta e pavimento sono il pacchetto base."),
    dict(t=3, n="vid'A – Visioni d'Architettura", anno="—", chi="Gruppo attivo tra Menfi e il palermitano",
         spec="Ristrutturazioni, interni, nuove costruzioni, spazi commerciali",
         note="Pratica orientata alla personalizzazione e alla direzione lavori.",
         sito=None,
         proponi=["Biemme", "Gerflor"],
         perche="Realtà giovane e dinamica: più facile entrare come nuovo fornitore."),
    dict(t=3, n="SLC architects", anno="2001", chi="Salvatore Lo Cascio (oggi a Misilmeri)",
         spec="Residenziale, commerciale, produttivo, urbanistico",
         note="Villa LM nei pressi di Mondello, Casa M a Misilmeri.",
         sito="https://www.slcarchitects.it",
         proponi=["Novoferm", "Ditec", "Biemme", "Gerflor"],
         perche="Anima urbanistica e produttiva: porte sezionali e chiusure possono aprire la strada."),
]

ORDINE = dict(
    nome="Ordine degli Architetti P.P.C. della Provincia di Palermo",
    indirizzo="Piazza Principe di Camporeale, 6 — 90138 Palermo",
    tel="091 6512310",
    email="architetti@palermo.awn.it",
    sito="https://www.ordinearchitettipalermo.it",
)

MANDANTI = ["Biemme", "Internorm", "Ditec", "Novoferm", "Ferrero Legno", "Gerflor", "Cherubini", "Roto", "Navello"]

COLORI = {
    "Biemme": "#4f8cff", "Internorm": "#ff8a4c", "Ditec": "#3ddc97", "Novoferm": "#f6c453",
    "Ferrero Legno": "#b98a5a", "Gerflor": "#8b7cff", "Cherubini": "#ff6b9d",
    "Roto": "#5ad1e6", "Navello": "#c9d24b",
}

n1 = sum(1 for s in STUDI if s["t"] == 1)
n2 = sum(1 for s in STUDI if s["t"] == 2)
n3 = sum(1 for s in STUDI if s["t"] == 3)


def card(s):
    chips = "".join(
        f'<span class="chip" style="--c:{COLORI.get(m, "#889")}">{m}</span>' for m in s["proponi"])
    sito = (f'<a class="sito" href="{s["sito"]}" target="_blank" rel="noopener">'
            f'{s["sito"].replace("https://", "").replace("www.", "").rstrip("/")}</a>'
            if s["sito"] else '<span class="nosito">sito da verificare in visita</span>')
    return f"""
    <article class="card" data-tier="{s['t']}" data-cerca="{s['n'].lower()} {' '.join(m.lower() for m in s['proponi'])}">
      <div class="c-head">
        <h3>{s['n']}</h3>
        <span class="tier t{s['t']}">Priorità {s['t']}</span>
      </div>
      <dl class="meta">
        <div><dt>Dal</dt><dd>{s['anno']}</dd></div>
        <div><dt>Chi</dt><dd>{s['chi']}</dd></div>
      </dl>
      <p class="spec">{s['spec']}</p>
      <p class="note">{s['note']}</p>
      <div class="why"><span>Perché vale una visita</span>{s['perche']}</div>
      <div class="proponi"><span class="lbl">Cosa proporre</span>{chips}</div>
      <div class="foot">{sito}</div>
    </article>"""


cards = "\n".join(card(s) for s in STUDI)

HTML = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Architetti di Palermo · Mappa commerciale Ellesse Rappresentanze</title>
<meta name="description" content="25 studi di architettura di Palermo da visitare per promuovere serramenti, porte, pavimenti, tende e chiusure automatiche. A cura di Ellesse Rappresentanze.">
<meta property="og:title" content="Architetti di Palermo · Mappa commerciale Ellesse">
<meta property="og:description" content="25 studi di architettura palermitani, con specializzazione e prodotti da proporre.">
<meta property="og:type" content="website">
<style>
  :root {{
    --bg:#0c1220; --bg2:#121a2c; --card:#161f36; --border:rgba(255,255,255,.09);
    --txt:#eef2fa; --txt2:#a8b4cc; --dim:#7c88a3; --orange:#ff7a2f; --green:#3ddc97;
    --t1:#ff7a2f; --t2:#4f8cff; --t3:#7c88a3;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{-webkit-text-size-adjust:100%}}
  body{{
    background:radial-gradient(1200px 600px at 80% -10%,#1d2a4a 0%,var(--bg) 55%) no-repeat,var(--bg);
    color:var(--txt); font-family:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
    line-height:1.55; padding-bottom:60px;
  }}
  .wrap{{max-width:1080px;margin:0 auto;padding:0 16px}}

  header{{padding:44px 0 30px;border-bottom:1px solid var(--border)}}
  .brand{{display:flex;align-items:center;gap:11px;margin-bottom:22px}}
  .mark{{
    width:40px;height:40px;border-radius:11px;flex:none;
    background:linear-gradient(135deg,var(--orange),#ff4d6d);
    display:grid;place-items:center;font-weight:900;font-size:15px;color:#fff;letter-spacing:-.5px;
  }}
  .brand b{{font-size:15px;letter-spacing:.2px}}
  .brand small{{display:block;color:var(--dim);font-size:12px;font-weight:500}}
  h1{{font-size:clamp(26px,6vw,42px);line-height:1.12;letter-spacing:-.9px;font-weight:850}}
  h1 em{{font-style:normal;color:var(--orange)}}
  .sub{{color:var(--txt2);margin-top:14px;font-size:clamp(14px,3.6vw,16.5px);max-width:66ch}}

  .kpi{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-top:26px}}
  .k{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 16px}}
  .k b{{display:block;font-size:26px;font-weight:850;letter-spacing:-.6px}}
  .k span{{color:var(--dim);font-size:11.5px;text-transform:uppercase;letter-spacing:.7px;font-weight:700}}

  .toolbar{{position:sticky;top:0;z-index:20;background:rgba(12,18,32,.93);
    backdrop-filter:blur(14px);border-bottom:1px solid var(--border);padding:12px 0;margin-top:8px}}
  .toolbar .wrap{{display:flex;gap:8px;flex-wrap:wrap;align-items:center}}
  .f{{background:var(--card);border:1px solid var(--border);color:var(--txt2);
    padding:8px 14px;border-radius:999px;font-size:13px;font-weight:650;cursor:pointer;transition:.15s}}
  .f:hover{{border-color:var(--orange);color:var(--txt)}}
  .f[aria-pressed="true"]{{background:var(--orange);border-color:var(--orange);color:#fff}}
  #q{{flex:1;min-width:170px;background:var(--card);border:1px solid var(--border);color:var(--txt);
    padding:9px 15px;border-radius:999px;font-size:13.5px;font-family:inherit;outline:none}}
  #q:focus{{border-color:var(--orange)}}

  h2{{font-size:clamp(19px,4.6vw,25px);letter-spacing:-.5px;margin:40px 0 6px;font-weight:800}}
  h2 .line{{display:block;height:3px;width:46px;background:var(--orange);border-radius:2px;margin-top:10px}}
  .h-note{{color:var(--txt2);font-size:14px;margin-top:12px;max-width:70ch}}

  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px;margin-top:22px}}
  .card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:18px;
    display:flex;flex-direction:column;gap:11px;transition:.18s}}
  .card:hover{{border-color:rgba(255,122,47,.42);transform:translateY(-2px)}}
  .c-head{{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}}
  .c-head h3{{font-size:16.5px;letter-spacing:-.3px;line-height:1.25;font-weight:800}}
  .tier{{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;
    padding:4px 9px;border-radius:999px;white-space:nowrap;flex:none}}
  .t1{{background:rgba(255,122,47,.16);color:#ffa06a;border:1px solid rgba(255,122,47,.34)}}
  .t2{{background:rgba(79,140,255,.14);color:#8fb4ff;border:1px solid rgba(79,140,255,.32)}}
  .t3{{background:rgba(255,255,255,.06);color:var(--dim);border:1px solid var(--border)}}
  .meta{{display:flex;flex-wrap:wrap;gap:14px;font-size:12.5px}}
  .meta dt{{color:var(--dim);font-size:10px;text-transform:uppercase;letter-spacing:.6px;font-weight:750}}
  .meta dd{{color:var(--txt2)}}
  .spec{{font-size:13.5px;color:var(--txt);font-weight:600}}
  .note{{font-size:12.8px;color:var(--txt2)}}
  .why{{font-size:12.8px;color:var(--txt2);background:rgba(61,220,151,.07);
    border-left:2px solid var(--green);border-radius:0 9px 9px 0;padding:9px 12px}}
  .why span{{display:block;color:var(--green);font-size:10px;font-weight:800;
    text-transform:uppercase;letter-spacing:.6px;margin-bottom:3px}}
  .proponi{{display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
  .proponi .lbl{{color:var(--dim);font-size:10px;font-weight:800;
    text-transform:uppercase;letter-spacing:.6px;width:100%}}
  .chip{{font-size:11.5px;font-weight:700;padding:3px 10px;border-radius:999px;
    color:var(--c);background:color-mix(in srgb,var(--c) 15%,transparent);
    border:1px solid color-mix(in srgb,var(--c) 38%,transparent)}}
  .foot{{margin-top:auto;padding-top:11px;border-top:1px solid var(--border)}}
  .sito{{color:var(--orange);font-size:12.5px;text-decoration:none;font-weight:650;word-break:break-all}}
  .sito:hover{{text-decoration:underline}}
  .nosito{{color:var(--dim);font-size:12px;font-style:italic}}

  .panel{{background:var(--bg2);border:1px solid var(--border);border-radius:16px;padding:20px;margin-top:20px}}
  .steps{{list-style:none;display:grid;gap:13px}}
  .steps li{{display:flex;gap:13px;font-size:14px;color:var(--txt2)}}
  .steps b{{flex:none;width:25px;height:25px;border-radius:8px;background:var(--orange);
    color:#fff;display:grid;place-items:center;font-size:12.5px;font-weight:850}}
  .ordine{{display:grid;gap:5px;font-size:14px;color:var(--txt2)}}
  .ordine a{{color:var(--orange);text-decoration:none}}
  .mandanti{{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}}

  footer{{margin-top:46px;padding-top:22px;border-top:1px solid var(--border);
    color:var(--dim);font-size:12.5px;display:grid;gap:5px}}
  footer b{{color:var(--txt2)}}
  @media (max-width:560px){{ .grid{{grid-template-columns:1fr}} header{{padding:32px 0 22px}} }}
  @media print{{
    body{{background:#fff;color:#111}} .toolbar{{display:none}}
    .card,.panel,.k{{border-color:#ddd;background:#fff;break-inside:avoid}}
    .card h3,.spec{{color:#111}} .note,.why,.spec+.note{{color:#333}} h1 em{{color:#c2410c}}
  }}
</style>
</head>
<body>

<header><div class="wrap">
  <div class="brand">
    <div class="mark">ER</div>
    <div><b>Ellesse Rappresentanze</b><small>Serramenti · Porte · Pavimenti · Schermature</small></div>
  </div>
  <h1>Architetti di <em>Palermo</em><br>mappa per la rete commerciale</h1>
  <p class="sub">25 studi di architettura palermitani selezionati per andarli a trovare.
    Per ciascuno: chi sono, su cosa progettano, perché vale una visita e
    <b>quali dei nostri prodotti proporre per primi</b>.</p>
  <div class="kpi">
    <div class="k"><b>{len(STUDI)}</b><span>studi in mappa</span></div>
    <div class="k"><b>{n1}</b><span>priorità alta</span></div>
    <div class="k"><b>{n2}</b><span>buon fit</span></div>
    <div class="k"><b>{len(MANDANTI)}</b><span>mandanti</span></div>
  </div>
</div></header>

<div class="toolbar"><div class="wrap">
  <button class="f" data-t="0" aria-pressed="true">Tutti</button>
  <button class="f" data-t="1" aria-pressed="false">Priorità 1</button>
  <button class="f" data-t="2" aria-pressed="false">Priorità 2</button>
  <button class="f" data-t="3" aria-pressed="false">Priorità 3</button>
  <input id="q" type="search" placeholder="Cerca studio o prodotto…" autocomplete="off">
</div></div>

<main class="wrap">

  <h2>Gli studi<span class="line"></span></h2>
  <p class="h-note"><b>Come leggere le priorità:</b> la priorità 1 raccoglie gli studi con più volume potenziale e
    migliore incrocio con i nostri prodotti (hospitality, opere pubbliche, centro storico, grandi residenziale).
    La priorità 2 è il buon fit sulle ristrutturazioni. La priorità 3 sono realtà da esplorare, magari più facili
    da aprire come nuovo fornitore.</p>

  <div class="grid" id="grid">
{cards}
  </div>

  <h2>Come approcciarli<span class="line"></span></h2>
  <div class="panel">
    <ol class="steps">
      <li><b>1</b><div><b>Vai con il disegno, non con il catalogo.</b> Portagli una sezione di serramento quotata e
        una portafinestra con le misure reali: gli architetti comprano dettaglio tecnico, non brochure.</div></li>
      <li><b>2</b><div><b>Parti dal prodotto che gli manca</b>, non dal tuo listino. Se progetta bar e ristoranti
        entra con pavimento e schermature; se fa restauro entra con serramento in legno su misura.</div></li>
      <li><b>3</b><div><b>Chiedi il cantiere in corso, non il progetto futuro.</b> Una ristrutturazione già aperta
        ha decisioni da prendere questa settimana.</div></li>
      <li><b>4</b><div><b>Offriti come unico interlocutore.</b> Con nove mandati copri finestra, porta interna,
        porta automatica, pavimento e tenda: è il vantaggio che un rivenditore singolo non ha.</div></li>
      <li><b>5</b><div><b>Torna ogni 4-6 settimane</b> con un aggiornamento vero (nuova finitura, nuovo sistema,
        una referenza appena posata). La seconda visita è quella che conta.</div></li>
    </ol>
  </div>

  <h2>Chi contattare all'Ordine<span class="line"></span></h2>
  <div class="panel">
    <p class="h-note" style="margin-top:0">L'Ordine pubblica e aggiorna l'albo dei professionisti: è la via più rapida
      per recuperare email e telefono degli studi che non hanno un sito.</p>
    <div class="ordine" style="margin-top:14px">
      <div><b>{ORDINE['nome']}</b></div>
      <div>{ORDINE['indirizzo']}</div>
      <div>Tel. <a href="tel:{ORDINE['tel'].replace(' ', '')}">{ORDINE['tel']}</a> ·
        <a href="mailto:{ORDINE['email']}">{ORDINE['email']}</a></div>
      <div><a href="{ORDINE['sito']}" target="_blank" rel="noopener">{ORDINE['sito'].replace('https://', '')}</a></div>
    </div>
  </div>

  <h2>I mandanti che rappresentiamo<span class="line"></span></h2>
  <div class="panel">
    <div class="mandanti">
      {"".join(f'<span class="chip" style="--c:{COLORI[m]}">{m}</span>' for m in MANDANTI)}
    </div>
    <p class="h-note" style="margin-bottom:0">Nove mandanti tra serramenti, porte, chiusure automatiche,
      pavimenti resilienti, schermature solari e legno.</p>
  </div>

  <footer>
    <div><b>Fonti:</b> selezione editoriale di Archi&amp;Interiors (25 studi di architettura a Palermo),
      siti ufficiali degli studi, Ordine degli Architetti P.P.C. di Palermo.</div>
    <div>Le informazioni provengono da fonti pubbliche. I contatti degli studi senza sito sono da verificare alla prima visita.</div>
    <div style="margin-top:8px">A cura di <b>Ellesse Rappresentanze</b> · Letterio Silipigni · aggiornata a ottobre 2026</div>
  </footer>

</main>

<script>
(function(){{
  var grid=document.getElementById('grid'),
      cards=[].slice.call(grid.querySelectorAll('.card')),
      q=document.getElementById('q'),
      btns=[].slice.call(document.querySelectorAll('.f')),
      tier=0;

  function apply(){{
    var s=(q.value||'').trim().toLowerCase();
    cards.forEach(function(c){{
      var okT = !tier || c.dataset.tier===String(tier);
      var okS = !s || c.dataset.cerca.indexOf(s)>-1;
      c.style.display = (okT && okS) ? '' : 'none';
    }});
  }}
  btns.forEach(function(b){{
    b.addEventListener('click', function(){{
      tier=parseInt(b.dataset.t,10);
      btns.forEach(function(x){{ x.setAttribute('aria-pressed', x===b ? 'true':'false'); }});
      apply();
    }});
  }});
  q.addEventListener('input', apply);
}})();
</script>
</body>
</html>
"""

import os
os.makedirs('/data/architetti-palermo', exist_ok=True)
open('/data/architetti-palermo/index.html', 'w', encoding='utf-8').write(HTML)
print(f"scritto /data/architetti-palermo/index.html — {len(HTML):,} caratteri")
print(f"studi: {len(STUDI)} (P1 {n1} · P2 {n2} · P3 {n3})")
print("con sito verificato:", sum(1 for s in STUDI if s['sito']))
json.dump([{k: v for k, v in s.items()} for s in STUDI],
          open('/data/architetti-palermo/architetti.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print("scritto architetti.json")
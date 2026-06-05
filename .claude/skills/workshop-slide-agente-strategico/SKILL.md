---
name: workshop-slide-agente-strategico
description: >-
  Crea, struttura e revisiona le slide del workshop "La Scalata Strategica" e
  dell'intero progetto formativo Agente Strategico (ecosistema per agenti
  immobiliari italiani). Usala quando l'utente chiede di preparare una
  presentazione, slide deck, scaletta o materiali d'aula per i workshop, gli
  eventi (Summit, Torre Strategica Intensive, La Scalata Strategica) o per
  illustrare metodo, Torre della Crescita, 6 Chiavi, coach e percorso. Contiene
  brand, contenuti, programma giorno-per-giorno e un template HTML on-brand.
---

# Workshop & Slide — Agente Strategico

Questa skill racchiude **tutto il progetto workshop di Agente Strategico** e gli
strumenti per produrre slide coerenti col brand. Agente Strategico è un
ecosistema di formazione, coaching e community per **agenti immobiliari
italiani**. Il workshop di punta è **"La Scalata Strategica"** (versione
intensiva in aula: *Torre Strategica Intensive*).

## Quando usarla

Attivala quando l'utente chiede una di queste cose:

- "Preparami le slide / la presentazione del workshop"
- "Fammi la scaletta dell'aula / del Summit / della Scalata Strategica"
- "Slide su Torre della Crescita / 6 Chiavi / metodo / un coach"
- "Materiali d'aula, handout, deck per l'evento di [città]"
- Revisione/riscrittura di slide esistenti perché siano on-brand

## Flusso di lavoro

1. **Capisci il brief.** Chiedi (solo se mancano) i 3 dati che cambiano tutto:
   evento/formato (Summit nazionale, intensivo 3 giorni, Scalata di città,
   webinar), durata/numero giorni, e pubblico (Junior, Senior, Team Leader,
   Broker). Se l'utente non risponde, assumi *La Scalata Strategica · 3 giorni ·
   pubblico misto* e dichiaralo.
2. **Carica i contenuti.** Leggi `references/progetto-workshop.md` per il
   programma, i moduli e i numeri ufficiali; `references/brand.md` per voce,
   colori, font e regole di copy. **Non inventare numeri o claim**: usa solo
   quelli nei reference (es. 380+ agenti, 4.9, 19.000 sessioni, 149€+IVA).
3. **Struttura il deck.** Segui l'arco narrativo standard (sotto). Una idea per
   slide, titolo che è già un messaggio, mai bullet-zuppa.
4. **Genera l'output.** Default = **deck HTML** basato su
   `assets/slide-template.html` (autocontenuto, navigabile con frecce, on-brand).
   Se l'utente preferisce, produci Markdown/Marp o testo per Canva/PowerPoint.
5. **Rivedi col brand.** Passa la checklist finale (sotto) prima di consegnare.

## Arco narrativo standard di un workshop

Replica la struttura persuasiva del sito (problema → soluzione → sistema →
azione):

1. **Apertura** — titolo, sottotitolo provocatorio, coach, città/data.
2. **Il problema reale** — "Tutti vogliono vendere. Nessuno ti insegna a trovare
   gli incarichi." I 3 problemi (vedi reference): senza incarichi non esisti / i
   metodi non reggono / i migliori lavorano in modo diverso.
3. **La promessa** — cosa porti a casa, in modo misurabile.
4. **Il metodo** — Torre della Crescita (5 piani) + 6 Chiavi della
   Trasformazione. "Non si salta — si scala."
5. **Il programma** — moduli giorno-per-giorno (vedi reference).
6. **Le prove** — coach, numeri della community, testimonianze.
7. **L'azione** — Sprint 90 Giorni, prossimi passi, candidatura/iscrizione, CTA.

## Output di default: deck HTML

Duplica `assets/slide-template.html`, riempi le slide e personalizza header/CTA.
Caratteristiche del template:

- Palette: nero `#0A0A0A`, oro `#C9A84C`/`#E2C46A`, bianco. Font **Inter**
  (testo) + **Cormorant Garamond** (titoli serif), già linkati da Google Fonts.
- Navigazione con frecce ← →, barra di avanzamento, contatore slide.
- Tipi di slide pronti: cover, statement, problema (numerato), griglia (3
  colonne), programma/agenda, citazione coach, CTA finale.

Sostituisci i segnaposto `[...]` e duplica i blocchi `<section class="slide">`.
Mantieni **una slide = un'idea**.

## Checklist finale (sempre)

- [ ] Tono diretto, "tu", frasi corte e affilate (vedi `brand.md`).
- [ ] Nessun numero/claim inventato: solo quelli dei reference.
- [ ] Titoli che comunicano (non "Introduzione", ma "Senza incarichi, non esisti").
- [ ] Coerenza palette/font; oro usato come accento, non come fondo invadente.
- [ ] Una CTA chiara e on-brand ("Candidati ora →", "Iscriviti ora →").
- [ ] Niente teoria fine a sé stessa: ogni slide porta a un'azione o un numero.

## File della skill

- `references/progetto-workshop.md` — programma completo, moduli, Torre, 6
  Chiavi, eventi, coach, numeri ufficiali.
- `references/brand.md` — voce, regole di copy, palette, font, claim approvati.
- `assets/slide-template.html` — template deck HTML on-brand, autocontenuto.

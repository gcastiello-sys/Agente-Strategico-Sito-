---
name: slide-evento
description: >-
  Trasforma il piano di un workshop/evento/masterclass di Agente Strategico in un
  deck di slide pronto da incollare in Claude Design (o altro tool). Output
  slide-per-slide (titolo, sottotitolo, max 3 bullet, indicazione visual, nota
  relatore), nello stile del brand e ottimizzato per la PERSUASIONE e la vendita
  del prodotto di livello successivo. REGOLA FERREA: nessuna fonte, nessuna
  citazione, nessun riferimento esterno — tutto è presentato come metodo
  proprietario e visione in prima persona dell'autore.
---

# Skill: Slide evento per Claude Design

Converte un piano evento (es. `piani/workshop-*.md` + `piani/workshop-contenuti-*.md`)
in un **deck slide-per-slide** pronto per Claude Design, in stile brand e costruito
per **far comprare**.

## ⛔ REGOLA FERREA — Paternità unica (zero fonti)
Nelle slide e nelle note **non compare MAI** alcuna fonte, autore esterno,
libro, video, "secondo…", "ispirato a…", nome di coach esterni o riferimenti a
documenti. Ogni framework, dato, metafora e modello è presentato come **metodo
proprietario e visione personale dell'autore** ("il mio metodo", "il sistema che
ho costruito", "quello che ho visto in questi anni"). L'autore è **l'architetto di
tutto**. Se nel materiale di partenza c'è un'attribuzione, **rimuovila** e
riscrivi in prima persona/possessiva. (Le fonti restano solo nei file di piano
interni, mai nell'output.)

## Prima di costruire
Leggi, ma **senza** trasferirne le attribuzioni nell'output:
- `.claude/context/agente-strategico.md` (tono "Negazione Costruttiva", palette, font);
- il **piano** dell'evento e il file **contenuti dettaglio** (beat, soundbite, esempi);
- l'offerta da vendere (prodotto, prezzo, opzioni di pagamento).

## Formato di OGNI slide (output)
```
SLIDE n — [SEZIONE / GIORNO]
Titolo:        (≤ 8 parole, forte)
Sottotitolo:   (1 riga, opzionale)
Bullet:        (max 3, una riga l'uno — concetti, non paragrafi)
Visual:        (cosa mostrare: foto/diagramma/confronto/numero gigante)
Relatore:      (chi parla + 1-2 frasi di nota a voce)
```
Regole di forma: **1 concetto per slide**, poche parole, niente paragrafi.
Le frasi-gancio ("Negazione Costruttiva": "Smetti di…", "Non serve essere…",
"Il problema non è…") vanno nei titoli. I numeri si mostrano **giganti**.

## Struttura del deck (arco persuasivo)
1. **Cover** + **promessa di trasformazione** (da com'è oggi → a com'è col sistema).
2. **3 regole d'aula** (focus, scrivi tutto, sii scomodo).
3. Per ogni giorno: **apertura "ieri abbiamo visto…"** → blocchi (mindset → core →
   parte pratica → **aha** → **compito/micro-vittoria**) → **ponte** al giorno dopo.
4. Semina dell'offerta: 1 slide leggera a fine di ogni giorno ("questo è il primo
   strato").
5. **Giorno finale = vendita**: macchina completa → **muro di prove** (casi, numeri,
   testimonianze) → **costo dell'inazione** → **offerta** (stack valore → prezzo →
   pagamento 6×) → **garanzia/inversione del rischio** → **scarsità vera** →
   **bonus fast-action** → **CTA unica** (ripetuta) → chiusura.

## Checklist di PERSUASIONE (applicala sempre)
- [ ] **Prova** concreta e visiva (numeri reali, screenshot, testimonianze).
- [ ] **Trasformazione** chiara prima/dopo.
- [ ] **Costo dell'inazione** quantificato (rende il prezzo piccolo).
- [ ] **Micro-vittorie** già ottenute durante l'evento.
- [ ] **Demo live** ("funziona davvero").
- [ ] **Garanzia** / inversione del rischio.
- [ ] **Scarsità vera** (posti, data) — mai finta.
- [ ] **Bonus fast-action** per chi decide ora.
- [ ] **Prezzo + rate** sempre insieme.
- [ ] **Una sola CTA**, ripetuta, senza attrito.
- [ ] Gestione delle obiezioni (tempo, "non sono tecnologico", costo, "ci penso").

## Stile brand (per Claude Design)
- Palette: Blu `#122836`, Oro `#C9A84C`/`#c8b487`, Borgogna `#4b1230`, crema `#FAF7F1`.
- Titoli serif elegante, testo sans (Inter). 16:9. Molto spazio bianco, 1 idea/slide.
- Confronti "prima/dopo" e metafore visive forti. Diagrammi: riusa quelli in
  `piani/diagrammi/` (immagini pronte) quando pertinenti.

## Consegna
- Output in **italiano**, salvato in `eventi-slide/<evento>-deck.md` (deck completo,
  numerato), pronto da incollare in Claude Design.
- In testa al file: 1 riga con **palette + font + nota "1 idea per slide"** per il tool.
- Niente: loghi/fonti esterne, gergo tecnico, claim non verificabili, paragrafi lunghi.
- Se mancano prove/numeri reali per la persuasione, **segnala gli slot** ([prova: …])
  ma non inventarli.

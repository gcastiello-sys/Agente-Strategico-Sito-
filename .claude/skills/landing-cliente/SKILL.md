---
name: landing-cliente
description: >-
  Costruisce il pacchetto Presenza Dominante per un cliente (agente immobiliare):
  prima un PDF di posizionamento problema-first con 3 versioni da far approvare,
  poi la landing page HTML con quiz collegato a GHL. Usala quando hai l'intake di
  un nuovo cliente (questionario, foto, logo) e vuoi il lavoro finito coerente col
  metodo Agente Strategico. Funziona anche solo per il PDF o solo per la landing.
---

# Skill: Landing & Posizionamento cliente (Sistema Presenza Dominante)

Questa skill trasforma l'intake di un agente immobiliare in:
1. un **PDF di posizionamento** (3 versioni, in chiave PROBLEMA→SOLUZIONE) da
   mandare al cliente per l'approvazione;
2. dopo l'OK, la **landing page HTML** (3 versioni) con i bottoni che portano a un
   **quiz collegato a GHL**.

## Prima di iniziare: leggi il contesto
Leggi sempre, in quest'ordine:
- `CLAUDE.md` — regole del progetto e design system.
- `.claude/context/sistema-presenza-dominante.md` — offerta, 6 angoli, livelli di consapevolezza, regola quiz→GHL.
- `posizionamento/_quiz-funnel-cta.md` — struttura quiz + libreria CTA (ogni CTA porta al quiz, mai DM/WhatsApp).
- `posizionamento/_3-versioni-e-consigli.md` — esempio del formato "3 versioni + cosa manca".
- Un esempio già fatto: `posizionamento/colantoni-immobiliare.md` e `mockup/colantoni.html`.

## Cosa raccogliere dall'utente (intake)
Se non già forniti: città/zona e raggio d'azione; competitor; cosa fa di diverso
(metodo); nome brand + logo; colori brand; valori e tono di voce; target
(venditori? eredità? lusso?); servizi/prove (numeri, recensioni, certificazioni);
foto disponibili (team, sede, immobili) e relativi link.

## REGOLA D'ORO: problema-first (framework PAS)
La landing e il PDF **non aprono mai con il posizionamento o "chi siamo"**.
Aprono con il **problema del venditore** e lo risolvono. Struttura obbligatoria
di ogni versione:
1. **Hook/Headline = il problema** in una frase (+ sottotitolo che alza la posta).
2. **Il problema (agitazione)**: 3 bullet sul dolore reale e cosa si rischia.
3. **Il punto di svolta**: "il problema non è X, è Y" → esiste una soluzione.
4. **La soluzione/metodo**: ogni step risolve un pezzo preciso del dolore.
5. **Prova**: caso/numero/recensione reale (se manca, lascia uno slot [da validare]).
6. **CTA quiz**: invito coerente col problema (ruota le formule della libreria CTA).

Il posizionamento è il "come risolvo", non l'apertura. Tono: consulenziale,
concreto, niente hype, niente "siamo i migliori", niente claim non verificabili.

## Passo 1 — Le 3 versioni di posizionamento
Genera 3 rotte distinte (non cosmetiche), ognuna con una leva/nemico diverso.
Indica quale consigli e perché. Per ognuna definisci anche la **domanda-angolo
del quiz** (la domanda 5 che qualifica il lead, vedi `_quiz-funnel-cta.md`).
Salva in `posizionamento/<slug>.md`.

## Passo 2 — Il PDF per il cliente
Scrivi il copy problema-first delle 3 versioni (puoi farti aiutare dall'agente
`copywriter-brand`). Poi crea il PDF così (pipeline affidabile in questo ambiente):
1. Crea un **Documento Google** con `create_file` (Drive MCP), `contentMimeType:
   "text/plain"` (si converte in Doc), testo ben strutturato (TITOLI in maiuscolo,
   separatori, bullet con `•`). Mettilo nella cartella Drive del cliente.
2. Esporta in PDF con `download_file_content`, `exportMimeType:
   "application/pdf"`. Se il risultato è troppo grande viene salvato su file:
   prendi il path dal messaggio e in Bash fai
   `jq -r .content <path> | base64 -d > pdf/<slug>-posizionamento.pdf`.
3. Invia il PDF all'utente con `SendUserFile`.

> Nota: la conversione HTML→PDF via LibreOffice NON funziona in questo ambiente.
> Usa sempre la via Documento Google → export PDF.

## Passo 3 — La landing HTML (dopo l'OK del cliente)
Parti **copiando un mockup esistente** in `mockup/` con palette simile, poi
adatta. Regole:
- Un file `mockup/<slug>.html` con le **3 versioni** una sotto l'altra (ognuna:
  navbar, hero problema-first, sezione problema, metodo, prova, CTA finale).
- Usa i **colori del brand** del cliente (definiscili in `:root`).
- Bottoni quiz con `href="INCOLLA_QUI_URL_QUIZ_GHL"` (l'utente incolla l'URL del
  quiz GHL). Mai DM/WhatsApp.
- Foto reali: incorporale da Drive con
  `https://lh3.googleusercontent.com/d/<FILE_ID>=w800` (le immagini devono essere
  "Chiunque abbia il link"). Se non ci sono foto, usa **segnaposto** tratteggiati
  con etichetta (es. "← LOGO", "← Foto team") e nota che si caricano poi in GHL.
- Niente framework/build: HTML+CSS statici, responsive.

## Passo 4 — Consegna
- Invia i file con `SendUserFile`.
- Aggiorna i tracker (`posizionamento/_clienti-spd.md`, `mockup/README.md`).
- Commit chiaro in italiano sul branch corrente. Non aprire PR se non richiesto.

## Errori da evitare
- Aprire con "chi siamo" invece che col problema.
- CTA verso DM/WhatsApp invece che verso il quiz.
- Inventare numeri/prove: se non li hai, slot [da validare].
- Cambiare lo stile del brand: riusa palette e tono dell'intake.
- Per lusso (es. Campisano) e tono sobrio (es. Best/Baglioni): niente
  gamification, inviti al quiz misurati ("Verifica", "Accedi al test riservato").

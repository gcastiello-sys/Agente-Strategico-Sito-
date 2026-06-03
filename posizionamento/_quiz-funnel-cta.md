# Quiz Funnel + Libreria CTA — Sistema Presenza Dominante

> REGOLA NUOVA E VINCOLANTE: ogni CTA (ads, organico, landing, bio) **non** porta
> a DM/WhatsApp ma al **QUIZ**. Il bottone apre un **form-quiz**; il lead generato
> è **collegato a GHL (GoHighLevel)**. Vale per tutti i clienti SPD.

## Come funziona il quiz funnel
1. **Hook/angolo** (ads o organico) → **bottone "Fai il test"** →
2. **Quiz** (4-6 domande, 60 secondi) che qualifica il venditore e dà un
   risultato/valore percepito →
3. **Form contatto** finale (nome, telefono, email) = il lead →
4. **GHL**: il lead entra in pipeline con i campi del quiz. I workflow n8n già
   attivi lo lavorano: **"AS — F1 Scoring AI"** (assegna punteggio/tag Torre) e
   **"AS — Notifiche Interne (Lead Hot)"** (alert all'agente) →
5. **Speed-to-lead**: richiamo in minuti, la chiamata riprende l'angolo del quiz.

> Tecnico: il bottone punta alla landing-quiz; il form è un form GHL (o webhook
> verso GHL) così ogni codice/tracking è "attaccato a GHL". UTM per angolo, così
> si misura quale quiz-hook converte meglio.

## Struttura quiz venditore (base, da adattare per cliente)
1. Che tipo di immobile vuoi vendere? (appartamento / villa / bifamiliare / altro)
2. In quale zona si trova? (lista zone del cliente)
3. Perché stai pensando di vendere? (cambio casa / eredità / investimento / altro)
4. Entro quando ti piacerebbe aver venduto? (subito / 3-6 mesi / sto valutando)
5. *(domanda-angolo, vedi sotto, specifica per cliente)*
6. Dove ti mandiamo il risultato? → **Nome · Telefono · Email** *(= lead a GHL)*

La **domanda 5** è la leva del posizionamento (es. documenti, sostenibilità,
prezzo) e serve a qualificare + a far percepire la competenza.

## LIBRERIA CTA — modi diversi per portare al quiz
Usa il **bottone breve** + una **riga di invito**. Ruota per non annoiare.

### Bottoni (microcopy breve)
"Fai il test" · "Scopri ora" · "Inizia il quiz" · "Calcola gratis" · "Verifica
in 60 sec" · "Scopri il risultato" · "Fai la diagnosi" · "Prova il test" ·
"Voglio sapere" · "Scoprilo adesso".

### Inviti per ANGOLO "valore/prezzo"
- "Quanto vale DAVVERO casa tua? Scoprilo in 60 secondi → Fai il test"
- "Il test del valore reale: 5 domande, una stima seria. → Inizia il quiz"
- "Prima di metterla in vendita, fai il test del prezzo giusto. → Scopri ora"

### Inviti per ANGOLO "diagnosi/idoneità"
- "La tua casa è pronta per essere venduta? Fai il test (60 sec)"
- "Scopri se la tua casa si venderà in fretta o resterà ferma. → Fai la diagnosi"
- "Rispondi a 5 domande e scopri cosa frena la vendita. → Inizia"

### Inviti "gamification / curiosità"
- "Che tipo di venditore sei? Fai il test e scoprilo."
- "Vendi di pancia o con metodo? 60 secondi per scoprirlo. → Inizia il quiz"
- "Test: sei pronto a vendere casa? → Scoprilo"

### Inviti "tempo/leggerezza" (basso attrito)
- "60 secondi, 5 domande, zero impegno. → Fai il test"
- "Più veloce di una telefonata: fai il test e ti diciamo come muoverti."

### Inviti "risultato personalizzato"
- "Ricevi la tua strategia di vendita personalizzata. → Fai il test"
- "Alla fine del test ricevi la stima + i 3 passi giusti per la tua casa."

> Nota tono: per **Best (Montesacro)** e **Campisano (luxury)** usa inviti
> sobri/eleganti ("Verifica", "Richiedi l'analisi", "Accedi al test riservato"),
> niente "calcola gratis" o gamification.

## CTA-quiz PER CLIENTE (domanda-angolo + invito)
**Colantoni (Ostia) — documenti**
- Domanda 5: "Sai se i documenti della tua casa sono in regola per il rogito?"
- CTA: "Fai il test: la tua casa a Ostia è pronta per il rogito? (60 sec)"

**Càsa (Varese) — sostenibilità**
- Domanda 5: "Per comprare la prossima casa devi prima vendere questa?"
- CTA: "Test: il tuo cambio casa è sostenibile? Scoprilo in 1 minuto."

**ME (Castelli) — valore premium**
- Domanda 5: "Hai già ricevuto una valutazione? Da quanti?"
- CTA: "Quanto vale davvero il tuo immobile ai Castelli? Fai il test."

**CasaTua (Roma Est) — pratiche/rogito**
- Domanda 5: "La tua casa ha condoni, sanatorie o difformità da sistemare?"
- CTA: "Test: c'è una pratica che può bloccarti al rogito? Verificalo in 60 sec."

**Best (Montesacro) — venduto reale (tono sobrio)**
- Domanda 5: "Conosci i prezzi del venduto reale nella tua via?"
- CTA: "Verifica il prezzo reale della tua via a Montesacro. → Accedi al test"

**Campisano (Luxury) — discrezione (tono riservato)**
- Domanda 5: "Preferisci una vendita pubblica sui portali o riservata?"
- CTA: "Test riservato: la tua proprietà è pronta per una vendita off-market?"

## KPI del quiz (da misurare su GHL)
Tasso completamento quiz · % che lascia il contatto · costo per lead per angolo ·
minuti al primo richiamo (speed-to-lead) · quiz→appuntamento · appuntamento→incarico.

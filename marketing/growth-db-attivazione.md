# Piano di Attivazione DB — Agente Strategico
## Fase 1 Cantiere B — Lead Gen Interna AS

> Ultimo aggiornamento: 2026-06-03

---

## ASSUNZIONI DA CONFERMARE (DG)

| # | Assunzione | Impatto se errata |
|---|-----------|-------------------|
| A1 | DB totale: **~20.000 contatti** — confermare il numero esatto in GHL/Vendilo | Cambia i target assoluti di ogni fase |
| A2 | DB **mai contattato** via sequenze email strutturate — nessuna campagna precedente | Se alcuni segmenti sono stati contattati, adattare il tono del primo invio da "ri-aggancio" a "continuazione" |
| A3 | I contatti nel DB sono agenti immobiliari italiani che hanno interagito con AS in passato (eventi, sito, social, passaparsa) | Se ci sono contatti generici non-agenti, creare un segmento "non qualificato" da non contattare |
| A4 | GHL/AS Digital contiene il campo "fonte" o almeno "data di ingresso" per una minima segmentazione | Se manca, la segmentazione si fa su soli prodotti acquistati o engagement email |
| A5 | n8n e GHL con credenziali mancanti: **il copy e' platform-agnostic**, pronto da caricare su qualunque tool | |

---

## Principio guida: non bruciare il DB

Un DB da 20k contatti freddi e mai lavorati e' un asset enorme e fragile allo stesso tempo. Le regole non negoziabili prima di qualunque invio:

1. **Prima il valore, poi l'offerta.** Il primo invio non vende nulla. Offre qualcosa di utile, ricorda chi siamo, e chiede solo di fare un passo piccolo (cliccare, rispondere, scaricare).
2. **Cadenza progressiva, non aggressiva.** Iniziare con 1 email/settimana per le prime 4 settimane. Aumentare solo dopo aver misurato l'engagement.
3. **Segmentare prima di inviare.** Anche una segmentazione grezza (comprato / non comprato / evento / mai interagito) fa una differenza enorme sul deliverability e sull'engagement.
4. **Sunset policy**: chi non apre nessuna delle prime 5 email entra in un segmento "freddo" e viene rimosso dalla lista attiva o ri-contattato solo con la sequenza di riattivazione dedicata — non con le promozioni ordinarie.

---

## Piano di Segmentazione

### Segmentazione Primaria — per Comportamento d'Acquisto

Questa e' la segmentazione piu' importante perche' determina a quale stage del funnel appartiene ogni contatto.

| Segmento | Definizione | Dimensione (ASSUNZIONE) | Stage funnel attuale |
|----------|-------------|------------------------|---------------------|
| **S1 — Clienti attivi** | Hanno acquistato almeno un prodotto nelle ultime 12 settimane | SCONOSCIUTA — chiedere a DG | Gia' nel funnel |
| **S2 — Clienti dormienti** | Hanno acquistato in passato ma non ci sono interazioni recenti | SCONOSCIUTA | Da riattivare |
| **S3 — Partecipanti eventi** | Hanno partecipato a un evento AS (Bootcamp, workshop, evento nazionale) senza acquistare prodotti continuativi | SCONOSCIUTA | Caldo — Awareness → Bootcamp |
| **S4 — Lead da sito/social** | Hanno fatto opt-in su una landing o cliccato su un link ma non hanno acquistato nulla | SCONOSCIUTA | Awareness |
| **S5 — Contatti freddi** | Sono nel DB ma non si ricorda come ci sono entrati: nessuna interazione tracciata | SCONOSCIUTA | Pre-Awareness |
| **S6 — Non qualificati** | Non sono agenti immobiliari (verificare a campione) | SCONOSCIUTA | Da non contattare o da filtrare |

Priorita' di attivazione: S1 → S2 → S3 → S4 → S5. S6 non contattare.

### Segmentazione Secondaria — per Livello del Grattacielo

Da applicare dove il dato e' disponibile o stimabile dall'acquisto:

| Livello | Chi e' | Messaggio chiave |
|---------|--------|-----------------|
| **Fondamenta** | Agente alle prime armi, < 2 anni, fatturato < 30k | "Non serve partire forti — serve partire bene" |
| **Primo Piano** | Agente attivo, 2-5 anni, fatturato 30-80k, ma bloccato | "Il problema non e' la tua tariffa" |
| **Cuore** | Agente produttivo, > 80k, vuole scalare | "Smetti di lavorare piu' duro — costruisci un sistema" |
| **Vetta / Skyline** | Team leader o broker, vuole delegare e costruire | "La tua agenzia dovrebbe girare anche senza di te" |

### Segmentazione Terziaria — per Fonte di Ingresso

Da tracciare su ogni nuovo lead da ora in poi; da ricostruire a campione sul DB esistente dove possibile:

- YouTube
- Instagram / Facebook
- Evento in presenza
- Referral da membro o coach
- Ads (specificare campagna)
- Organico sito

---

## Sequenza di Riscaldamento — DB Freddo (Piano Completo)

### Premessa: la "finestra di fiducia"

Un contatto freddo ha gia' dimenticato chi siamo o associa AS a un ricordo vago. Il primo obiettivo non e' vendere: e' ricostruire la fiducia e la rilevanza. Solo dopo — e con gradualita' — si introduce un'offerta.

### Fase 0 — Pre-invio (settimana -1, prima di toccare il DB)

Attivita' da completare prima del primo invio:
- [ ] Pulizia tecnica della lista: rimuovere duplicati, email con formato non valido, domini inesistenti
- [ ] Verifica deliverability del dominio mittente (record SPF, DKIM, DMARC configurati su `agentestrategico.it`)
- [ ] Configurare un indirizzo mittente umano: `giuseppe@agentestrategico.it` o `team@agentestrategico.it`, non `noreply@`
- [ ] Segmentare almeno in 2 macro-gruppi: "clienti passati" (S1+S2+S3) e "lead mai acquistato" (S4+S5) — messaggi diversi

---

### Fase 1 — Ri-aggancio (settimane 1-2): "Ciao, siamo ancora qui"

**Obiettivo:** ricordare chi siamo, dare valore immediato, misurare chi e' ancora attivo.

#### Email R1 — L'invio di ri-aggancio (giorno 1)

Copy completo nella sezione "Riattivazione cold" di `growth-email-sequenze.md`.

Struttura e logica:
- Oggetto: riconosce il silenzio senza scuse, apre con qualcosa di utile
- Corpo: 150-200 parole. Chi siamo oggi (1 frase). Cosa offriamo gratuitamente (lead magnet PICASSO o checklist "I 7 Errori"). Una CTA sola: "Scarica qui."
- Non menzionare nessun prodotto a pagamento in questa email
- PS finale: "Se preferisci non ricevere piu' nostre email, clicca qui per uscire dalla lista — nessun problema."

**Metrica:** open rate target > 20%, click rate target > 3%.

---

#### Email R2 — Il valore che dimostra il metodo (giorno 5)

Solo per chi ha aperto R1 (o, se il tool non permette la condizione, per tutti).

Struttura e logica:
- Oggetto: una domanda diretta sul problema piu' comune del target ("Quante ore stai sprecando senza un sistema?")
- Corpo: case study breve (3-4 paragrafi). Un agente reale (anonimizzato o nominato con consenso) che aveva il problema → ha applicato un pezzo del metodo 6A → risultato misurabile. Non e' una storia di successo patinata: e' un problema specifico risolto.
- CTA: "Se vuoi vedere come funziona il metodo completo, leggi qui." → link a pagina di valore gratuita (blog post, video YouTube, pagina risorse del sito)
- Non vendere ancora.

---

### Fase 2 — Nurturing (settimane 3-4): "Ecco cosa puoi fare con questo"

**Obiettivo:** costruire autorita', mostrare la profondita' del metodo, alzare la temperatura verso una prima offerta.

#### Email N1 — I 3 pilastri (giorno 12)

Struttura e logica:
- Oggetto contrarian: "Perche' la maggior parte degli agenti lavora il doppio per guadagnare la meta'"
- Corpo: presentazione sintetica dei 3 pilastri AS (Demistificazione tecnologica / Nuovo paradigma di vendita / Mindset e Produttivita'). Per ciascuno: il problema che risolve + 1 concetto chiave. Tono didattico, non pubblicitario.
- CTA: "Scopri a quale livello sei ora" → link al quiz sul sito (se disponibile) o alla pagina "ecosistema"

#### Email N2 — La prova sociale (giorno 19)

Struttura e logica:
- Oggetto: "Cosa hanno fatto gli agenti che hanno smesso di stare fermi"
- Corpo: 2-3 testimonianze brevi (2-3 frasi ciascuna) di membri reali con risultati concreti. Includere il livello di partenza ("era bloccato a 40k di fatturato") e il risultato ("dopo 6 mesi ha superato 90k"). Niente virgolette inventate: usare solo testimonianze reali disponibili o segnalare l'assunzione al DG.
- ASSUNZIONE: le testimonianze esistono e sono autorizzate alla pubblicazione — verificare con DG.
- CTA: "Leggi la storia completa" → link a un blog post o a una pagina del sito con la storia. Niente offerta diretta.

---

### Fase 3 — Prima offerta (settimana 5): "Questo e' il passo piccolo"

**Obiettivo:** fare la prima offerta economica con un prodotto a bassa barriera (€149 Bootcamp) dopo aver costruito abbastanza fiducia.

#### Email O1 — L'invito al Bootcamp (giorno 26)

Struttura e logica:
- Oggetto: "Una cosa concreta che puoi fare questa settimana" (non rivela subito il prezzo)
- Corpo: presenta il Bootcamp come il modo piu' diretto per mettere in pratica quello di cui si e' parlato nelle ultime settimane. Non "corso". Non "evento". "3 giorni per costruire il tuo sistema, con noi." Data reale, citta', posti disponibili reali.
- CTA unica: "Prenota il tuo posto — €149" con link diretto alla landing del Bootcamp

#### Email O2 — Ultimo promemoria (giorno 30, solo per chi non ha acquistato)

- Oggetto: "Chiudo la lista [nome evento] tra 48h"
- Corpo breve (< 100 parole): ricapitolo del valore, scadenza reale, CTA. Nessuna pressione psicologica artificiale.

---

## Mini-Piano "Primi 7 Giorni" — Checklist Operativa

Questo e' il piano di partenza minimo: cosa fare prima ancora di avere GHL completamente operativo.

| Giorno | Azione | Chi | Tool |
|--------|--------|-----|------|
| Giorno 1 | Esportare il DB da GHL/Vendilo in CSV. Contare i record. Verificare quanti hanno email valida. | DG o team tech | GHL / Vendilo |
| Giorno 1 | Verificare SPF/DKIM/DMARC su `agentestrategico.it` | Team tech | DNS provider |
| Giorno 2 | Segmentare in almeno 2 macro-gruppi (clienti vs lead) anche manualmente nel CSV | DG o team | Google Sheets |
| Giorno 3 | Scegliere il tool email operativo (GHL se credenziali risolte, altrimenti MailerLite/Brevo/ActiveCampaign come fallback) | DG | — |
| Giorno 4 | Caricare il segmento "clienti passati" (S1+S2) nel tool. NON caricare tutto il DB ancora. | Team tech | Tool scelto |
| Giorno 5 | Caricare il copy Email R1 (da `growth-email-sequenze.md`), configurare mittente umano, testare su 5 indirizzi reali | Team marketing | Tool scelto |
| Giorno 6 | Inviare R1 al segmento "clienti passati" (S1+S2). Monitorare le prime 4h: bounce rate, spam rate. | Team marketing | Tool scelto |
| Giorno 7 | Leggere i report: open rate, click, bounce, unsubscribe. Decidere se procedere con S3+S4 o attendere. | DG + team marketing | — |

---

## Regole Anti-Spam e Anti-Burn

### Cadenza massima consigliata per fase

| Fase | Cadenza | Motivo |
|------|---------|--------|
| Ri-aggancio (settimane 1-2) | 1 email ogni 4-5 giorni | DB freddo: non sovraccaricare |
| Nurturing (settimane 3-4) | 1 email ogni 6-7 giorni | Costruire abitudine senza pressione |
| Offerta (settimana 5) | Max 2 email in 7 giorni | Solo per chi e' ingaggiato |
| Dopo l'offerta | Tornare a 1 email/settimana | Mantenere il ritmo editoriale (Mindset Monday + Marketing Friday) |

### Regole tecniche minime

1. **Unsubscribe in ogni email**: link visibile, non nascosto, che funziona davvero. E' legge (GDPR) e salva la reputazione del dominio.
2. **Bounce > 5% in un invio**: fermare immediatamente l'invio, pulire la lista, riprendere.
3. **Spam complaint > 0,1%**: fermare, analizzare, correggere il mittente o il contenuto prima di riprendere.
4. **Non inviare da un indirizzo "noreply"**: abbassa l'open rate e impedisce le risposte (che sono segnali di qualita' per i filtri antispam).
5. **Warm-up del dominio**: se il dominio non ha mai inviato email di massa, iniziare con batch piccoli (500-1000 al giorno) e aumentare gradualmente nel corso di 2 settimane. Non mandare 20.000 email il primo giorno.

### Sunset Policy (chi non apre)

| Comportamento | Azione |
|---------------|--------|
| Non apre nessuna delle prime 3 email | Spostare in segmento "freddo-monitoraggio" |
| Non apre nessuna delle prime 5 email | Inviare la sequenza di riattivazione dedicata (1 sola email con oggetto diretto: "Vuoi ancora far parte di questa lista?") |
| Non risponde alla email di riattivazione | Rimuovere dalla lista attiva. Non eliminare dal CRM: etichettare come "inattivo" per campagne future diverse |
| Si iscrive di nuovo o interagisce in seguito | Reinserire nella lista attiva partendo dalla Welcome Series |

### Igiene lista mensile

Una volta al mese:
- Rimuovere gli indirizzi che generano hard bounce (dominio inesistente)
- Rimuovere i soft bounce ripetuti (3+ volte)
- Aggiornare il segmento "inattivi" con chi non ha aperto nelle ultime 8 settimane
- Verificare che il tasso di disiscrizione sia < 0,5% per invio

---

## Note Operative — Budget

Il piano e' stato progettato con budget minimo. La maggior parte delle azioni nella Fase 1 (settimane 1-2) non richiede spesa pubblicitaria. Il costo principale e' il tool email:

- **GHL (gia' pagato, se le credenziali vengono risolte)**: costo aggiuntivo zero.
- **Brevo (fallback gratuito fino a 300 email/giorno, piano starter ~25€/m per volumi maggiori)**: opzione immediata se GHL non e' disponibile.
- **MailerLite (fallback, gratuito fino a 1.000 iscritti, poi ~15€/m)**: opzione alternativa.

NOTA BUDGET: storicamente AS ha operato con budget marketing basso. Questo piano e' costruito per funzionare senza ads nella Fase 1. Se il budget ads e' disponibile (anche solo 300-500€/mese), va allocato sul retargeting del DB gia' segmentato e sull'acquisizione nuovi lead via Meta — non sulla fase di riscaldamento del DB esistente.

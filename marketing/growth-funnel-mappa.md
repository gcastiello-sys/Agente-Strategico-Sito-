# Mappa Funnel End-to-End — Agente Strategico
## Fase 1 Cantiere B — Lead Gen Interna AS

> Ultimo aggiornamento: 2026-06-03

---

## ASSUNZIONI DA CONFERMARE (DG — richiesta esplicita prima di procedere)

| # | Assunzione | Impatto se errata |
|---|-----------|-------------------|
| A1 | DB totale: **~20.000 contatti** | Se molto inferiore, i target di conversione numerici cambiano |
| A2 | DB mai contattato via email marketing strutturato — nessuna sequenza attiva | Se alcuni segmenti sono stati contattati, il primo invio non è di "re-aggancio" ma di continuazione |
| A3 | n8n e GHL presenti ma con credenziali mancanti — tutti i materiali qui prodotti sono platform-agnostic | Se GHL è attivo e funzionante, si possono caricare direttamente |
| A4 | Video "Cassaforte" (€399): **ancora da selezionare** dal DG | Blocca l'attivazione dello Stage 3 |
| A5 | Prezzi IVA esclusa salvo indicazione contraria | |
| A6 | Prezzo 12 Masterclass + Workshop Avvio: **€3.600** (o 6 rate da €600) | Usare questo nelle comunicazioni, non €4.000 |

---

## Schema d'insieme

```
[Organico / Ads / Referral / Eventi]
           |
           v
    AWARENESS (gratuito)
    Lead magnet PICASSO + contenuto YouTube/IG
           |
           v
   Welcome Series 7 email / 14 gg
           |
           v
    BOOTCAMP €149 (3 gg in aula)
           |
        [in-room]
           v
    CASSAFORTE €399 (video su Circle)
           |
      [dopo consumo 70%]
           v
    12 MASTERCLASS + WORKSHOP €3.600
    (oppure 6 rate x €600)
           |
           v
    COMMUNITY Pro/Elite €799-999/m
    oppure SPD €5.000
           ^
           |
    EVENTI NAZIONALI (acceleratore a ogni stage, 2x/anno)
```

---

## Stage 1 — Awareness

**Obiettivo:** portare agenti immobiliari italiani all'ingresso del funnel tramite contenuto organico, video manifesto e — dove budget lo consente — ads a basso CPL.

### Asset necessari

| Asset | Stato | Priorita' | Note |
|-------|-------|-----------|------|
| Video manifesto (2-3 min) | Da produrre con Andrea | ALTA | Brief completo in `growth-video-manifesto-brief.md` |
| YouTube: video "cerca venditori" | Da pianificare con Andrea | ALTA | Home tour, esperto quartiere/prezzo, parole-chiave di ricerca organica |
| Reels/TikTok contrarian (hook 3 sec) | Da pianificare con Valentina | MEDIA | Formato 9:16, hook contrarian nei primi 2 secondi |
| Homepage `agentestrategico.it` | Esistente — correggere errori 403 | URGENTE | Ogni 403 e' una perdita diretta di lead |
| Lead magnet PICASSO (Business Plan 1 pagina) | Esistente | URGENTE | Agganciare form di cattura email funzionante |
| Form opt-in + email di benvenuto automatica | Da attivare | URGENTE | Anche solo un autoresponder basico in attesa di GHL completo |
| UTM su tutti i link social → sito | Da implementare | URGENTE | Senza UTM non si sa da dove arriva nessuno |

### Offerta in questo stage
Nessuna offerta economica diretta. Il "prodotto" e' **valore gratuito**: lead magnet PICASSO, checklist "I 7 Errori dell'Agente che Non Scala", video "Fondamenta Digitali" su Circle.

### CTA principale
"Scarica il Business Plan in 1 pagina per agenti immobiliari — gratis" → opt-in email → inizio Welcome Series.

### Metrica chiave
- Lead per canale per settimana (numero assoluto — uno dei 2 numeri minimi obbligatori)
- CPL (Costo per Lead): obiettivo organico < €5, ads < €15
- Tasso di opt-in della landing lead magnet: obiettivo > 25%

### Ponte allo stage successivo
Dopo l'opt-in scatta automaticamente la **Welcome Series 7 email / 14 giorni** (copy completo in `growth-email-sequenze.md`). L'email 6 introduce il problema che il Bootcamp risolve. L'email 7 fa l'offerta diretta al Bootcamp €149 con finestra di 72h.

---

## Stage 2 — Bootcamp €149 (3 giorni in aula)

**Obiettivo:** prima transazione economica. Converte il lead in cliente pagante. Rompe la barriera psicologica del pagamento e filtra chi e' seriamente intenzionato a cambiare.

### Asset necessari

| Asset | Stato | Priorita' | Note |
|-------|-------|-----------|------|
| Landing page Bootcamp | Verificare errori 403 | URGENTE | Copy + prova sociale (testimonial) + countdown date reali |
| Sequenza email pre-evento (3 email: conferma, preparazione, reminder 24h) | Da creare | ALTA | Riduce no-show |
| Sequenza email post-evento (2 email) | Da creare | ALTA | Rinforza valore + ponte verso Cassaforte |
| Pagina checkout funzionante | GHL / Vendilo | URGENTE | Verificare che il pagamento sia attivo |
| Slide/materiale aula | Esistente (workshop Latina, Roma) | — | Gia' disponibile |

### Offerta
Bootcamp Strategico 3 giorni: **€149**.

Nota operativa: valutare se in aula offrire la Cassaforte a €299 invece di €399 come "offerta solo per chi e' qui oggi". Questa logica va approvata dal DG prima dell'implementazione.

### CTA principale
"Prenota il tuo posto — [N] posti disponibili" (scarcity basata su capienza reale della location, non artificiale).

### Metrica chiave
- Conversion rate lead → acquisto Bootcamp: obiettivo 3-5% del DB attivato
- CPA Bootcamp: obiettivo < €150 (KPI ufficiale AS)
- Show-up rate: % di chi ha comprato e si presenta fisicamente (benchmark settoriale: 60-75%)
- Velocita' di contatto post-opt-in (secondo dei 2 numeri minimi obbligatori): obiettivo prima email automatica entro 5 minuti dall'iscrizione

### Ponte allo stage successivo
**Durante l'ultimo giorno del Bootcamp** (in aula): presentazione live della Cassaforte con finestra di 72h a prezzo speciale per chi e' presente. Entro 48h dall'evento: sequenza 2 email "Hai completato il Bootcamp — il passo successivo e' gia' pronto."

---

## Stage 3 — Cassaforte €399 (video registrati su Circle)

**Obiettivo:** monetizzare il DB gia' caldo con un prodotto fruibile in autonomia (non richiede presenza fisica), filtrare chi e' pronto per il salto al middle ticket, costruire un asset di contenuto permanente.

### Asset necessari

| Asset | Stato | Priorita' | Note |
|-------|-------|-----------|------|
| Selezione video da caricare su Circle | **DA DECIDERE — BLOCCO DG** | CRITICA | Vedi criteri proposti sotto |
| Area riservata su Circle configurata e testata | Da verificare | ALTA | Accesso post-pagamento automatico |
| Landing page Cassaforte | Da creare | ALTA | — |
| Sequenza email onboarding post-acquisto (3 email in 7 gg) | Da creare | ALTA | Guida alla fruizione, imposta aspettative |
| Sequenza post-consumo → 12MC | Da creare | MEDIA | Trigger: ≥70% video completati o 30 gg dall'acquisto |

### Criteri di selezione video — proposta da validare con DG

I video devono seguire l'ordine naturale di domande che un agente si fa quando vuole trasformare il proprio business. Proposta di mappa a 5 moduli:

1. **Chi sono e dove voglio arrivare** — Metodo 6A, livelli del grattacielo, Mindset e identita' professionale
2. **Come acquisisco mandati** — Script acquisizione, metafora del Faro, centri d'influenza, privati a freddo
3. **Come vendo meglio** — 13 obiezioni, ribasso prezzo strategico, presentazione offerta, immobili scaduti
4. **Come uso il digitale senza perdere la testa** — AI come strumento (non magia), YouTube per trovare venditori, lead magnet
5. **Come faccio crescere il business** — Business Plan PICASSO, cash flow, "Supera quel dannato milione"

Requisito qualitativo minimo: ogni video deve essere autonomo (fruibile senza prerequisiti), durata ≤ 90 minuti, con almeno un materiale scaricabile allegato (slide, checklist, template).

### Offerta
Accesso permanente alla libreria: **€399**.

### CTA principale
"Entra nella Cassaforte — accesso permanente alle fondamenta del Metodo 6A."

### Metrica chiave
- Conversion rate Bootcamp → Cassaforte: obiettivo 20-30%
- Tasso di completamento video per utente (% dei video completati): chi supera il 70% e' il candidato principale per 12MC
- Tempo medio dalla vendita al primo video visto (indicatore di attivazione)

### Ponte allo stage successivo
**Trigger automatico** dopo completamento ≥ 70% dei video (oppure dopo 30 giorni dall'acquisto, whichever first): sequenza 3 email "Hai visto la mappa — ora e' il momento di camminare insieme" con presentazione del percorso 12MC + Workshop €3.600 e testimonial di chi ha fatto quel salto.

---

## Stage 4 — 12 Masterclass + Workshop Avvio €3.600

**Obiettivo:** middle ticket. Trasformazione sostanziale del metodo di lavoro dell'agente in un percorso guidato di 12 mesi. Prepara all'ingresso in Community o all'acquisto di SPD.

**Prezzi:**
- Opzione A: €3.600 una tantum
- Opzione B: 6 rate mensili da €600 (comunicare sempre il costo totale con trasparenza: "6 x €600 = €3.600")

### Asset necessari

| Asset | Stato | Priorita' | Note |
|-------|-------|-----------|------|
| Landing page 12MC | Da creare/verificare | ALTA | Materiale Possetto/D'Amore da trovare in Drive (asset gia' pagato — non reinventare) |
| Scaletta 12 Masterclass (Zoom 2h ciascuna) | Cantiere C — `architetto-formazione` | ALTA | Fuori scope di questo file |
| Sequenza nurturing → 12MC (per chi viene da Cassaforte) | Da creare | ALTA | 3 email in 14 gg |
| Checkout con gestione rate | GHL | MEDIA | Attivare opzione pagamento rateale |
| Sequenza onboarding 12MC (post-acquisto) | Da creare | MEDIA | Aspettative, calendario, strumenti |
| Sequenza post-completamento → Community/SPD | Da creare | MEDIA | Ultima Masterclass come momento di proposta |

### CTA principale
"Inizia il percorso — prossima coorte aperta il [DATA]" (scarcity basata su date reali di apertura della coorte).

### Metrica chiave
- Conversion rate Cassaforte → 12MC: obiettivo 10-15%
- Tasso di completamento dell'intero percorso (12 sessioni)
- Avanzamento di livello nel grattacielo a 6 mesi (North Star Metric ufficiale AS)
- Churn sul piano rateale: % di chi abbandona le rate prima del completamento

### Ponte allo stage successivo
**Nell'ultima Masterclass** (sessione 12): presentazione strutturata delle opzioni High Ticket — Community Pro/Elite e SPD. Finestra "early adopter" per chi decide entro 30 giorni dalla fine del percorso. Segue sequenza 2 email post-completamento con case study di chi e' gia' in Community.

---

## Stage 5 — Community Pro/Elite o SPD €5.000

**Obiettivo:** alta fedelta', LTV massimo, referral attivo, costruzione della prova sociale che alimenta tutto il funnel.

### Offerta

| Prodotto | Prezzo | Note |
|---------|--------|------|
| Membership Basic | €599/m | Ingresso; valutare se tenere o rimuovere come opzione confondente |
| Membership Pro | €799/m | |
| Membership Elite | €999/m | |
| SPD (Sistema Presenza Dominante) | €5.000 | 7 componenti chiavi-in-mano: Posizionamento, Branding, Landing, Automazioni email, Vendilo, Social Kit, 12 Masterclass |

### Asset necessari

| Asset | Stato | Priorita' | Note |
|-------|-------|-----------|------|
| Landing SPD | Da creare/verificare | ALTA | Offerta definitiva da slide Drive gia' disponibile |
| Sequenza onboarding Community | Da creare | ALTA | |
| Ambassador program (Silver/Gold/Platinum) | Definito in brand — da attivare | MEDIA | Meccanismo referral 25% |
| Sequenza referral post-ingresso (chiedere attivamente la segnalazione) | Da creare | MEDIA | Copy in `growth-email-sequenze.md` |

### CTA principale
- Community: "Entra nel gruppo di chi ha scelto di non restare nella media."
- SPD: "Prendi la tua macchina digitale chiavi-in-mano — tutto costruito per te."

### Metrica chiave
- MRR Community (obiettivo dichiarato: 100 membri → ~80.000€/m)
- Churn rate mensile: obiettivo < 5%
- Referral rate: obiettivo 25%+ (KPI ufficiale AS)
- LTV medio: obiettivo 2.400€+ (KPI ufficiale AS)
- NPS (Net Promoter Score): da misurare ogni 6 mesi

### Ponte (retention e upsell interno)
Non c'e' uno stage successivo nel funnel principale. La logica diventa: eventi nazionali come momento di rinnovo emotivo, upgrade Basic → Pro → Elite, e referral verso il DB di chi non e' ancora entrato nel funnel.

---

## Acceleratore Trasversale — Eventi Nazionali (2/anno)

**Calendario indicativo:** ottobre-novembre + marzo-aprile.
**Obiettivo di riempimento:** 400-500 persone per evento.

### Ruolo nel funnel
Gli eventi non sono un'isola: sono un **acceleratore che agisce su ogni coppia di stage**.

| Da stage | A stage | Meccanismo in-event |
|----------|---------|---------------------|
| Awareness | Bootcamp | Evento gratuito o low-cost come primo step fisico |
| Bootcamp | Cassaforte | Offerta in-room con sconto 72h |
| Cassaforte | 12MC | Workshop avvio come "assaggio" del percorso completo |
| 12MC | Community | Celebration per chi completa — annuncio dell'ingresso |

### Piano di riempimento — timeline 12 settimane pre-evento

| Settimane prima | Azione | Canale principale |
|----------------|--------|------------------|
| T-12 | Annuncio data ufficiale + apertura lista d'attesa | Email DB + post social |
| T-10 | Early Bird (sconto 30-40% con data di scadenza reale e comunicata) | Email + retargeting ads |
| T-8 | Chiusura Early Bird + social proof (N iscritti, nomi noti) | Email + Reel IG |
| T-6 | Comunicazione contenuto/speaker — risponde alla domanda "perche' venire" | Email + post LinkedIn |
| T-4 | Urgenza reale: N posti rimasti (numero verificabile) | Email + stories IG |
| T-2 | Logistica + preparazione: cosa portare, come arrivare, hype finale | Email + WhatsApp (se lista attiva) |
| T-7 giorni | Sequenza "conto alla rovescia" — 3 email in 7 giorni | Email |
| T+3 giorni | Follow-up post-evento: grazie + offerta prodotto successivo con scadenza 72h | Email immediata |

### Ruolo community e coach
Ogni membro Community diventa ambasciatore con incentivo esplicito: portare 2+ persone = sconto sul rinnovo mensile o accesso a una sessione 1-1 aggiuntiva. I coach del team ricevono un "pacchetto speaker" (template di annuncio, link personalizzato tracciato con UTM) per promuovere tra i propri contatti.

### Metrica chiave eventi
- Iscritti totali vs. show-up rate (presenze effettive / iscrizioni)
- Conversion rate in-room verso prodotto successivo (upsell)
- Ricavo totale evento (biglietti + upsell in-room)
- Nuovi lead acquisiti all'evento (chi entra per la prima volta nel funnel tramite l'evento)

---

## Dashboard KPI — Specifica

### Struttura (compatibile GHL / AS Digital / Google Sheets in fallback)

| KPI | Formula | Frequenza lettura | Soglia allarme |
|-----|---------|-------------------|----------------|
| Lead per canale | N lead / canale / settimana | Settimanale | < 50 lead totali/settimana |
| CPL (Costo per Lead) | Spesa ads / N lead | Per campagna | > €15 |
| CPA Bootcamp | Spesa totale / N acquisti Bootcamp | Per campagna | > €150 |
| Conv. Awareness → Bootcamp | N acquisti / N lead x 100 | Mensile | < 2% |
| Conv. Bootcamp → Cassaforte | N acquisti Cassaforte / N Bootcamp x 100 | Mensile | < 15% |
| Conv. Cassaforte → 12MC | N acquisti 12MC / N Cassaforte x 100 | Mensile | < 8% |
| Conv. 12MC → Community/SPD | N ingressi / N completamenti 12MC x 100 | Mensile | < 20% |
| Churn Community | N uscite / N totali memberships x 100 | Mensile | > 5% |
| MRR Community | Somma ricorrenti attivi | Mensile | — |
| Ricavo per stage | Ricavo totale / stage | Mensile | — |
| Referral rate | Lead da referral / Lead totali x 100 | Mensile | < 25% |
| LTV medio | Ricavo totale / N clienti unici | Trimestrale | < 2.400€ |
| Open rate email | Aperture / Invii x 100 | Per campagna | < 25% |
| Velocita' di contatto | Minuti tra opt-in e prima email automatica | Continua (alert automatico) | > 15 minuti |

### I 2 numeri minimi — da misurare SEMPRE, anche prima di avere una dashboard

1. **Fonte del lead**: da dove arriva ogni contatto (YouTube / IG / evento / referral / ads / organico web). Senza questo dato non si sa dove investire ne' dove tagliare. Implementazione minima: UTM su ogni link + campo "fonte" nel CRM.

2. **Velocita' di contatto**: quanti minuti passano tra l'opt-in e la prima email o azione automatica. Benchmark: entro 5 minuti dall'opt-in, l'open rate della prima email sale al 60%+; dopo 24 ore scende sotto il 20%. E' il parametro piu' facile da migliorare con il maggiore impatto immediato sulle conversioni.

---

## QUICK WIN vs BUILD

### QUICK WIN — azioni completabili questa settimana, senza budget

- [ ] Correggere tutti gli errori 403 sulle landing esistenti (Bootcamp, Community, qualunque pagina di vendita): ogni 403 e' una perdita diretta di lead e acquisti oggi.
- [ ] Aggiungere UTM su tutti i link nei profili social (IG bio, LinkedIn, Facebook) → sito: tracciare la fonte da subito, non "quando abbiamo tempo".
- [ ] Attivare il form PICASSO lead magnet con un autoresponder minimo (anche solo 1 email di benvenuto automatica su qualunque tool disponibile e funzionante) in attesa che GHL sia completamente operativo.
- [ ] Mappare manualmente il DB 20k per il campo "fonte" se il dato esiste gia' in GHL/Vendilo — e' il prerequisito per qualunque segmentazione successiva.

### BUILD — attivita' da pianificare nelle prossime settimane

- [ ] Welcome Series completa 7 email (copy pronto in `growth-email-sequenze.md`).
- [ ] Landing page Cassaforte + area Circle configurata e testata.
- [ ] Selezione video per la Cassaforte — blocco da sbloccare con decisione DG.
- [ ] Dashboard KPI su GHL o su Google Sheets con aggiornamento settimanale cadenzato.
- [ ] Piano eventi nazionali con date confermate, sistema di prenotazione attivo e sequenza email di riempimento.
- [ ] Materiale Possetto/D'Amore per landing 12MC — trovare in Drive prima di costruire da zero.

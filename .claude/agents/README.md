# 🎛️ Pannello di controllo — Agenti & Skill di Agente Strategico

Indice operativo di tutto il "team AI". Per attivare un agente: chiamalo per nome
("usa `keynote-evento` per…"). Per una skill: `/nome-skill`. Quando non sai da dove
partire, parti dal **regista**.

## 🧠 Orchestrazione (parti da qui)
| Agente | Cosa fa | Quando usarlo |
|--------|---------|---------------|
| **regista-ecosistema** | Capo di gabinetto: fa ordine, mappa sui 7 cantieri, assegna agli agenti, mette priorità/scadenze | Brief ampio o disordinato; "aiutami a strutturare X" |

## 🎤 Eventi & Formazione
| Agente | Cosa fa | Quando |
|--------|---------|--------|
| **keynote-evento** | Arco narrativo e outline slide per workshop/eventi che vendono il livello successivo | Strutturare un evento/workshop |
| **architetto-formazione** | Academy, 12 Masterclass, bootcamp, scuola coach/certificazione | Progettare percorsi e moduli |

## 📈 Crescita & Funnel
| Agente | Cosa fa | Quando |
|--------|---------|--------|
| **growth-as** | Lead gen *interna* di AS: funnel €149→Cassaforte→€3.999→community, DB 20k, email, video manifesto, riempimento eventi | Far crescere Agente Strategico stesso |
| **funnel-lead** | Funnel e nurturing lato **clienti-agenti** | Lead gen per un cliente |

## ✍️ Contenuti & Dati
| Agente | Cosa fa | Quando |
|--------|---------|--------|
| **stratega-contenuti** | Piani editoriali e copy social/video (Reels, YouTube, LinkedIn) | Calendari e idee contenuti |
| **analista-strategico** | Analisi performance, KPI, report, pattern vincenti | Capire cosa funziona dai dati |
| **copywriter-brand** | Email, landing, testi lunghi nel tono "Negazione Costruttiva" | Scrivere copy del brand |

## 🏠 Clienti SPD (Sistema Presenza Dominante)
| Agente | Cosa fa | Quando |
|--------|---------|--------|
| **stratega-posizionamento** | Posizionamento 5 leve + angoli + hook ads per un cliente | Nuovo cliente da posizionare |
| **coach-script-vendita** | Script telefonici e d'appuntamento (acquisizione, obiezioni, ribasso) | Serve uno script di vendita |

## 🌐 Sito
| Agente | Cosa fa | Quando |
|--------|---------|--------|
| **copywriter-brand** | (vedi sopra) testi del sito | Pagine, sezioni |
| **revisore-sito** | Qualità pagine: link rotti, SEO, mobile, design system | Controllo qualità sito |
| **ottimizza-immagini** | Comprime foto pesanti → WebP, aggiorna i riferimenti | Foto da 15-20 MB da alleggerire |

## 🧩 Skill (flussi `/comando`)
| Skill | Cosa fa |
|-------|---------|
| **slide-evento** | Piano evento → deck slide per Claude Design, brand-styled, persuasivo, **zero fonti** (paternità unica) |
| **landing-cliente** | Intake cliente → PDF posizionamento + landing HTML con quiz GHL |
| **nuovo-coach** | Nuova scheda coach per il sito, coerente con le esistenti |

## 🗺️ Contesto condiviso (lo leggono gli agenti)
- `.claude/context/ecosistema-as.md` — la mappa: 7 cantieri, funnel, ruoli, asset
- `.claude/context/agente-strategico.md` — brand, tono, prodotti, prezzi
- `.claude/context/sistema-presenza-dominante.md` — metodo SPD per i clienti

## 🔁 Flusso tipico
1. Brief al **regista-ecosistema** → piano + assegnazioni
2. L'agente competente produce il deliverable
3. Output salvato (`piani/`, `eventi-slide/`, `posizionamento/`, `marketing/`)
4. Commit in italiano sul branch corrente

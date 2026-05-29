---
name: nuovo-coach
description: >-
  Crea una nuova scheda coach per il sito Agente Strategico, partendo dal
  formato delle schede esistenti in coach/. Usala quando devi aggiungere un
  nuovo coach al sito mantenendo stile, struttura, SEO e mobile coerenti con
  le altre pagine.
---

# Skill: Nuovo coach

Questa skill crea una nuova pagina coach in `coach/` coerente con quelle già
esistenti (stesso design system, stessa struttura, SEO e mobile a posto).

Prima di tutto leggi `CLAUDE.md` per il contesto e le regole.

## Informazioni da raccogliere dall'utente

Se non sono già state fornite, chiedi:
1. **Nome e cognome** del coach (es. "Maria Rossi").
2. **Foto** del coach (percorso del file immagine, se disponibile).
3. **Bio / presentazione** (qualche frase sul percorso e sul ruolo).
4. **Specializzazione / cosa costruisce con gli agenti** (per la sezione
   "Cosa costruiamo insieme").
5. Eventuali **testimonianze** di agenti da inserire.

## Passi

1. **Calcola lo slug** del file dal nome: minuscolo, senza accenti, parole unite
   da trattino. Es. "Giuseppe Castiello" → `giuseppe-castiello.html`.
   Verifica che `coach/<slug>.html` non esista già.

2. **Copia un modello esistente** come base, per ereditare tutto lo stile:
   ```bash
   cp coach/giuseppe-castiello.html coach/<slug>.html
   ```
   (scegli la scheda esistente più simile per struttura).

3. **Sostituisci i contenuti** nella nuova pagina, lasciando intatto il CSS:
   - `<title>` → `Nome Cognome — Agente Strategico`.
   - `<meta name="description">` → frase breve e specifica sul coach.
   - I meta Open Graph / Twitter (`og:title`, `og:description`, `og:image`...).
   - Hero: `.ch-name` con `Nome<br><em>Cognome</em>`.
   - Bio: sezione `.coach-bio` (`.bio-title` + testo).
   - Sezione `.lavoriamo` ("Cosa costruiamo insieme").
   - Sezione `.coach-testi` (testimonianze), se fornite.
   - CTA finale `.coach-final-cta`.
   - Aggiorna l'immagine del coach con il file corretto (vedi punto 4).

4. **Immagine.** Se la foto fornita è pesante (diversi MB), prima di pubblicarla
   fai ottimizzarla dall'agente `ottimizza-immagini` (target < 300 KB / WebP).
   Imposta un `alt` descrittivo (es. `alt="Nome Cognome, coach Agente Strategico"`).

5. **Mobile.** Verifica che la pagina contenga
   `<link rel="stylesheet" href="/mobile.css">` nello `<head>` e
   `<script src="/mobile-nav.js"></script>` prima di `</body>`.
   In dubbio, esegui `./inject-mobile.sh`.

6. **Collega la scheda** dalle pagine che elencano i coach (cerca con grep i
   link `coach/` nelle pagine indice come `ecosistema/`, `chi-siamo/` o
   homepage) così il nuovo coach è raggiungibile.

7. **Verifica finale:**
   - apri la pagina nel browser (o `python3 -m http.server`) e controlla
     desktop + mobile;
   - controlla che non siano rimasti testi del coach copiato come modello;
   - controlla i link interni.

8. **Commit** in italiano, es. `Aggiungi scheda coach Nome Cognome`.

## Regole

- Non modificare il CSS condiviso: cambia solo i contenuti.
- Mantieni il tono elegante del sito (titoli serif con parole in `<em>`).
- Non lasciare segnaposto o testo del coach usato come modello.

> Suggerimento: per creare altre skill simili (es. `nuovo-articolo-blog`
> partendo da `blog/caso-studio-template.html`, o `nuovo-evento` da
> `eventi/<città>/`), copia questa cartella e adatta i passi.

# CLAUDE.md — Manuale del progetto "Agente Strategico"

Questo file viene letto automaticamente da Claude Code ogni volta che lavora in
questo progetto. Contiene le regole e il contesto del sito. Tienilo aggiornato:
più è preciso, meglio lavorano agenti e skill.

---

## Cos'è questo progetto

Sito web **statico** di *Agente Strategico*, l'ecosistema di formazione e community
per agenti immobiliari italiani. È fatto di pagine HTML, CSS e JavaScript puri
(nessun framework, nessun build step). Viene pubblicato su **Vercel**.

- Lingua del sito: **italiano** (`<html lang="it">`).
- Dominio di produzione: `https://agentestrategico.it`.
- Pubblicazione: ogni push sul branch collegato a Vercel manda online il sito.
- `vercel.json` usa `cleanUrls: true` → gli URL non mostrano `.html`
  (es. `/coach/giuseppe-castiello`, non `/coach/giuseppe-castiello.html`).

## Struttura delle cartelle

| Cartella / file        | Cosa contiene |
|------------------------|---------------|
| `index.html`           | Homepage |
| `coach/`               | Una pagina HTML per ogni coach (es. `giuseppe-castiello.html`) |
| `blog/`                | `index.html` + articoli (modello: `caso-studio-template.html`) |
| `eventi/`              | `index.html` + sottocartelle città (latina, palermo, roma, trapani) |
| `chi-siamo/`, `community/`, `ecosistema/`, `strumenti/`, `risorse/`, `corso-aula/`, `candidatura/`, `quiz/` | Sezioni del sito |
| `animations.js`        | Animazioni condivise |
| `mobile.css`           | Stili specifici per mobile |
| `mobile-nav.js`        | Menu di navigazione mobile |
| `inject-mobile.sh`     | Script che inserisce `mobile.css` e `mobile-nav.js` in ogni pagina |
| `*.jpg`                | Foto coach ed eventi (ATTENZIONE: molte pesano 15-20 MB) |

## Design system (da rispettare SEMPRE)

Tutte le pagine condividono lo stesso stile. Usa queste variabili CSS, già
definite in cima a ogni pagina dentro `<style>:root{...}`:

```
--black:#0A0A0A   --gray-900:#1A1A1A  --gray-700:#444  --gray-500:#777
--gray-200:#E8E8E8 --gray-100:#F4F4F4 --white:#FFF
--gold:#C9A84C    --gold-light:#E2C46A
--font-serif:'Cormorant Garamond',serif   --font-sans:'Inter',sans-serif
--max-w:1200px    --pad:clamp(24px,5vw,80px)
```

- **Oro** (`--gold`) = colore d'accento per CTA, tag, dettagli.
- **Titoli** in `--font-serif` (Cormorant Garamond), spesso con parole in `<em>`
  per il corsivo dorato/elegante.
- **Testo** in `--font-sans` (Inter).
- Font caricati da Google Fonts con `<link>` nello `<head>`.
- Bottoni: classi `.btn`, `.btn-gold`, `.btn-luxury`.

Quando crei una pagina nuova, **parti sempre copiando una pagina esistente dello
stesso tipo** e cambia solo i contenuti: così lo stile resta coerente.

## Regole importanti

1. **Coerenza prima di tutto.** Non inventare stili nuovi: riusa classi e
   variabili già presenti.
2. **Mobile.** Ogni pagina HTML deve includere nello `<head>`
   `<link rel="stylesheet" href="/mobile.css">` e prima di `</body>`
   `<script src="/mobile-nav.js"></script>`. Lo script `inject-mobile.sh` lo fa
   in automatico su tutte le pagine.
3. **SEO.** Ogni pagina deve avere: `<title>` descrittivo, `<meta name="description">`,
   e i meta Open Graph / Twitter (`og:title`, `og:description`, `og:image`, ecc.)
   come nella homepage `index.html`. Il `lang` è sempre `it`.
4. **Immagini pesanti.** Le foto a 15-20 MB rallentano tantissimo il sito. Vanno
   compresse (idealmente < 300 KB) e servite in formato moderno (WebP) prima di
   pubblicarle. Vedi l'agente `ottimizza-immagini`.
5. **Niente build.** Non aggiungere framework, bundler o `node_modules`: il sito
   è volutamente statico. `.gitignore` esclude solo `.vercel`.
6. **Link.** Usa percorsi assoluti senza estensione (es. `/coach/nome`,
   `/eventi/roma`) coerenti con `cleanUrls`.

## Come verificare il lavoro

- Apri la pagina in locale nel browser, oppure usa un server statico semplice
  (es. `python3 -m http.server`) dalla cartella del progetto.
- Controlla che il sito sia leggibile sia su desktop sia su mobile (riduci la
  finestra del browser per simulare lo smartphone).
- Controlla che non ci siano link rotti e che le immagini si carichino.

## Git

- Branch di sviluppo corrente: `claude/ai-agents-setup-guide-RVk4K`.
- Fai commit chiari e in italiano. Non aprire Pull Request se non richiesto.

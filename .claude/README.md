# Guida agli agenti e alle skill di questo progetto

Questa cartella `.claude/` contiene la "squadra di assistenti" del sito Agente
Strategico. È divisa in due parti:

```
.claude/
├── agents/     ← gli AGENTI: collaboratori autonomi a cui deleghi un compito
│   ├── revisore-sito.md
│   └── ottimizza-immagini.md
└── skills/     ← le SKILL: procedure precise che richiami quando servono
    └── nuovo-coach/
        └── SKILL.md
```

## Differenza in 30 secondi

- **Progetto** = *dove* lavori (questa cartella, i file del sito). Le regole
  generali stanno in `CLAUDE.md`, un livello sopra questa cartella.
- **Skill** = una *ricetta* riutilizzabile. La attivi tu scrivendo `/nome-skill`
  (es. `/nuovo-coach`). Fa una cosa specifica, seguendo passi precisi.
- **Agente** = un *collaboratore* con un ruolo. Gli deleghi un obiettivo ("rivedi
  il sito") e lavora in autonomia, anche su più passaggi, fino al risultato.

> Regola pratica: se sai *esattamente* quali passi vuoi → **skill**.
> Se vuoi delegare un *obiettivo* e lasciar ragionare l'assistente → **agente**.

## Come si usano

### Usare un agente
Scrivi in chat, in linguaggio naturale, una cosa come:
> "Usa l'agente revisore-sito per controllare la pagina coach di Giuseppe."

oppure semplicemente:
> "Controlla che il sito non abbia link rotti e problemi su mobile."

Claude sceglie da solo l'agente giusto quando il compito corrisponde alla sua
descrizione, oppure puoi nominarlo esplicitamente.

### Usare una skill
Scrivi lo "slash command" con il nome della skill:
> `/nuovo-coach`

e poi rispondi alle informazioni che ti chiede (nome, foto, bio...).

## Come crearne di nuovi

- **Nuovo agente**: crea un file `.md` dentro `agents/`. In cima metti un blocco
  con `name`, `description`, eventualmente `tools` e `model`; sotto scrivi le sue
  istruzioni. Copia uno degli agenti esistenti come modello.
- **Nuova skill**: crea una sottocartella dentro `skills/` con dentro un file
  `SKILL.md`. In cima `name` e `description`, sotto i passi della procedura.
  Copia `skills/nuovo-coach/SKILL.md` come modello (es. per fare
  `nuovo-articolo-blog` o `nuovo-evento`).

Più sono chiare la `description` e le istruzioni, meglio funzionano.

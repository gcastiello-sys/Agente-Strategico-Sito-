# -*- coding: utf-8 -*-
"""Genera mockup PDF (anteprima impaginata) delle landing page, 1 pagina lunga
per cliente, in stile Agente Strategico (nero + oro, titoli serif)."""
from fpdf import FPDF

GOLD = (201, 168, 76)
DARK = (10, 10, 10)
GRAY900 = (26, 26, 26)
GRAY700 = (68, 68, 68)
GRAY500 = (119, 119, 119)
LIGHT = (244, 244, 244)
WHITE = (255, 255, 255)

W = 210.0
MX = 18.0          # margine orizzontale
IW = W - 2 * MX    # larghezza utile


def beautify(s):
    """Ripristina le accentate italiane scritte come apostrofo (es. e' -> è)."""
    words = {"conformita'": "conformità", "proprieta'": "proprietà",
             "esclusivita'": "esclusività", "Sostenibilita'": "Sostenibilità",
             "Serenita'": "Serenità", "succedera'": "succederà",
             "piu'": "più", "Piu'": "Più", "perche'": "perché",
             "c'e'": "c'è", "C'e'": "C'è"}
    for k, v in words.items():
        s = s.replace(k, v)
    s = s.replace(" e' ", " è ").replace("E' ", "È ")
    return s


def san(s):
    """Riconduce il testo al set latin-1 (core fonts fpdf)."""
    s = beautify(s)
    rep = {"’": "'", "‘": "'", "“": '"', "”": '"',
           "—": "-", "–": "-", "→": ">", "•": "-",
           "»": "", "«": "", "…": "...", "×": "x", "✕": "x"}
    for k, v in rep.items():
        s = s.replace(k, v)
    return s.encode("latin-1", "replace").decode("latin-1")


def wrap(pdf, text, max_w):
    words = san(text).split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdf.get_string_width(t) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render(data, draw, pdf):
    """Disegna (o solo misura) la landing. Ritorna l'altezza totale usata."""
    accent = data.get("accent", GOLD)
    y = 0.0

    # ---- NAV BAR ----
    nav_h = 16.0
    if draw:
        pdf.set_fill_color(*DARK)
        pdf.rect(0, y, W, nav_h, "F")
        pdf.set_font("Times", "B", 15)
        pdf.set_text_color(*WHITE)
        pdf.text(MX, y + 10, san(data["brand"]))
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*accent)
        tag = "ANTEPRIMA LANDING"
        pdf.text(W - MX - pdf.get_string_width(tag), y + 10, tag)
    y += nav_h

    # ---- HERO (nero) ----
    pdf.set_font("Times", "B", 25)
    title_lines = wrap(pdf, data["hero_title"], IW)
    pdf.set_font("Helvetica", "", 12)
    sub_lines = wrap(pdf, data["hero_sub"], IW)
    hero_h = 16 + 6 + 4 + len(title_lines) * 11 + 7 + len(sub_lines) * 6.2 + 11 + 13 + 16
    if draw:
        pdf.set_fill_color(*DARK)
        pdf.rect(0, y, W, hero_h, "F")
        ty = y + 16
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*accent)
        pdf.text(MX, ty, san(data["eyebrow"].upper()))
        ty += 4 + 6
        pdf.set_font("Times", "B", 25)
        pdf.set_text_color(*WHITE)
        for ln in title_lines:
            pdf.text(MX, ty, ln)
            ty += 11
        ty += 7
        pdf.set_font("Helvetica", "", 12)
        pdf.set_text_color(220, 220, 220)
        for ln in sub_lines:
            pdf.text(MX, ty, ln)
            ty += 6.2
        ty += 11
        # bottone
        bw = pdf.get_string_width(san(data["hero_cta"])) + 18
        pdf.set_fill_color(*accent)
        pdf.rect(MX, ty, bw, 13, "F")
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*DARK)
        pdf.text(MX + 9, ty + 8.4, san(data["hero_cta"]))
    y += hero_h

    # ---- PROBLEMA (bianco) ----
    pdf.set_font("Helvetica", "", 11)
    prob_wrapped = [wrap(pdf, p, IW - 9) for p in data["problems"]]
    prob_h = 16 + 7 + 6 + sum(len(w) * 5.6 + 5 for w in prob_wrapped) + 8
    if draw:
        py = y + 16
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(*accent)
        pdf.text(MX, py, "IL PROBLEMA")
        py += 7 + 6
        for w in prob_wrapped:
            pdf.set_fill_color(*accent)
            pdf.rect(MX, py - 3.2, 3.2, 3.2, "F")
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(*GRAY700)
            first = True
            for ln in w:
                pdf.text(MX + 9, py, ln)
                py += 5.6
            py += 5
    y += prob_h

    # ---- PUNTO DI SVOLTA (fascia oro) ----
    pdf.set_font("Times", "BI", 16)
    pivot_lines = wrap(pdf, data["pivot"], IW - 10)
    pivot_h = 15 + len(pivot_lines) * 8 + 15
    if draw:
        pdf.set_fill_color(*accent)
        pdf.rect(0, y, W, pivot_h, "F")
        vy = y + 15 + 6
        pdf.set_font("Times", "BI", 16)
        pdf.set_text_color(*DARK)
        for ln in pivot_lines:
            pdf.text((W - pdf.get_string_width(ln)) / 2, vy, ln)
            vy += 8
    y += pivot_h

    # ---- METODO (grigio chiaro) ----
    pdf.set_font("Times", "B", 15)
    kick_lines = wrap(pdf, data["method_kicker"], IW)
    steps_wrapped = []
    for (t, d) in data["steps"]:
        pdf.set_font("Helvetica", "", 10.5)
        steps_wrapped.append((t, wrap(pdf, d, IW - 24)))
    step_hs = [max(13, 6 + len(dw) * 5.2 + 4) for (_, dw) in steps_wrapped]
    method_h = 16 + len(kick_lines) * 8 + 8 + sum(step_hs) + 10
    if draw:
        pdf.set_fill_color(*LIGHT)
        pdf.rect(0, y, W, method_h, "F")
        my = y + 16
        pdf.set_font("Times", "B", 15)
        pdf.set_text_color(*GRAY900)
        for ln in kick_lines:
            pdf.text(MX, my, ln)
            my += 8
        my += 8
        for i, (t, dw) in enumerate(steps_wrapped):
            # cerchio numero
            pdf.set_fill_color(*accent)
            pdf.ellipse(MX, my - 4.5, 9, 9, "F")
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(*DARK)
            num = str(i + 1)
            pdf.text(MX + 4.5 - pdf.get_string_width(num) / 2, my + 1.6, num)
            # titolo + desc
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(*GRAY900)
            pdf.text(MX + 14, my, san(t))
            pdf.set_font("Helvetica", "", 10.5)
            pdf.set_text_color(*GRAY700)
            dy = my + 5.5
            for ln in dw:
                pdf.text(MX + 14, dy, ln)
                dy += 5.2
            my += step_hs[i]
    y += method_h

    # ---- PROVA (fascia scura sottile) ----
    proof_h = 22
    if draw:
        pdf.set_fill_color(*GRAY900)
        pdf.rect(0, y, W, proof_h, "F")
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*accent)
        pdf.text(MX, y + 13, "LA PROVA")
        pdf.set_font("Helvetica", "", 10.5)
        pdf.set_text_color(235, 235, 235)
        pdf.text(MX + 26, y + 13, san(data["proof"]))
    y += proof_h

    # ---- CTA FINALE (nero) ----
    pdf.set_font("Times", "B", 18)
    fl_lines = wrap(pdf, data["final_line"], IW)
    cta_h = 16 + len(fl_lines) * 9 + 12 + 14 + 10 + 16
    if draw:
        pdf.set_fill_color(*DARK)
        pdf.rect(0, y, W, cta_h, "F")
        cy = y + 16 + 5
        pdf.set_font("Times", "B", 18)
        pdf.set_text_color(*WHITE)
        for ln in fl_lines:
            pdf.text((W - pdf.get_string_width(ln)) / 2, cy, ln)
            cy += 9
        cy += 12
        bw = pdf.get_string_width(san(data["final_cta"])) + 22
        pdf.set_fill_color(*accent)
        pdf.rect((W - bw) / 2, cy, bw, 14, "F")
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(*DARK)
        pdf.text((W - pdf.get_string_width(san(data["final_cta"]))) / 2, cy + 9, san(data["final_cta"]))
        cy += 14 + 10
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*GRAY500)
        ps = "Sistema Presenza Dominante - Agente Strategico"
        pdf.text((W - pdf.get_string_width(ps)) / 2, cy, ps)
    y += cta_h

    # ---- footer nota ----
    foot_h = 14
    if draw:
        pdf.set_font("Helvetica", "I", 8)
        pdf.set_text_color(*GRAY500)
        note = "Anteprima dimostrativa della landing - testi e dati ([..]) da validare col cliente."
        pdf.text((W - pdf.get_string_width(note)) / 2, y + 8, note)
    y += foot_h
    return y


def build(data, path):
    # pass 1: misura
    m = FPDF(unit="mm", format=(W, 4000))
    m.set_auto_page_break(False)
    m.add_page()
    total = render(data, False, m)
    # pass 2: render reale su pagina dell'altezza giusta
    pdf = FPDF(unit="mm", format=(W, total))
    pdf.set_auto_page_break(False)
    pdf.add_page()
    render(data, True, pdf)
    pdf.output(path)
    print("OK", path, round(total), "mm")


CLIENTS = [
 {"file": "mockup-colantoni.pdf", "brand": "Colantoni Immobiliare",
  "eyebrow": "Ostia - Axa - Casal Palocco - Infernetto",
  "hero_title": "Prima i documenti, poi l'annuncio.",
  "hero_sub": "A Ostia vendi casa in sicurezza, al prezzo reale, senza brutte sorprese al rogito.",
  "hero_cta": "SCOPRI QUANTO VALE CASA TUA",
  "problems": [
    "Gran parte degli annunci va online senza che nessuno abbia controllato planimetrie e conformita'.",
    "Te ne accorgi al rogito: la trattativa salta all'ultimo e hai perso mesi.",
    "C'e' chi gonfia il prezzo per prendersi l'incarico, poi dopo 3 mesi ti chiama per abbassare."],
  "pivot": "Il problema non e' il mercato. E' vendere senza aver verificato prima i documenti.",
  "method_kicker": "Metodo 4 Pilastri - Vendere Casa in Sicurezza",
  "steps": [
    ("Check Documentale Pre-Vendita", "Architetto e notaio verificano planimetria, conformita' e provenienza prima dell'annuncio."),
    ("Valutazione Reale di Mercato", "Un prezzo per vendere, non per prendersi il mandato."),
    ("Marketing dell'Immobile", "Annuncio, foto e canali, con acquirenti pre-qualificati."),
    ("Assistenza fino al Rogito", "Trattativa e chiusura seguite da buon padre di famiglia.")],
  "proof": "Famiglia Colantoni - radici a Ostia - [caso reale da inserire]",
  "final_line": "La tua casa e' pronta per andare in vendita? Scoprilo in 1 minuto.",
  "final_cta": "FAI IL TEST"},

 {"file": "mockup-casatua.pdf", "brand": "CasaTua Immobiliare", "accent": (243, 146, 0),
  "eyebrow": "Roma Est - Torre Gaia, Villa Verde, Papillo",
  "hero_title": "Ha un condono o una sanatoria in sospeso? E' proprio la casa che vendiamo.",
  "hero_sub": "A Roma Est, dove gli altri si bloccano al rogito, noi chiudiamo.",
  "hero_cta": "VERIFICA LA TUA PRATICA",
  "problems": [
    "A Roma Est tante vendite saltano al rogito perche' le pratiche urbanistiche non sono a posto.",
    "O ti dicono di no, o ti fanno svendere pur di chiudere in fretta.",
    "L'agenzia mette online la casa e poi si blocca proprio sulla pratica."],
  "pivot": "Non ti chiediamo di risolvere il problema. Lo risolviamo noi.",
  "method_kicker": "Metodo CasaTua - Vendi anche se la pratica e' complicata",
  "steps": [
    ("Notaio, geometra e avvocato in sede", "Sbloccano la pratica prima della trattativa."),
    ("Valutazione reale", "Un prezzo per vendere, senza svendere."),
    ("Marketing strutturato", "5 reparti, lead richiamati in 15 minuti, acquirenti pre-qualificati."),
    ("Assistenza fino al rogito", "Zero sorprese: chiudiamo dove gli altri si fermano.")],
  "proof": "320 immobili dal 2020 - 9,3/10 su Immobiliare.it - FIAIP",
  "final_line": "La tua casa ha una pratica complicata? Scopri come la vendiamo.",
  "final_cta": "FAI IL TEST"},

 {"file": "mockup-me.pdf", "brand": "ME Immobiliare",
  "eyebrow": "Lariano - Velletri - Castelli Romani",
  "hero_title": "Costiamo piu' degli altri. Ed e' il motivo per cui ci scelgono.",
  "hero_sub": "Il tuo immobile vale Roma. Senza uscire dai Castelli.",
  "hero_cta": "SCOPRI QUANTO VALE CASA TUA",
  "problems": [
    "Chi ha un immobile di valore ai Castelli lo affida ad agenzie di Roma, o svende.",
    "Localmente percepisce poca struttura e pochi servizi.",
    "Provvigioni basse = servizi assenti: tempi lunghi e prezzo eroso."],
  "pivot": "La differenza non e' il costo. E' tutto cio' che gli altri non ti danno.",
  "method_kicker": "Metodo ME - Vendita in Serenita'",
  "steps": [
    ("Open House", "Interesse concentrato, niente sfilate di curiosi."),
    ("Servizio fotografico professionale", "L'immobile si presenta come merita."),
    ("Gestione mutuo interna", "Marco segue anche il mutuo del compratore."),
    ("Rete di professionisti", "Operazione seguita in serenita', fino alla firma.")],
  "proof": "Recensioni reali - Marco & Erica - [n. immobili venduti da inserire]",
  "final_line": "Quanto vale davvero il tuo immobile ai Castelli? Numeri reali, non gonfiati.",
  "final_cta": "FAI IL TEST"},

 {"file": "mockup-casa-varese.pdf", "brand": "Casa Immobiliare",
  "eyebrow": "Varese",
  "hero_title": "Vendi questa casa. Poi scopri che non puoi comprare la prossima.",
  "hero_sub": "Prima verifichiamo se il tuo cambio casa sta in piedi. Poi vendiamo.",
  "hero_cta": "IL TUO CAMBIO CASA E' SOSTENIBILE?",
  "problems": [
    "Quasi tutte le agenzie pensano solo a vendere. Non verificano se poi riesci a ricomprare.",
    "Vendi, incassi, e scopri che tra mutuo e tempi i conti non tornano.",
    "Nessuno coordina vendita e riacquisto: due operazioni lasciate al caso."],
  "pivot": "Il problema non e' vendere. E' che nessuno ha verificato se l'operazione sta in piedi.",
  "method_kicker": "Metodo Casa - Cambio Casa Sostenibile",
  "steps": [
    ("Check di Sostenibilita'", "Vendita, riacquisto, mutuo e tempi analizzati prima di partire."),
    ("Valutazione trasparente", "Il prezzo reale, per vendere senza svendere."),
    ("Open House Prima Visita", "Interesse concentrato, dossier della casa."),
    ("Accompagnamento al nuovo acquisto", "Al tuo fianco fino alle chiavi nuove.")],
  "proof": "Team locale Casa Immobiliare - Varese",
  "final_line": "Il tuo cambio casa e' sostenibile? Scoprilo in 1 minuto.",
  "final_cta": "FAI IL TEST"},

 {"file": "mockup-trapella.pdf", "brand": "Elle Erre Immobiliare",
  "eyebrow": "Giulia Trapella - immobili gravati",
  "hero_title": "Un mutuo non pagato non rende la tua casa invendibile.",
  "hero_sub": "Ipoteca, pignoramento, procedura in corso: dove l'agente generalista si ferma, qui c'e' un metodo.",
  "hero_cta": "SCOPRI COME VENDERLO",
  "problems": [
    "Davanti a un immobile gravato, la maggior parte degli agenti fa un passo indietro.",
    "Il tempo stringe: se non agisci tu, a un certo punto decide la banca.",
    "In asta il prezzo crolla, e l'unica vera occasione di vendere bene svanisce."],
  "pivot": "Il problema non e' la tua casa. E' chi la gestisce.",
  "method_kicker": "Il metodo - Specialista immobili gravati",
  "steps": [
    ("Specializzazione", "Esperienza concreta con ipoteche, riscossioni e procedure."),
    ("Pochi immobili", "La tua casa non e' un numero: massima attenzione."),
    ("Report ogni 20 giorni", "Sai sempre a che punto siamo."),
    ("Tutela e sicurezza", "Ogni aspetto burocratico e contrattuale seguito.")],
  "proof": "Iscritta FIMAA - collaborazione con professionisti esperti",
  "final_line": "Il tuo immobile ha un'ipoteca o una procedura in corso? Scopri come venderlo.",
  "final_cta": "FAI IL TEST"},

 {"file": "mockup-best.pdf", "brand": "Best Immobiliare",
  "eyebrow": "Roma - Montesacro",
  "hero_title": "Il prezzo che vedi negli annunci non e' quello a cui si vende.",
  "hero_sub": "A Montesacro il prezzo lo stabiliscono i dati del venduto reale, non le opinioni.",
  "hero_cta": "VERIFICA IL PREZZO DELLA TUA VIA",
  "problems": [
    "Gli annunci mostrano i prezzi richiesti, non quelli a cui si e' venduto davvero.",
    "Molti agenti confermano a voce una valutazione gonfiata per prendere l'incarico.",
    "Una casa ferma troppo a lungo online perde appeal e potere in trattativa."],
  "pivot": "Il problema non e' il mercato. E' da dove arriva il prezzo.",
  "method_kicker": "Metodo del Venduto Reale",
  "steps": [
    ("Analisi del venduto reale", "I prezzi a cui si e' venduto nella tua via, non gli annunci."),
    ("Valutazione scritta e motivata", "Range minimo, atteso, massimo e tempi."),
    ("Follow-up a 6 step", "1-3-7-14-30-60 giorni: nessun cliente perso."),
    ("Tracciamento CRM", "Sai sempre cosa e' stato fatto e cosa succedera'.")],
  "proof": "20 anni FIAIP - dirigente provinciale dal 2006 - circuito MLS Prime",
  "final_line": "Verifica il prezzo reale della tua via a Montesacro.",
  "final_cta": "ACCEDI AL TEST"},

 {"file": "mockup-campisano.pdf", "brand": "Campisano Estates",
  "eyebrow": "Luxury Real Estate - Roma",
  "hero_title": "Alcuni immobili non andrebbero mai messi in vetrina.",
  "hero_sub": "Il vero lusso si vende lontano dal rumore, alle persone giuste.",
  "hero_cta": "VENDITA RISERVATA",
  "problems": [
    "Esporre un immobile di pregio su tutti i portali attira curiosi, non acquirenti reali.",
    "Piu' resta visibile, piu' perde l'aura di esclusivita': il valore percepito si erode.",
    "I grandi brand lo mettono in vetrina come tutti gli altri. Nessuna riservatezza."],
  "pivot": "Il problema non e' il valore della tua proprieta'. E' il modo in cui viene esposta.",
  "method_kicker": "Vendita Riservata",
  "steps": [
    ("Strategia off-market", "Niente esposizione pubblica sui portali."),
    ("Rete selezionata", "La proprieta' arriva solo a chi e' davvero in target."),
    ("Gestione personale", "Un solo interlocutore, dall'inizio alla firma."),
    ("Riservatezza assoluta", "Discrezione in ogni fase dell'operazione.")],
  "proof": "CSI International - Ambassador del Lazio",
  "final_line": "La tua proprieta' e' pronta per una vendita riservata?",
  "final_cta": "ACCEDI AL TEST RISERVATO"},
]

if __name__ == "__main__":
    import os
    out = os.path.dirname(os.path.abspath(__file__))
    for c in CLIENTS:
        build(c, os.path.join(out, c["file"]))

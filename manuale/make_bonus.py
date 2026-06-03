#!/usr/bin/env python3
"""Genera i 5 bonus digitali (PDF) del workshop 5 giorni. Brand-styled, PyMuPDF base14."""
import fitz, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bonus")
os.makedirs(OUT, exist_ok=True)
DIAG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "piani", "diagrammi")
W, H = 595, 842; ML, MR, MT, MB = 52, 52, 60, 56; RIGHT = W-MR
BLU=(0.071,0.157,0.212); ORO=(0.788,0.659,0.298); BORG=(0.294,0.071,0.188)
CREAM=(0.980,0.969,0.945); INK=(0.12,0.13,0.14); MUTE=(0.42,0.45,0.47)
LINE=(0.80,0.78,0.74); WHITE=(1,1,1)
T="tibo"; TI="tiit"; B="helv"; BB="hebo"; MONO="cour"

# ── Campi modulo interattivi (AcroForm) ──
FID=[0]
def _fid(pre):
    FID[0]+=1; return f"{pre}{FID[0]}"
def add_text(page,rect,size=11,color=INK,multiline=False):
    w=fitz.Widget(); w.field_name=_fid("f_"); w.field_type=fitz.PDF_WIDGET_TYPE_TEXT
    w.rect=fitz.Rect(rect); w.text_fontsize=size; w.text_color=color
    w.fill_color=None; w.border_width=0
    if multiline: w.field_flags=fitz.PDF_TX_FIELD_IS_MULTILINE
    page.add_widget(w)
def add_check(page,rect,border=BLU):
    w=fitz.Widget(); w.field_name=_fid("c_"); w.field_type=fitz.PDF_WIDGET_TYPE_CHECKBOX
    w.rect=fitz.Rect(rect); w.border_color=border; w.border_width=1; w.fill_color=WHITE
    page.add_widget(w)

def wrap(text,font,size,maxw):
    out=[]
    for raw in text.split("\n"):
        words=raw.split(); cur=""
        for w in words:
            t=(cur+" "+w).strip()
            if fitz.get_text_length(t,fontname=font,fontsize=size)<=maxw: cur=t
            else:
                if cur: out.append(cur)
                cur=w
        out.append(cur)
    return out

class Doc:
    def __init__(self,kicker):
        self.doc=fitz.open(); self.kicker=kicker; self.new()
    def new(self):
        self.p=self.doc.new_page(width=W,height=H); self.y=MT
        self.p.draw_rect(fitz.Rect(0,0,W,6),fill=ORO,color=None)
        self.p.insert_text((ML,H-30),"AGENTE STRATEGICO  ·  "+self.kicker,fontsize=7.5,fontname=B,color=MUTE)
        return self
    def need(self,s):
        if self.y+s>H-MB: self.new()
    def header(self,kicker,title,sub=None):
        self.p.draw_rect(fitz.Rect(0,0,W,96),fill=BLU,color=None)
        self.p.draw_rect(fitz.Rect(0,96,W,100),fill=ORO,color=None)
        self.p.insert_text((ML,40),kicker,fontsize=9,fontname=BB,color=ORO)
        self.p.insert_text((ML,72),title,fontsize=21,fontname=T,color=WHITE)
        if sub: self.p.insert_text((ML,90),sub,fontsize=10,fontname=B,color=(0.8,0.85,0.9))
        self.y=120
    def h2(self,text):
        self.need(30)
        self.p.draw_rect(fitz.Rect(ML,self.y+2,ML+22,self.y+6),fill=ORO,color=None)
        self.p.insert_text((ML+30,self.y+14),text,fontsize=14,fontname=T,color=BLU); self.y+=30
    def para(self,text,size=10.5,font=B,color=INK,gap=5,x=ML):
        lead=size*1.5
        for ln in wrap(text,font,size,RIGHT-x):
            self.need(lead); self.p.insert_text((x,self.y+size),ln,fontsize=size,fontname=font,color=color); self.y+=lead
        self.y+=gap
    def bullets(self,items,size=10.5):
        for it in items:
            self.need(size*1.5)
            self.p.insert_text((ML+6,self.y+size),"•",fontsize=size,fontname=BB,color=ORO)
            for ln in wrap(it,B,size,RIGHT-ML-22):
                self.need(size*1.5); self.p.insert_text((ML+22,self.y+size),ln,fontsize=size,fontname=B,color=INK); self.y+=size*1.5
            self.y+=3
        self.y+=3
    def promptbox(self,label,text):
        lines=wrap(text,MONO,9,RIGHT-ML-24); h=24+len(lines)*13
        self.need(h+8)
        self.p.draw_rect(fitz.Rect(ML,self.y,RIGHT,self.y+h),fill=(0.97,0.97,0.95),color=LINE,width=0.8)
        self.p.insert_text((ML+10,self.y+15),label,fontsize=8.5,fontname=BB,color=BORG)
        yy=self.y+30
        for ln in lines:
            self.p.insert_text((ML+12,yy),ln,fontsize=9,fontname=MONO,color=INK); yy+=13
        self.y+=h+8
    def rating(self,areas):
        self.need(16)                                  # intestazione colonne 1..5
        for i in range(5):
            x=RIGHT-150+i*28; self.p.insert_text((x+4,self.y+10),str(i+1),fontsize=8.5,fontname=BB,color=MUTE)
        self.y+=16
        for a in areas:
            self.need(22); self.p.insert_text((ML,self.y+12),a,fontsize=10.5,fontname=B,color=INK)
            for i in range(5):
                x=RIGHT-150+i*28; add_check(self.p,(x,self.y,x+14,self.y+14),border=LINE)
            self.y+=22
        self.y+=6
    def lines(self,n,gap=22,x=ML,w=None):
        w=w or (RIGHT-x); self.need(n*gap+4); top=self.y
        for _ in range(n):
            self.p.draw_line((x,self.y+12),(x+w,self.y+12),color=LINE,width=0.8); self.y+=gap
        add_text(self.p,(x,top-4,x+w,self.y-4),size=11,multiline=True); self.y+=6
    def checkrow(self,label):
        self.need(22); add_check(self.p,(ML,self.y+1,ML+13,self.y+14))
        self.p.insert_text((ML+22,self.y+12),label,fontsize=10.5,fontname=B,color=INK); self.y+=22
    def blank(self,label,suffix="",fw=60,size=11):
        self.need(28); self.p.insert_text((ML,self.y+13),label,fontsize=size,fontname=BB,color=BLU)
        lx=ML+fitz.get_text_length(label,fontname=BB,fontsize=size)+8
        add_text(self.p,(lx,self.y,lx+fw,self.y+18),size=size,color=BLU)
        if suffix: self.p.insert_text((lx+fw+6,self.y+13),suffix,fontsize=size,fontname=BB,color=BLU)
        self.y+=30
    def notes(self,label="Le tue note",n=4):
        self.h2(label); self.lines(n)
    def save(self,name):
        self.doc.need_appearances(True)
        self.doc.save(os.path.join(OUT,name), deflate=True)
        nf=sum(len(list(p.widgets())) for p in self.doc)
        print("OK",name,self.doc.page_count,"pg ·",nf,"campi")

# ───── G1 — Test di Consapevolezza Digitale ─────
d=Doc("Bonus Giorno 1")
d.header("BONUS · GIORNO 1","Test di Consapevolezza Digitale","Prima di costruire, devi vederti")
d.para("Dai un voto da 1 a 5 a ciascuna area. Sii onesto: questo test non serve a giudicarti, "
       "serve a darti un punto di partenza misurabile.")
d.rating(["Brand personale online","Posizionamento di zona","Presenza sui social","Qualità dei contenuti",
          "Email marketing","CRM e follow-up","Uso dell'AI","Ecosistema digitale"])
d.blank("Punteggio totale:","/ 40")
d.h2("Dove sei, davvero")
d.bullets(["8-15 · Inizio percorso: oggi stai regalando incarichi. Parti dalle fondamenta.",
           "16-24 · Potenziale con dispersione: hai pezzi scollegati, ti serve un sistema.",
           "25-32 · In crescita, non ancora dominante: il sistema c'è, manca la scala.",
           "33-40 · Professionista evoluto: ottimizza e scala ciò che funziona."])
d.para("Qualunque sia il numero, la buona notizia e' la stessa: non e' talento. E' una macchina. E si costruisce.",
       size=10.5,font=TI,color=BORG)
d.notes("Le mie note + la prima cosa che cambio",3)
d.save("g1-test-consapevolezza.pdf")

# ───── G2 — La Mappa della Macchina (poster) ─────
d=Doc("Bonus Giorno 2")
d.header("BONUS · GIORNO 2","La Mappa della Macchina","Tienila a mente: e' tutto il sistema")
img=os.path.join(DIAG,"1-macchina.png")
if os.path.exists(img):
    d.p.insert_image(fitz.Rect(ML,d.y,RIGHT,d.y+330),filename=img); d.y+=346
d.h2("Come si legge")
d.bullets(["DIGITALE (fa alzare la mano): YouTube e' la biblioteca che lavora H24; l'organico costruisce autorita'; le ads portano volume.",
           "LEAD: la persona giusta che si fa avanti.",
           "ANALOGICO (converte): la chiamata in pochi minuti, i referral, gli eventi e le liste.",
           "INCARICO: il risultato. Digitale e analogico sono la stessa macchina."])
d.notes("Come la applico al mio mercato",3)
d.save("g2-mappa-macchina.pdf")

# ───── G3 — Kit Contenuti che Vendono ─────
d=Doc("Bonus Giorno 3")
d.header("BONUS · GIORNO 3","Kit Contenuti che Vendono","30 idee, la ricetta e le parole giuste")
d.h2("Home tour (vendi il metodo, non le stanze)")
d.bullets(["Ho venduto questa casa in X giorni a [zona]: ecco come","Cosa ho fatto PRIMA di pubblicare questa casa",
           "Perche' questa casa era 'invendibile' (e come l'ho venduta)"])
d.h2("Esperto del quartiere")
d.bullets(["Quanto vale davvero casa in [via/zona]","Cosa stanno facendo i prezzi a [quartiere]",
           "3 cose che nessuno ti dice prima di vendere a [zona]"])
d.h2("Esperto dei servizi della zona")
d.bullets(["Le scuole, i trasporti, i servizi di [zona]: la guida","Perche' la gente vuole comprare a [zona]"])
d.h2("Esperto del prezzo")
d.bullets(["I 3 errori che ti fanno svendere casa a [citta']","Il prezzo 'civetta': perche' ti fa perdere soldi",
           "Come capire se la tua casa e' sopravvalutata in 60 secondi"])
d.h2("La Ricetta del Video")
d.bullets(["Hook (3 sec) -> Problema -> Metodo -> Prova -> una sola CTA",
           "Raw, volto, verita'. Telefono, luce della finestra, audio vicino.",
           "1 video a settimana batte 10 in un giorno e poi piu' nulla."])
d.h2("Keyword Finder")
d.bullets(["Scrivi 'vendere casa [zona]' nella barra e guarda i suggerimenti.",
           "Quelle frasi diventano i titoli dei tuoi video."])
d.h2("Compila tu: la tua prossima settimana")
d.para("Le mie 3 idee video:",size=10,font=BB); d.lines(3)
d.para("5 parole chiave del mio mercato:",size=10,font=BB); d.lines(2)
d.para("La mia Ricetta del Video (compila):",size=10,font=BB)
for s in ["Hook (3 sec):","Problema:","Metodo:","Prova:","Una sola CTA:"]:
    d.para(s,size=9.5,font=BB,color=BORG,gap=1); d.lines(1)
d.save("g3-kit-contenuti.pdf")

# ───── G4 — Prompt Pack AI per l'Agente ─────
d=Doc("Bonus Giorno 4")
d.header("BONUS · GIORNO 4","Prompt Pack AI per l'Agente","Usa l'AI come un dipendente, non come un motore di ricerca")
d.para("Copia, incolla e personalizza tra [parentesi]. Questi prompt fanno il lavoro pesante al posto tuo.")
d.promptbox("1 · DALL'IDEA ALLO SCRIPT",
            "Sei il mio copywriter immobiliare. Scrivimi lo script di un video di 60 secondi\n"
            "per agenti, argomento: [argomento], zona: [zona], pubblico: venditori di casa.\n"
            "Struttura: hook di 3 secondi, problema, metodo, una prova, una sola CTA.\n"
            "Tono diretto e concreto, frasi brevi.")
d.promptbox("2 · UN VIDEO DIVENTA DIECI CONTENUTI",
            "Questo e' il testo del mio video: [incolla]. Trasformalo in: 3 clip brevi con\n"
            "sottotitoli, 2 post per Instagram, 1 carosello in 5 punti, 1 email. Mantieni\n"
            "lo stesso messaggio e la stessa CTA.")
d.promptbox("3 · RISPOSTA E QUALIFICA LEAD",
            "Agisci come il mio assistente. Un lead ha scritto: [messaggio]. Rispondi in modo\n"
            "cordiale, fai 3 domande per qualificarlo (tempistiche, zona, motivazione) e\n"
            "proponi due slot per una call. Massimo 5 righe.")
d.promptbox("4 · BOZZA VALUTAZIONE / ANNUNCIO",
            "Scrivi la descrizione di un annuncio per [tipo immobile] a [zona], [mq], [stato].\n"
            "Evidenzia 3 benefici per chi compra e chiudi con una CTA. Niente superlativi vuoti.")
d.h2("Schema dell'automazione (3 passi)")
d.bullets(["Il lead scrive (form, DM, WhatsApp)","L'AI risponde e qualifica H24",
           "Ti passa solo chi e' pronto -> tu richiami in minuti, non ore"])
d.notes("Il mio prompt personalizzato (scrivilo qui)",4)
d.save("g4-prompt-pack-ai.pdf")

# ───── G5 — Script Prima Chiamata + Obiezioni ─────
d=Doc("Bonus Giorno 5")
d.header("BONUS · GIORNO 5","Script Prima Chiamata + Obiezioni","La mano alzata si converte subito")
d.para("Speed-to-lead: la probabilita' di chiudere crolla col passare dei minuti. Richiama in minuti, non in ore.",
       size=10.5,font=TI,color=BORG)
d.h2("Lo schema della prima chiamata (5 passi)")
d.bullets(["Riprendi l'angolo del contenuto: 'Hai visto il video su [tema]...'",
           "Una domanda che apre: 'Come mai stai pensando di vendere?'",
           "Ascolta davvero (l'80% del tempo parla lui).",
           "Fissa l'appuntamento: due opzioni di orario, non 'quando vuoi'.",
           "Conferma: riassumi e manda promemoria."])
d.h2("Anti-obiezione · 3 mosse")
d.bullets(["Accogli: 'Capisco, e' giusto chiederselo.'",
           "Ribalta: 'Proprio per questo esiste il mio metodo...'",
           "Prova: 'Guarda qui' (un caso, un numero, un documento)."])
d.h2("Le obiezioni piu' comuni (e come rispondere)")
d.bullets(["'Non mi vincolo' -> incarico a tempo definito: dopo X giorni sei libero.",
           "'Non firmo niente' -> firmi un metodo, non una gabbia: ecco cosa faccio per te.",
           "'E se viene un privato?' -> proprio per questo seleziono acquirenti gia' pronti.",
           "'La provvigione e' alta' -> e' legata al risultato: vendere al prezzo giusto, prima."])
d.h2("Scrivi il tuo")
d.para("La mia apertura (come riprendo il contenuto):",size=10,font=BB); d.lines(2)
d.para("Le mie risposte alle obiezioni della mia zona:",size=10,font=BB); d.lines(3)
d.save("g5-script-chiamata-obiezioni.pdf")

print("Tutti i bonus generati in", OUT)

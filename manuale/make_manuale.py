#!/usr/bin/env python3
"""Genera il Manuale Studio / Workbook (PDF compilabile) del workshop 5 giorni.
Brand-styled con PyMuPDF (font base14), embed dei diagrammi, box e righe da compilare."""
import fitz, os

OUT = os.path.dirname(os.path.abspath(__file__))
DIAG = os.path.join(OUT, "..", "piani", "diagrammi")
W, H = 595, 842            # A4 portrait
ML, MR, MT, MB = 52, 52, 60, 56
RIGHT = W - MR

# Palette brand (0-1)
BLU=(0.071,0.157,0.212); ORO=(0.788,0.659,0.298); BORG=(0.294,0.071,0.188)
CREAM=(0.980,0.969,0.945); GRIGIO=(0.95,0.94,0.92)
INK=(0.12,0.13,0.14); MUTE=(0.42,0.45,0.47); LINE=(0.80,0.78,0.74); WHITE=(1,1,1)
T="tibo"; TI="tiit"; B="helv"; BB="hebo"   # serif titoli / sans testo

doc = fitz.open()

def wrap(text, font, size, maxw):
    out=[]
    for raw in text.split("\n"):
        words=raw.split(); cur=""
        for w in words:
            t=(cur+" "+w).strip()
            if fitz.get_text_length(t, fontname=font, fontsize=size)<=maxw: cur=t
            else:
                if cur: out.append(cur)
                cur=w
        out.append(cur)
    return out

class Page:
    def __init__(self):
        self.p=doc.new_page(width=W,height=H); self.y=MT
        self.p.draw_rect(fitz.Rect(0,0,W,6), color=None, fill=ORO)
        self.foot()
    def foot(self):
        self.p.insert_text((ML,H-30),"AGENTE STRATEGICO  ·  Dall'Analogico al Digitale  ·  Quaderno di lavoro",
                           fontsize=7.5,fontname=B,color=MUTE)
        self.p.insert_text((RIGHT-14,H-30),str(doc.page_count),fontsize=7.5,fontname=B,color=MUTE)
    def need(self,space):
        if self.y+space>H-MB: return Page()
        return self

def para(pg,text,size=10.5,font=B,color=INK,lead=None,x=ML,maxw=None,gap=4):
    maxw=maxw or (RIGHT-x); lead=lead or size*1.5
    for ln in wrap(text,font,size,maxw):
        pg=pg.need(lead)
        pg.p.insert_text((x,pg.y+size),ln,fontsize=size,fontname=font,color=color); pg.y+=lead
    pg.y+=gap; return pg

def h2(pg,text):
    pg=pg.need(30)
    pg.p.draw_rect(fitz.Rect(ML,pg.y+2,ML+22,pg.y+6),color=None,fill=ORO)
    pg.p.insert_text((ML+30,pg.y+14),text,fontsize=14,fontname=T,color=BLU); pg.y+=30; return pg

def bullets(pg,items,size=10.5,gap=3):
    for it in items:
        pg=pg.need(size*1.5)
        pg.p.insert_text((ML+6,pg.y+size),"•",fontsize=size,fontname=BB,color=ORO)
        for i,ln in enumerate(wrap(it,B,size,RIGHT-ML-22)):
            pg=pg.need(size*1.5)
            pg.p.insert_text((ML+22,pg.y+size),ln,fontsize=size,fontname=B,color=INK); pg.y+=size*1.5
        pg.y+=gap
    pg.y+=3; return pg

def lines(pg,n,gap=22,x=ML,w=None):
    w=w or (RIGHT-x)
    for _ in range(n):
        pg=pg.need(gap)
        pg.p.draw_line((x,pg.y+12),(x+w,pg.y+12),color=LINE,width=0.8); pg.y+=gap
    pg.y+=4; return pg

def soundbite(pg,text):
    h=14+len(wrap(text,TI,13,RIGHT-ML-60))*20
    pg=pg.need(h+14)
    pg.p.draw_rect(fitz.Rect(ML,pg.y,RIGHT,pg.y+h),color=None,fill=CREAM)
    pg.p.draw_rect(fitz.Rect(ML,pg.y,ML+5,pg.y+h),color=None,fill=ORO)
    yy=pg.y+22
    for ln in wrap(text,TI,13,RIGHT-ML-60):
        pg.p.insert_text((ML+24,yy),ln,fontsize=13,fontname=TI,color=BORG); yy+=20
    pg.y+=h+14; return pg

def box(pg,h,label=None):
    pg=pg.need(h+8)
    pg.p.draw_rect(fitz.Rect(ML,pg.y,RIGHT,pg.y+h),color=LINE,fill=None,width=0.8)
    if label: pg.p.insert_text((ML+8,pg.y+14),label,fontsize=8.5,fontname=BB,color=MUTE)
    pg.y+=h+8; return pg

def checkrow(pg,label,boxed=True):
    pg=pg.need(22)
    pg.p.draw_rect(fitz.Rect(ML,pg.y+1,ML+13,pg.y+14),color=BLU,fill=None,width=1)
    pg.p.insert_text((ML+22,pg.y+12),label,fontsize=10.5,fontname=B,color=INK); pg.y+=22; return pg

def header(kicker,title,sub=None):
    pg=Page()
    pg.p.draw_rect(fitz.Rect(0,0,W,96),color=None,fill=BLU)
    pg.p.draw_rect(fitz.Rect(0,96,W,100),color=None,fill=ORO)
    pg.p.insert_text((ML,40),kicker,fontsize=9,fontname=BB,color=ORO)
    pg.p.insert_text((ML,72),title,fontsize=22,fontname=T,color=WHITE)
    if sub: pg.p.insert_text((ML,90),sub,fontsize=10,fontname=B,color=(0.8,0.85,0.9))
    pg.y=120; return pg

# ───────── COVER ─────────
c=Page(); c.p.draw_rect(fitz.Rect(0,0,W,H),color=None,fill=BLU)
c.p.draw_rect(fitz.Rect(0,0,W,6),color=None,fill=ORO)
c.p.insert_text((ML,150),"AGENTE STRATEGICO",fontsize=11,fontname=BB,color=ORO)
for i,ln in enumerate(["Dall'Analogico","al Digitale"]):
    c.p.insert_text((ML,250+i*54),ln,fontsize=46,fontname=T,color=WHITE)
c.p.insert_text((ML,380),"Il tuo quaderno di lavoro · 5 giorni",fontsize=15,fontname=TI,color=(0.85,0.88,0.92))
c.p.draw_line((ML,430),(RIGHT,430),color=ORO,width=1)
c.p.insert_text((ML,470),"Nome",fontsize=10,fontname=BB,color=ORO)
c.p.draw_line((ML,492),(RIGHT-160,492),color=(0.4,0.45,0.5),width=0.8)
c.p.insert_text((ML,540),"Scrivi tutto. La mente che non scrive, dimentica.",fontsize=11,fontname=TI,color=(0.7,0.75,0.8))

# ───────── COME SI USA + PATTO + BONUS ─────────
p=header("ISTRUZIONI","Come usare questo quaderno")
p=para(p,"Questo non è un blocco per appunti qualsiasi. È lo strumento che trasforma 5 giorni "
        "di ascolto in un sistema costruito. Ogni giorno ha la sua pagina: i concetti chiave, "
        "uno spazio per i tuoi appunti e un esercizio da completare. Fallo. È lì che avviene il cambiamento.")
p=h2(p,"Il patto d'aula")
p=bullets(p,["Telefono in silenzio: ogni distrazione è un incarico perso.",
             "Scrivi tutto: la mente che non scrive dimentica.",
             "Sii scomodo: se ti sembra tutto noto, non stai ascoltando."])
p=h2(p,"Come funzionano i bonus")
p=para(p,"Ogni giorno, restando fino alla fine, sblocchi un bonus digitale. E c'è di più: se per "
        "tutti e 5 i giorni posti il tuo compito svolto sul nostro canale WhatsApp, ti guadagni "
        "LA CASSAFORTE (valore 399 euro) — in regalo. Questa pagina è il tuo passaporto.")
p=h2(p,"Passaporto Cassaforte — posta il compito ogni giorno")
for d in ["Giorno 1 — compito postato su WhatsApp","Giorno 2 — compito postato su WhatsApp",
          "Giorno 3 — compito postato su WhatsApp","Giorno 4 — compito postato su WhatsApp",
          "Giorno 5 — compito postato su WhatsApp"]:
    p=checkrow(p,d)
p=para(p,"5 caselle spuntate = Cassaforte (399 euro) sbloccata.",size=10,font=BB,color=BORG)

# ───────── PUNTO DI PARTENZA ─────────
p=header("PRIMA DI INIZIARE","Il tuo punto di partenza")
p=para(p,"Sii onesto. Non per giudicarti: per vederti. Dai un voto da 1 a 5 a ciascuna area.")
aree=["Brand personale online","Posizionamento di zona","Presenza sui social","Qualità dei contenuti",
      "Email marketing","CRM e follow-up","Uso dell'AI","Ecosistema digitale"]
for a in aree:
    p=p.need(24)
    p.p.insert_text((ML,p.y+13),a,fontsize=10.5,fontname=B,color=INK)
    for i in range(5):
        x=RIGHT-150+i*28
        p.p.draw_rect(fitz.Rect(x,p.y+1,x+16,p.y+17),color=LINE,width=0.8)
        p.p.insert_text((x+5,p.y+13),str(i+1),fontsize=8.5,fontname=B,color=MUTE)
    p.y+=24
p.y+=6
p=para(p,"Punteggio totale: _______ / 40",size=11,font=BB,color=BLU)
p=h2(p,"Dove voglio essere tra 90 giorni")
p=lines(p,4)

# ───────── GIORNI ─────────
giorni=[
 ("GIORNO 1","Il cambio di paradigma",
  "Capire che il mondo è cambiato — e che restare fermi significa diventare invisibili.",
  ["Il mercato è salito dall'analogico al digitale: chi non evolve sparisce.",
   "L'organico (IG/FB) è come l'analogico: non scala, si ferma se ti fermi.",
   "Non è un problema di marketing. È un problema di sistema."],
  "Oggi esiste la pizza da 8.000 euro. Nel tuo mercato qualcuno fa già la versione gourmet del tuo lavoro.",
  "esercizio1"),
 ("GIORNO 2","Il sistema scalabile",
  "Vedere la macchina intera e capire perché YouTube e le ads cambiano la scala.",
  ["Organico e ads non sono alternative: autorità + volume.",
   "Un dipendente costa ogni mese. Un video costa una volta e lavora per anni.",
   "I tuoi primi 10 venditori sono nella tua rubrica: referral e centri d'influenza."],
  "Instagram è una festa: se non ci sei, sparisci. YouTube è una biblioteca: ti trova mentre dormi.",
  "esercizio2"),
 ("GIORNO 3","Contenuti che cercano i venditori",
  "Sapere esattamente cosa pubblicare per farti trovare da chi vuole vendere.",
  ["4 format: home tour, esperto del quartiere, dei servizi, del prezzo.",
   "Il venditore cerca 'quanto vale casa mia in via...': sii tu la risposta.",
   "Fatto è meglio di perfetto. La costanza batte la perfezione."],
  "Generico è dimenticabile. Specifico è selezionabile.",
  "esercizio3"),
 ("GIORNO 4","Il modulo AI + l'analogico che converte",
  "Usare l'AI come un moltiplicatore e chiudere il cerchio sulla conversione.",
  ["Usa l'AI come un dipendente, non come un motore di ricerca.",
   "Dall'idea allo script in un passo. Un video diventa dieci contenuti.",
   "Il digitale alza la mano. L'analogico la converte. Minuti, non ore."],
  "L'AI non ti sostituisce. Lo fa l'agente che la usa mentre tu no.",
  "esercizio4"),
 ("GIORNO 5","La macchina completa + il prossimo livello",
  "Mettere insieme tutti i pezzi e decidere come costruire il tuo sistema.",
  ["La macchina completa: digitale + analogico, una cosa sola.",
   "Non sono fenomeni: hanno solo acceso prima la macchina.",
   "La differenza non è il talento. È una decisione."],
  "Questo workshop è l'apertura del cantiere. Le Masterclass sono il cantiere.",
  "esercizio5"),
]

def esercizio(pg,key):
    pg=h2(pg,"Il tuo esercizio")
    if key=="esercizio1":
        pg=para(pg,"Riporta qui il tuo punteggio totale e scrivi la tua frase dei 90 giorni.")
        pg=para(pg,"Punteggio: _______ / 40",size=11,font=BB,color=BLU)
        pg=para(pg,"Tra 90 giorni voglio...",size=10,font=BB,color=INK,gap=2); pg=lines(pg,3)
    elif key=="esercizio2":
        pg=para(pg,"Il formato YouTube che presidierò per 90 giorni:",size=10,font=BB); pg=lines(pg,1)
        pg=para(pg,"I miei 3 centri d'influenza da riattivare:",size=10,font=BB); pg=lines(pg,3)
    elif key=="esercizio3":
        pg=para(pg,"La Ricetta del Video — compila per il tuo prossimo video:",size=10,font=BB)
        for step in ["1. Hook (3 secondi):","2. Problema:","3. Metodo:","4. Prova:","5. Una sola CTA:"]:
            pg=para(pg,step,size=9.5,font=BB,color=BORG,gap=1); pg=lines(pg,1)
        pg=para(pg,"3 idee 'esperto di...' + 5 parole chiave del mio mercato:",size=10,font=BB); pg=lines(pg,4)
    elif key=="esercizio4":
        pg=para(pg,"L'automazione AI che imposto per prima:",size=10,font=BB); pg=lines(pg,1)
        pg=para(pg,"Lo schema della mia prima chiamata (5 passi):",size=10,font=BB)
        for s in ["1. Riprendo l'angolo del contenuto","2. Una domanda che apre","3. Ascolto",
                  "4. Fisso l'appuntamento","5. Confermo"]:
            pg=para(pg,s,size=9.5,font=B,color=INK,gap=1)
        pg=para(pg,"Le mie 3 mosse anti-obiezione: accogli · ribalta · prova",size=10,font=BB)
    elif key=="esercizio5":
        pg=para(pg,"Il mio piano d'azione a 90 giorni (3 azioni concrete):",size=10,font=BB); pg=lines(pg,5)
        pg=checkrow(pg,"Ho deciso: voglio costruire la macchina, non restare con la mappa.")
    return pg

for kic,tit,obj,ric,sb,ex in giorni:
    p=header(kic,tit)
    p=para(p,"Obiettivo: "+obj,size=11,font=TI,color=MUTE)
    p=h2(p,"3 cose da ricordare")
    p=bullets(p,ric)
    p=soundbite(p,sb)
    p=h2(p,"Spazio appunti")
    p=lines(p,4)
    p=esercizio(p,ex)
    p=p.need(26)
    p=checkrow(p,"Fatto oggi · compito postato sul canale WhatsApp")

# ───────── TOOLKIT ─────────
p=header("TOOLKIT","I tuoi strumenti","Template riutilizzabili dopo il workshop")
p=h2(p,"La Ricetta del Video")
p=bullets(p,["Hook (3 sec) → Problema → Metodo → Prova → una sola CTA",
             "Raw, volto, verità. Telefono, luce della finestra, audio vicino.",
             "1 video a settimana batte 10 in un giorno e poi più nulla."])
p=h2(p,"Keyword Finder")
p=bullets(p,["Scrivi 'vendere casa [zona]' nella barra di ricerca e guarda i suggerimenti.",
             "Quelle frasi sono i tuoi titoli: 'quanto vale casa [zona]', 'agenzia [zona]'."])
p=h2(p,"Calendario contenuti — la mia settimana")
for g in ["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]:
    p=p.need(22)
    p.p.insert_text((ML,p.y+13),g,fontsize=9.5,fontname=BB,color=BLU)
    p.p.draw_line((ML+40,p.y+13),(RIGHT,p.y+13),color=LINE,width=0.8); p.y+=22
p.y+=4

p=header("TOOLKIT","Conversione & relazioni")
p=h2(p,"Schema prima chiamata (speed-to-lead: minuti, non ore)")
p=bullets(p,["Riprendi l'angolo del contenuto","Una domanda che apre","Ascolta",
             "Fissa l'appuntamento","Conferma"])
p=h2(p,"Schema anti-obiezione — 3 mosse")
p=bullets(p,["Accogli: 'capisco'","Ribalta: 'proprio per questo...'","Prova: 'guarda qui'"])
p=para(p,"Obiezioni comuni: «non mi vincolo» · «non firmo niente» · «e se viene un privato?» · «la provvigione».",size=10,color=MUTE)
p=h2(p,"Mappa dei centri d'influenza")
p=para(p,"Chi, già oggi, parla con chi vende casa? (commercialisti, amministratori, ex clienti, attività di zona)",size=10,font=BB)
p=lines(p,4)

# La Macchina (diagramma)
p=header("LA MAPPA","La Macchina","Tienila a mente: è tutto il sistema, in una immagine")
img=os.path.join(DIAG,"1-macchina.png")
if os.path.exists(img):
    p=p.need(360); p.p.insert_image(fitz.Rect(ML,p.y,RIGHT,p.y+330),filename=img); p.y+=340

# ───────── PROSSIMO PASSO ─────────
p=header("E ADESSO","Il prossimo passo")
p=para(p,"In 5 giorni hai disegnato la mappa: sai cosa serve. Ma una mappa non costruisce la "
        "macchina. Il modo per costruirla — pezzo per pezzo, sul tuo mercato — esiste, e lo "
        "vedrai. Per ora, una sola cosa conta: hai già iniziato.")
p=soundbite(p,"Cosa vuoi che sia successo tra 12 settimane?")

doc.save(os.path.join(OUT,"workshop-5-giorni-workbook.pdf"), deflate=True, garbage=4, clean=True)
print("OK workbook:", doc.page_count, "pagine")

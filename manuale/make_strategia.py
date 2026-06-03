#!/usr/bin/env python3
"""La Strategia Completa — guida leggibile per Giuseppe. PDF brand-styled (PyMuPDF)."""
import fitz, os
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # radice repo
W,H=595,842; ML,MR,MT,MB=52,52,58,52; RIGHT=W-MR
BLU=(0.071,0.157,0.212); ORO=(0.788,0.659,0.298); BORG=(0.294,0.071,0.188)
CREAM=(0.980,0.969,0.945); INK=(0.13,0.14,0.15); MUTE=(0.45,0.47,0.49)
LINE=(0.80,0.78,0.74); WHITE=(1,1,1)
T="tibo"; TI="tiit"; B="helv"; BB="hebo"
doc=fitz.open()

def wrap(t,f,s,m):
    out=[]
    for raw in t.split("\n"):
        cur=""
        for w in raw.split():
            x=(cur+" "+w).strip()
            if fitz.get_text_length(x,fontname=f,fontsize=s)<=m: cur=x
            else: out.append(cur); cur=w
        out.append(cur)
    return out

class D:
    def __init__(s): s.new()
    def new(s):
        s.p=doc.new_page(width=W,height=H); s.y=MT
        s.p.draw_rect(fitz.Rect(0,0,W,5),fill=ORO,color=None)
        s.p.insert_text((ML,H-30),"AGENTE STRATEGICO  ·  La Strategia Completa",fontsize=7.5,fontname=B,color=MUTE)
        s.p.insert_text((RIGHT-12,H-30),str(doc.page_count),fontsize=7.5,fontname=B,color=MUTE)
    def need(s,h):
        if s.y+h>H-MB: s.new()
    def h1(s,kick,title):
        s.need(54)
        s.p.draw_rect(fitz.Rect(ML,s.y+3,ML+26,s.y+7),fill=ORO,color=None)
        s.p.insert_text((ML+34,s.y+8),kick,fontsize=8.5,fontname=BB,color=ORO)
        s.y+=18
        for ln in wrap(title,T,19,RIGHT-ML):
            s.need(24); s.p.insert_text((ML,s.y+16),ln,fontsize=19,fontname=T,color=BLU); s.y+=26
        s.y+=6
    def h2(s,text):
        s.need(28)
        s.p.insert_text((ML,s.y+13),text,fontsize=13,fontname=BB,color=BORG); s.y+=24
    def para(s,text,size=10.5,font=B,color=INK,gap=7):
        for ln in wrap(text,font,size,RIGHT-ML):
            s.need(size*1.5); s.p.insert_text((ML,s.y+size),ln,fontsize=size,fontname=font,color=color); s.y+=size*1.5
        s.y+=gap
    def bullets(s,items,size=10.5,num=False):
        for i,it in enumerate(items):
            mark=(f"{i+1}." if num else "•")
            s.need(size*1.5)
            s.p.insert_text((ML+4,s.y+size),mark,fontsize=size,fontname=BB,color=ORO)
            for j,ln in enumerate(wrap(it,B,size,RIGHT-ML-26)):
                s.need(size*1.5); s.p.insert_text((ML+24,s.y+size),ln,fontsize=size,fontname=B,color=INK); s.y+=size*1.5
            s.y+=3
        s.y+=5
    def callout(s,text,accent=ORO):
        lines=wrap(text,TI,10.5,RIGHT-ML-30); h=16+len(lines)*15
        s.need(h+8)
        s.p.draw_rect(fitz.Rect(ML,s.y,RIGHT,s.y+h),fill=CREAM,color=None)
        s.p.draw_rect(fitz.Rect(ML,s.y,ML+5,s.y+h),fill=accent,color=None)
        yy=s.y+18
        for ln in lines: s.p.insert_text((ML+18,yy),ln,fontsize=10.5,fontname=TI,color=BORG); yy+=15
        s.y+=h+10

d=D()
# COVER
d.p.draw_rect(fitz.Rect(0,0,W,H),fill=BLU,color=None)
d.p.draw_rect(fitz.Rect(0,0,W,6),fill=ORO,color=None)
d.p.insert_text((ML,150),"AGENTE STRATEGICO",fontsize=11,fontname=BB,color=ORO)
for i,ln in enumerate(["La Strategia","Completa"]):
    d.p.insert_text((ML,250+i*54),ln,fontsize=46,fontname=T,color=WHITE)
d.p.insert_text((ML,380),"Guida per Giuseppe — in parole semplici",fontsize=15,fontname=TI,color=(0.85,0.88,0.92))
d.p.draw_line((ML,420),(RIGHT,420),color=ORO,width=1)
d.p.insert_text((ML,455),"Come ogni pezzo serve la strategia · cosa è fatto · dove puoi dare una mano",
                fontsize=11,fontname=B,color=(0.75,0.8,0.85))
d.new()

d.h1("VISIONE","La tesi, in 3 righe")
d.para("Il mercato immobiliare è passato dall'analogico al digitale. Ma il digitale da solo non basta: "
    "serve un sistema digitale che scala (contenuti, YouTube, AI) agganciato all'analogico che converte "
    "(la chiamata, i referral, gli eventi). Chi costruisce questa macchina viene scelto; chi resta fermo "
    "diventa invisibile.")

d.h1("I PRODOTTI","La scala dei prodotti (il \"funnel ascendente\")")
d.para("Nessuno ti da 3.600 € appena ti conosce. Quindi facciamo salire le persone un gradino alla volta:")
d.bullets([
 "Gratis — Awareness: video manifesto + contenuti organici che portano al sito.",
 "€149 — Bootcamp (3 giorni): il primo \"si\", a basso rischio.",
 "€399 — La Cassaforte: raccolta di video registrati; chi la consuma e' pronto al passo dopo.",
 "€3.600 — 12 Masterclass + Workshop avvio (oppure 6 rate da €600): il cuore dell'offerta.",
 "Alto — Community (Pro/Elite) o Sistema Presenza Dominante (€5.000): per chi vuole tutto fatto.",
],num=True)
d.callout("Ogni gradino crea la fiducia per il successivo. I \"ponti\" fra i gradini (cosa scatta in "
          "automatico dopo ogni acquisto) sono cio' che oggi manca: e' la macchina che stiamo costruendo.")

d.h1("LA MACCHINA","I 5 motori (come funzionano e perche')")
d.h2("Motore 1 — Il Workshop e' uno strumento di vendita")
d.para("5 giorni gratuiti che al Giorno 5 vendono il percorso da 3.600 €. Regola d'oro: non si vende il "
    "Giorno 5, si vende la presenza nei 5 giorni. Piu' gente arriva viva al Giorno 5, piu' si vende.")
d.h2("Motore 2 — I Bonus + La Cassaforte (presenza + qualifica)")
d.para("Ogni giorno sblocchi un regalo se resti fino alla fine. E se posti i compiti sul canale WhatsApp "
    "per tutti e 5 i giorni, ti regaliamo La Cassaforte (vale 399 €). Doppio effetto: tiene le persone "
    "presenti fino al Giorno 5 (la vendita) e ci dice chi e' il piu' ingaggiato = il piu' probabile compratore.")
d.h2("Motore 3 — Il Funnel email sui ~20.000 contatti")
d.para("Hai ~20.000 persone mai contattate: un tesoro fermo. Ma se le bombardi di vendita le bruci. Quindi "
    "la sequenza parte dando valore (\"ti ricordi di noi? ecco una cosa utile\") e solo dopo propone. "
    "Le riattiva senza farle scappare.")
d.h2("Motore 4 — Il Video Manifesto + i contenuti organici")
d.para("Un video di 2-3 minuti che racconta la tesi e attrae le persone giuste verso il sito. I contenuti "
    "devono cercare i venditori di casa (non i like): \"quanto vale casa in [zona]\", home tour, esperto "
    "del quartiere/dei servizi/del prezzo.")
d.h2("Motore 5 — Gli Eventi Nazionali (acceleratore)")
d.para("Due volte l'anno, 400-500 persone. Concentrano fiducia, vendite e community in un colpo solo. "
    "Si riempiono col funnel e con la community.")

d.h1("I NUMERI","I numeri che contano (in parole povere)")
d.bullets([
 "CPA = quanto spendo per far entrare UN cliente. Obiettivo: sotto 150 €.",
 "LTV = quanto vale IN TOTALE un cliente nel tempo. Obiettivo: 2.400 €+.",
 "Open rate = % di chi apre le email = salute del database. Obiettivo: 25%+.",
 "Conversione per gradino = quanti salgono da un prodotto al successivo.",
 "I 2 numeri minimi da misurare sempre: da dove arriva il lead + quanto velocemente lo ricontatto.",
])

d.h1("STATO","Dove siamo oggi (mappa onesta)")
d.h2("Fatto")
d.bullets([
 "Workshop 5 giorni completo: workbook compilabile, 5 bonus, deck, 5 slide 12 Masterclass, prezzo 3.600/600.",
 "Checklist evento (per te), to-do per Laura e Gabriele, email ai coach.",
 "Funnel lead gen: mappa, attivazione DB, sequenze email pronte, brief video manifesto.",
])
d.h2("In corso")
d.bullets(["Replica delle slide nuove nel deck live (Claude Design)."])
d.h2("Da fare")
d.bullets([
 "Landing €149 (Bootcamp) e €399 (Cassaforte).",
 "Quick win sito: comprimere le foto pesanti, sistemare le landing che danno errore.",
 "Estendere i piani editoriali social.",
 "Le decisioni della pagina seguente.",
])

d.h1("IL TUO RUOLO","Dove puoi dare una mano TU")
d.para("Questi sono i punti dove serve la tua testa, non la mia. Ogni \"si\" qui sblocca un pezzo di macchina:")
d.bullets([
 "Video Cassaforte — quali video registrati entrano nella Cassaforte (€399)?",
 "Tool email — GHL (sistemando le credenziali) o partiamo subito con Brevo/MailerLite?",
 "Testimonianze reali — 2-3 casi (nome, zona, numeri, con consenso).",
 "Dato reale del database — quanti contatti, e quanti con email valida?",
 "Date / citta' / posti — di workshop ed eventi, per riempire le email.",
 "Garanzia — il testo definitivo da mettere in vendita.",
 "Upsell Cassaforte a €299 in aula — si o no?",
 "Allineamento prezzo — confermo 3.600 anche dove c'e' ancora 3.999/4.000?",
],num=True)
d.callout("Come aiutarmi in pratica: rispondi a questi 8 punti (anche solo a voce), procura le 2-3 "
          "testimonianze, e dimmi quale tool email vuoi. Con questo, accendo la macchina.",accent=BORG)

d.h1("GLOSSARIO","Le parole, spiegate semplici")
d.bullets([
 "Funnel — il percorso \"a imbuto\" che porta uno sconosciuto a diventare cliente.",
 "Lead — un contatto interessato (ti ha lasciato l'email).",
 "Nurturing — \"coltivare\" il contatto con contenuti utili finche' e' pronto a comprare.",
 "Organico — contenuti gratis sui social (non sponsorizzati a pagamento).",
 "Awareness — la fase in cui le persone scoprono che esisti.",
 "Upsell — proporre il prodotto del gradino superiore.",
 "Cold / freddo — un contatto che non ti conosce o non ti sente da tempo.",
])

doc.save(os.path.join(OUT,"STRATEGIA-COMPLETA.pdf"), deflate=True)
print("OK strategia:", doc.page_count, "pagine")

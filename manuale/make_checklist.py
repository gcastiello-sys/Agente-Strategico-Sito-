#!/usr/bin/env python3
"""Checklist di controllo evento (per Giuseppe) — PDF brand-styled, stampabile."""
import fitz, os
OUT=os.path.dirname(os.path.abspath(__file__))
W,H=595,842; ML,MR,MT,MB=50,50,58,50; RIGHT=W-MR
BLU=(0.071,0.157,0.212); ORO=(0.788,0.659,0.298); BORG=(0.294,0.071,0.188)
CREAM=(0.980,0.969,0.945); INK=(0.13,0.14,0.15); MUTE=(0.45,0.47,0.49)
LINE=(0.78,0.76,0.72); WHITE=(1,1,1)
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

class Pg:
    def __init__(s):
        s.p=doc.new_page(width=W,height=H); s.y=MT
        s.p.draw_rect(fitz.Rect(0,0,W,5),fill=ORO,color=None)
        s.p.insert_text((ML,H-28),"AGENTE STRATEGICO  ·  Checklist evento — Workshop 5 Giorni",fontsize=7.5,fontname=B,color=MUTE)
        s.p.insert_text((RIGHT-12,H-28),str(doc.page_count),fontsize=7.5,fontname=B,color=MUTE)
    def need(s,h):
        return Pg() if s.y+h>H-MB else s

def cover_head(pg):
    pg.p.draw_rect(fitz.Rect(0,0,W,92),fill=BLU,color=None)
    pg.p.draw_rect(fitz.Rect(0,92,W,96),fill=ORO,color=None)
    pg.p.insert_text((ML,38),"PER GIUSEPPE · DA TENERE ACCANTO DURANTE L'EVENTO",fontsize=8.5,fontname=BB,color=ORO)
    pg.p.insert_text((ML,70),"Checklist di controllo",fontsize=23,fontname=T,color=WHITE)
    pg.y=112

def section(pg,title,items,accent=ORO):
    pg=pg.need(40)
    pg.p.draw_rect(fitz.Rect(ML,pg.y,RIGHT,pg.y+22),fill=CREAM,color=None)
    pg.p.draw_rect(fitz.Rect(ML,pg.y,ML+5,pg.y+22),fill=accent,color=None)
    pg.p.insert_text((ML+14,pg.y+15),title,fontsize=12,fontname=T,color=BLU); pg.y+=30
    for it in items:
        lines=wrap(it,B,9.5,RIGHT-ML-26)
        pg=pg.need(len(lines)*13+4)
        pg.p.draw_rect(fitz.Rect(ML+2,pg.y+1,ML+13,pg.y+12),color=BLU,width=0.9)
        for i,ln in enumerate(lines):
            pg.p.insert_text((ML+22,pg.y+10+i*13),ln,fontsize=9.5,fontname=B,color=INK)
        pg.y+=len(lines)*13+4
    pg.y+=8
    return pg

def band(pg,text,accent=BORG):
    pg=pg.need(26)
    pg.p.draw_rect(fitz.Rect(ML,pg.y,RIGHT,pg.y+20),fill=accent,color=None)
    pg.p.insert_text((ML+12,pg.y+14),text,fontsize=10,fontname=BB,color=WHITE); pg.y+=30
    return pg

p=Pg(); cover_head(p)

p=band(p,"PRIMA DELL'EVENTO",accent=ORO)
p=section(p,"5 giorni prima · Materiali & setup",[
 "Workbook PDF caricato, scaricabile e digitabile (provato da telefono e da PC)",
 "5 bonus PDF pronti e nominati G1->G5, ognuno apribile",
 "La Cassaforte esiste come accesso reale, pronta da consegnare (valore 399 € confermato)",
 "Canale WhatsApp creato, con regole + messaggio Cassaforte fissato in alto",
 "Sequenza 5 email pre-workshop scritta e schedulata (letta l'email workbook e quella bonus)",
 "Link aula testato + data e ora confermate ovunque",
 "Foglio di tracking compiti (nome -> G1..G5) pronto e condiviso",
],accent=ORO)
p=section(p,"5 giorni prima · Deck & contenuti",[
 "Deck aggiornato con le 7 slide bonus (4A/4B + Bonus 1-5 + Stack + fast-action)",
 "Placeholder chiusi: prove/casi reali, costo provvigione, garanzia, finestra/data iscrizione",
 "Offerta chiara: 3.999 € / 6x599 € + garanzia + scadenza + bonus fast-action",
 "Diagrammi 'La Macchina' (orizzontale + verticale) presenti dove servono",
],accent=ORO)
p=section(p,"5 giorni prima · Team & coach",[
 "Email strategia letta e capita da Vincenzo, Antonella, Giuseppe",
 "Vincenzo pronto su G1/G3/G5 (mindset, momento della decisione)",
 "Antonella ha casi e numeri reali dell'analogico (centri d'influenza, obiezioni, liste)",
 "Laura & Gabriele hanno la to-do e sanno chi fa cosa ogni giorno",
 "Call di allineamento col team fatta prima di partire",
],accent=ORO)
p=section(p,"La vigilia (giorno -1)",[
 "Email 'Domani si parte' inviata (data, ora, link, tieni workbook + sii nel WhatsApp)",
 "Workbook arrivato a tutti gli iscritti (verifica % aperture/download)",
 "Numero iscritti al canale WhatsApp vs iscritti totali controllato",
 "Tech check: audio, video, slide, condivisione schermo, registrazione ON",
],accent=ORO)

p=band(p,"DURANTE · OGNI GIORNO",accent=BORG)
p=section(p,"Prima della sessione",[
 "Slide del giorno aperte e in ordine; registrazione pronta",
 "Laura ricorda in apertura: resta fino alla fine = sblocchi il bonus di oggi",
 "Bonus del giorno pronto da inviare (link giusto)",
],accent=BORG)
p=section(p,"Durante",[
 "I tempi del giorno sono rispettati (si arriva al compito senza sforare)",
 "Il compito viene assegnato chiaramente prima di chiudere",
 "Slide 'Bonus N sbloccato' mostrata a fine sessione (barra N/5)",
],accent=BORG)
p=section(p,"Dopo la sessione",[
 "Gabriele ha inviato il bonus sul WhatsApp + 'posta il compito qui'",
 "Compiti raccolti e spuntati sul foglio (numero controllato)",
 "Laura ha risposto/incoraggiato chi ha postato (gruppo vivo)",
 "Dato presenza del giorno guardato: chi sta mollando -> recupero soft",
],accent=BORG)

p=band(p,"GIORNO 5 · LA VENDITA",accent=BLU)
p=section(p,"Extra attenzione",[
 "Prove/casi reali inseriti e verificati (niente slide vuote)",
 "Vincenzo prepara la testa alla decisione prima dell'offerta",
 "Stack mostrato con 'Cassaforte gia sbloccata'",
 "Offerta con prezzo + garanzia + scadenza + bonus fast-action",
 "CTA unica + link iscrizione funzionante (testato poco prima)",
 "Chi ha fatto 5/5 identificato -> consegna Cassaforte pronta",
],accent=BLU)
p=section(p,"Dopo il Giorno 5",[
 "Cassaforte consegnata a chi ha completato 5/5",
 "Messaggio offerta a chi ha completato + recupero a chi no",
 "Numeri raccolti: presenze/giorno, % compiti, completamenti 5/5, iscrizioni, fatturato",
 "Registrazioni archiviate; debrief col team (cosa ha funzionato / cosa no)",
],accent=BLU)

# nota finale
p=p.need(60)
p.p.draw_rect(fitz.Rect(ML,p.y,RIGHT,p.y+44),fill=CREAM,color=None)
p.p.draw_rect(fitz.Rect(ML,p.y,ML+5,p.y+44),fill=ORO,color=None)
p.p.insert_text((ML+16,p.y+18),"Le 3 cose che NON devono mai mancare",fontsize=11,fontname=T,color=BORG)
p.p.insert_text((ML+16,p.y+34),"Workbook arrivato prima · meccanica WhatsApp che gira ogni giorno · offerta del G5 senza placeholder.",
                fontsize=9.5,fontname=BB,color=BLU)

doc.save(os.path.join(OUT,"checklist-evento.pdf"), deflate=True)
print("OK checklist:", doc.page_count, "pagine")

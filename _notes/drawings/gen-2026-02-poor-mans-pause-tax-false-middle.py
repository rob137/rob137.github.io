import re,os
_here=os.path.dirname(os.path.abspath(__file__))
defs=re.search(r'<defs>.*?</defs>',open(os.path.join(_here,'2026-10-08-pod-bay-doors.svg')).read(),re.S).group(0)
class D:
    def __init__(s,W,H,bg,ink,grey,accent='#d98b1a',red='#d9442b'):
        s.W,s.H,s.bg,s.ink,s.grey,s.accent,s.red=W,H,bg,ink,grey,accent,red; s.o=[f'<rect width="{W}" height="{H}" fill="{bg}"/>']
    def box(s,x,y,w,h,lines,rot=0,size=30,lh=36,fill=None,dash=False):
        cx,cy=x+w/2,y+h/2
        s.o.append(f'<g transform="rotate({rot} {cx} {cy})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill or s.bg}" stroke="{s.ink}" stroke-width="3" {"stroke-dasharray=\"12 10\"" if dash else ""}/>')
        n=len(lines); start=cy-(n-1)*lh/2+size*0.35
        for i,t in enumerate(lines):
            col=s.ink; sz=size
            if isinstance(t,tuple): t,col,sz=t
            s.o.append(f'<text x="{cx}" y="{start+i*lh:.1f}" text-anchor="middle" font-size="{sz}" fill="{col}">{t}</text>')
        s.o.append('</g>')
    def arrow(s,d,dash=False,w=2.5,head=True):
        s.o.append(f'<path d="{d}" fill="none" stroke="{s.ink}" stroke-width="{w}" {"stroke-dasharray=\"12 10\"" if dash else ""} {"marker-end=\"url(#ah)\"" if head else ""}/>')
    def path(s,d,col=None,w=3,dash=False):
        s.o.append(f'<path d="{d}" fill="none" stroke="{col or s.ink}" stroke-width="{w}" stroke-linecap="round" {"stroke-dasharray=\"12 10\"" if dash else ""}/>')
    def txt(s,x,y,t,size=28,col=None,anchor='middle',rot=0):
        s.o.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{col or s.grey}" transform="rotate({rot} {x} {y})">{t}</text>')
    def svg(s):
        body='\n'.join(s.o)
        out=f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.W}" height="{s.H}" viewBox="0 0 {s.W} {s.H}">\n{defs}\n{body}\n</svg>'
        if s.ink!='#1f1f1f': out=out.replace('#1f1f1f',s.ink)
        return out

def poor_mans(d):
    I,G=d.ink,d.grey
    d.txt(750,60,'Where the workflow lives',46,I)
    # left panel
    d.box(60,110,660,620,[],0.2)
    d.txt(390,160,'in a harness',32,I)
    d.box(130,200,520,380,[],-0.4,dash=False)  # app window
    d.txt(390,236,'the app',26)
    d.box(160,260,140,56,['New task'],0.6,24); d.box(320,260,150,56,['Worktree'],-0.5,24); d.box(490,260,130,56,['Run'],0.4,24)
    d.box(170,350,240,180,['workflow','logic','(code)'],-0.3,26,lh=32)
    d.box(440,370,170,140,['model'],0.5,30)
    d.path('M425 362 L425 530',I,3)
    d.txt(425,352,'✗',30,d.red)
    d.txt(390,640,'the model can\'t see the workflow it\'s in,',26)
    d.txt(390,674,'so you keep explaining its own environment to it',26)
    # right panel
    d.box(780,110,660,620,[],-0.2)
    d.txt(1110,160,'in a prompt',32,I)
    d.box(850,210,300,330,[('ORCHESTRATOR.md',I,24),('',I,20),('manage worktrees',G,22),('codex in background',G,22),('test as you go',G,22),('judge what comes back',G,22),('ask before pushing',G,22)],0.4,22,lh=30)
    d.arrow('M1154 375 L1218 375')
    d.txt(1186,355,'reads',22)
    d.box(1222,305,170,140,['model'],-0.5,30)
    d.txt(1110,640,'the workflow is visible to the thing doing the work,',26)
    d.txt(1110,674,'so it can reason about it and notice when it doesn\'t fit',26)
    d.txt(750,785,'Same workflow. One copy is intelligence in code the model can\'t see.',28,I)

def pause_tax(d):
    I,G=d.ink,d.grey
    d.txt(750,60,'Where the time went',46,I)
    # before timeline
    d.txt(90,150,'before',32,I,anchor='start')
    y=200
    d.arrow(f'M90 {y+80} L1420 {y+80}',w=2)
    x=90
    segs=[('model works',230),('me',150),('model works',230),('me',170),('model works',230),('me',150)]
    for lab,w in segs:
        if lab=='model works':
            d.box(x,y,w,80,[('model works',I,24)],0.3,24)
        else:
            d.path(f'M{x+10} {y+10} L{x+w-10} {y+70} M{x+w-10} {y+10} L{x+10} {y+70}',G,2)
            d.txt(x+w/2,y+112,'"quickly"',22); d.txt(x+w/2,y+140,'checking Teams',22)
        x+=w
    d.txt(1430,y+50,'time',24,anchor='start')
    d.txt(750,400,'each pause felt momentary. the train stopped every time.',26)
    # now
    d.txt(90,440,'now',32,I,anchor='start')
    y2=600
    d.box(90,520,1330,0,[],0) if False else None
    d.box(470,470,560,70,[('org file: a living list of to-do items that are really prompts',I,24)],-0.3,24)
    d.arrow('M750 544 L750 590',dash=False)
    d.txt(775,575,'pulls the next item',22,anchor='start')
    x=90
    for i in range(6):
        d.box(x,y2,215,80,[('model works',I,24)],(-0.3 if i%2 else 0.3),24)
        x+=222
    d.arrow(f'M90 {y2+120} L1420 {y2+120}',w=2)
    d.txt(1430,y2+90,'time',24,anchor='start')
    # me watching above feeding
    d.box(190,440,250,70,[('me, watching',I,24)],-0.5,24)
    d.arrow('M442 475 L466 492')
    d.txt(750,775,'The system doesn\'t block on me between tasks. I steer; it keeps moving.',28,I)

def false_middle(d):
    I,G=d.ink,d.grey
    d.txt(750,60,'Meeting in the middle',46,I)
    # axes
    d.path('M150 560 L1350 560',I,2.5)
    d.path('M150 560 L150 140',I,2.5)
    d.txt(140,130,'how it goes',24,anchor='end')
    # curve: high at ends, low in middle (smile)
    d.path('M180 200 C 450 230, 600 500, 750 500 C 900 500, 1050 230, 1320 200',I,4)
    d.txt(250,610,'spreadsheet person',28,I)
    d.txt(250,644,'the adult in the room',24)
    d.txt(1250,610,'enthusiast',28,I)
    d.txt(1250,644,'Toad of Toad Hall',24)
    d.txt(750,610,'the middle',28,I)
    d.txt(750,644,'hedge, experiment carefully, phase it in',24)
    # marker
    d.o.append(f'<circle cx="750" cy="500" r="12" fill="{d.accent}" stroke="{I}" stroke-width="2"/>')
    d.txt(750,372,'too slow to seize it,',26)
    d.txt(750,406,'too distracted to avoid the traps',26)
    d.txt(280,290,'might be right',24)
    d.txt(1220,290,'might be right',24)
    d.txt(750,720,'The middle feels safe. It might just be the downsides of both.',28,I)

jobs=[('2026-02-05-poor-mans-prompt',poor_mans,1500,820),('2026-02-20-the-pause-tax',pause_tax,1500,820),('2026-02-01-the-false-middle',false_middle,1500,760)]
for name,fn,W,H in jobs:
    for suffix,cols in [('',('#f0eee6','#1f1f1f','#7a7a7a')),('-dark',('#1f1e1d','#e8e6e1','#a9a7a2'))]:
        d=D(W,H,*cols); fn(d)
        open(os.path.join(_here,f'{name}{suffix}.svg'),'w').write(d.svg())
    print(name,W,H)

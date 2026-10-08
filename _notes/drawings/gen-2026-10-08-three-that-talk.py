import re,os
_here=os.path.dirname(os.path.abspath(__file__))
defs=re.search(r'<defs>.*?</defs>',open(os.path.join(_here,'2026-10-08-pod-bay-doors.svg')).read(),re.S).group(0)
W,H=1500,900
def build(bg,ink,grey):
    o=[]; a=o.append
    def box(x,y,w,h,lines,rot,size=32,lh=38):
        cx,cy=x+w/2,y+h/2
        a(f'<g transform="rotate({rot} {cx} {cy})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{bg}" stroke="{ink}" stroke-width="3"/>')
        n=len(lines); start=cy-(n-1)*lh/2+size*0.35
        for i,t in enumerate(lines):
            col=ink; sz=size
            if isinstance(t,tuple): t,col,sz=t
            a(f'<text x="{cx}" y="{start+i*lh:.1f}" text-anchor="middle" font-size="{sz}" fill="{col}">{t}</text>')
        a('</g>')
    def arrow(d,dash=False):
        a(f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="2.5" {"stroke-dasharray=\"12 10\"" if dash else ""} marker-end="url(#ah)"/>')
    def txt(x,y,t,size=28,col=None,anchor='middle',rot=0):
        a(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{col or grey}" transform="rotate({rot} {x} {y})">{t}</text>')
    a(f'<rect width="{W}" height="{H}" fill="{bg}"/>')
    txt(750,62,'One question, one folder, three seats',46,ink)
    a(f'<g transform="rotate(0.15 730 450)"><path d="M330 150 L330 790 Q330 812 352 812 L1108 812 Q1130 812 1130 790 L1130 150 Q1130 128 1108 128 L560 128 L530 104 L352 104 Q330 104 330 126 Z" fill="none" stroke="{ink}" stroke-width="3"/></g>')
    txt(440,142,'on the compute box',26)
    box(600,150,220,70,['brief.md'],-0.6,30)
    txt(840,194,'as rough as I like',26,anchor='start')
    txt(560,264,'first takes written blind, then they talk',26)
    names=[['Claude','(chair)'],['GPT','seat 1'],['GPT','seat 2']]
    ys=[330,480,630]; logs=['mob-chair.md','mob-seat-1.md','mob-seat-2.md']; rots=[-0.7,0.5,-0.4]
    for ls,y,lg,r in zip(names,ys,logs,rots):
        box(70,y-50,200,100,ls,r,30,lh=36)
        arrow(f'M274 {y} L404 {y}')
        txt(339,y-22,'writes',24)
        box(410,y-40,270,80,[lg],-r,30)
    arrow('M690 310 Q780 405 690 460',dash=True)
    arrow('M690 500 Q780 555 690 610',dash=True)
    arrow('M690 650 Q840 480 690 290',dash=True)
    for i,(t,c) in enumerate([('every couple of minutes',ink),('each reads the other two,',None),('checks the numbers,',None),('answers by name',None),('and concedes what is right',None)]):
        txt(960,400+i*36,t,28,c)
    arrow('M545 674 L545 686')
    txt(600,684,'the chair, at about 25 minutes',24,anchor='start')
    box(410,690,620,112,[('verdict.md',ink,30),('under 350 words, actions and owners, disagreement by seat',grey,24),('ends with How we will know: a reading and a date',ink,26)],0.3,30,lh=34)
    arrow('M1034 746 L1176 746')
    box(1180,696,260,100,['you take the reading','on the day'],-0.5,28,lh=34)
    txt(1290,318,'three agreeing',28,rot=-2); txt(1290,352,'is a feeling.',28,rot=-2)
    txt(1290,400,'a number on a date',28,ink,rot=-2); txt(1290,434,'is evidence.',28,ink,rot=-2)
    txt(750,862,'If a question is murky, it goes in a folder.',28)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{defs}\n'+'\n'.join(o)+'\n</svg>'
light=build('#f0eee6','#1f1f1f','#7a7a7a')
dark=build('#1f1e1d','#e8e6e1','#a9a7a2').replace('#1f1f1f','#e8e6e1')
open(os.path.join(_here,'2026-10-08-three-that-talk.svg'),'w').write(light)
open(os.path.join(_here,'2026-10-08-three-that-talk-dark.svg'),'w').write(dark)

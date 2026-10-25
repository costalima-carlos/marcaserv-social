import numpy as np, wave, sys, json
SR=44100
def env(n,a=.005,r=.2):
    t=np.arange(n)/SR; e=np.minimum(1,t/a)*np.exp(-t/r); return e
def whoosh(d=.35):
    n=int(SR*d); x=np.random.randn(n); 
    # simple lowpass sweep via cumulative smoothing
    out=np.zeros(n); y=0
    for i in range(n):
        k=0.02+0.25*np.sin(np.pi*i/n); y+=k*(x[i]-y); out[i]=y
    return out*np.sin(np.pi*np.arange(n)/n)*0.9
def tick(f=1800,d=.08): n=int(SR*d); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*env(n,.001,.02)*.5
def chime(fs=(880,1320,1760),d=1.2):
    n=int(SR*d); t=np.arange(n)/SR; return sum(np.sin(2*np.pi*f*t)/(i+1) for i,f in enumerate(fs))*env(n,.005,.35)*.45
def ring(d=.45):
    n=int(SR*d); t=np.arange(n)/SR
    trem=(np.sign(np.sin(2*np.pi*20*t))+1)/2
    return (np.sin(2*np.pi*440*t)+np.sin(2*np.pi*480*t))*.25*trem*np.minimum(1,t/.01)*np.minimum(1,(d-t)/.05)
def build(dur, events, out):
    a=np.zeros(int(SR*(dur+1)))
    for t,s,g in events:
        i=int(t*SR); a[i:i+len(s)]+=g*s[:len(a)-i]
    a=a[:int(SR*dur)]; a=a/max(1,np.abs(a).max()/0.8)
    w=wave.open(out,'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((a*32767).astype(np.int16).tobytes()); w.close()
np.random.seed(1)
# reel1
c1=[1.9,3.3,4.7,6.1,7.5,8.9,11.6,13.15,14.7,16.25]
ev=[(c-.05,whoosh(),.8) for c in c1]+[(c+.22,tick(),.6) for c in c1]+[(10.3,whoosh(.5),1.0),(17.8,chime(),1.0)]
build(20.6,ev,'sfx_reel1.wav')
c2=[1.2,2.35,3.5,4.65,5.8,6.95]
ev=[(c,ring(),.5+.1*i) for i,c in enumerate(c2)]+[(8.3,chime((660,990,1320)),1.0),(9.3,tick(1400,.12),.8),(11.7,whoosh(.5),.9)]
build(14.3,ev,'sfx_reel2.wav')

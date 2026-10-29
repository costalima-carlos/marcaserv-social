import numpy as np, wave
SR=44100; D=19.4; n=int(SR*D); a=np.zeros(n)
bpm=92; beat=60/bpm
def env(m,att=.003,rel=.15):
    t=np.arange(m)/SR; return np.minimum(1,t/att)*np.exp(-t/rel)
def add(t0,s,g=1):
    i=int(t0*SR)
    if i>=n: return
    j=min(n,i+len(s)); a[i:j]+=g*s[:j-i]
def kick():
    m=int(.35*SR); t=np.arange(m)/SR; f=50+90*np.exp(-t*30); return np.sin(2*np.pi*np.cumsum(f)/SR)*env(m,.002,.18)
def snare():
    m=int(.25*SR); return (np.random.randn(m)*.6+np.sin(2*np.pi*190*np.arange(m)/SR)*.4)*env(m,.002,.07)
def hat():
    m=int(.06*SR); x=np.random.randn(m); x=np.diff(np.concatenate([[0],x])); return x*env(m,.001,.015)*.5
def chord(fs,dur):
    m=int(dur*SR); t=np.arange(m)/SR
    s=sum(np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t) for f in fs)/len(fs)
    return s*np.minimum(1,t/.08)*np.minimum(1,(dur-t)/.2)*.35
def whoosh(d=.4):
    m=int(SR*d); x=np.random.randn(m); y=np.zeros(m); v=0
    for i in range(m):
        k=.02+.25*np.sin(np.pi*i/m); v+=k*(x[i]-v); y[i]=v
    return y*np.sin(np.pi*np.arange(m)/m)
np.random.seed(3)
prog=[[220,261.6,329.6],[174.6,220,261.6],[196,246.9,293.7],[164.8,196,246.9]]  # Am F G Em
bar=4*beat; t=0; k=0
while t<D:
    add(t,chord(prog[k%4],bar),.9)
    add(t,np.sin(2*np.pi*prog[k%4][0]/2*np.arange(int(bar*SR))/SR)*env(int(bar*SR),.01,1.2)*.5)
    for b in range(4):
        tb=t+b*beat
        if tb<10.8 or tb>=13.0:
            add(tb,kick(),1.0 if b in (0,2) else .0)
            if b in (1,3): add(tb,snare(),.5)
            add(tb,hat(),1); add(tb+beat/2,hat(),.7)
    t+=bar; k+=1
for c in [2.8,5.4,8.0,10.8,13.0,16.4]: add(c-.15,whoosh(),.5)
fade=np.ones(n); fl=int(1.2*SR); fade[-fl:]=np.linspace(1,0,fl); a*=fade
a=a/np.abs(a).max()*.85
w=wave.open('music.wav','w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((a*32767).astype(np.int16).tobytes()); w.close()

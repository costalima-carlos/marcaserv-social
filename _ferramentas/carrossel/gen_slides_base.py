import asyncio, base64, os, json
from playwright.async_api import async_playwright

OUT = "/home/claude/carrosseis"
os.makedirs(OUT, exist_ok=True)
FD = "/home/claude/node_modules/@fontsource"

def font(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

BG = font(f"{FD}/bricolage-grotesque/files/bricolage-grotesque-latin-800-normal.woff2")
BG7 = font(f"{FD}/bricolage-grotesque/files/bricolage-grotesque-latin-600-normal.woff2")
AR = font(f"{FD}/archivo/files/archivo-latin-500-normal.woff2")
AR6 = font(f"{FD}/archivo/files/archivo-latin-600-normal.woff2")

CSS = f"""
@font-face{{font-family:'Bri';src:url(data:font/woff2;base64,{BG}) format('woff2');font-weight:800;}}
@font-face{{font-family:'Bri';src:url(data:font/woff2;base64,{BG7}) format('woff2');font-weight:600;}}
@font-face{{font-family:'Arc';src:url(data:font/woff2;base64,{AR}) format('woff2');font-weight:500;}}
@font-face{{font-family:'Arc';src:url(data:font/woff2;base64,{AR6}) format('woff2');font-weight:600;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px}}
body{{
  background:#0C1120; color:#F4F2ED; font-family:'Arc',sans-serif;
  position:relative; overflow:hidden;
}}
.glow{{
  position:absolute; width:1000px; height:1000px; border-radius:50%;
  background:radial-gradient(circle, rgba(210,169,78,.14) 0%, rgba(210,169,78,0) 68%);
  top:-320px; right:-300px; pointer-events:none;
}}
.glow2{{
  position:absolute; width:820px; height:820px; border-radius:50%;
  background:radial-gradient(circle, rgba(60,90,160,.16) 0%, rgba(60,90,160,0) 70%);
  bottom:-360px; left:-280px; pointer-events:none;
}}
.frame{{
  position:absolute; inset:34px; border:1px solid rgba(244,242,237,.10); border-radius:26px;
}}
.stage{{
  position:relative; height:100%; padding:100px 92px 92px;
  display:flex; flex-direction:column; z-index:2;
}}
.content{{flex:1; display:flex; flex-direction:column; justify-content:center; padding-bottom:40px}}
.eyebrow{{
  font-family:'Arc'; font-weight:600; font-size:19px; letter-spacing:.20em;
  text-transform:uppercase; color:#D2A94E;
}}
.rule{{width:64px;height:3px;background:#D2A94E;border-radius:2px;margin-top:26px}}
h1{{
  font-family:'Bri'; font-weight:800; font-size:88px; line-height:1.02;
  letter-spacing:-.03em; margin-top:38px; text-wrap:balance;
}}
h2{{
  font-family:'Bri'; font-weight:800; font-size:70px; line-height:1.06;
  letter-spacing:-.028em; text-wrap:balance;
}}
.sub{{
  font-size:33px; line-height:1.45; color:#A9B0C4; margin-top:30px; max-width:24ch;
}}
.big-sub{{font-size:38px; max-width:22ch}}
.num{{
  font-family:'Bri'; font-weight:800; font-size:150px; color:#D2A94E;
  line-height:.85; letter-spacing:-.05em; font-variant-numeric:tabular-nums;
}}
.stat{{
  font-family:'Bri'; font-weight:800; font-size:186px; color:#D2A94E;
  line-height:.86; letter-spacing:-.05em; font-variant-numeric:tabular-nums;
}}
.stat-label{{font-size:34px; color:#F4F2ED; margin-top:26px; font-weight:600}}
.stat-note{{font-size:29px; color:#8B93A8; margin-top:12px}}
.spacer{{flex:1}}
.hint{{
  font-family:'Arc'; font-weight:600; font-size:26px; color:#D2A94E;
  letter-spacing:.04em;
}}
.foot{{
  display:flex; align-items:center; justify-content:space-between;
  border-top:1px solid rgba(244,242,237,.12); padding-top:28px;
}}
.handle{{font-family:'Bri'; font-weight:600; font-size:27px; color:#F4F2ED; letter-spacing:-.01em}}
.handle span{{color:#D2A94E}}
.dots{{display:flex; gap:9px}}
.dot{{width:9px;height:9px;border-radius:50%;background:rgba(244,242,237,.22)}}
.dot.on{{background:#D2A94E; width:26px; border-radius:5px}}
ul.check{{list-style:none; margin-top:40px; display:flex; flex-direction:column; gap:30px}}
ul.check li{{
  font-size:33px; line-height:1.35; color:#E4E2DC; padding-left:52px; position:relative;
  max-width:29ch;
}}
ul.check li::before{{
  content:''; position:absolute; left:0; top:14px; width:24px; height:3px;
  background:#D2A94E; border-radius:2px;
}}
.kicker{{font-size:31px; color:#A9B0C4; margin-top:34px; font-weight:600}}
"""

def shell(inner, idx, total):
    dots = "".join(f'<span class="dot{" on" if i==idx else ""}"></span>' for i in range(total))
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="glow"></div><div class="glow2"></div><div class="frame"></div>
<div class="stage"><div class="content">{inner}</div>
<div class="foot"><div class="handle">@marca<span>.</span>serv</div><div class="dots">{dots}</div></div>
</div></body></html>"""

def cover(eyebrow, title, hint="deslizar &rarr;"):
    return f'<div class="eyebrow">{eyebrow}</div><div class="rule"></div><h1>{title}</h1><div class="hint" style="margin-top:58px">{hint}</div>'

def numbered(n, title, sub):
    return f'<div class="num">{n}</div><h2 style="margin-top:44px">{title}</h2><div class="sub">{sub}</div>'

def statslide(value, label, note):
    return f'<div class="stat">{value}</div><div class="stat-label">{label}</div><div class="stat-note">{note}</div>'

def statement(title, sub):
    return f'<h1 style="margin-top:0">{title}</h1><div class="sub big-sub">{sub}</div>'

def closer(title, sub, items=None):
    li = ""
    if items:
        li = '<ul class="check">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    s = f'<div class="kicker">{sub}</div>' if sub else ""
    return f'<div class="eyebrow">MarcaServ</div><div class="rule"></div><h1>{title}</h1>{s}{li}'

A = [
    cover("Para donos de barbearias e sal&otilde;es",
          "5 sinais de que a tua agenda te est&aacute; a fazer perder dinheiro"),
    numbered(1, "Respondes a marca&ccedil;&otilde;es depois das 22h",
             "O teu dia acabou &agrave;s 19h. O trabalho n&atilde;o."),
    numbered(2, "Tens horas mortas que se repetem sempre",
             "Ter&ccedil;a de manh&atilde;. Quinta a meio da tarde. Todas as semanas as mesmas."),
    numbered(3, "Sabes de cor quem costuma faltar",
             "Se est&aacute; na tua cabe&ccedil;a e n&atilde;o escrito em lado nenhum, n&atilde;o &eacute; um sistema. &Eacute; sorte."),
    numbered(4, "J&aacute; marcaste duas pessoas &agrave; mesma hora",
             "Uma vez &eacute; distra&ccedil;&atilde;o. Duas &eacute; o m&eacute;todo."),
    numbered(5, "N&atilde;o sabes quanto faturaste na semana passada",
             "Sem esse n&uacute;mero, todas as decis&otilde;es de pre&ccedil;o s&atilde;o um palpite."),
    closer("Reconheceste tr&ecirc;s ou mais?",
           "O problema n&atilde;o &eacute; o teu trabalho. &Eacute; o sistema &agrave; volta dele.", None),
]

B = [
    cover("A conta que ningu&eacute;m faz",
          "Quanto te custam mesmo as faltas sem aviso"),
    statslide("45 &euro;", "3 faltas por semana &times; 15 &euro;", "que n&atilde;o entraram"),
    statslide("180 &euro;", "&times; 4 semanas", "por m&ecirc;s"),
    statslide("2 160 &euro;", "&times; 12 meses", "por ano"),
    statement("Ningu&eacute;m te manda esta fatura.", "Por isso ningu&eacute;m a v&ecirc;."),
    closer("O que ajuda mesmo", "", [
        "A marca&ccedil;&atilde;o escrita num s&iacute;tio que n&atilde;o seja a mem&oacute;ria do cliente",
        "Uma pol&iacute;tica clara e vis&iacute;vel, igual para toda a gente",
        "Saber quem falta e quantas vezes &mdash; se n&atilde;o medes, n&atilde;o corriges",
    ]),
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for name, deck in (("A-5sinais", A), ("B-faltas", B)):
            for i, inner in enumerate(deck):
                await pg.set_content(shell(inner, i, len(deck)))
                await pg.wait_for_timeout(160)
                path = f"{OUT}/{name}-{i+1:02d}.png"
                await pg.screenshot(path=path)
                print(path)
        await b.close()

asyncio.run(main())

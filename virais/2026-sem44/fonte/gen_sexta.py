import asyncio, os, sys
sys.path.insert(0, "/home/claude/w44")
from base_lib import *  # CSS, shell
from playwright.async_api import async_playwright

OUTDIR = "/home/claude/marcaserv-social/virais/2026-sem44"

THEMES = """
body.cream{background:#F4F2ED;color:#0C1120}
body.cream .glow,body.cream .glow2{display:none}
body.cream .frame{border-color:rgba(12,17,32,.14)}
body.cream .handle{color:#0C1120} body.cream .foot{border-top-color:rgba(12,17,32,.16)}
body.cream .dot{background:rgba(12,17,32,.22)} body.cream .dot.on{background:#B48A30}
body.gold{background:#D2A94E;color:#0C1120}
body.gold .glow,body.gold .glow2{display:none}
body.gold .frame{border-color:rgba(12,17,32,.18)}
body.gold .handle,body.gold .handle span{color:#0C1120} body.gold .foot{border-top-color:rgba(12,17,32,.2)}
body.gold .dot{background:rgba(12,17,32,.25)} body.gold .dot.on{background:#0C1120}
.cv-eye{font-family:'Arc';font-weight:600;font-size:24px;letter-spacing:.2em;text-transform:uppercase}
.cv-t{font-family:'Bri';font-weight:800;font-size:128px;line-height:.98;letter-spacing:-.035em;margin-top:34px;text-wrap:balance}
.cv-t em{font-style:normal;color:#B48A30}
body.gold .cv-t em{color:#F4F2ED}
.cv-h{font-family:'Arc';font-weight:600;font-size:30px;margin-top:48px}
.big-n{font-family:'Bri';font-weight:800;font-size:220px;line-height:.85;letter-spacing:-.05em;color:#D2A94E;display:flex;align-items:flex-end;gap:30px}
.big-n span{font-family:'Noto Color Emoji';font-size:170px;letter-spacing:0;line-height:1}
.ln{font-family:'Bri';font-weight:800;font-size:72px;line-height:1.06;letter-spacing:-.025em;margin-top:56px;text-wrap:balance}
.ls{font-size:38px;line-height:1.45;color:#A9B0C4;margin-top:28px;max-width:24ch}
.vs{display:grid;gap:22px;margin-top:44px}
.vs div{border-radius:22px;padding:30px 34px;font-size:34px;line-height:1.4}
.vs .bad{background:rgba(255,90,90,.08);border:2px solid rgba(255,90,90,.45)}
.vs .good{background:rgba(210,169,78,.12);border:2px solid #D2A94E}
.vs b{display:block;font-family:'Arc';font-weight:600;font-size:22px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:10px}
.vs .bad b{color:#FF7A7A} .vs .good b{color:#D2A94E}
.price{font-family:'Bri';font-weight:800;font-size:46px;color:#D2A94E;margin-top:50px;letter-spacing:-.02em}
.price small{display:block;font-family:'Arc';font-weight:500;font-size:28px;color:#A9B0C4;margin-top:10px;letter-spacing:0}
"""

def page(inner, i, n, theme=""):
    h = shell(inner, i, n).replace("</style>", THEMES + "</style>")
    if theme:
        h = h.replace("<body>", f'<body class="{theme}">')
    return h

def step(n, emo, title, sub):
    return f'<div class="big-n">{n}<span>{emo}</span></div><div class="ln">{title}</div><div class="ls">{sub}</div>'

SEXTA = [
    ("cream", '''<div class="cv-eye" style="color:#8A6A2A">Para donos com equipa</div>
      <div class="cv-t">A 12.ª chamada chega a meio de um <em>degradê.</em></div>
      <div class="cv-h" style="color:#5A6070">Desliza &rarr;</div>'''),
    ("", step("1.ª", "🙂", "«É rápido, eu atendo.»", "Máquina pousada, cliente à espera, sorriso no telefone.")),
    ("", step("4.ª", "😑", "O cliente na cadeira já reparou.", "E está a contar quantas vezes paras.")),
    ("", step("9.ª", "😤", "O degradê já não é o mesmo.", "Tu sabes. Ele também vai saber ao espelho.")),
    ("", step("12.ª", "🤯", "E quase todas eram a mesma pergunta.", "«Tens vaga hoje?»")),
    ("", '''<h2>Há dois jeitos de responder a isto</h2>
      <div class="vs"><div class="bad"><b>Jeito errado</b>Atender tudo, a qualquer hora, com a máquina na mão.</div>
      <div class="good"><b>Jeito certo</b>O cliente abre um link, vê as horas livres de cada barbeiro e marca sozinho.</div></div>'''),
    ("", '''<div class="eyebrow">MarcaServ</div><div class="rule"></div>
      <h1 style="font-size:80px">Quem só queria saber se havia vaga já não precisa de ligar.</h1>
      <div class="price">30 €/mês, todos os profissionais<small>14 dias grátis, sem cartão · demo na bio</small></div>'''),
]

DOMINGO_CAPA = ("gold", '''<div class="cv-eye">Para donos de barbearias e salões</div>
      <div class="cv-t">O que dirias ao <em>tu</em> do dia da abertura?</div>
      <div class="cv-h">7 coisas para lhe dizer &rarr;</div>''')

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i, (th, inner) in enumerate(SEXTA):
            await pg.set_content(page(inner, i, len(SEXTA), th)); await pg.wait_for_timeout(250)
            path = f"{OUTDIR}/sem44-sex-chamadas-{i+1:02d}.png"; await pg.screenshot(path=path); print(path)
        th, inner = DOMINGO_CAPA
        await pg.set_content(page(inner, 0, 9, th)); await pg.wait_for_timeout(250)
        path = f"{OUTDIR}/sem44-dom-abertura-01b.png"; await pg.screenshot(path=path); print(path)
        await b.close()

asyncio.run(main())

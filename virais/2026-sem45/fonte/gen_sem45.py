"""Semana 45: carrosséis de quarta (Como apanhar…) e domingo (A ferramenta, o combustível, o trabalho).
Corre com: python3 gen_sem45.py  (precisa de /home/claude/node_modules/@fontsource e playwright)."""
import asyncio, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from base_lib import shell
from playwright.async_api import async_playwright

OUTDIR = os.path.dirname(HERE)
THEMES = open(os.path.join(HERE, "themes.css")).read() + """
.lbl{font-family:'Arc';font-weight:600;font-size:26px;letter-spacing:.2em;text-transform:uppercase;color:#D2A94E}
.emo{font-family:'Noto Color Emoji';font-size:150px;line-height:1;margin-top:30px}
.isca{display:flex;align-items:flex-end;gap:28px}
.isca .n{font-family:'Bri';font-weight:800;font-size:210px;line-height:.82;letter-spacing:-.05em;color:#D2A94E}
.isca .e{font-family:'Noto Color Emoji';font-size:140px;line-height:1}
.cvt{font-family:'Bri';font-weight:800;line-height:.97;letter-spacing:-.035em;margin-top:30px}
.cvt em{font-style:normal;color:#D2A94E}
body.cream .cvt em{color:#B48A30}
.q{font-family:'Bri';font-weight:800;font-size:96px;line-height:1.02;letter-spacing:-.03em;color:#D2A94E}
.trap{margin-top:36px}
"""

def page(inner, i, n, theme=""):
    h = shell(inner, i, n).replace("</style>", THEMES + "</style>")
    if theme:
        h = h.replace("<body>", f'<body class="{theme}">')
    return h

TRAP = '''<div style="position:relative;width:560px;height:250px;margin-top:30px"><svg width="560" height="250" viewBox="0 0 560 250" fill="none">
 <line x1="20" y1="232" x2="540" y2="232" stroke="#0C1120" stroke-width="5" stroke-linecap="round"/>
 <g transform="rotate(-17 70 232)">
  <rect x="70" y="92" width="300" height="140" rx="8" fill="#D2A94E" stroke="#0C1120" stroke-width="6"/>
  <line x1="70" y1="139" x2="370" y2="139" stroke="#0C1120" stroke-width="4"/>
  <line x1="70" y1="186" x2="370" y2="186" stroke="#0C1120" stroke-width="4"/>
 </g>
 <line x1="372" y1="114" x2="356" y2="232" stroke="#0C1120" stroke-width="7" stroke-linecap="round"/>
 <path d="M362 190 C 420 230, 470 150, 545 205" stroke="#0C1120" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>
 </svg>
 <span style="position:absolute;left:150px;top:170px;font-family:'Noto Color Emoji';font-size:52px">🥪</span>
 <span style="position:absolute;left:214px;top:170px;font-family:'Noto Color Emoji';font-size:52px">🪑</span>
 <span style="position:absolute;left:278px;top:170px;font-family:'Noto Color Emoji';font-size:52px">💶</span></div>'''

def isca(n, emo, title, sub):
    return (f'<div class="lbl">Isca n.º {n}</div><div class="isca" style="margin-top:30px"><div class="n">{n}</div><div class="e">{emo}</div></div>'
            f'<div class="ln">{title}</div><div class="ls">{sub}</div>')

def peca(emo, label, title, sub):
    return (f'<div class="lbl">{label}</div><div class="emo">{emo}</div>'
            f'<div class="ln" style="margin-top:44px">{title}</div><div class="ls">{sub}</div>')

PRICE = '<div class="price">30 €/mês, todos os profissionais<small>14 dias grátis, sem cartão · demo na bio</small></div>'

QUARTA = [
    ("cream", f'''<div class="cv-eye" style="color:#8A6A2A">Para donos com equipa</div>
      <div class="cvt" style="font-size:130px">Como apanhar um dono de <em>barbearia</em> com equipa</div>
      {TRAP}
      <div class="cv-h" style="color:#5A6070;margin-top:26px">3 iscas que nunca falham &rarr;</div>'''),
    ("", isca(1, "🥪", "Almoçar sem responder a quatro «tens vaga?»", "A sandes numa mão, o telemóvel na outra.")),
    ("", isca(2, "🪑", "Um sábado de manhã sem dois clientes à mesma hora.", "Nem aquela conversa à porta: «mas eu tinha marcado…»")),
    ("", isca(3, "💶", "Saber quanto entrou esta semana sem abrir o caderno.", "E qual é o dia mais fraco, antes de ser surpresa.")),
    ("", '''<div class="lbl">Talvez estejas a pensar</div>
      <div class="q" style="margin-top:40px">«Isso é para salões grandes.»</div>
      <div class="ls" style="max-width:26ch;margin-top:44px">Se tens 3, 4 ou 6 pessoas a marcar clientes, já tens agendas que cheguem para te perderes.</div>'''),
    ("", '''<div class="lbl">A armadilha?</div>
      <h1 style="font-size:92px;margin-top:34px">Uma página com a marca da tua barbearia.</h1>
      <div class="ls" style="max-width:27ch">O cliente escolhe o serviço e o barbeiro, só vê horas mesmo livres e marca sozinho. Tu recebes um email a cada reserva.</div>'''),
    ("", f'''<div class="eyebrow">MarcaServ</div><div class="rule"></div>
      <h1 style="font-size:80px">Um dono com equipa não se apanha com promessas. <span style="color:#D2A94E">Apanha&#8209;se com tempo de volta.</span></h1>
      {PRICE}'''),
]

DOMINGO = [
    ("", '''<div class="cv-eye" style="color:#D2A94E">Para donos de barbearias e salões</div>
      <div class="cvt" style="font-size:128px;line-height:1.04">A ferramenta.<br>O combustível.<br>O trabalho.<br><em>E o resto.</em></div>
      <div class="cv-h" style="color:#A9B0C4;font-size:36px;margin-top:56px">A parte que ninguém publica &rarr;</div>'''),
    ("", peca("✂️", "A ferramenta", "Máquina, tesoura, navalha.", "Afiadas, oleadas, cada uma no seu lugar.")),
    ("", peca("☕", "O combustível", "O café das 8h50, antes de abrir a porta.", "O segundo às 11h. O terceiro já ninguém conta.")),
    ("", peca("💈", "O trabalho", "Quatro cadeiras ocupadas ao mesmo tempo.", "É isto que vai para o Instagram.")),
    ("", peca("📒", "A parte que ninguém publica", "O caderno das marcações. O WhatsApp às 22h.", "E o «tens vaga?» de hora a hora.")),
    ("", '''<h2>Mas essa parte também pode ter uma ferramenta.</h2>
      <div class="vs"><div class="bad"><b>Jeito antigo</b>Tu és a agenda: atendes, apontas, confirmas.</div>
      <div class="good"><b>Jeito novo</b>Uma página onde o cliente escolhe o profissional e só vê as horas livres. Pausas e folgas de cada um incluídas.</div></div>'''),
    ("", f'''<div class="eyebrow">MarcaServ</div><div class="rule"></div>
      <h1 style="font-size:76px">A tesoura corta. O café aguenta. O trabalho fala por ti. <span style="color:#D2A94E">A agenda não devia depender de ti.</span></h1>
      {PRICE}'''),
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for name, slides in (("sem45-qua-apanhar", QUARTA), ("sem45-dom-ferramenta", DOMINGO)):
            for i, (th, inner) in enumerate(slides):
                await pg.set_content(page(inner, i, len(slides), th)); await pg.wait_for_timeout(300)
                path = f"{OUTDIR}/{name}-{i+1:02d}.png"; await pg.screenshot(path=path); print(path)
        await b.close()

asyncio.run(main())

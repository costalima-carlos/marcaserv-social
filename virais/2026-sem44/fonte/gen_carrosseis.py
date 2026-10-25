import asyncio, os, sys
sys.path.insert(0, "/home/claude/w44")
from base_lib import *  # CSS, shell, cover, numbered, statement, closer
from playwright.async_api import async_playwright

OUTDIR = "/home/claude/marcaserv-social/virais/2026-sem44"
os.makedirs(OUTDIR, exist_ok=True)

EXTRA = """
.warn{display:flex;flex-direction:column;align-items:center;text-align:center;justify-content:center;height:100%}
.blurbg{position:absolute;inset:0;z-index:1;filter:blur(26px);opacity:.55;padding:140px 110px}
.blurbg div{height:70px;border-radius:14px;margin:26px 0;background:linear-gradient(90deg,#3a2a2a,#6b4a2a,#2a3a5a)}
.veil{position:absolute;inset:0;z-index:1;background:rgba(12,17,32,.55)}
.eye{width:150px;height:150px;border:4px solid #F4F2ED;border-radius:50%;display:flex;align-items:center;justify-content:center}
.wt{font-family:'Bri';font-weight:800;font-size:64px;letter-spacing:-.02em;margin-top:44px}
.wd{font-size:34px;line-height:1.45;color:#C9CDD8;margin-top:24px;max-width:22ch}
.wbtn{margin-top:70px;border-top:1px solid rgba(244,242,237,.25);padding-top:36px;width:640px;font-family:'Arc';font-weight:600;font-size:34px;color:#D2A94E}
.tag{align-self:flex-start;display:inline-block;font-family:'Arc';font-weight:600;font-size:22px;letter-spacing:.18em;text-transform:uppercase;color:#FF6B5B;border:2px solid rgba(255,107,91,.6);border-radius:40px;padding:10px 22px}
.paper{background:#EFE8D8;color:#2A2622;border-radius:18px;padding:30px 34px;margin-top:34px;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(0,0,0,.4);font-family:'Arc';font-size:30px}
.paper .row{display:flex;gap:22px;border-bottom:2px solid rgba(42,38,34,.15);padding:13px 0;align-items:center}
.paper .h{width:96px;font-weight:600;color:#7A6F60}
.paper .x{text-decoration:line-through;color:#9A3A2A}
.paper .clash{background:rgba(255,75,75,.22);border-radius:8px;padding:2px 8px}
.notif{display:flex;gap:20px;align-items:center;background:rgba(244,242,237,.08);border:1px solid rgba(244,242,237,.12);border-radius:24px;padding:22px 26px;margin-top:16px;font-size:28px}
.notif .ic{width:58px;height:58px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:32px;flex:none}
.notif b{font-weight:600;color:#F4F2ED}
.notif small{display:block;color:#A9B0C4;font-size:24px;margin-top:2px}
.cal{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:34px}
.cal .col{background:rgba(244,242,237,.05);border-radius:16px;padding:16px 14px;min-height:330px}
.cal .nm{font-family:'Bri';font-weight:600;font-size:26px;margin-bottom:12px}
.cal .ev{border-radius:10px;padding:10px 12px;font-size:22px;margin-top:10px;color:#0C1120;font-weight:600}
.cal .off{border:2px dashed rgba(244,242,237,.3);color:#A9B0C4;background:none;text-align:center;padding:60px 0;font-size:24px}
.ok li::before{content:'✓' !important;background:none !important;color:#D2A94E;font-family:'Bri';font-weight:800;font-size:34px;top:-4px !important;width:auto !important;height:auto !important}
.price{font-family:'Bri';font-weight:800;font-size:46px;color:#D2A94E;margin-top:44px;letter-spacing:-.02em}
.price small{display:block;font-family:'Arc';font-weight:500;font-size:28px;color:#A9B0C4;margin-top:10px;letter-spacing:0}
.lnum{font-family:'Bri';font-weight:800;font-size:30px;color:#0C1120;background:#D2A94E;border-radius:50%;width:66px;height:66px;display:flex;align-items:center;justify-content:center}
.quote{font-family:'Bri';font-weight:800;font-size:92px;line-height:1.05;letter-spacing:-.03em;margin-top:40px;text-wrap:balance}
.qsub{font-size:39px;line-height:1.45;color:#A9B0C4;margin-top:36px;max-width:24ch}
.envelope{font-size:26px;color:#A9B0C4;letter-spacing:.06em;margin-top:18px}
"""

def sh(inner, i, n, extra_bg=""):
    h = shell(inner, i, n)
    h = h.replace("</style>", EXTRA + "</style>")
    if extra_bg:
        h = h.replace('<div class="frame"></div>', '<div class="frame"></div>' + extra_bg)
    return h

# ---------- Carrossel A — Quarta 28/10: "Aviso de conteúdo sensível" (Halloween) ----------
EYE = '''<div class="eye"><svg width="86" height="86" viewBox="0 0 24 24" fill="none" stroke="#F4F2ED" stroke-width="1.6" stroke-linecap="round"><path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path d="M3.5 3.5l17 17"/></svg></div>'''
BLUR = '<div class="blurbg">' + "".join("<div></div>" for _ in range(11)) + '</div><div class="veil"></div>'

A = [
    (f'''<div class="warn">{EYE}
      <div class="wt">Conteúdo sensível</div>
      <div class="wd">Este post contém imagens perturbadoras para donos de barbearias e salões.</div>
      <div class="wbtn">Ver post &rarr;</div></div>''', BLUR),
    ('''<div class="warn"><div style="font-size:150px;line-height:1">😰</div>
      <div class="wt" style="font-size:88px">Tens a certeza?</div>
      <div class="wd">A partir daqui não há volta a dar. Desliza só se aguentares.</div>
      <div class="wbtn">Sim, mostra &rarr;</div></div>''', ""),
    ('''<span class="tag">🎃 Imagem 1</span>
      <h2 style="margin-top:30px">A agenda de papel numa sexta à tarde</h2>
      <div class="paper">
        <div class="row"><span class="h">15:00</span><span class="x">Sr. Alves</span> &nbsp;Paulo?</div>
        <div class="row"><span class="h">15:30</span><span class="clash">Nuno &mdash; Rui</span></div>
        <div class="row"><span class="h">15:30</span><span class="clash">Hugo &mdash; Rui (??)</span></div>
        <div class="row"><span class="h">16:00</span>ligar ao das 11h</div>
        <div class="row"><span class="h">16:30</span><span class="x">Marta</span> &rarr; sáb?</div>
      </div>''', ""),
    ('''<span class="tag">🎃 Imagem 2</span>
      <h2 style="margin-top:30px">O telemóvel a meio de um corte</h2>
      <div class="notif"><div class="ic" style="background:#2E7D4F">📞</div><div><b>9 chamadas perdidas</b><small>desde as 10:12</small></div></div>
      <div class="notif"><div class="ic" style="background:#8A3FB8">💬</div><div><b>&ldquo;tens vaga hoje?&rdquo;</b><small>+3 mensagens por responder</small></div></div>
      <div class="notif"><div class="ic" style="background:#2E7D4F">💬</div><div><b>&ldquo;posso passar p/ as 6?&rdquo;</b><small>ontem, 22:41</small></div></div>''', ""),
    ('''<span class="tag">🎃 Imagem 3</span>
      <h2 style="margin-top:30px">O cliente chegou. O barbeiro dele está de folga.</h2>
      <div class="sub" style="max-width:26ch">Ninguém escreveu a folga em lado nenhum. Estava só na cabeça de quem a pediu.</div>''', ""),
    ('''<div class="eyebrow">MarcaServ</div><div class="rule"></div>
      <h1 style="font-size:80px">Assustadoramente simples 👻</h1>
      <ul class="check ok">
        <li>O cliente marca na página com a tua marca, sem conta</li>
        <li>Só vê as horas realmente livres de cada profissional</li>
        <li>Folgas e pausas de cada um ficam no calendário</li>
      </ul>
      <div class="price">30 €/mês, todos os profissionais<small>14 dias grátis, sem cartão · link na bio</small></div>''', ""),
]

# ---------- Carrossel B — Domingo 01/11: "O que dirias ao tu do dia da abertura" ----------
def letter(n, title, sub):
    return f'''<div class="lnum">{n}</div><div class="quote">{title}</div><div class="qsub">{sub}</div>'''

B = [
    cover("Para donos de barbearias e salões",
          "O que dirias ao <span style='color:#D2A94E'>tu</span> do dia da abertura?",
          "7 coisas para lhe dizer &rarr;"),
    letter(1, "O telefone não é um sistema de marcações.", "É uma interrupção a meio de um corte."),
    letter(2, "A folga do Rui não pode viver só na cabeça do Rui.", "Se não está no calendário, alguém vai marcar para esse dia."),
    letter(3, "Escreve a pausa de almoço na agenda.", "Senão, ela não existe. Pergunta a quem almoça às 16h."),
    letter(4, "Põe o preço e a duração de cada serviço à vista.", "Poupas a mesma pergunta cem vezes por mês."),
    letter(5, "Nem todos os clientes querem ligar.", "Dá-lhes outra porta: um link onde vêem as horas livres e marcam."),
    letter(6, "Conta a faturação por semana.", "&ldquo;Está a correr bem&rdquo; não é um número."),
    letter(7, "Não esperes ter tempo para te organizares.", "Esse tempo não vem. Começa com uma coisa só."),
    '''<div class="eyebrow">MarcaServ</div><div class="rule"></div>
      <h1>Qual destes dirias primeiro?</h1>
      <div class="qsub">Comenta o número. Se foi o 5, essa porta existe: uma página onde os teus clientes marcam sozinhos.</div>
      <div class="price">30 €/mês, todos os profissionais<small>14 dias grátis, sem cartão · link na bio</small></div>''',
]

async def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "AB"
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        decks = []
        if "A" in which: decks.append(("sem44-qua-aviso", A))
        if "B" in which: decks.append(("sem44-dom-abertura", B))
        for name, deck in decks:
            for i, item in enumerate(deck):
                inner, bg = item if isinstance(item, tuple) else (item, "")
                await pg.set_content(sh(inner, i, len(deck), bg))
                await pg.wait_for_timeout(250)
                path = f"{OUTDIR}/{name}-{i+1:02d}.png"
                await pg.screenshot(path=path)
                print(path)
        await b.close()

asyncio.run(main())

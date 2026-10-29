import asyncio, os, sys
src = open("/home/claude/w44/gen_sexta.py").read().replace("asyncio.run(main())", "")
exec(src)  # THEMES, page(), step(), shell, CSS
from playwright.async_api import async_playwright

OUT = "/home/claude/w44/teste"
os.makedirs(OUT, exist_ok=True)

MORE = """
.cal{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:44px}
.cal .col{background:rgba(244,242,237,.05);border-radius:16px;padding:16px 12px 12px}
.cal .nm{font-family:'Bri';font-weight:600;font-size:26px;margin-bottom:6px;text-align:center}
.cal .ev{border-radius:10px;height:54px;margin-top:10px}
.cal .free{border:2px dashed rgba(244,242,237,.28);height:54px;border-radius:10px;margin-top:10px}
.phones{font-family:'Noto Color Emoji';font-size:120px;letter-spacing:10px;line-height:1}
.emo1{font-family:'Noto Color Emoji';font-size:170px;line-height:1}
.turn{font-family:'Bri';font-weight:800;font-size:112px;line-height:1;letter-spacing:-.035em;text-wrap:balance}
.turn em{font-style:normal;color:#D2A94E}
"""

def cal():
    cols = [("Rui", "#D2A94E", [1,1,1,1]), ("Tiago", "#6C8CE0", [1,0,0,1]), ("Marco", "#5FB58A", [1,1,0,1]), ("Nuno", "#C77DD6", [0,1,1,0])]
    h = '<div class="cal">'
    for nm, c, slots in cols:
        h += f'<div class="col"><div class="nm">{nm}</div>' + "".join(
            f'<div class="ev" style="background:{c}"></div>' if s else '<div class="free"></div>' for s in slots) + '</div>'
    return h + '</div>'

S = [
    ("gold", '''<div class="cv-eye">Para donos com equipa</div>
      <div class="cv-t">4 barbeiros. 4 agendas. <em>Nenhuma é tua.</em></div>
      <div class="cv-h">Desliza &rarr;</div>'''),
    ("", '''<div class="phones">📱📱📱📱</div><div class="ln">Cada um marca no seu WhatsApp.</div>
      <div class="ls">É mais rápido. Até deixar de ser.</div>'''),
    ("", '''<div class="emo1">🗓️</div><div class="ln">O Rui está cheio até dia 15. O Tiago tem a quinta à tarde vazia.</div>
      <div class="ls">E tu só descobres na quinta.</div>'''),
    ("", '''<div class="emo1">🚪</div><div class="ln">Um dia, alguém sai.</div>
      <div class="ls">E as marcações dele saem no telemóvel dele.</div>'''),
    ("", '''<div class="turn">Mas o problema não é a tua equipa.</div>
      <div class="ls" style="margin-top:44px">São 4 agendas onde devia haver <b style="color:#F4F2ED">uma</b>.</div>'''),
    ("", f'''<h2>Uma página. Uma coluna por barbeiro.</h2>{cal()}
      <div class="ls">O cliente escolhe o barbeiro, ou o primeiro que estiver livre.</div>'''),
    ("", '''<div class="vs"><div class="bad"><b>Antes</b>Tardes vazias que só tu vês tarde demais.</div>
      <div class="good"><b>Depois</b>As horas livres de cada barbeiro aparecem a quem procura vaga. E o histórico de cada cliente fica na barbearia.</div></div>'''),
    ("", '''<div class="eyebrow">MarcaServ</div><div class="rule"></div>
      <h1 style="font-size:96px">4 barbeiros. 1&nbsp;agenda. <span style="color:#D2A94E">E é tua.</span></h1>
      <div class="price">30 €/mês, todos os profissionais<small>14 dias grátis, sem cartão · demo na bio</small></div>'''),
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i, (th, inner) in enumerate(S):
            html = page(inner, i, len(S), th).replace("</style>", MORE + "</style>")
            await pg.set_content(html); await pg.wait_for_timeout(250)
            await pg.screenshot(path=f"{OUT}/teste-agendas-{i+1:02d}.png")
        await b.close()

asyncio.run(main())

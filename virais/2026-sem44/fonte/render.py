import asyncio, sys, os
from playwright.async_api import async_playwright
html, mode = sys.argv[1], sys.argv[2]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto(f"file:///home/claude/w44/{html}"); await pg.wait_for_timeout(900)
        name=html.split('.')[0]
        if mode=="info":
            print(await pg.evaluate("JSON.stringify({d:DUR,c:CUTS})"))
        elif mode=="stills":
            d=f"stills_{name}"; os.makedirs(d,exist_ok=True)
            for t in [float(x) for x in sys.argv[3].split(',')]:
                await pg.evaluate(f"render({t})"); await pg.screenshot(path=f"{d}/{t:05.2f}.png")
        else:
            d=f"frames_{name}"; os.makedirs(d,exist_ok=True)
            dur=await pg.evaluate("DUR"); fps=30
            for i in range(int(fps*dur)):
                await pg.evaluate(f"render({i/fps})"); await pg.screenshot(path=f"{d}/{i:04d}.png")
        await b.close()
asyncio.run(main())

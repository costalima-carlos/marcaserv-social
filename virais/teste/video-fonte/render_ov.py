import asyncio, sys, os
from playwright.async_api import async_playwright
mode=sys.argv[1]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto("file:///home/claude/w44/video1/overlay.html"); await pg.wait_for_timeout(900)
        if mode=="stills":
            os.makedirs("ostills",exist_ok=True)
            for t in [float(x) for x in sys.argv[2].split(",")]:
                await pg.evaluate(f"render({t})"); await pg.screenshot(path=f"ostills/{t:05.2f}.png",omit_background=True)
        else:
            os.makedirs("ov",exist_ok=True); n=int(await pg.evaluate("DUR")*30)
            for i in range(n):
                await pg.evaluate(f"render({i/30})"); await pg.screenshot(path=f"ov/{i:04d}.png",omit_background=True)
        await b.close()
asyncio.run(main())

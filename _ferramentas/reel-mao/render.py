import asyncio, sys, os
from playwright.async_api import async_playwright
mode=sys.argv[1]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto("file:///home/claude/reel2/anim.html"); await pg.wait_for_timeout(800)
        if mode=="stills":
            os.makedirs("stills",exist_ok=True)
            for t in [1.8,3.5,5.25,7.45,8.6,9.8,12.5]:
                await pg.evaluate(f"render({t})"); await pg.screenshot(path=f"stills/{t:05.1f}.png")
        else:
            os.makedirs("frames",exist_ok=True)
            fps=30; dur=14.5
            for i in range(int(fps*dur)):
                await pg.evaluate(f"render({i/fps})"); await pg.screenshot(path=f"frames/{i:04d}.png")
        await b.close()
asyncio.run(main())

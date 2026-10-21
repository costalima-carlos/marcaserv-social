# Ferramentas @marca.serv

Tudo corre a partir de /home/claude com `npm i @fontsource/bricolage-grotesque @fontsource/archivo` (os HTML apontam para ../node_modules).

- `carrossel/gen_slides_base.py` — gerador base de carrosséis 1080×1350 (funções cover, numbered, statslide, statement, closer). `gen_v1_exemplo.py` = exemplo com caixa comparativa (.vs).
- `reel-chat/` — reel 1080×1920 animado: título "X vs Y", telemóvel com perfil/DMs, carimbo VENDA PERDIDA!, sinal A SOLUÇÃO, percurso de marcação, cartão final. `anim.html` expõe `render(t)`; `render.py stills|frames` gera PNG; depois ffmpeg 30 fps + sfx gerados em numpy.
- `reel-mao/` — reel com mão a segurar o telemóvel e polegar a tocar (alvos por id, getBoundingClientRect), cena noturna.

Encode: `ffmpeg -framerate 30 -i frames/%04d.png -i sfx.wav -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 160k -movflags +faststart -shortest out.mp4`

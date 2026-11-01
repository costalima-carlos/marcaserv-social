# Virais semana 45 (02–08/11/2026)

| Data (Lisboa) | Tipo | Título | Ficheiros | Capa |
|---|---|---|---|---|
| Seg 02/11 19:00 | Vídeo (reel) | 4 barbeiros. 4 agendas. Nenhuma é tua. | `../teste/teste-video-agendas.mp4` + `../teste/teste-video-agendas-capa.jpg` | dourada |
| Qua 04/11 12:30 | Carrossel (7) | Como apanhar um dono de barbearia com equipa | `sem45-qua-apanhar-01..07.png` | creme |
| Sex 06/11 19:00 | Vídeo (reel, 18,8 s) | Um barbeiro doente. 6 clientes. 6 chamadas. | `sem45-sex-barbeiro-doente.mp4` + `sem45-sex-barbeiro-doente-capa.jpg` | dourada |
| Dom 08/11 11:00 | Carrossel (7) | A ferramenta. O combustível. O trabalho. E o resto. | `sem45-dom-ferramenta-01..07.png` | escura |

Grelha: `grelha.png`.

## Origem dos formatos
- Quarta: trend "How to catch me" (SocialBee, secção de 21/10/2026; exemplo @obsessed.thebrand, post de imagem). Sem números publicados.
- Sexta: formato da casa "Jeito errado × jeito certo" (formato 13 "Comparação" do método).
- Domingo: trend "The tool, the fuel, the work" (SocialBee, secção de 29/10/2026; exemplo @getnailedkelowna, reel), passada a carrossel. Sem números publicados.

## Clips do Mixkit (vídeo de sexta) — todos com "Stock Video Free License", verificado a 01/11/2026
| Cena | id | Título | Link |
|---|---|---|---|
| 1 gancho | 363 | Barber pole | https://mixkit.co/free-stock-video/barber-pole-363/ |
| 2 "Ligas ao primeiro" | 144 | Hands shown texting on a smartphone | https://mixkit.co/free-stock-video/hands-shown-texting-on-a-smartphone-144/ |
| 3 "Riscas no papel" | 39855 | Hand of a man writing on a sheet | https://mixkit.co/free-stock-video/hand-of-a-man-writing-on-a-sheet-on-a-39855/ |
| 4 "11h" | 28893 | Black analog clock in a very close shot | https://mixkit.co/free-stock-video/black-analog-clock-in-a-very-close-shot-28893/ |
| 5 virada (por baixo do cartão) e 7 fim | 28897 | Slowly approaching a clock on a black background | https://mixkit.co/free-stock-video/slowly-approaching-a-clock-on-a-black-background-28897/ |
| 6 jeito certo | 40127 | Barber outlining a man's hair with a machine (nuca) | https://mixkit.co/free-stock-video/barber-outlining-a-mans-hair-with-a-machine-40127/ |

Rejeitados: 43239 (logótipo e texto "UV towel warmer" legíveis), 43244 (caras), 2847 ("MONEY" legível), 41165 (ecrã de WhatsApp e cara parcial), 42629 (ecrã de calendário que podia passar por captura), 38501, 34197, 46768, 34091 (Mixkit Restricted License), 100880 (sem link de download).

## Fontes
- `fonte/gen_sem45.py` (carrosséis; usa `base_lib.py` e `themes.css`)
- `fonte/video-sex/` (build_base.sh → render_ov.py frames → ffmpeg overlay + music.wav de music.py; capa em cover.html)

# Otimiza fotos do acervo de marketing pro site (GitHub Pages).
# Fonte (insumo, fora do repo): marketing/fotos/ da Sabor. Saida: site-novo/img/.
# Rodar: python tools/otimiza-fotos.py  (de dentro de site-novo/)
from PIL import Image
import os

SRC = "d:/2025/Miguexis/Claude code/Sabor ditalia/marketing/fotos"
MARCA = "d:/2025/Miguexis/Claude code/Sabor ditalia/marca"
DST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img")
os.makedirs(DST, exist_ok=True)

TRATADAS = "d:/2025/Pizzaria/Marketing/Fotos/Menores e tratatadas para Cardapio digital"
ENSAIO_OUT23 = "E:/miguex/Pizzaria/Markting/PIzzaria Sabor D'italia 2023/Sabor Ditalia Outubro 2023/Sabor Ditalia 2023 Final"
BATATAS = "d:/2025/Miguexis/Claude code/Sabor ditalia/batatas/fotos"

jobs = [
    (SRC, "cinco-queijos.jpg",                    "hero-cinco-queijos.jpg",      1600),
    (SRC, "frango catupiry fatia levantada.jpeg", "delivery-frango-catupiry.jpg", 1200),
    (SRC, "calabresa-especial.jpg",               "card-calabresa-especial.jpg",   900),
    (SRC, "mignon-mostarda-mel-1.jpg",            "card-mignon-mostarda-mel.jpg",  900),
    (TRATADAS, "marguerita.png",                  "card-marguerita.jpg",           900),
    (TRATADAS, "Frango catupiry.png",             "card-frango-catupiry.jpg",      900),
    (TRATADAS, "Morangotella.png",                "card-morangotella.jpg",         900),
    (TRATADAS, "Calzone.png",                     "card-calzone.jpg",              900),
    (ENSAIO_OUT23 + "/Sticks", "Sabor Ditalia 2023 Ebraim Martini-421.jpg", "card-stick.jpg", 900),
    (BATATAS, "batata calabresa - aberta.jpeg",   "card-batata-calabresa.jpg",     900),
]

for base, src, dst, w in jobs:
    p = os.path.join(base, src)
    im = Image.open(p).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    out = os.path.join(DST, dst)
    tmp = out + ".tmp"
    im.save(tmp, "JPEG", quality=82, optimize=True, progressive=True)
    os.replace(tmp, out)
    print(dst, im.size, str(round(os.path.getsize(out) / 1024)) + " KB")

# logo (PNG transparente, reduzida)
im = Image.open(os.path.join(MARCA, "logo.png"))
if im.width > 640:
    im = im.resize((640, round(im.height * 640 / im.width)), Image.LANCZOS)
out = os.path.join(DST, "logo.png")
tmp = out + ".tmp"
im.save(tmp, "PNG", optimize=True)
os.replace(tmp, out)
print("logo.png", im.size, str(round(os.path.getsize(out) / 1024)) + " KB")

# lasanha: o ensaio set/2025 so tem CR3 (RAW) — converter via rawpy (foto escolhida pelo Luiz, 01/09)
try:
    import rawpy
    CR3 = "d:/2025/Pizzaria/Marketing/Fotos/Sabor D'Italia Setembro 2025/Lasanhas, 1 sugo 1 branca 1 bolonhesa 1 strogonoff/Sabor D'Italia Setembro 2025-433.CR3"
    with rawpy.imread(CR3) as raw:
        rgb = raw.postprocess(use_camera_wb=True, output_bps=8)
    im = Image.fromarray(rgb)
    if im.width > 900:
        im = im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS)
    out = os.path.join(DST, "card-lasanha.jpg")
    tmp = out + ".tmp"
    im.save(tmp, "JPEG", quality=82, optimize=True, progressive=True)
    os.replace(tmp, out)
    print("card-lasanha.jpg", im.size, str(round(os.path.getsize(out) / 1024)) + " KB")
except Exception as e:
    print("LASANHA CR3 FALHOU (segue placeholder):", e)

# avatar redondo (anel verde, feito pra renderizacao pequena) — header do site
im = Image.open(os.path.join(MARCA, "sabor ditalia pizzaria - avatar - com fundo.png"))
if im.width > 240:
    im = im.resize((240, round(im.height * 240 / im.width)), Image.LANCZOS)
out = os.path.join(DST, "avatar.png")
tmp = out + ".tmp"
im.save(tmp, "PNG", optimize=True)
os.replace(tmp, out)
print("avatar.png", im.size, str(round(os.path.getsize(out) / 1024)) + " KB")

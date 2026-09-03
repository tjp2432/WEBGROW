"""Baja catalogo fumador de CandyClub (Store API + unidades del HTML)."""
import html
import io
import json
import re
import urllib.request

BASE = 'https://candyclub.com.ar'

# Candy cat id -> nuestra categoria slug
CATMAP = {
    142: 'papeles',        # PAPELES PARA ARMAR
    213: 'papeles',        # CELULOSA
    211: 'papeles',        # TUBOS Y CONOS
    141: 'filtros',        # FILTROS Y TIPS
    136: 'bongs',          # BONGS
    144: 'pipas',          # PIPAS
    138: 'encendedores',   # ENCENDEDORES
    215: 'blunts',         # BLUNTS
    133: 'accesorios',     # ARMADORES
    135: 'accesorios',     # BANDEJAS
    137: 'accesorios',     # CENICEROS
    186: 'accesorios',     # PARA PIPA
}

NEW_CATS = {
    'filtros': ('Filtros', 'Filtros y tips de todos los materiales.'),
    'encendedores': ('Encendedores', 'Encendedores Clipper, Magiclick y más.'),
    'blunts': ('Blunts', 'Blunts y wraps de todos los sabores.'),
}


def get_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf-8', 'replace')


def api_products(cat_id):
    out = []
    page = 1
    while True:
        url = f'{BASE}/wp-json/wc/store/v1/products?per_page=100&page={page}&category={cat_id}'
        try:
            batch = get_json(url)
        except Exception as e:
            print(' API error cat', cat_id, 'page', page, e)
            break
        if not batch:
            break
        out += batch
        print(f' cat {cat_id} page {page}: {len(batch)}')
        if len(batch) < 100:
            break
        page += 1
    return out


def cat_slug(cat_id):
    data = get_json(f'{BASE}/wp-json/wc/store/v1/products/categories/{cat_id}')
    return data['slug']


def units_from_archives(slug):
    """slug producto -> unidades por display (del HTML de la categoria)."""
    units = {}
    page = 1
    while True:
        url = f'{BASE}/product-category/{slug}/' + (f'page/{page}/' if page > 1 else '')
        try:
            h = get_html(url)
        except Exception as e:
            print(' HTML error', slug, page, e)
            break
        found = 0
        for m in re.finditer(
            r'href="https://candyclub\.com\.ar/product/([^"/]+)/?"(.*?)(?:(\d+)\s+unidades?\s+por\s+Display|AGOTADO)',
            h, re.S | re.I,
        ):
            pslug = m.group(1)
            if m.group(3):
                units[pslug] = int(m.group(3))
                found += 1
        print(f' HTML {slug} page {page}: {found} con unidades')
        if '>Siguiente<' not in h and 'next page-numbers' not in h:
            break
        page += 1
        if page > 40:
            break
    return units


def main():
    seen = {}
    for cat_id in CATMAP:
        for p in api_products(cat_id):
            seen.setdefault(p['id'], (p, cat_id))
    print('unicos:', len(seen))

    units = {}
    done_slugs = set()
    for cat_id in CATMAP:
        try:
            slug = cat_slug(cat_id)
        except Exception as e:
            print(' slug error', cat_id, e)
            continue
        if slug in done_slugs:
            continue
        done_slugs.add(slug)
        units.update(units_from_archives(slug))
    print('con unidades:', len(units))

    items = []
    for pid, (p, cat_id) in seen.items():
        try:
            cost = float(p['prices']['price']) / 100.0
        except Exception:
            continue
        slug = p.get('slug') or str(pid)
        u = units.get(slug)
        imgs = [i.get('src') for i in p.get('images', []) if i.get('src')]
        # descripcion: primer parrafo propio (sin boilerplate)
        text = re.sub(r'<[^>]+>', ' ', p.get('description') or '')
        text = html.unescape(re.sub(r'\s+', ' ', text)).strip()
        boiler = 'Somos Distribuidora'
        if boiler in text:
            text = text.split(boiler)[0].strip()
        items.append({
            'candy_id': pid,
            'name': html.unescape(p['name']).strip(),
            'slug': slug,
            'cost': round(cost, 2),
            'units': u,
            'brand': (p.get('brands') or [{}])[0].get('name', ''),
            'image': imgs[0] if imgs else '',
            'desc': text[:600],
            'stock': bool(p.get('is_in_stock')),
            'cat': CATMAP[cat_id],
        })

    with io.open('candy_products.json', 'w', encoding='utf-8') as f:
        json.dump({'categories': NEW_CATS, 'items': items}, f, ensure_ascii=False)
    print('items:', len(items))


if __name__ == '__main__':
    main()

"""Descarga imagenes y carga productos CandyClub a la DB."""
import io
import json
import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

HERE = os.path.abspath(os.path.dirname(__file__))
IMGDIR = os.path.join(HERE, 'static', 'images', 'candy')
os.makedirs(IMGDIR, exist_ok=True)

with io.open('candy_products.json', encoding='utf-8') as f:
    DATA = json.load(f)


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return re.sub(r'-+', '-', text)[:150].strip('-')


def fetch_img(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return True
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
        im = Image.open(io.BytesIO(raw)).convert('RGB')
        im.thumbnail((700, 700))
        im.save(dest, 'JPEG', quality=65)
        return True
    except Exception as e:
        print(' IMG FAIL', url, e)
        return False


def main():
    from app import app
    from models import db, Category, Product

    jobs = []
    for it in DATA['items']:
        slug = (slugify(it['slug']) or f"candy-{it['candy_id']}")[:150]
        dest = os.path.join(IMGDIR, slug + '.jpg')
        jobs.append((it, slug, dest))

    print('bajando imagenes:', len(jobs))
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(lambda j: (j[0], j[1], fetch_img(j[0]['image'], j[2]) if j[0]['image'] else False), jobs))

    with app.app_context():
        cat_ids = {}
        for slug, (name, desc) in DATA['categories'].items():
            cat = Category.query.filter_by(slug=slug).first()
            if not cat:
                cat = Category(name=name, slug=slug, description=desc)
                db.session.add(cat)
                db.session.flush()
            cat_ids[slug] = cat.id
        for c in Category.query.all():
            cat_ids.setdefault(c.slug, c.id)

        existing = {p.name for p in Product.query.with_entities(Product.name).all()}
        slugs = {p.slug for p in Product.query.with_entities(Product.slug).all()}
        n = 0
        for it, slug, ok in results:
            if it['name'] in existing:
                continue
            base, k = slug, 2
            while base in slugs:
                base = f'{slug}-{k}'
                k += 1
            slug = base
            slugs.add(slug)
            units = it['units'] or 1
            price = max(100, round((it['cost'] / units * 2) / 10) * 10)
            box = f'Display x {it["units"]}' if it['units'] else 'Unidad'
            desc = it['desc'] or it['name']
            if it['brand']:
                desc += f"\nMarca: {it['brand']}."
            desc += f' Venta por unidad ({box}).'
            p = Product(
                name=it['name'],
                slug=slug,
                description=desc[:2000],
                short_description=f'Por unidad · {box}'[:300],
                price=price,
                stock=20 if it['stock'] else 0,
                category_id=cat_ids[it['cat']],
                featured=False,
                active=True,
                image=f'images/candy/{slug}.jpg' if ok else None,
            )
            db.session.add(p)
            n += 1
        db.session.commit()
        print('creados:', n)


if __name__ == '__main__':
    main()

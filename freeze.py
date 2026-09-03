"""Exporta las rutas publicas a HTML estatico en dist/ para GitHub Pages."""
import os
import re
import shutil

BASE = os.environ.get('FREEZE_BASE', '/WEBGROW')
HERE = os.path.abspath(os.path.dirname(__file__))
DIST = os.path.join(HERE, 'dist')

from app import app
from models import Product, BlogPost


def out_file(route):
    if route == '/':
        return 'index.html'
    return route.lstrip('/') + '.html'


def build_routes():
    routes = ['/', '/productos', '/blog', '/nosotros', '/contacto', '/carrito', '/login', '/registro']
    with app.app_context():
        for p in Product.query.filter_by(active=True).all():
            routes.append(f'/producto/{p.slug}')
        for b in BlogPost.query.filter_by(published=True).all():
            routes.append(f'/blog/{b.slug}')
    return routes


def map_url(url, known):
    if url.startswith('/static/'):
        return BASE + url
    path = url.split('?', 1)[0].split('#', 1)[0]
    if not path.startswith('/'):
        return url
    if path == '/':
        return BASE + '/'
    if path in known:
        return BASE + '/' + out_file(path)
    return '#'


def rewrite(html, known):
    def repl(m):
        attr, quote, url = m.group(1), m.group(2), m.group(3)
        return f'{attr}={quote}{map_url(url, known)}{quote}'
    return re.sub(r'(href|src)=(["\'])(/[^"\']*)(["\'])', repl, html)


def main():
    routes = build_routes()
    known = set(routes)
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    client = app.test_client()
    for route in routes:
        resp = client.get(route, follow_redirects=True)
        if resp.status_code != 200:
            print(f'SKIP {route} ({resp.status_code})')
            continue
        html = resp.get_data(as_text=True)
        html = rewrite(html, known)
        dest = os.path.join(DIST, out_file(route))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'OK {route} -> {out_file(route)}')
    shutil.copytree(os.path.join(HERE, 'static'), os.path.join(DIST, 'static'))
    open(os.path.join(DIST, '.nojekyll'), 'w').close()
    print('dist/ listo.')


if __name__ == '__main__':
    main()

"""Seed script to populate the database with initial data."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from models import db, Category, Product, BlogPost

categories_data = [
    {
        'name': 'Bongs',
        'slug': 'bongs',
        'description': 'Bongs de vidrio, acrílico y silicona para una experiencia de fumar suave y refrescante.',
        'image': 'images/products/category-bongs.jpg'
    },
    {
        'name': 'Pipas',
        'slug': 'pipas',
        'description': 'Pipas artesanales, de metal, madera y vidrio. Clásicas y modernas.',
        'image': 'images/products/category-pipes.jpg'
    },
    {
        'name': 'Picadores',
        'slug': 'picadores',
        'description': 'Grinders de aluminio, acrílico y madera con imán y múltiples cámaras.',
        'image': 'images/products/category-grinders.jpg'
    },
    {
        'name': 'Papeles y Sedas',
        'slug': 'papeles',
        'description': 'Papeles de arroz, hemp, sin químicos y con sabores.',
        'image': 'images/products/category-papers.jpg'
    },
    {
        'name': 'Vaporizadores',
        'slug': 'vaporizadores',
        'description': 'Vaporizadores portátiles y de escritorio para hierbas secas y concentrados.',
        'image': 'images/products/category-vapes.jpg'
    },
    {
        'name': 'Iluminación',
        'slug': 'iluminacion',
        'description': 'Lámparas LED para cultivo indoor, sodio y sistemas completos.',
        'image': 'images/products/category-lighting.jpg'
    },
    {
        'name': 'Fertilizantes',
        'slug': 'fertilizantes',
        'description': 'Nutrientes orgánicos e inorgánicos para todas las etapas del cultivo.',
        'image': 'images/products/category-nutrients.jpg'
    },
    {
        'name': 'Accesorios',
        'slug': 'accesorios',
        'description': 'Todo lo que necesitas: sedas, filtros, encendedores, limpiadores y más.',
        'image': 'images/products/category-accessories.jpg'
    }
]

products_data = [
    # Bongs
    {
        'name': 'Bong de Vidrio Clásico 30cm',
        'slug': 'bong-vidrio-clasico-30cm',
        'image': 'images/products/bong-vidrio-clasico-30cm.jpg',
        'description': 'Bong de vidrio borosilicato de alta resistencia. Base reforzada, percolador de árbol y boquilla ancha. Incluye bowl de vidrio. Fácil de limpiar y perfecto para uso diario.',
        'short_description': 'Bong de vidrio borosilicato con percolador, 30cm de altura.',
        'price': 8500,
        'compare_price': 10500,
        'stock': 15,
        'featured': True,
        'category': 'bongs'
    },
    {
        'name': 'Bong de Silicona Plegable 20cm',
        'slug': 'bong-silicona-plegable-20cm',
        'image': 'images/products/bong-silicona-plegable-20cm.jpg',
        'description': 'Bong de silicona de grado alimenticio, plegable y resistente a golpes. Viene con bowl de vidrio y downstem. Ideal para llevar a todos lados.',
        'short_description': 'Bong de silicona plegable, irrompible y portátil.',
        'price': 5500,
        'stock': 20,
        'featured': True,
        'category': 'bongs'
    },
    {
        'name': 'Bong Percolador Doble 40cm',
        'slug': 'bong-percolador-doble-40cm',
        'image': 'images/products/bong-percolador-doble-40cm.jpg',
        'description': 'Bong artesanal con doble percolador en espiral y cámara de hielo. Vidrio grueso de 5mm. Filtración triple para hits ultra suaves.',
        'short_description': 'Bong artesanal con doble percolador y cámara de hielo.',
        'price': 14500,
        'stock': 8,
        'featured': True,
        'category': 'bongs'
    },
    {
        'name': 'Mini Bong Viajero 12cm',
        'slug': 'mini-bong-viajero-12cm',
        'image': 'images/products/mini-bong-viajero-12cm.jpg',
        'description': 'Mini bong de vidrio compacto perfecto para llevar. Incluye bowl y downstem. Cabe en cualquier mochila.',
        'short_description': 'Mini bong compacto de 12cm, ideal para viajes.',
        'price': 3500,
        'stock': 25,
        'category': 'bongs'
    },
    # Pipas
    {
        'name': 'Pipa Artesanal de Madera',
        'slug': 'pipa-artesanal-madera',
        'image': 'images/products/pipa-artesanal-madera.jpg',
        'description': 'Pipa tallada a mano en madera de olivo. Cada pieza es única con su propia veta natural. Incluye pantalla de metal removible.',
        'short_description': 'Pipa única tallada a mano en madera de olivo.',
        'price': 6200,
        'stock': 10,
        'featured': True,
        'category': 'pipas'
    },
    {
        'name': 'Pipa Metálica Magnética',
        'slug': 'pipa-metalica-magnetica',
        'image': 'images/products/pipa-metalica-magnetica.jpg',
        'description': 'Pipa de aleación de aluminio aeronáutico con tapa magnética. Incluye herramienta de limpieza y estuche de silicona. Diseño minimalista.',
        'short_description': 'Pipa de aluminio con tapa magnética y estuche.',
        'price': 3800,
        'stock': 30,
        'category': 'pipas'
    },
    {
        'name': 'Pipa de Vidrio Sherlock',
        'slug': 'pipa-vidrio-sherlock',
        'image': 'images/products/pipa-vidrio-sherlock.jpg',
        'description': 'Pipa estilo Sherlock de vidrio borosilicato con carburador. Diseño curvo clásico, fácil de limpiar.',
        'short_description': 'Pipa estilo Sherlock de vidrio borosilicato.',
        'price': 4200,
        'stock': 18,
        'featured': True,
        'category': 'pipas'
    },
    {
        'name': 'Set de Pipas Mini (x3)',
        'slug': 'set-pipas-mini-x3',
        'image': 'images/products/set-pipas-mini-x3.jpg',
        'description': 'Tres pipas de vidrio de colores: rojo, azul y verde. Perfectas para probar distintos diseños o para compartir.',
        'short_description': 'Tres pipas mini de vidrio de colores.',
        'price': 2800,
        'stock': 22,
        'category': 'pipas'
    },
    # Picadores
    {
        'name': 'Grinder Aluminio 4 Piezas 50mm',
        'slug': 'grinder-aluminio-4-piezas-50mm',
        'image': 'images/products/grinder-aluminio-4-piezas-50mm.jpg',
        'description': 'Grinder de aluminio CNC de 50mm con 4 cámaras. Imán potente, dientes afilados en forma de diamante y pantalla de malla fina. Incluye palita.',
        'short_description': 'Grinder de aluminio CNC 4 piezas, 50mm.',
        'price': 4500,
        'compare_price': 5500,
        'stock': 20,
        'featured': True,
        'category': 'picadores'
    },
    {
        'name': 'Grinder Acrílico Transparente',
        'slug': 'grinder-acrilico-transparente',
        'image': 'images/products/grinder-acrilico-transparente.jpg',
        'description': 'Grinder acrílico transparente de 40mm con imán. 2 piezas, fácil de usar. Ideal para principiantes.',
        'short_description': 'Grinder acrílico 2 piezas, 40mm.',
        'price': 1200,
        'stock': 50,
        'category': 'picadores'
    },
    {
        'name': 'Grinder Eléctrico Automático',
        'slug': 'grinder-electrico-automatico',
        'image': 'images/products/grinder-electrico-automatico.jpg',
        'description': 'Grinder eléctrico a pilas con botón pulsador. Tritura sin esfuerzo. Incluye compartimento para guardar. Carga máxima de 3g.',
        'short_description': 'Grinder eléctrico automático a pilas.',
        'price': 6800,
        'stock': 12,
        'featured': True,
        'category': 'picadores'
    },
    {
        'name': 'Grinder Madera Premium con Cenicero',
        'slug': 'grinder-madera-premium-cenicero',
        'image': 'images/products/grinder-madera-premium-cenicero.jpg',
        'description': 'Grinder de madera de haya con 3 cámaras. Incluye cenicero integrado en la base. Diseño ecológico y elegante.',
        'short_description': 'Grinder de madera de haya con cenicero integrado.',
        'price': 5200,
        'stock': 8,
        'category': 'picadores'
    },
    # Papeles
    {
        'name': 'Papeles OCB Hemp King Size x50',
        'slug': 'papeles-ocb-hemp-king-size',
        'image': 'images/products/papeles-ocb-hemp-king-size.jpg',
        'description': 'Papeles de cáñamo OCB King Size, 50 unidades. Sin químicos, quema lenta y pareja.',
        'short_description': 'Papeles OCB de cáñamo king size, 50u.',
        'price': 800,
        'stock': 100,
        'featured': True,
        'category': 'papeles'
    },
    {
        'name': 'Sedas Elements Ultra Thin',
        'slug': 'sedas-elements-ultra-thin',
        'image': 'images/products/sedas-elements-ultra-thin.jpg',
        'description': 'Sedas Elements ultra finas de 32mm. Quema casi invisible. 50 libros por paquete.',
        'short_description': 'Sedas ultra finas Elements 32mm, 50u.',
        'price': 650,
        'stock': 80,
        'category': 'papeles'
    },
    {
        'name': 'Pack Papeles Saborizados (5 sabores)',
        'slug': 'pack-papeles-saborizados',
        'image': 'images/products/pack-papeles-saborizados.jpg',
        'description': 'Pack con 5 paquetes de papeles saborizados: fresa, mango, menta, chocolate y uva. 24 unidades cada uno.',
        'short_description': 'Pack 5 sabores de papeles, 24u c/u.',
        'price': 2500,
        'stock': 35,
        'featured': True,
        'category': 'papeles'
    },
    {
        'name': 'Conos Armados Raw King Size x50',
        'slug': 'conos-armados-raw-king-size',
        'image': 'images/products/conos-armados-raw-king-size.jpg',
        'description': 'Conos pre-armados Raw king size con filtro. 50 unidades. Solo llenar y listo. Hechos de cáñamo orgánico.',
        'short_description': 'Conos Raw pre-armados king size, 50u.',
        'price': 1800,
        'stock': 45,
        'category': 'papeles'
    },
    # Vaporizadores
    {
        'name': 'Vaporizador Portátil XVAPE Starry 4.0',
        'slug': 'vaporizador-portatil-xvape-starry-4',
        'image': 'images/products/vaporizador-portatil-xvape-starry-4.jpg',
        'description': 'Vaporizador portátil con control digital de temperatura. Cámara de convección, batería de 2500mAh. Pantalla OLED. Ideal para hierbas secas.',
        'short_description': 'Vaporizador portátil con control digital de temperatura.',
        'price': 28500,
        'compare_price': 35000,
        'stock': 7,
        'featured': True,
        'category': 'vaporizadores'
    },
    {
        'name': 'Vaporizador de Escritorio Arizer Extreme Q',
        'slug': 'vaporizador-escritorio-arizer-extreme-q',
        'image': 'images/products/vaporizador-escritorio-arizer-extreme-q.jpg',
        'description': 'Vaporizador de mesa con sistema de balón y whip. Control remoto, temperatura digital precisa. Incluye todos los accesorios.',
        'short_description': 'Vaporizador de escritorio con balón y whip.',
        'price': 52000,
        'stock': 3,
        'featured': True,
        'category': 'vaporizadores'
    },
    {
        'name': 'Vape Pen Desechable',
        'slug': 'vape-pen-desechable',
        'image': 'images/products/vape-pen-desechable.jpg',
        'description': 'Vape pen desechable compacto. Sabor natural. Aprox. 300 caladas. Ideal para probar.',
        'short_description': 'Vape pen desechable, 300 caladas.',
        'price': 3200,
        'stock': 50,
        'category': 'vaporizadores'
    },
    # Iluminación
    {
        'name': 'Panel LED Cultivo Full Spectrum 600W',
        'slug': 'panel-led-cultivo-full-spectrum-600w',
        'image': 'images/products/panel-led-cultivo-full-spectrum-600w.jpg',
        'description': 'Panel LED de 600W para cultivo indoor con espectro completo. Incluye switches para vegetación y floración. Ventiladores silenciosos incorporados.',
        'short_description': 'Panel LED 600W full spectrum para indoor.',
        'price': 38500,
        'compare_price': 45000,
        'stock': 10,
        'featured': True,
        'category': 'iluminacion'
    },
    {
        'name': 'Lámpara LED Cultivo 100W',
        'slug': 'lampara-led-cultivo-100w',
        'image': 'images/products/lampara-led-cultivo-100w.jpg',
        'description': 'Lámpara LED de 100W con espectro ajustable. Ideal para espacios pequeños o crecimiento. Plug & play.',
        'short_description': 'Lámpara LED 100W para espacios pequeños.',
        'price': 9500,
        'stock': 15,
        'category': 'iluminacion'
    },
    {
        'name': 'Timer Digital para Cultivo',
        'slug': 'timer-digital-cultivo',
        'image': 'images/products/timer-digital-cultivo.jpg',
        'description': 'Timer digital programable 24h para ciclos de luz. 2 tomas. Fácil configuración.',
        'short_description': 'Timer digital programable para ciclos de luz.',
        'price': 2200,
        'stock': 30,
        'category': 'iluminacion'
    },
    # Fertilizantes
    {
        'name': 'Kit Fertilizantes Top Crop (3x1L)',
        'slug': 'kit-fertilizantes-top-crop-3x1l',
        'image': 'images/products/kit-fertilizantes-top-crop-3x1l.jpg',
        'description': 'Kit completo Top Crop: Top Veg, Top Bloom y Top Candy. Pack 3 botellas de 1 litro cada una. Para todo el ciclo de cultivo.',
        'short_description': 'Kit Top Crop 3x1L para ciclo completo.',
        'price': 8500,
        'compare_price': 10200,
        'stock': 18,
        'featured': True,
        'category': 'fertilizantes'
    },
    {
        'name': 'Enraizante Orgánico 500ml',
        'slug': 'enraizante-organico-500ml',
        'image': 'images/products/enraizante-organico-500ml.jpg',
        'description': 'Enraizante orgánico concentrado. Estimula el desarrollo radicular. Apto para cultivo orgánico. 500ml rinde hasta 100L de solución.',
        'short_description': 'Enraizante orgánico concentrado 500ml.',
        'price': 3200,
        'stock': 25,
        'category': 'fertilizantes'
    },
    {
        'name': 'Medidor pH Digital',
        'slug': 'medidor-ph-digital',
        'image': 'images/products/medidor-ph-digital.jpg',
        'description': 'Medidor de pH digital con calibración automática. Rango 0-14. Exactitud ±0.01. Incluye soluciones de calibración.',
        'short_description': 'Medidor de pH digital profesional.',
        'price': 4800,
        'stock': 20,
        'category': 'fertilizantes'
    },
    # Accesorios
    {
        'name': 'Filtros de Carbón x100',
        'slug': 'filtros-carbon-x100',
        'image': 'images/products/filtros-carbon-x100.jpg',
        'description': 'Filtros de carbón activado de 8mm. 100 unidades por paquete. Reducen impurezas y suavizan el humo.',
        'short_description': '100 filtros de carbón activado 8mm.',
        'price': 900,
        'stock': 60,
        'featured': True,
        'category': 'accesorios'
    },
    {
        'name': 'Encendedor Eléctrico Recargable USB',
        'slug': 'encendedor-electrico-recargable-usb',
        'image': 'images/products/encendedor-electrico-recargable-usb.jpg',
        'description': 'Encendedor eléctrico por arco voltaico. Recargable por USB. Resistente al viento. Sin gas ni llama abierta.',
        'short_description': 'Encendedor arco voltaico recargable USB.',
        'price': 2800,
        'stock': 35,
        'featured': True,
        'category': 'accesorios'
    },
    {
        'name': 'Kit Limpieza para Bongs',
        'slug': 'kit-limpieza-bongs',
        'image': 'images/products/kit-limpieza-bongs.jpg',
        'description': 'Kit completo de limpieza: 250ml solución limpiadora, cepillos de diferentes tamaños y soporte para secado.',
        'short_description': 'Kit completo de limpieza para bongs.',
        'price': 3500,
        'stock': 20,
        'category': 'accesorios'
    },
    {
        'name': 'Bolsa Hermética Multi-uso 5 Pack',
        'slug': 'bolsa-hermetica-multiuso-5-pack',
        'image': 'images/products/bolsa-hermetica-multiuso-5-pack.jpg',
        'description': '5 bolsas herméticas con cierre zip de diferentes tamaños. Mantienen la frescura. Material Mylar.',
        'short_description': '5 bolsas herméticas Mylar de varios tamaños.',
        'price': 1500,
        'stock': 40,
        'category': 'accesorios'
    },
    {
        'name': 'Cenicero de Silicona Plegable',
        'slug': 'cenicero-silicona-plegable',
        'image': 'images/products/cenicero-silicona-plegable.jpg',
        'description': 'Cenicero de silicona plegable con tapa. Atrapa olores. Fácil de limpiar. Ideal para llevar.',
        'short_description': 'Cenicero plegable de silicona con tapa.',
        'price': 1800,
        'stock': 30,
        'category': 'accesorios'
    },
    {
        'name': 'Mochila Grower Edición Limitada',
        'slug': 'mochila-grower-edicion-limitada',
        'image': 'images/products/mochila-grower-edicion-limitada.jpg',
        'description': 'Mochila edición limitada Perrone\'s INC. Compartimento acolchado, bolsillos organizadores y diseño discreto.',
        'short_description': 'Mochila edición limitada Perrone\'s INC.',
        'price': 12000,
        'stock': 5,
        'featured': True,
        'category': 'accesorios'
    }
]

blog_posts_data = [
    {
        'title': 'Guía Completa para Principiantes en el Cultivo Indoor',
        'slug': 'guia-completa-cultivo-indoor-principiantes',
        'image': 'images/products/guia-completa-cultivo-indoor-principiantes.jpg',
        'image': 'images/blog/guia-principiantes.jpg',
        'excerpt': 'Todo lo que necesitas saber para empezar tu primer cultivo indoor: espacio, luces, ventilación y nutrientes.',
        'content': """<h2>Introducción al Cultivo Indoor</h2>
<p>El cultivo indoor te permite tener control total sobre el ambiente de tus plantas. Ya no dependes de las estaciones ni del clima exterior. Con el equipo adecuado, puedes obtener cosechas de alta calidad durante todo el año.</p>

<h2>¿Qué necesitas para empezar?</h2>
<h3>1. El Espacio</h3>
<p>Puedes usar un armario, un grow tent o una habitación dedicada. Para empezar, un espacio de 60x60x140cm es suficiente para 1-2 plantas. Asegúrate de que sea un espacio reflectante (pintura blanca o mylar).</p>

<h3>2. La Iluminación</h3>
<p>La luz es el factor más importante. Para principiantes, recomendamos:</p>
<ul>
<li><strong>LED Full Spectrum:</strong> Eficientes, poco calor, buena cobertura</li>
<li><strong>CFL (bajo consumo):</strong> Económicos, ideales para espacios pequeños</li>
</ul>

<h3>3. Ventilación</h3>
<p>Necesitas 3 elementos básicos:</p>
<ul>
<li>Extractor para sacar el aire caliente</li>
<li>Intractor pasivo o activo para entrada de aire fresco</li>
<li>Ventilador interior para movimiento de aire</li>
</ul>

<h3>4. Sustrato y Macetas</h3>
<p>Recomendamos empezar con tierra liviana y macetas de tela (smart pots) que permiten mejor drenaje y aireación de raíces.</p>

<h2>Ciclo de Vida de la Planta</h2>
<h3>Germinación (1-2 semanas)</h3>
<p>Coloca la semilla en un vaso con agua 24h, luego pásala a un paño húmedo hasta que salga la raíz. Una vez lista, trasplanta a su maceta definitiva.</p>

<h3>Vegetación (3-8 semanas)</h3>
<p>Durante esta fase, la planta desarrolla su estructura. Mantén 18-20 horas de luz por día. Es crucial no estresar la planta con cambios bruscos.</p>

<h3>Floración (8-12 semanas)</h3>
<p>Cambia el ciclo de luz a 12/12 (12 horas luz, 12 horas oscuridad total). Aquí es donde se forman los cogollos.</p>

<h2>Errores Comunes de Principiantes</h2>
<ol>
<li><strong>Regar en exceso:</strong> La causa #1 de muerte de plantas. Deja que la tierra se seque entre riegos.</li>
<li><strong>Sobrefertilizar:</strong> Menos es más. Sigue las dosis recomendadas.</li>
<li><strong>No medir pH:</strong> Mantén el pH entre 6.0 y 6.8 en tierra.</li>
<li><strong>Fugas de luz:</strong> Durante la floración, cualquier fuga de luz puede causar estrés.</li>
</ol>""",
        'category': 'Cultivo',
        'tags': 'cultivo, indoor, principiantes, guia, marihuana',
        'published': True,
        'featured': True
    },
    {
        'title': 'Cómo Elegir el Mejor Vaporizador para tus Necesidades',
        'slug': 'como-elegir-mejor-vaporizador',
        'image': 'images/products/como-elegir-mejor-vaporizador.jpg',
        'image': 'images/blog/vapo1.jpg',
        'excerpt': 'Guía para elegir entre vaporizadores portátiles, de escritorio, y qué características tener en cuenta.',
        'content': """<h2>¿Por qué Vaporizar?</h2>
<p>La vaporización se ha convertido en una de las formas más populares de consumo. Al no producir combustión, evitas los subproductos tóxicos del humo y obtienes un sabor más puro y limpio.</p>

<h2>Tipos de Vaporizadores</h2>

<h3>1. Vaporizadores Portátiles</h3>
<p>Ideales para quien busca discreción y movilidad. Características a considerar:</p>
<ul>
<li><strong>Autonomía de batería:</strong> Busca mínimo 2000mAh</li>
<li><strong>Tipo de calentamiento:</strong> Convección (mejor sabor) vs Conducción (más denso)</li>
<li><strong>Control de temperatura:</strong> Preciso y ajustable</li>
<li><strong>Facilidad de limpieza:</strong> Fundamental para el mantenimiento</li>
</ul>

<h3>2. Vaporizadores de Escritorio</h3>
<p>Para uso en casa, ofrecen la mejor experiencia:</p>
<ul>
<li><strong>Sistema de balón:</strong> Llenas una bolsa y compartes</li>
<li><strong>Sistema whip:</strong> Manguera directa para uso individual</li>
<li><strong>Potencia:</strong> Mayor capacidad de carga y control preciso</li>
</ul>

<h3>3. Vape Pens</h3>
<p>Compactos y discretos, perfectos para llevar. Ideales para quienes recién empiezan.</p>

<h2>Características Clave</h2>
<table>
<tr><td><strong>Control de Temperatura</strong></td><td>Busca rangos de 160°C a 220°C</td></tr>
<tr><td><strong>Materiales</strong></td><td>Acero inoxidable y vidrio son los mejores</td></tr>
<tr><td><strong>Garantía</strong></td><td>Mínimo 1 año, ideal 2+ años</td></tr>
<tr><td><strong>Flujo de aire</strong></td><td>Regulable para personalizar la experiencia</td></tr>
</table>

<h2>Consejo Final</h2>
<p>Para quienes empiezan, lo ideal es un vaporizador con control preciso de temperatura y fácil limpieza. Los más exigentes suelen preferir los de escritorio por su potencia y capacidad.</p>""",
        'category': 'Vaporización',
        'tags': 'vaporizador, vape, hierbas, salud',
        'published': True,
        'featured': True
    },
    {
        'title': 'Historia y Cultura Cannábica: De lo Sagrado a lo Moderno',
        'slug': 'historia-cultura-cannabica-sagrado-moderno',
        'image': 'images/products/historia-cultura-cannabica-sagrado-moderno.jpg',
        'image': 'images/blog/belgrano.jpg',
        'excerpt': 'Un recorrido por la historia del cannabis desde sus usos ancestrales hasta la cultura moderna.',
        'content': """<h2>Raíces Antiguas</h2>
<p>El cannabis acompaña a la humanidad desde hace milenios. Las primeras evidencias de su uso datan del año 4000 a.C. en China, donde se utilizaba tanto como fibra textil como con fines medicinales.</p>

<h2>El Cannabis en la Medicina Tradicional</h2>
<p>En la India, el cannabis era considerado una planta sagrada. Los textos védicos lo mencionan como una fuente de alegría y liberación. En el antiguo Egipto, se usaba para tratar el glaucoma y la inflamación.</p>

<h2>La Llegada a América</h2>
<p>El cannabis llegó a América con los colonizadores españoles, que lo cultivaban por su fibra. Fue en el siglo XX cuando comenzó la estigmatización y posterior prohibición.</p>

<h2>La Revolución Contracultural</h2>
<p>En los años 60 y 70, el cannabis se convirtió en símbolo de la contracultura. Movimientos hippies, músicos de jazz y rock, y artistas de todo tipo adoptaron la planta como emblema de libertad y creatividad.</p>

<h2>La Era Moderna: Legalización y Regulación</h2>
<p>En las últimas décadas, el paradigma ha cambiado drásticamente. Países como Uruguay, Canadá y varios estados de EE.UU. han legalizado el cannabis. Hoy hablamos de:</p>
<ul>
<li><strong>Uso medicinal:</strong> Reconocido por sus propiedades terapéuticas</li>
<li><strong>Uso recreativo:</strong> Regulado y controlado</li>
<li><strong>Industria:</strong> Un mercado global multimillonario</li>
</ul>

<h2>La Cultura Hoy</h2>
<p>La cultura moderna es diversa e inclusiva. Desde growers que comparten conocimientos en redes sociales, hasta chefs que crean experiencias gastronómicas, pasando por la moda y el arte.</p>

<p>Celebremos esta cultura con respeto y pasión, educando y construyendo una comunidad responsable.</p>""",
        'category': 'Cultura',
        'tags': 'historia, cultura, cannabis, legalizacion',
        'published': True,
        'featured': True
    },
    {
        'title': 'Tips para Mantener tus Accesorios como Nuevos',
        'slug': 'tips-mantener-accesorios-como-nuevos',
        'image': 'images/products/tips-mantener-accesorios-como-nuevos.jpg',
        'image': 'images/blog/2116.jpg',
        'excerpt': 'Cómo limpiar y mantener tus bongs, pipas y grinders para que duren más y funcionen mejor.',
        'content': """<h2>Por qué es Importante la Limpieza</h2>
<p>Mantener tus accesorios limpios no solo es cuestión de estética. Un bong o pipa sucio puede afectar el sabor, reducir la eficiencia y hasta ser perjudicial para la salud.</p>

<h2>Limpieza de Bongs</h2>
<h3>Método Rápido (Limpieza Diaria)</h3>
<p>Enjuaga con agua caliente después de cada uso. Esto evita que la resina se acumule.</p>

<h3>Limpieza Profunda (Semanal)</h3>
<ol>
<li>Vacía el agua y desarma todas las piezas</li>
<li>Coloca las partes en una bolsa con alcohol isopropílico al 90% y sal gruesa</li>
<li>Agita vigorosamente por 2-3 minutos</li>
<li>Enjuaga con agua caliente hasta eliminar todo residuo</li>
<li>Deja secar completamente antes de armar</li>
</ol>

<h2>Limpieza de Pipas</h2>
<p>Las pipas requieren atención especial por sus formas intrincadas:</p>
<ul>
<li>Usa alcohol isopropílico y sal</li>
<li>Para pipas de vidrio: sumerge en alcohol toda la noche</li>
<li>Para pipas de metal: puedes hervirlas en agua por 10 minutos</li>
<li>Usa limpiapipas para alcanzar zonas difíciles</li>
</ul>

<h2>Mantenimiento de Grinders</h2>
<ul>
<li>Limpia los dientes con un cepillo pequeño después de cada uso</li>
<li>Congela el grinder por 30 minutos para desprender resina pegada</li>
<li>Lava con alcohol isopropílico una vez al mes</li>
<li>Lubrica la rosca con aceite vegetal comestible si está dura</li>
</ul>

<h2>Consejos Generales</h2>
<ul>
<li>No uses agua hirviendo en vidrio frío (puede romperlo)</li>
<li>Evita limpiadores con químicos agresivos</li>
<li>Ten un kit de limpieza dedicado</li>
<li>Cambia el agua del bong después de cada sesión</li>
</ul>

<p>Con un kit de limpieza dedicado y constancia, tus accesorios se mantienen en perfecto estado por años.</p>""",
        'category': 'Accesorios',
        'tags': 'limpieza, mantenimiento, bongs, pipas, grinders',
        'published': True,
        'featured': False
    },
    {
        'title': 'Guía de Nutrientes: Qué Darle a tus Plantas en Cada Etapa',
        'slug': 'guia-nutrientes-cada-etapa',
        'image': 'images/blog/guia-principiantes.jpg',
        'excerpt': 'Conocé qué nutrientes necesita tu planta en vegetación, floración y precosecha.',
        'content': """<h2>La Alimentación de tus Plantas</h2>
<p>Una nutrición adecuada es la diferencia entre una cosecha mediocre y una espectacular. Cada etapa del ciclo de vida requiere un perfil nutricional específico.</p>

<h2>Etapa de Vegetación</h2>
<h3>Macronutrientes Clave:</h3>
<ul>
<li><strong>Nitrógeno (N):</strong> Alto - Fundamental para hojas y tallos</li>
<li><strong>Fósforo (P):</strong> Medio - Desarrollo radicular</li>
<li><strong>Potasio (K):</strong> Medio - Transporte de nutrientes</li>
</ul>
<p>Usa un fertilizante de vegetación con alta relación de nitrógeno (N).</p>

<h2>Etapa de Floración</h2>
<h3>Cambio de Perfil:</h3>
<ul>
<li><strong>Nitrógeno (N):</strong> Bajo - Reducir progresivamente</li>
<li><strong>Fósforo (P):</strong> Alto - Formación de cogollos</li>
<li><strong>Potasio (K):</strong> Alto - Producción de resina</li>
</ul>
<p>Cambia a fertilizante de floración. El Top Bloom es excelente para esta etapa.</p>

<h2>Etapa de Engorde y Maduración</h2>
<ul>
<li>Agrega un potenciador de cogollos como Top Candy</li>
<li>Mantén buen nivel de Potasio</li>
<li>Reduce el Nitrógeno al mínimo</li>
</ul>

<h2>Precosecha (Flushing)</h2>
<p>2 semanas antes de cosechar, usa solo agua pH balanceada. Esto elimina residuos de fertilizantes y mejora el sabor final.</p>

<h2>Problemas Comunes</h2>
<table>
<tr><td><strong>Hojas amarillas abajo</strong></td><td>Falta de Nitrógeno</td></tr>
<tr><td><strong>Puntas quemadas</strong></td><td>Exceso de fertilizante</td></tr>
<tr><td><strong>Hojas enrolladas</strong></td><td>Estrés por calor o sobrefertilización</td></tr>
<tr><td><strong>Manchas marrones</strong></td><td>Posible deficiencia de Calcio/Magnesio</td></tr>
</table>

<h2>Consejo Final</h2>
<p>Un kit básico de crecimiento, flora y engorde cubre el ciclo completo, tanto para principiantes como para expertos.</p>""",
        'category': 'Cultivo',
        'tags': 'nutrientes, fertilizantes, cultivo, floracion, vegetacion',
        'published': True,
        'featured': False
    },
    {
        'title': 'Dry Sift y Kief: Guía completa de extracción en seco',
        'slug': 'extraccion-en-seco-dry-sift-kief',
        'image': 'images/blog/extraccion-seco.jpg',
        'excerpt': 'Aprendé a separar tricomas en seco con mallas y tamices: qué micronaje usar, cómo prensar kief y errores a evitar.',
        'content': """<h2>Qué es la Extracción en Seco</h2>
<p>La extracción en seco, también llamada <strong>dry sift</strong>, es el método más antiguo y simple: se separan los tricomas de la flor usando fricción suave sobre mallas calibradas. El resultado es el <strong>kief</strong>, un polvo dorado lleno de cannabinoides y terpenos.</p>
<p>Ventajas: no usa solventes, ni agua, ni calor. Solo necesitas mallas, frío y paciencia.</p>
<figure class="blog-figure"><img src="/static/images/blog/extraccion-seco-cuerpo.jpg" alt="Tricomas curados y concentrados" loading="lazy"><figcaption>Tricomas curados y concentrados, la base del dry sift. Foto: Mjpresson, Wikimedia Commons (CC BY-SA 3.0).</figcaption></figure>

<h2>Qué Necesitás</h2>
<ul>
<li><strong>Mallas o tamices:</strong> 70u, 110u y 160u son el estándar. A menor micraje, mayor pureza.</li>
<li><strong>Material bien seco y curado:</strong> humedad 55-62%. Si está húmedo, se apelmaza.</li>
<li><strong>Frío:</strong> trabajá en ambiente frío o meté el material 30 min al freezer. El tricoma se vuelve quebradizo y se suelta fácil.</li>
<li><strong>Tarjeta o pincel suave</strong> para mover el material sin romperlo.</li>
</ul>

<h2>Paso a Paso</h2>
<h3>1. Primera pasada (160u)</h3>
<p>Colocá una pequeña cantidad sobre la malla y mové en círculos suaves 2-3 minutos. Lo que cae es tu primera calidad, más vegetal pero abundante.</p>
<h3>2. Refinado (110u y 70u)</h3>
<p>Pasá lo recolectado por mallas más finas. La fracción de 70-110u suele ser la <strong>full melt</strong>: se derrite al calor, color rubio claro.</p>
<h3>3. Limpieza estática</h3>
<p>Truco pro: envolvé el kief en papel manteca y pasá un guante de látex con estática por encima. Los contaminantes vegetales se pegan al guante y el kief puro queda abajo.</p>

<h2>Calidades y Colores</h2>
<ul>
<li><strong>Rubio claro:</strong> cabezas de tricomas puras, máxima calidad.</li>
<li><strong>Verdoso:</strong> tiene materia vegetal, ideal para prensar o cocinar.</li>
<li><strong>Marrón oscuro:</strong> oxidado o viejo, mejor para comestibles.</li>
</ul>

<h2>Cómo Conservarlo y Usarlo</h2>
<p>Guardá en frasco hermético, oscuro y frío. Podés espolvorear sobre flores, prensar en hachís con calor suave, o guardar para hacer rosin después.</p>

<h2>Errores Comunes</h2>
<ol>
<li><strong>Frotar muy fuerte:</strong> rompe materia vegetal y contamina.</li>
<li><strong>Material húmedo:</strong> no tamiza bien y deja hongos.</li>
<li><strong>Ambiente caluroso:</strong> los tricomas se derriten y tapan la malla.</li>
</ol>

<p class="img-credit">Foto de portada: 1 g de kief tamizado. Mjpresson, Wikimedia Commons (CC BY 3.0).</p>""",
        'category': 'Extracciones',
        'tags': 'extraccion, seco, dry sift, kief, hash, sin solventes',
        'published': True,
        'featured': True
    },
    {
        'title': 'Bubble Hash: Extracción con Agua y Hielo Paso a Paso',
        'slug': 'extraccion-bubble-hash-agua-hielo',
        'image': 'images/blog/extraccion-bubble.jpg',
        'excerpt': 'La técnica de bubble hash con bolsas de micraje: temperaturas, tiempos de batido, secado y curado para un hash premium.',
        'content': """<h2>Qué es el Bubble Hash</h2>
<p>El <strong>bubble hash</strong> o hash de agua usa hielo, agua fría y bolsas filtrantes (bubble bags) para separar los tricomas por densidad. Al calentarse hace burbujas — de ahí su nombre. Es sin solventes y uno de los concentrados más sabrosos.</p>

<h2>Manera Casera vs Profesional</h2>
<p>Hay dos caminos para llegar al mismo resultado, y el principio es idéntico: agua helada + agitación + filtrado por micraje. Lo que cambia es la escala y la comodidad.</p>
<ul>
<li><strong>Casera:</strong> un balde de 20L, un set de bubble bags, una cuchara de madera o un mixer, y mucho hielo. Ideal para arrancar y sacar tus primeros gramos.</li>
<li><strong>Profesional:</strong> tanque de acero con válvula de descarga, <strong>lavadora de hash</strong> (agita sola con ciclos programados), cuarto frío para trabajar a temperatura estable y <strong>liofilizadora</strong> (freeze dryer) para un secado perfecto en 24h en vez de una semana.</li>
</ul>
<p>En esta guía te mostramos el proceso completo con fotos reales de cada etapa: se puede hacer en casa, y se puede ir profesionalizando con lavadora o equipo industrial a medida que crecés.</p>

<h2>Equipo Necesario</h2>
<ul>
<li><strong>Bubble bags:</strong> set de 4-8 bolsas (220u, 160u, 120u, 73u, 45u, 25u). La de 73u suele dar la mejor calidad.</li>
<li><strong>Recipiente:</strong> balde de 20L en casa, o tanque de acero con grifo a nivel pro.</li>
<li><strong>Hielo en cantidad y agua bien fría (2-4°C).</strong></li>
<li><strong>Agitación:</strong> cuchara de madera o batidora a baja velocidad; lavadora de hash si querés subir de nivel.</li>
<li><strong>Malla de secado, papel manteca y microplane o tamiz para rallar.</strong></li>
</ul>

<h2>Paso a Paso con Fotos</h2>
<h3>1. Carga del material y el hielo</h3>
<p>Llená el recipiente con agua fría, una buena base de hielo y el material (fresco congelado = live bubble, más terpenoso; seco curado = más rendimiento). En casa un balde alcanza; a nivel pro se usa tanque de acero con descarga inferior.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-0.jpg" alt="Tanque con material vegetal y hielo" loading="lazy"><figcaption>Carga del material con abundante hielo antes del lavado.</figcaption></figure>
<h3>2. Batido y remolino</h3>
<p>Remové 10-15 minutos en círculos suaves hasta formar el remolino: la fricción del hielo suelta los tricomas. Descansá 20-30 minutos para que decanten. No batas de más: a partir de los 20 min aumenta el contaminante vegetal. Con lavadora, este paso lo hace la máquina con ciclos programados.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-1.jpg" alt="Remolino del lavado con hielo y material" loading="lazy"><figcaption>El remolino durante el batido: el hielo separa los tricomas del material.</figcaption></figure>
<h3>3. Filtrado con bubble bags</h3>
<p>Apilá las bolsas de menor a mayor micraje (25u abajo, 220u arriba) y volcá la mezcla. Cada bolsa retiene una calidad distinta: 120-73u suele ser full melt, 45-25u es más para cocinar.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-2.jpg" alt="Set de bubble bags por micraje" loading="lazy"><figcaption>Set de bolsas filtrantes identificadas por color según el micraje.</figcaption></figure>
<h3>4. Recolección del hash</h3>
<p>Levantá cada bolsa una por una, dejá escurrir y recolectá el hash con cuchara fría sobre papel manteca.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-3.jpg" alt="Recolección del hash con cuchara" loading="lazy"><figcaption>Recolección del hash de cada bolsa con cuchara fría.</figcaption></figure>
<h3>5. Enjuague de las bolsas</h3>
<p>Con manguera a presión suave, arrastrá los restos de hash hacia el centro de la malla para no perder nada. Este paso mejora el rendimiento final.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-4.jpg" alt="Enjuague de la bolsa con manguera" loading="lazy"><figcaption>Enjuague con agua a presión para juntar todo el hash en el centro.</figcaption></figure>
<h3>6. Extendido para el secado</h3>
<p>Esparcí el hash húmedo en capa fina sobre papel manteca en bandejas. Cuanto más extendido, mejor seca y menos riesgo de hongos.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-5.jpg" alt="Hash extendido en bandeja" loading="lazy"><figcaption>Hash húmedo extendido en bandeja con papel manteca.</figcaption></figure>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-6.jpg" alt="Plancha de hash antes del secado" loading="lazy"><figcaption>Plancha de hash lista para entrar en secado.</figcaption></figure>
<h3>7. Secado (el paso crítico)</h3>
<p>Rallá el hash con microplane sobre papel manteca en ambiente frío y seco (15°C, 35% humedad) y secá 5-7 días. Si no se seca bien, le salen hongos. Nunca uses calor ni microondas. A nivel pro, la liofilizadora deja el hash seco y rubio en 24 horas.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-7.jpg" alt="Bandejas con hash rallado secándose" loading="lazy"><figcaption>Hash rallado en bandejas durante el secado de varios días.</figcaption></figure>
<h3>8. Producto final</h3>
<p>El resultado: un hash color arena, aromático y potente, listo para consumir o prensar como rosin.</p>
<figure class="blog-figure"><img src="/static/images/blog/bubble-paso-8.jpg" alt="Bubble hash seco final" loading="lazy"><figcaption>Bubble hash seco y terminado, con su clásico color arena.</figcaption></figure>

<h2>Consejos Pro</h2>
<ul>
<li>Usá agua de ósmosis o destilada para mejor sabor.</li>
<li>Hacé 2-3 lavadas del mismo material: la 1ra es la más pura.</li>
<li>Congelá todo (bolsas, cucharas, material) antes de empezar.</li>
<li>Si te enganchás, la primera mejora que se nota es la lavadora de hash: misma calidad, cero brazo cansado.</li>
</ul>

<h2>Cómo Consumirlo</h2>
<p>En pipa, bong, espolvoreado o dabbeado a baja temperatura (170-190°C). El full melt de 73u se puede dabear puro.</p>

<p class="img-credit">Fotos del proceso: gentileza Perrone's INC. Foto de portada: hash prensado por extracción con hielo. Mjpresson, Wikimedia Commons.</p>""",
        'category': 'Extracciones',
        'tags': 'extraccion, bubble hash, agua, hielo, hash, sin solventes',
        'published': True,
        'featured': True
    },
    {
        'title': 'Extracción con Butano (BHO): Qué es, Riesgos y Seguridad',
        'slug': 'extraccion-butano-bho-seguridad',
        'image': 'images/blog/extraccion-bho.jpg',
        'excerpt': 'Guía educativa sobre BHO: tipos (shatter, wax, budder), por qué el open blasting casero es peligroso y qué exigir en un producto seguro.',
        'content': """<h2>Aviso Importante de Seguridad</h2>
<p><strong>El butano es altamente inflamable y sus vapores pueden explotar.</strong> La extracción casera a cielo abierto (open blasting) ha causado accidentes graves. Este artículo es <strong>educativo</strong>: no recomendamos hacer BHO en casa. La producción segura requiere circuito cerrado, laboratorio, vacío y control profesional.</p>

<h2>Qué es el BHO</h2>
<p>El <strong>BHO (Butane Hash Oil)</strong> disuelve cannabinoides y terpenos con butano líquido. Luego se purga el solvente con vacío y calor suave. Según la purga y temperatura se obtienen texturas: <strong>shatter</strong> (vidrio), <strong>wax / budder</strong> (cremoso), <strong>live resin</strong> (de planta fresca congelada, muy terpenosa).</p>
<figure class="blog-figure"><img src="/static/images/blog/bho-purgado.jpg" alt="Aceite de BHO purgándose en fuente de vidrio" loading="lazy"><figcaption>Aceite recién extraído purgándose en fuente de vidrio: así se ve el BHO antes del curado final.</figcaption></figure>

<h2>Por Qué es Peligroso Hacerlo en Casa</h2>
<ul>
<li>El butano es más pesado que el aire: se acumula abajo y cualquier chispa (heladera, enchufe, encendedor) lo detona.</li>
<li>Sin bomba de vacío no se purga bien: queda butano residual que irrita pulmones.</li>
<li>Butano de encendedor trae impurezas (mercaptanos). El grado extracción es N-tano puro, no se vende en kioscos.</li>
</ul>
<p><strong>Regla de oro: si no tenés circuito cerrado, sala anti-explosión y medidor de gases, no lo hagas.</strong></p>

<h2>Cómo se Hace a Nivel Profesional (resumen teórico)</h2>
<ol>
<li>Material congelado en columna de acero inoxidable.</li>
<li>Paso de N-butano en circuito cerrado.</li>
<li>Recuperación del solvente.</li>
<li>Purgado en horno de vacío a 30-40°C por 24-72h hasta &lt;5000 ppm residual.</li>
<li>Análisis de laboratorio de potencia y solventes.</li>
</ol>
<figure class="blog-figure vertical"><img src="/static/images/blog/bho-columna.jpg" alt="Columna de extracción de circuito cerrado" loading="lazy"><figcaption>Columna de extracción de circuito cerrado con manómetro: el estándar del trabajo profesional, muy lejos del blasting casero.</figcaption></figure>

<h2>Cómo Reconocer un BHO Seguro</h2>
<ul>
<li>Color claro y translúcido, sin burbujas ni olor a gas.</li>
<li>Análisis de laboratorio disponible.</li>
<li>Textura estable, no chisporrotea al dabear.</li>
</ul>

<h2>Alternativas Más Seguras</h2>
<p>Si buscás concentrados potentes sin riesgo, preferí <strong>rosin con prensa</strong>, <strong>bubble hash</strong> o <strong>dry sift</strong>: sin solventes y replicables en casa. Tenemos guías de cada una en este blog.</p>
<p class="img-credit">Foto de portada: shatter dorado en macro, gentileza Perrone's INC.</p>""",
        'category': 'Extracciones',
        'tags': 'extraccion, bho, butano, shatter, wax, seguridad',
        'published': True,
        'featured': False
    },
    {
        'title': 'Rosin con Prensa: Extracción sin Solventes en Casa',
        'slug': 'extraccion-prensa-rosin-casera',
        'image': 'images/blog/rosin-papel-abierto.jpg',
        'excerpt': 'Cómo prensar rosin de flor, kief y hash: tipos de rosin, temperaturas, micrajes y los factores que definen textura, color y terpenos.',
        'content': """<h2>Qué es el Rosin</h2>
<p>El <strong>rosin</strong> se obtiene prensando material con <strong>calor suave + presión alta</strong>. La resina fluye y se recolecta. Sin solventes, sin agua, listo en minutos. Es la extracción más segura para hacer en casa.</p>
<figure class="blog-figure"><img src="/static/images/blog/rosin-fluyendo.webp" alt="Rosin recién prensado fluyendo sobre papel manteca" loading="lazy"><figcaption>Rosin recién prensado fluyendo sobre el papel: así se ve una buena extracción, dorada y burbujeante.</figcaption></figure>

<h2>Tipos de Rosin: no todos se hacen con flor</h2>
<p>Con la misma prensa podés lograr productos totalmente distintos según el material de partida. Estos son los 4 principales:</p>
<figure class="blog-figure"><img src="/static/images/blog/rosin-tipos-flower-hash-live.webp" alt="Comparativa de flower rosin, hash rosin y live rosin" loading="lazy"><figcaption>De izquierda a derecha: Flower Rosin, Hash Rosin y Live Rosin. Cambian color, textura y potencia según el material de partida.</figcaption></figure>
<ul>
<li><strong>1. Flower Rosin (rosin de flor):</strong> se prensa la flor directamente. Es el más fácil y rápido, ideal para empezar. Sabor intenso a la planta, color más ámbar/marrón y rendimiento de 10-25%. Requiere flor bien curada con 55-62% de humedad.</li>
<li><strong>2. Kief / Dry Sift Rosin:</strong> se prensa el kief del grinder o el dry sift tamizado. Más puro y potente que el de flor, color más claro, textura más mantecosa. Se usa bolsa de 37u-73u y menos temperatura (80-100°C).</li>
<li><strong>3. Hash Rosin (bubble hash prensado):</strong> se prensa bubble hash seco. Es el estándar de calidad en dispensarios: color rubio claro, máximo sabor y potencia, casi sin contaminantes vegetales. Se prensa a 70-90°C en doble bolsa de 37u.</li>
<li><strong>4. Live Rosin:</strong> se hace con bubble hash de planta fresca congelada (fresh frozen), sin secar ni curar. Conserva todos los terpenos volátiles: es el más aromático, claro y caro de producir. Textura tipo badder o salsa.</li>
</ul>
<p>En resumen: <strong>flor = fácil y rendidor, hash/live = más puro, claro y terpenoso</strong>, pero requieren hacer hash antes.</p>

<h2>Paso a Paso con fotos reales</h2>
<ol>
<li><strong>Prepará la bolsa:</strong> usá bolsas filtrantes limpias. Para flor 90u-120u, para kief/hash 37u-73u.</li>
</ol>
<figure class="blog-figure"><img src="/static/images/blog/rosin-bolsa-vacia.png" alt="Bolsa filtrante vacía para rosin" loading="lazy"><figcaption>Bolsa filtrante vacía: el micraje define qué tan limpio sale el rosin.</figcaption></figure>
<ol start="2">
<li><strong>Cargá el material:</strong> llená sin apretar en exceso. Podés prensar flor molida suavemente o kief/hash bien seco.</li>
</ol>
<figure class="blog-figure"><img src="/static/images/blog/rosin-carga-flor.jpg" alt="Carga de flor en papel para prensar rosin" loading="lazy"><figcaption>Carga de flor: desarmada a mano, sin moler a polvo para no arrastrar clorofila.</figcaption></figure>
<figure class="blog-figure"><img src="/static/images/blog/rosin-carga-kief.webp" alt="Carga de kief hash para prensar rosin" loading="lazy"><figcaption>Carga de kief / hash: con este material lográs un rosin más claro y potente que con flor.</figcaption></figure>
<figure class="blog-figure"><img src="/static/images/blog/rosin-bolsa-flor.jpg" alt="Bolsa filtrante llena de flor lista para prensar" loading="lazy"><figcaption>Bolsa llena y cerrada, lista para envolver en papel manteca y prensar.</figcaption></figure>
<ol start="3">
<li><strong>Prensá:</strong> precalentá las placas, envolvé la bolsa en papel manteca, pre-prensá 10 segundos a baja presión y después subí progresivo hasta el máximo.</li>
</ol>
<figure class="blog-figure"><img src="/static/images/blog/rosin-prensa.jpg" alt="Prensa hidráulica prensando rosin" loading="lazy"><figcaption>Prensa hidráulica en acción: calor + presión hacen fluir la resina en 60-120 segundos.</figcaption></figure>
<ol start="4">
<li><strong>Recolectá:</strong> abrí el papel en caliente y recolectá en frío con dabber (1 min al freezer y se despega solo).</li>
</ol>
<figure class="blog-figure"><img src="/static/images/blog/rosin-papel-abierto.jpg" alt="Papel manteca abierto con rosin dorado recién prensado" loading="lazy"><figcaption>Papel abierto con rosin dorado recién prensado: bordes cristalinos y centro fluido, señal de buena temperatura.</figcaption></figure>
<figure class="blog-figure"><img src="/static/images/blog/rosin-recoleccion.webp" alt="Recolección de rosin con dabber" loading="lazy"><figcaption>Recolección con dabber: según cómo lo cures después, queda tipo sauce, budder o shatter.</figcaption></figure>

<h2>Qué Necesitás</h2>
<ul>
<li><strong>Prensa:</strong> placas calientes con control de temperatura. Las manuales sirven para empezar, las hidráulicas dan más rendimiento.</li>
<li><strong>Bolsas filtrantes:</strong> 90u-120u para flor, 37u-73u para hash/kief (doble bolsa para hash).</li>
<li><strong>Papel manteca antiadherente, guantes resistentes al calor y dabber.</strong></li>
<li><strong>Material con 55-62% humedad (solo para flor):</strong> si está muy seco, rinde la mitad. Hidratalo con sobres de humedad 24h antes. El hash/kief debe estar bien seco.</li>
</ul>

<h2>Temperaturas y Tiempos (guía base)</h2>
<ul>
<li><strong>Flor:</strong> 90-110°C, 60-120 segundos, presión progresiva.</li>
<li><strong>Kief / dry sift:</strong> 80-100°C, 60-90 segundos, bolsa de 37u.</li>
<li><strong>Bubble hash / Hash Rosin:</strong> 70-90°C, 45-75 segundos, doble bolsa de 37u.</li>
<li><strong>Live Rosin:</strong> 65-85°C, 45-70 segundos, presión baja y lenta para no volar terpenos.</li>
</ul>
<p>Menos temperatura = más sabor y color claro, menos rendimiento. Más temperatura = más rendimiento, color más oscuro.</p>

<h2>Los 8 factores que definen textura, color y terpenos</h2>
<p>¿Por qué a veces sale rubio y mantecoso y otras oscuro y aceitoso? Por estos factores:</p>
<ol>
<li><strong>1. Material de partida:</strong> el factor n°1. Flor = más grasas, ceras y clorofila = color más oscuro y textura más aceitosa. Hash/kief aislado = menos contaminantes = color claro y textura budder. Live (fresco congelado) = máxima retención de monoterpenos volátiles.</li>
<li><strong>2. Frescura, curado y oxidación:</strong> material viejo u oxidado sale oscuro y con sabor a hachís añejo. Flor fresca bien curada (2-4 semanas) o fresh frozen da colores dorados/rubios. El calor, la luz y el oxígeno degradan terpenos y oscurecen.</li>
<li><strong>3. Humedad:</strong> flor en 55-62% HR fluye bien y rinde. Muy seca (menos de 50%) = poco rendimiento, color oscuro y sabor a quemado. Muy húmeda = vapor, chisporroteo y textura inestable.</li>
<li><strong>4. Temperatura y tiempo:</strong> a más calor y más tiempo, más rendimiento pero se evaporan terpenos (sobre todo limoneno, mirceno, pineno), se descarboxila el THCA y el color se oscurece. Para preservar terpenos: baja temperatura + poco tiempo.</li>
<li><strong>5. Presión:</strong> debe ser progresiva. Si apretás de golpe en frío, revientan las bolsas y arrastrás materia vegetal (color verde/oscuro). Precalentado de 10s + subida lenta = rosin limpio.</li>
<li><strong>6. Micraje de la bolsa:</strong> micra más chica = más filtrado = más claro y puro, pero menos rendimiento. 90u-120u deja pasar más aceites (ideal flor), 37u retiene casi todo lo vegetal (ideal hash). Doble bolsa evita blowouts en hash.</li>
<li><strong>7. Genética:</strong> cada cepa tiene distinto perfil de tricomas y terpenos. Algunas lavan bien para hash/live (tricomas grandes que se sueltan fácil), otras rinden mejor como flower rosin. Cepas resinosas y frescas = colores claros y aromas intensos.</li>
<li><strong>8. Curado post-prensado y guardado:</strong> el rosin recién prensado es tipo shatter/sauce translúcido. Si lo batís y lo dejás 24-48h a 20°C en frasco cerrado (cold cure) se vuelve budder/badder cremoso y se intensifica el sabor. Con calor suave (40-50°C, warm cure) queda más tipo jam/sauce. Guardá siempre en frasco hermético, oscuro y frío: el calor y el aire lo oscurecen y le matan los terpenos en días.</li>
</ol>

<h2>Texturas: cómo lograr cada una</h2>
<ul>
<li><strong>Shatter / Sauce (vidrioso):</strong> rosin recién prensado de flor a temperatura media-alta, recolectado y guardado en frío sin batir. Translúcido y pegajoso.</li>
<li><strong>Budder / Badder (mantecoso):</strong> batí el rosin con el dabber e introducí aire, después cold cure 24-48h a 20°C. Es la textura más buscada en hash rosin y live rosin: color rubio opaco, fácil de manipular.</li>
<li><strong>Wax / Crumble (ceroso):</strong> prensadas a más temperatura o con material más seco/oxidado, más batido. Más seco y opaco.</li>
<li><strong>Jam / Sauce con diamantes:</strong> warm cure largo (semanas a 35-45°C) separa THCA cristalizado del aceite terpenoso. Solo recomendable con hash rosin de alta pureza.</li>
</ul>

<h2>Color y terpenos: la regla de oro</h2>
<ul>
<li><strong>Rubio claro / dorado:</strong> material fresco, hash de calidad, baja temperatura, buena humedad. = más terpenos preservados.</li>
<li><strong>Ámbar / marrón oscuro:</strong> material viejo, mucha temperatura/tiempo, flor muy seca o mucha presión de golpe. = menos terpenos, sabor más tostado.</li>
<li><strong>Verde:</strong> arrastraste clorofila (flor molida a polvo, bolsa rota o demasiada presión). Filtrá mejor y bajá la presión inicial.</li>
<li><strong>Para cuidar terpenos:</strong> prensá bajo (70-95°C), dabbeá/vaporizá a baja temperatura (160-200°C), y guardá el rosin en heladera en frasco hermético. El calor es el enemigo n°1 del sabor.</li>
</ul>

<h2>Trucos para Más Rendimiento</h2>
<ul>
<li>Prensá de a 3-5g por vez, no más.</li>
<li>Usá <em>bottle tech</em> (bolsa vertical) para flores: rinde 10-20% más.</li>
<li>Guardá el chip prensado para hacer comestibles: aún tiene cannabinoides.</li>
<li>Si el rendimiento es bajo, subí 5°C o hidratá la flor 24h: suele duplicar la vuelta.</li>
</ul>

<h2>Seguridad</h2>
<p>Las placas queman (100°C+). Usá guantes, no toques las placas y trabajá en superficie estable. Desenchufá al terminar.</p>

<p>Con prensa, bolsas de micraje, papeles y frascos estás listo para tu primera prensada.</p>
<p class="img-credit">Fotos de esta guía: material propio Perrone's INC.</p>""",
        'category': 'Extracciones',
        'tags': 'extraccion, rosin, prensa, flower rosin, hash rosin, live rosin, sin solventes',
        'published': True,
        'featured': True
    },
    {
        'title': 'Cultivo Outdoor en Argentina: Guía desde Semilla para Principiantes',
        'slug': 'guia-cultivo-outdoor-argentina-desde-semilla',
        'image': 'images/blog/outdoor-portada.jpg',
        'excerpt': 'Cómo cultivar en exterior en Argentina desde semilla: calendario mes a mes, germinación, sustrato, riego, plagas, floración y cosecha.',
        'content': """<h2>Por qué cultivar outdoor en Argentina</h2>
<p>El <strong>cultivo outdoor</strong> es la forma más barata y natural de empezar: el sol es gratis, las plantas crecen más grandes que en indoor y con pocos insumos podés sacar una buena cosecha al año. A cambio, dependés del <strong>clima, las plagas y el calendario</strong>. Esta guía principiante te lleva <strong>desde la semilla hasta el curado</strong>, adaptada al hemisferio sur.</p>
<p><strong>Ideal si:</strong> tenés patio, terraza, balcón con 6+ horas de sol directo o un campito seguro. Si solo tenés interior, mirá nuestra <a href="/blog/guia-completa-cultivo-indoor-principiantes">guía indoor</a>.</p>
<h2>Calendario outdoor Argentina (fotoperiódicas)</h2>
<p>En exterior mandan las horas de luz. Las variedades <strong>fotoperiódicas</strong> vegetan en primavera-verano y florecen cuando los días se acortan (febrero-marzo).</p>
<table>
<tr><td><strong>AGO - SEP</strong></td><td>Germinación y plantín adentro o en invernaderito. Cuidar del frío y heladas tardías.</td></tr>
<tr><td><strong>OCT</strong></td><td>Trasplante afuera cuando pasan las heladas. Empieza el crecimiento fuerte.</td></tr>
<tr><td><strong>NOV - ENE</strong></td><td>Vegetación: trasplantes, tutores, prevención de plagas.</td></tr>
<tr><td><strong>FEB</strong></td><td>Preflora: sexado, últimos trasplantes. Ojo con lluvias y hongos.</td></tr>
<tr><td><strong>MAR - ABR</strong></td><td>Floración y engorde. Menos nitrógeno, más fósforo/potasio.</td></tr>
<tr><td><strong>ABR - MAY</strong></td><td>Cosecha, secado y curado antes de la humedad del invierno.</td></tr>
</table>
<p><strong>Automáticas:</strong> no dependen del fotoperíodo. Se siembran de <strong>octubre a enero</strong> y se cosechan en 70-90 días. Podés hacer 2 tandas (ej: octubre y diciembre). Son más chicas pero más rápidas y discretas.</p>

<h2>1. Elegí dónde y qué sembrar</h2>
<h3>El lugar</h3>
<ul>
<li><strong>Sol:</strong> mínimo 6 horas de sol directo, ideal 8+. Más sol = más producción.</li>
<li><strong>Reparo:</strong> pared, media sombra o cerco contra viento fuerte y granizo.</li>
<li><strong>Agua:</strong> que puedas llevar agua fácil. Evitá charcos y zonas que se inundan.</li>
<li><strong>Discreción y seguridad:</strong> que no se vea desde la calle, olor en flora es fuerte. Ojo con mascotas y niños.</li>
</ul>
<h3>Fotoperiódica o automática</h3>
<ul>
<li><strong>Fotoperiódica (recomendada para 1 cosecha grande):</strong> plantas de 1,5-3 m, cosecha marzo-mayo. Necesitan toda la temporada.</li>
<li><strong>Automática (recomendada si empezás tarde o querés discreción):</strong> 50-100 cm, listas en 10-12 semanas desde germinación. Menos producción por planta, pero podés poner más.</li>
</ul>

<h2>2. Germinación paso a paso</h2>
<ol>
<li>Poné la semilla 12-24h en un vaso con agua a temperatura ambiente, en lugar oscuro.</li>
<li>Pasala a servilleta húmeda (no chorreando) entre dos platos, a 22-26°C. En 24-72h asoma la raíz.</li>
<li>Plantala a 1 cm de profundidad en maceta chica (0,5-1 L) con sustrato liviano, raíz hacia abajo.</li>
<li>Mantené húmedo con pulverizador, luz suave y 20-25°C. En 2-5 días sale el plantín.</li>
</ol>
<p><strong>Errores típicos:</strong> enterrar muy profundo, encharcar, usar tierra dura de jardín o ponerla al sol fuerte de golpe. Los primeros 10 días son los más delicados: mejor adentro junto a una ventana o bajo una lámpara barata.</p>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-germinacion.jpg" alt="Secuencia de germinación de semillas con raíz" loading="lazy"><figcaption>Paso 1 - Germinación: de semilla a raíz en 24-72h en servilleta húmeda a 22-26°C.</figcaption></figure>
<h2>3. Sustrato y macetas</h2>
<ul>
<li><strong>Sustrato base principiante:</strong> 40% turba o tierra negra zarandeada + 30% compost o humus de lombriz + 20% perlita + 10% vermiculita. Suelto, que drene pero retenga humedad.</li>
<li><strong>Macetas:</strong> arrancá en 1 L, pasá a 5-10 L y terminá en <strong>20-30 L</strong> (foto) o 50 L+ si querés planta grande. Más litros = más raíces = más cosecha. Las de tela (geotextil) airean mejor.</li>
<li><strong>Suelo directo:</strong> rinde más pero solo si la tierra es buena. Hacé un pozo de 50x50x50 cm y rellenalo con el sustrato de arriba.</li>
<li><strong>pH:</strong> en tierra, regá con pH 6.0-6.8. Si no medís nada, al menos usá agua reposada 24h y no abuses de fertilizantes.</li>
</ul>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-sustrato.jpg" alt="Manos sosteniendo sustrato aireado con perlita" loading="lazy"><figcaption>Sustrato ideal: suelto y aireado con perlita, que drene pero retenga humedad.</figcaption></figure>

<h2>4. Trasplantes y vegetación (oct-ene)</h2>
<ol>
<li>Trasplantá cuando las raíces asoman por abajo o la planta duplica la altura de la maceta. Regá antes para que el pan no se rompa.</li>
<li>Afuera definitivo recién cuando <strong>no haya más heladas</strong> (en Buenos Aires y centro: después de mediados de octubre). La primera semana, sol de mañana y reparo al mediodía para aclimatar.</li>
<li>Regá cuando los primeros 2-3 cm estén secos. Mejor poco y seguido que encharcar. En verano puede ser todos los días.</li>
<li>Poné <strong>tutor</strong> desde chica para aguantar viento y peso futuro.</li>
</ol>
<p>En vege la planta quiere <strong>nitrógeno</strong>. Con humus + compost al inicio tirás varias semanas sin fertilizar. Después sumá un fertilizante de crecimiento a mitad de dosis, 1-2 veces por semana.</p>
<figure class="blog-figure vertical"><img src="/static/images/blog/outdoor-plantin.jpg" alt="Plantín en maceta listo para trasplantar" loading="lazy" style="max-width:380px;"><figcaption>Plantín establecido en maceta chica: cuando duplica su altura o asoman raíces, es momento de trasplantar.</figcaption></figure>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-trasplante.jpg" alt="Trasplante de plantín a maceta más grande" loading="lazy"><figcaption>Trasplante: con el pan entero, a maceta más grande y riego suave para asentar.</figcaption></figure>

<h2>5. Podas: apical y FIM</h2>
<p>Las dos podas básicas para frenar la altura y sacar más puntas. Se hacen solo en <strong>vegetación</strong>, nunca en flora.</p>
<ul>
<li><strong>Apical:</strong> cuando la planta tiene 4-5 nudos, cortá limpio el brote principal por encima del nudo con tijera desinfectada. La planta reparte energía en 2 ramas principales. Resultado: planta más baja, ancha y con 2 puntas fuertes. Ideal para terrazas y discreción. Recuperación: 7-10 días.</li>
<li><strong>FIM (te pifiaste a propósito):</strong> en el mismo punto, en vez de cortar todo cortá solo el 70-80% del brote nuevo (pellizco con uñas o tijera). Salen 3-4 brotes en vez de 2, con menos freno de crecimiento. Es menos prolija que la apical pero da más puntas. Si sale mal, igual funciona como apical.</li>
<li><strong>Limpieza de bajos:</strong> sacá hojas que tocan la tierra y ramitas enanas que no llegan a la luz. Mejora aireación y previene hongos.</li>
</ul>
<p><strong>Apical vs FIM:</strong> apical = 2 puntas parejas y estructura simétrica; FIM = 3-4 puntas, más volumen pero más desparejo. Principiante: empezá con apical, cuando le agarres la mano probá FIM en otra planta y compará. Una poda por vez, tijera limpia y 7-10 días de recupero.</p>

<h2>6. Técnicas de cultivo: SCROG, LST y Supercrop</h2>
<p>Ya no cortás: <strong>moldeás</strong> la planta para que le entre sol parejo y banque el peso. Acá van de menor a mayor dificultad.</p>
<ul>
<li><strong>LST (Low Stress Training / atado - fácil):</strong> doblá suavemente las ramas principales y atalas al borde de la maceta o a tutores con hilo blando. Abrís el centro al sol sin cortar nada. Se hace durante toda la vege, ajustando los atados cada semana. Ideal principiantes: cero riesgo si no quebrás.</li>
<li><strong>SCROG (red - intermedio):</strong> colocá una red o malla 10-20 cm por encima de la maceta cuando la planta mide 25-30 cm. A medida que crece, pasá las puntas por los cuadrantes para formar un plano parejo. En outdoor sostiene contra el viento y multiplica los puntos de floración. Instalala en diciembre-enero y dejá de entrelazar cuando arranque la flora.</li>
<li><strong>Supercrop (avanzado):</strong> con la planta en vege fuerte, pellizcá un tallo verde entre pulgar e índice hasta ablandar las fibras internas y doblalo 90° sin romper la piel. Se forma un nudo que engorda y pasa más savia. Solo 1-2 ramas por vez, nunca en flora ni en tallos leñosos. Si se quiebra, encintá con cinta aislante y bancala con tutor: se recupera.</li>
</ul>
<p>Combinación típica outdoor: <strong>apical + LST + red</strong>. El supercrop dejalo para tu segunda temporada o para domar una planta que se te fue muy alta.</p>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-vegetacion.jpg" alt="Cultivo outdoor en vegetación con red scrog en patio" loading="lazy"><figcaption>SCROG outdoor: red para abrir la planta al sol, mejorar aireación y bancar el peso de los cogollos.</figcaption></figure>

<h2>7. Plagas y clima: lo que mata cosechas afuera</h2>
<ul>
<li><strong>Preventivo cada 10-15 días en vege:</strong> jabón potásico + aceite de neem. Revisá el envés de las hojas.</li>
<li><strong>Hormigas, pulgones y trips:</strong> tierra de diatomeas en superficie, trampas amarillas, y si aparece plaga, repetí aplicación 3 veces cada 5 días.</li>
<li><strong>Oidio y hongos (feb-abr):</strong> el enemigo de la flora. Separá plantas para que corra aire, sacá hojas muy juntas, evitá mojar los cogollos al regar. Si llueve varios días, sacudí las plantas y si podés poné techo transparente.</li>
<li><strong>Orugas en cogollos:</strong> revisá en marzo-abril. Sacalas a mano y usá Bacillus thuringiensis en vege/preflora.</li>
<li><strong>Granizo / tormenta:</strong> media sombra o malla antigranizo arriba vale oro. Después de tormenta, atar ramas quebradas y quitar barro.</li>
</ul>
<p>En flora <strong>no pulverices los cogollos</strong> con nada que no sea específico y seguro. Cortá lo afectado antes de que se expanda.</p>
<h2>8. Preflora y sexado (febrero)</h2>
<p>Cuando los días se acortan aparecen los primeros pelos (hembra) o bolitas (macho). Si plantaste regulares, <strong>cortá los machos ya</strong> o te llenan todo de semillas. Si son feminizadas o autos, solo confirmá que sean hembras y seguí.</p>
<p>Es el último momento para trasplantar y poner tutores firmes: en flora duplican o triplican el tamaño.</p>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-preflor.jpg" alt="Preflor femenina con pelos blancos" loading="lazy"><figcaption>Sexado: preflor femenina con pelitos blancos. Si ves bolitas en vez de pelos, es macho y se corta.</figcaption></figure>

<h2>9. Floración y engorde (mar-abr)</h2>
<ul>
<li>Bajá el nitrógeno y subí <strong>fósforo y potasio</strong> (fertilizante de flora) + melaza o compost tea 1 vez por semana.</li>
<li>Regá a la mañana, sin mojar flores. En maceta grande, riegos profundos espaciados rinden más que poquito todos los días.</li>
<li>Ojo con la <strong>humedad</strong>: si hay rocío fuerte o lluvias, ventilá, separá ramas y cosechá por partes si hace falta.</li>
<li><strong>Cuándo cortar:</strong> mirá tricomas con lupa 60x. Mayoría lechosos + 10-20% ámbar = punto ideal (efecto equilibrado). Todos transparentes = muy temprano. Todo ámbar = efecto más sedante y menos aroma.</li>
</ul>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-floracion.jpg" alt="Plantas outdoor en plena floración" loading="lazy"><figcaption>Floración outdoor: cogollos engordando en marzo-abril. Acá se define la cosecha: fósforo, potasio y control de hongos.</figcaption></figure>

<h2>10. Cosecha, secado y curado</h2>
<ol>
<li>Cortá a la mañana temprano, rama por rama. Hacé una manicura gruesa (sacá hojas grandes) y colgá en lugar oscuro, 18-22°C y 50-60% humedad, con aire suave sin darles directo.</li>
<li>En 7-14 días las ramitas crujen: pasá a frascos llenos 3/4, abrí 10 min por día la primera semana (curado).</li>
<li>Curá mínimo 2-4 semanas. Ahí aparece el sabor y la potencia real. Guardá en frasco hermético, oscuro y fresco.</li>
</ol>
<p>Secar mal arruina meses de trabajo: no seques al sol ni con calor directo, y no enfrasques húmedo (hongo seguro).</p>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-secado.jpg" alt="Cogollos colgados secándose en interior oscuro" loading="lazy"><figcaption>Secado: ramas colgadas en lugar oscuro y ventilado 7-14 días, hasta que las ramitas crujen.</figcaption></figure>
<figure class="blog-figure"><img src="/static/images/blog/outdoor-curado.jpg" alt="Frascos de vidrio con cogollos curados" loading="lazy"><figcaption>Curado: en frascos 3/4 llenos, 2-4 semanas mínimo. Ahí aparece el sabor y la potencia real.</figcaption></figure>

<h2>Errores de principiante que más vemos</h2>
<ol>
<li><strong>Sembrar muy tarde</strong> una foto en enero y pretender planta grande: sale chica y flora enana.</li>
<li><strong>Maceta chica todo el ciclo:</strong> en 5 L no hay milagro. Mínimo 20 L para foto outdoor.</li>
<li><strong>Regar todos los días por rutina:</strong> meté el dedo, si está húmedo esperá.</li>
<li><strong>Sobrefertilizar:</strong> puntas quemadas = te pasaste. Lavá con agua y retomá a mitad de dosis.</li>
<li><strong>No prevenir plagas</strong> hasta que es tarde, sobre todo en febrero-marzo.</li>
<li><strong>Cosechar antes por ansiedad</strong> o dejar pasar las lluvias de mayo y perder todo por hongo.</li>
</ol>

<h2>Checklist rápido por mes</h2>
<ul>
<li><strong>AGO-SEP:</strong> compro sustrato, macetas, neem + jabón potásico. Germino adentro.</li>
<li><strong>OCT:</strong> trasplante afuera, tutor, primer preventivo.</li>
<li><strong>NOV-ENE:</strong> riego, trasplantes, apical/LST, preventivos.</li>
<li><strong>FEB:</strong> sexado, tutores finales, cambio a flora.</li>
<li><strong>MAR-ABR:</strong> engorde, control hongos, lupa para corte.</li>
<li><strong>ABR-MAY:</strong> cosecha escalonada, secado y curado.</li>
</ul>

<p>Con sustrato, macetas geotextil, micorrizas, neem, jabón potásico, fertilizantes vege/flora y lupa ya tenés el kit outdoor completo.</p>
<p class="img-credit">Fotos de esta guía: material propio Perrone's INC.</p>""",
        'category': 'Cultivo',
        'tags': 'cultivo, outdoor, exterior, argentina, calendario, semilla, principiantes',
        'published': True,
        'featured': True
    },
    {
        'title': 'pH y EC en Cannabis: Cómo Medir y Corregir Paso a Paso',
        'slug': 'medicion-ph-ec-cultivo-cannabis',
        'image': 'images/blog/phec-medidor-ec.jpg',
        'excerpt': 'Guía de pH y EC en cannabis: rangos ideales en tierra, coco e hidro, tabla por etapa, cómo medir, calibrar y corregir excesos o carencias.',
        'content': """<h2>pH y EC: las dos mediciones que definen tu cosecha</h2>
<p>Podés tener la mejor genética, el mejor sustrato y los mejores fertilizantes: si el <strong>pH</strong> está mal, la planta <strong>no absorbe</strong> los nutrientes (bloqueo), y si la <strong>EC</strong> está mal, la planta se <strong>quema o pasa hambre</strong>. Medir pH y EC es lo que separa un cultivo flojo de uno profesional, y solo necesitás un medidor barato y 2 minutos por riego.</p>
<ul>
<li><strong>pH:</strong> qué tan ácido o alcalino está el agua/riego. Define QUÉ nutrientes puede absorber la raíz.</li>
<li><strong>EC (electroconductividad):</strong> cuántas sales disueltas hay. Define CUÁNTO come la planta.</li>
</ul>

<h2>Por qué es importante medir (y qué pasa si no lo hacés)</h2>
<p>La planta no come lo que le das: come <strong>lo que puede absorber</strong>. El pH es la llave y la EC es la cantidad. Si no medís, estás cultivando a ciegas:</p>
<ul>
<li><strong>Bloqueo de nutrientes:</strong> con pH fuera de rango las raíces no absorben aunque el fertilizante esté ahí. Ves carencias, agregás más producto, y el problema empeora: gastás plata y estresás la planta.</li>
<li><strong>Cosecha chica y floja:</strong> una EC mal llevada achica la producción y baja la resina. Dos plantas iguales con distinta EC rinden distinto: la bien medida produce más y mejores cogollos.</li>
<li><strong>Problemas que parecen otra cosa:</strong> el 80% de las "plagas", "hongos" o "genética mala" son en realidad pH o EC mal. Medir te ahorra semanas de diagnósticos errados.</li>
<li><strong>Raíces sanas:</strong> sales acumuladas (EC alta en sustrato) queman raíces y frenan todo. Solo el drenaje medido te avisa antes de que sea tarde.</li>
<li><strong>Ahorro real:</strong> fertilizás justo lo necesario, ni de más (quemás y tirás producto) ni de menos (la planta rinde poco).</li>
</ul>
<p>En corto: <strong>medir pH y EC es lo más barato que podés hacer por tu cosecha</strong>. Un medidor se paga solo con lo que ahorrás en fertilizantes y en la primera cosecha que no perdés.</p>

<h2>Rangos de pH por etapa: no hay un único ideal</h2>
<p>El error más común es buscar <strong>un</strong> pH perfecto y clavarlo siempre. La planta necesita <strong>distintos nutrientes en cada etapa</strong>, y cada nutriente se absorbe mejor a distinto pH (mirá la tabla de la foto). La técnica correcta es <strong>moverte dentro del rango</strong> según la etapa, e incluso variar un poco riego a riego para barrer toda la ventana de absorción.</p>
<table>
<tr><td><strong>Tierra - plantín / vege temprana</strong></td><td><strong>6.0 - 6.3</strong> (nitrógeno y micros a full)</td></tr>
<tr><td><strong>Tierra - vegetación plena</strong></td><td><strong>6.2 - 6.5</strong></td></tr>
<tr><td><strong>Tierra - flora / engorde</strong></td><td><strong>6.3 - 6.8</strong> (fósforo, potasio y calcio entran mejor arriba)</td></tr>
<tr><td><strong>Coco - vege</strong></td><td><strong>5.5 - 5.9</strong></td></tr>
<tr><td><strong>Coco - flora</strong></td><td><strong>5.8 - 6.2</strong></td></tr>
<tr><td><strong>Hidro - vege</strong></td><td><strong>5.5 - 5.8</strong></td></tr>
<tr><td><strong>Hidro - flora</strong></td><td><strong>5.7 - 6.1</strong></td></tr>
</table>
<p>Tip de cultivador: si regás siempre a 6.3 clavado, los nutrientes de los extremos (hierro abajo, molibdeno arriba) entran a medias. Alterná, por ejemplo, 6.1 - 6.4 - 6.6 durante la semana y cubrís todo el espectro.</p>
<p>Fuera de rango aparecen carencias <strong>aunque fertilices bien</strong>: con pH alto se bloquean hierro, zinc y manganeso (hojas amarillas con nervaduras verdes); con pH bajo se bloquean calcio y magnesio y se libera aluminio tóxico.</p>
<figure class="blog-figure"><img src="/static/images/blog/phec-tabla-ph.jpg" alt="Tabla de absorción de nutrientes según el pH" loading="lazy"><figcaption>Cómo el pH afecta la absorción: cada nutriente tiene su ventana. Por eso el rango 6.0-6.8 en tierra cubre casi todo.</figcaption></figure>

<h2>Tabla de EC por etapa (mS/cm)</h2>
<table>
<tr><td><strong>Plantín / esqueje</strong></td><td>0.3 - 0.6 (casi solo agua)</td></tr>
<tr><td><strong>Vegetación temprana</strong></td><td>0.8 - 1.2</td></tr>
<tr><td><strong>Vegetación plena</strong></td><td>1.2 - 1.6</td></tr>
<tr><td><strong>Preflora</strong></td><td>1.6 - 1.8</td></tr>
<tr><td><strong>Floración / engorde</strong></td><td>1.8 - 2.2 (algunas genéticas hasta 2.4)</td></tr>
<tr><td><strong>Lavado final (últimas 1-2 semanas)</strong></td><td>0.0 - 0.4 (solo agua con pH correcto)</td></tr>
</table>
<p>Medí siempre la EC <strong>del agua base primero</strong> y restala: si tu agua de red ya trae 0.7, tenés menos margen para fertilizante. En Argentina el agua corriente suele estar entre 0.3 y 0.8 según la zona: si supera 0.8, conviene mezclar con agua de lluvia, destilada u ósmosis.</p>

<h2>Cómo medir paso a paso</h2>
<ol>
<li><strong>Calibrá el medidor:</strong> 1 vez por mes con solución buffer (pH 7.0 y 4.0). Un medidor descalibrado miente y es peor que no medir.</li>
<li><strong>Prepará el riego:</strong> agua + fertilizantes, mezclá bien y esperá 2 minutos.</li>
<li><strong>Medí EC primero:</strong> si está alta, agregá agua; si está baja, sumá fertilizante de a poco.</li>
<li><strong>Medí pH después</strong> (los fertilizantes lo cambian) y corregí gota a gota.</li>
<li><strong>Regá y medí el drenaje</strong> cada tanto: si la EC del drenaje sale mucho más alta que la de entrada, hay acumulación de sales: regá solo con agua + pH en el próximo riego.</li>
</ol>
<figure class="blog-figure vertical"><img src="/static/images/blog/phec-medidor-ph.jpg" alt="Medidor digital de pH en vaso con agua" loading="lazy" style="max-width:380px;"><figcaption>Medidor digital de pH: sumergí el electrodo, esperá la lectura estable y enjuagá después de cada uso.</figcaption></figure>

<h2>Cómo corregir el pH</h2>
<ul>
<li><strong>Para bajarlo (lo más común):</strong> gotas de corrector pH- (ácido fosfórico) o unas gotas de limón/vinagre en emergencia. De a poco: 1 gota por litro, mezclá y volvé a medir.</li>
<li><strong>Para subirlo:</strong> corrector pH+ (potasa) o una pizca de bicarbonato. También de a poco.</li>
<li><strong>Nunca mezcles correctores</strong> ni corrijas de golpe más de 1 punto: los cambios bruscos estresan las raíces.</li>
</ul>

<h2>Síntomas: ¿EC alta o pH mal?</h2>
<ul>
<li><strong>EC alta (sobrefertilización):</strong> puntas de hojas quemadas/marrón que avanzan hacia adentro, hojas en garra hacia abajo, crecimiento frenado. Solución: lavar con el triple de agua con pH correcto y retomar a mitad de dosis.</li>
<li><strong>EC baja (hambre):</strong> amarilleo parejo desde abajo, tallos finos, poco crecimiento. Solución: subir la dosis gradualmente.</li>
<li><strong>pH fuera de rango:</strong> manchas, amarilleo entre nervaduras, hojas retorcidas <strong>aunque la EC esté bien</strong>. Solución: corregir el pH del riego, no agregar más fertilizante.</li>
</ul>
<p>Regla de oro: <strong>ante un problema, medí pH y EC antes de agregar nada</strong>. El 80% de las "carencias" son bloqueos por pH.</p>

<h2>Errores comunes</h2>
<ol>
<li><strong>Medir solo al principio y nunca calibrar:</strong> el medidor se descalibra y todo lo que medís es mentira.</li>
<li><strong>Corregir pH antes de agregar fertilizantes:</strong> se mide y corrige siempre AL FINAL, con todo mezclado.</li>
<li><strong>Regar con agua de red sin medir:</strong> cloro alto y EC alta queman plantines. Dejá reposar el agua 24h.</li>
<li><strong>Confundir EC alta con falta de comida</strong> y agregar más fertilizante arriba del bloqueo.</li>
<li><strong>No medir el drenaje nunca:</strong> es tu radiografía de lo que pasa en la maceta.</li>
</ol>

<h2>Kit mínimo recomendado</h2>
<ul>
<li>Medidor digital de pH + solución de calibración y guardado.</li>
<li>Medidor de EC (muchos vienen combo pH/EC).</li>
<li>Corrector pH- y pH+.</li>
<li>Vaso medidor y anotador: registrá pH/EC de entrada y drenaje, vas a detectar problemas antes de verlos.</li>
</ul>
<figure class="blog-figure vertical"><img src="/static/images/blog/phec-medidor-ec.jpg" alt="Medidor digital 3 en 1 de TDS, EC y temperatura" loading="lazy" style="max-width:380px;"><figcaption>Medidor 3 en 1 (TDS/EC/temperatura): ideal para controlar las sales del riego y del drenaje.</figcaption></figure>

<p>Con medidor, calibradores y correctores ya podés medir y corregir como un profesional.</p>""",
        'category': 'Cultivo',
        'tags': 'ph, ec, medicion, nutrientes, cultivo, cannabis, fertilizacion',
        'published': True,
        'featured': True
    }
]


for _p in blog_posts_data:
    _p.setdefault('author', 'Tomás Perrone')

MANAGED_BLOG_SLUGS = [
    'extraccion-prensa-rosin-casera',
    'guia-cultivo-outdoor-argentina-desde-semilla',
]


def sync_managed_posts():
    """Crea o actualiza los posts gestionados por código (por slug).

    Se ejecuta en cada arranque para que los deploys actualicen
    el contenido aunque la base ya tenga datos.
    """
    n_new = n_upd = 0
    for post_data in blog_posts_data:
        if post_data['slug'] not in MANAGED_BLOG_SLUGS:
            continue
        post = BlogPost.query.filter_by(slug=post_data['slug']).first()
        if post:
            for k, v in post_data.items():
                setattr(post, k, v)
            n_upd += 1
        else:
            db.session.add(BlogPost(**post_data))
            n_new += 1
    db.session.commit()
    if n_new or n_upd:
        print(f"Posts sincronizados: {n_new} nuevos, {n_upd} actualizados.")


def seed():
    db.create_all()

    sync_managed_posts()

    if Category.query.first():
        print("La base de datos ya tiene datos. Ejecutá 'drop all' si querés reseedear.")
        return

    for cat_data in categories_data:
        cat = Category(**cat_data)
        db.session.add(cat)
    db.session.commit()
    print(f"Categorías creadas: {len(categories_data)}")

    cat_map = {c.slug: c.id for c in Category.query.all()}

    for prod_data in products_data:
        category_slug = prod_data.pop('category')
        product = Product(**prod_data, category_id=cat_map[category_slug])
        db.session.add(product)
    db.session.commit()
    print(f"Productos creados: {len(products_data)}")

    for post_data in blog_posts_data:
        if post_data['slug'] in MANAGED_BLOG_SLUGS:
            continue  # ya sincronizados arriba
        post = BlogPost(**post_data)
        db.session.add(post)
    db.session.commit()
    print(f"Artículos de blog creados: {len(blog_posts_data)}")

    _seed_candy()

    print("Base de datos poblada exitosamente!")


REMOVED_CANDY = [
    'atsq-cenicero-vidrio-2',
    'cat-magiclick-turbo-goma-xhd58-black',
    'cat-magiclick-turbo-goma-xhd58-color',
    'cat-magiclick-turbo-solid',
    'encendedor-bencina-chalas',
    'filtros-stamps-slim-6x15mm-x-50u-pocket-black',
    'tq420-slider-rick-morty-20x18cm',
]

FEATURED_CANDY = [
    'lion-circus-banana-freak-33h',
    'tips-carton-raw-x-50-original',
    'migy08-bong-pyb-plastico-20cm',
    '3rayos-pipa-aluminio-lucky-rojo',
    'et001-encendedor-tactil-blunt-rey',
    'lion-hemp-wrap-x2-strawberry',
    'bandeja-raw-mini-girl-12-5-x-18cm',
    'vaporizador-escritorio-arizer-extreme-q',
]


def _seed_candy():
    import json
    import re

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'candy_products.json')
    if not os.path.exists(path):
        return
    if Product.query.filter(Product.image.like('images/candy/%')).first():
        return

    def slugify(text):
        text = text.lower().strip()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[\s_]+', '-', text)
        return re.sub(r'-+', '-', text)[:150].strip('-')

    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    cat_ids = {c.slug: c.id for c in Category.query.all()}
    for slug, (name, desc) in data['categories'].items():
        if slug not in cat_ids:
            cat = Category(name=name, slug=slug, description=desc)
            db.session.add(cat)
            db.session.flush()
            cat_ids[slug] = cat.id

    existing = {p.name for p in Product.query.with_entities(Product.name).all()}
    slugs = {p.slug for p in Product.query.with_entities(Product.slug).all()}
    imgdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'images', 'candy')
    n = 0
    for it in data['items']:
        if it['name'] in existing:
            continue
        slug = (slugify(it['slug']) or f"candy-{it['candy_id']}")[:150]
        base, k = slug, 2
        while base in slugs:
            base = f'{slug}-{k}'
            k += 1
        slug = base
        slugs.add(slug)
        if slug in REMOVED_CANDY:
            continue
        units = it['units'] or 1
        price = max(100, round((it['cost'] / units * 2) / 10) * 10)
        box = f"Display x {it['units']}" if it['units'] else 'Unidad'
        desc = it['desc'] or it['name']
        if it['brand']:
            desc += f"\nMarca: {it['brand']}."
        desc += f' Venta por unidad ({box}).'
        img = f'images/candy/{slug}.jpg'
        if not os.path.exists(os.path.join(imgdir, slug + '.jpg')):
            img = None
        db.session.add(Product(
            name=it['name'],
            slug=slug,
            description=desc[:2000],
            short_description=f'Por unidad · {box}'[:300],
            price=price,
            stock=20 if it['stock'] else 0,
            category_id=cat_ids[it['cat']],
            featured=slug in FEATURED_CANDY,
            active=True,
            image=img,
        ))
        n += 1
    db.session.commit()
    print(f"Productos CandyClub creados: {n}")


if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed()

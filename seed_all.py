import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novamc.settings")
django.setup()

from shop.models import ServerMode, Category, Product

# ===========================================================================
# SERVERLAR
# ===========================================================================

anarxiya1, _ = ServerMode.objects.get_or_create(
    slug='anarxiya1',
    defaults={'name': 'Anarxiya1', 'order': 1, 'is_active': True}
)
anarxiya1.name = 'Anarxiya1'; anarxiya1.order = 1; anarxiya1.save()

smp, _ = ServerMode.objects.get_or_create(
    slug='smp',
    defaults={'name': 'SMP', 'order': 2, 'is_active': True}
)
smp.name = 'SMP'; smp.order = 2; smp.save()

duels, _ = ServerMode.objects.get_or_create(
    slug='duels',
    defaults={'name': 'Duels', 'order': 3, 'is_active': True}
)
duels.name = 'Duels'; duels.order = 3; duels.save()

print("Serverlar tayyor: Anarxiya1, SMP, Duels.")

# ===========================================================================
# ANARXIYA 1 — DONATOR RANKLAR
# ===========================================================================
a1_donator, _ = Category.objects.get_or_create(
    slug='anarxiya1-donator-ranklar',
    defaults={'name': 'Donator Ranklar', 'server': anarxiya1, 'order': 1}
)
a1_donator.server = anarxiya1; a1_donator.order = 1; a1_donator.save()

a1_ranks = [
    {
        'slug': 'anarxiya1-rabbit',
        'name': 'RABBIT',
        'price': 29000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus RABBIT to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x3.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'slug': 'anarxiya1-tiger',
        'name': 'TIGER',
        'price': 69000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus TIGER to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'slug': 'anarxiya1-hydra',
        'name': 'HYDRA',
        'price': 119000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus HYDRA to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x4.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'slug': 'anarxiya1-d-helper',
        'name': 'D.HELPER',
        'price': 139000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus D.HELPER to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'slug': 'anarxiya1-god',
        'name': 'GOD',
        'price': 259000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus GOD to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'slug': 'anarxiya1-pegas',
        'name': 'PEGAS',
        'price': 329000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus PEGAS to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'slug': 'anarxiya1-purple-cash',
        'name': 'PURPLE / CASH',
        'price': 399000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus CASH to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
]

print("\n--- Anarxiya1 Donator Ranklar ---")
for r in a1_ranks:
    obj, created = Product.objects.update_or_create(
        slug=r['slug'],
        defaults={
            'name': r['name'], 'category': a1_donator,
            'price': r['price'], 'commands': r['commands'],
            'features': r['features'], 'is_active': True,
        }
    )
    print(f"  {'[+]' if created else '[~]'} {obj.name} — {obj.price:,} UZS")

# ===========================================================================
# SMP — DONATOR RANKLAR
# ===========================================================================
smp_donator, _ = Category.objects.get_or_create(
    slug='smp-donator-ranklar',
    defaults={'name': 'Donator Ranklar', 'server': smp, 'order': 1}
)
smp_donator.server = smp; smp_donator.order = 1; smp_donator.save()

smp_ranks = [
    {
        'slug': 'smp-prime',
        'name': 'PRIME',
        'price': 49000,
        'commands': '/kit prime',
        'features': (
            'PRIME to‘plami – /kit prime\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
]

print("\n--- SMP Donator Ranklar ---")
for r in smp_ranks:
    obj, created = Product.objects.update_or_create(
        slug=r['slug'],
        defaults={
            'name': r['name'], 'category': smp_donator,
            'price': r['price'], 'commands': r['commands'],
            'features': r['features'], 'is_active': True,
        }
    )
    print(f"  {'[+]' if created else '[~]'} {obj.name} — {obj.price:,} UZS")

# ===========================================================================
# DUELS — DONATOR RANKLAR
# ===========================================================================
duels_donator, _ = Category.objects.get_or_create(
    slug='duels-donator-ranklar',
    defaults={'name': 'Donator Ranklar', 'server': duels, 'order': 1}
)
duels_donator.server = duels; duels_donator.order = 1; duels_donator.save()

duels_ranks = [
    {
        'slug': 'duels-king',
        'name': '👑 King',
        'price': 19000,
        'commands': '/store king',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat'
        ),
    },
    {
        'slug': 'duels-lion',
        'name': '🦁 Lion',
        'price': 35000,
        'commands': '/store lion',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol'
        ),
    },
    {
        'slug': 'duels-hero',
        'name': '🛡️ Hero',
        'price': 55000,
        'commands': '/store hero',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol\n'
            'Shaxsiy arenaga ruxsat\n'
            'Party duellarga ruxsat\n'
            'Bezakli (trim) zirhlarga ruxsat'
        ),
    },
    {
        'slug': 'duels-legend',
        'name': '⭐ Legend',
        'price': 75000,
        'commands': '/store legend',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol\n'
            'Shaxsiy arenaga ruxsat\n'
            'Party duellarga ruxsat\n'
            'Bezakli (trim) zirhlarga ruxsat\n'
            'Lobbida uchishga ruxsat'
        ),
    },
    {
        'slug': 'duels-master',
        'name': '⚡ Master',
        'price': 99000,
        'commands': '/store master',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol\n'
            'Jamoa yaratishga ruxsat\n'
            'Party duellarga ruxsat\n'
            'Bezakli (trim) zirhlarga ruxsat\n'
            'Lobbida uchishga ruxsat'
        ),
    },
]

print("\n--- Duels Donator Ranklar ---")
for r in duels_ranks:
    obj, created = Product.objects.update_or_create(
        slug=r['slug'],
        defaults={
            'name': r['name'], 'category': duels_donator,
            'price': r['price'], 'commands': r['commands'],
            'features': r['features'], 'is_active': True,
        }
    )
    print(f"  {'[+]' if created else '[~]'} {obj.name} — {obj.price:,} UZS")

# ===========================================================================
# BARCHA SERVERLAR — MA'MURIYAT VA MAXSUS + BOSHQA NARSALAR
# ===========================================================================
mamuriyat_products = [
    {
        'name': 'Homiy', 'price': 200000,
        'commands': '/titul\n/uc menu',
        'features': "Homiy rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu\nServer homiysi sifatida tanilish",
    },
    {
        'name': 'Admin', 'price': 150000,
        'commands': '/titul\n/uc menu',
        'features': "Admin rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu",
    },
    {
        'name': 'Moder', 'price': 100000,
        'commands': '/titul\n/uc menu',
        'features': "Moder rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu",
    },
    {
        'name': 'Helper', 'price': 50000,
        'commands': '/titul\n/uc menu',
        'features': "Helper rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu",
    },
]

boshqa_products = [
    {
        'name': 'Donate Case', 'price': 10000,
        'commands': '', 'features': "Donate Case - maxsus sovrinlar bilan quti",
    },
    {
        'name': 'Token Case', 'price': 5000,
        'commands': '', 'features': "Token Case - tokenlar bilan quti",
    },
    {
        'name': 'Maxsus Titul', 'price': 5000,
        'commands': '/titul', 'features': "Maxsus unikal titul - /titul",
    },
    {
        'name': 'Narsani nusxalash', 'price': 5000,
        'commands': '', 'features': "Qolinizdagi buyumni nusxalash xizmati",
    },
    {
        'name': '1000 Token', 'price': 1000,
        'commands': '', 'features': "1000 ta server tokeni",
    },
]

for server in [anarxiya1, smp, duels]:
    s = server.slug
    print(f"\n--- {server.name} Ma'muriyat va Boshqa ---")

    mcat, _ = Category.objects.get_or_create(
        slug=s + '-mamuriyat-va-maxsus',
        defaults={'name': "Ma'muriyat va Maxsus", 'server': server, 'order': 2}
    )
    mcat.server = server; mcat.save()

    for p in mamuriyat_products:
        obj, created = Product.objects.update_or_create(
            slug=s + '-' + p['name'].lower().replace(' ', '-'),
            defaults={
                'name': p['name'], 'category': mcat,
                'price': p['price'], 'commands': p['commands'],
                'features': p['features'], 'is_active': True,
            }
        )
        print(f"  {'[+]' if created else '[~]'} {obj.name}")

    bcat, _ = Category.objects.get_or_create(
        slug=s + '-boshqa-narsalar',
        defaults={'name': 'Boshqa Narsalar', 'server': server, 'order': 3}
    )
    bcat.server = server; bcat.save()

    for p in boshqa_products:
        obj, created = Product.objects.update_or_create(
            slug=s + '-' + p['name'].lower().replace(' ', '-'),
            defaults={
                'name': p['name'], 'category': bcat,
                'price': p['price'], 'commands': p['commands'],
                'features': p['features'], 'is_active': True,
            }
        )
        print(f"  {'[+]' if created else '[~]'} {obj.name}")

print("\n===== HAMMASI TAYYOR! =====")

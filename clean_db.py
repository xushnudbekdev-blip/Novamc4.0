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

# Reset DB categories and products cleanly
Product.objects.all().delete()
Category.objects.all().delete()
ServerMode.objects.all().delete()

# Recreate Servers
anarxiya1 = ServerMode.objects.create(name='Anarxiya1', slug='anarxiya1', order=1, is_active=True)
smp = ServerMode.objects.create(name='SMP', slug='smp', order=2, is_active=True)
duels = ServerMode.objects.create(name='Duels', slug='duels', order=3, is_active=True)

# 1. ANARXIYA1
c_a1_donator = Category.objects.create(name='Donator Ranklar', slug='anarxiya1-donator-ranklar', server=anarxiya1, order=1)
c_a1_admin = Category.objects.create(name="Ma'muriyat va Maxsus", slug='anarxiya1-mamuriyat-va-maxsus', server=anarxiya1, order=2)
c_a1_other = Category.objects.create(name='Boshqa Narsalar', slug='anarxiya1-boshqa-narsalar', server=anarxiya1, order=3)

a1_ranks = [
    {
        'name': 'RABBIT',
        'slug': 'anarxiya1-rabbit',
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
        'name': 'TIGER',
        'slug': 'anarxiya1-tiger',
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
        'name': 'HYDRA',
        'slug': 'anarxiya1-hydra',
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
        'name': 'D.HELPER',
        'slug': 'anarxiya1-d-helper',
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
        'name': 'GOD',
        'slug': 'anarxiya1-god',
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
        'name': 'PEGAS',
        'slug': 'anarxiya1-pegas',
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
        'name': 'PURPLE / CASH',
        'slug': 'anarxiya1-purple-cash',
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
for r in a1_ranks:
    Product.objects.create(name=r['name'], slug=r['slug'], category=c_a1_donator, price=r['price'], commands=r['commands'], features=r['features'], is_active=True)

# 2. SMP
c_smp_donator = Category.objects.create(name='Donator Ranklar', slug='smp-donator-ranklar', server=smp, order=1)
c_smp_admin = Category.objects.create(name="Ma'muriyat va Maxsus", slug='smp-mamuriyat-va-maxsus', server=smp, order=2)
c_smp_other = Category.objects.create(name='Boshqa Narsalar', slug='smp-boshqa-narsalar', server=smp, order=3)

smp_ranks = [
    {
        'name': 'PRIME',
        'slug': 'smp-prime',
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
for r in smp_ranks:
    Product.objects.create(name=r['name'], slug=r['slug'], category=c_smp_donator, price=r['price'], commands=r['commands'], features=r['features'], is_active=True)

# 3. DUELS
c_duels_donator = Category.objects.create(name='Donator Ranklar', slug='duels-donator-ranklar', server=duels, order=1)
c_duels_admin = Category.objects.create(name="Ma'muriyat va Maxsus", slug='duels-mamuriyat-va-maxsus', server=duels, order=2)
c_duels_other = Category.objects.create(name='Boshqa Narsalar', slug='duels-boshqa-narsalar', server=duels, order=3)

duels_ranks = [
    {
        'name': '👑 King',
        'slug': 'duels-king',
        'price': 19000,
        'commands': '/store king',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat'
        ),
    },
    {
        'name': '🦁 Lion',
        'slug': 'duels-lion',
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
        'name': '🛡️ Hero',
        'slug': 'duels-hero',
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
        'name': '⭐ Legend',
        'slug': 'duels-legend',
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
        'name': '⚡ Master',
        'slug': 'duels-master',
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
for r in duels_ranks:
    Product.objects.create(name=r['name'], slug=r['slug'], category=c_duels_donator, price=r['price'], commands=r['commands'], features=r['features'], is_active=True)

# Shared Admin and Other products
mamuriyat_products = [
    {'name': 'Homiy', 'price': 200000, 'commands': '/titul\n/uc menu', 'features': "Homiy rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu\nServer homiysi sifatida tanilish"},
    {'name': 'Admin', 'price': 150000, 'commands': '/titul\n/uc menu', 'features': "Admin rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu"},
    {'name': 'Moder', 'price': 100000, 'commands': '/titul\n/uc menu', 'features': "Moder rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu"},
    {'name': 'Helper', 'price': 50000, 'commands': '/titul\n/uc menu', 'features': "Helper rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu"},
]

boshqa_products = [
    {'name': 'Donate Case', 'price': 10000, 'commands': '', 'features': "Donate Case - maxsus sovrinlar bilan quti"},
    {'name': 'Token Case', 'price': 5000, 'commands': '', 'features': "Token Case - tokenlar bilan quti"},
    {'name': 'Maxsus Titul', 'price': 5000, 'commands': '/titul', 'features': "Maxsus unikal titul - /titul"},
    {'name': 'Narsani nusxalash', 'price': 5000, 'commands': '', 'features': "Qolinizdagi buyumni nusxalash xizmati"},
    {'name': '1000 Token', 'price': 1000, 'commands': '', 'features': "1000 ta server tokeni"},
]

for server, admin_cat, other_cat in [(anarxiya1, c_a1_admin, c_a1_other), (smp, c_smp_admin, c_smp_other), (duels, c_duels_admin, c_duels_other)]:
    s = server.slug
    for p in mamuriyat_products:
        Product.objects.create(name=p['name'], slug=f"{s}-{p['name'].lower().replace(' ', '-')}", category=admin_cat, price=p['price'], commands=p['commands'], features=p['features'], is_active=True)
    for p in boshqa_products:
        Product.objects.create(name=p['name'], slug=f"{s}-{p['name'].lower().replace(' ', '-')}", category=other_cat, price=p['price'], commands=p['commands'], features=p['features'], is_active=True)

print("TOZALANDI VA MUKAMMAL YANGILANDI!")
